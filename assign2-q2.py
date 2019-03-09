'''
Section 3 - Q2
Write a programme that reads a distance matrix from a file and constructs a phylogenetic tree using UPGMA. 
The output tree should be in Newick format.
'''

#NOTE: i and j switched around when passing values for printing when i = 0, j = 1 means (1,0) in grid
def print_matrix(matrix,n):
	print("\nDistance Matrix: ")
	for i in range(0,n):
		for j in range(0,n):
			space = '   '
			num_length = len(str(matrix[i][j]))
			space = space[num_length-1:] # for formatting, reduce the space to put after a longer number
			
			print(matrix[i][j], end=space)
		print('')

def min_and_pos_in_matrix(matrix,n):
	# store very first non-zero value of matrix (0,0) as min score
	min_and_pos = [matrix[1][0], 0, 1] # 3 element list stores min in index 0 and then the j and i coordinates in the index 1 and 2 
	for i in range(0,n): 
		for j in range(0,n):
			if (matrix[i][j] != 0 and matrix[i][j] < min_and_pos[0]):
				min_and_pos[0] = matrix[i][j]
				min_and_pos[1] = j
				min_and_pos[2] = i
	return min_and_pos # returns the list for min and pos

def get_square_matrix(n):
	matrix = [] # initially empty
	for i in range(0,n): # initialise to square with 0's of size n x n where n = number of species
		matrix.append([]) # append empty row to initialise
		for j in range(0, n):
			matrix[i].append(0)
	return matrix

fileName = "dm.txt"

#open file at first to get calculate number of sequences from # of lines
fileHandler = open(fileName, 'r')
#distance scores in any row OR # of columns = number of taxa/species/sequences
sequences = 0
for line in fileHandler.readlines(): # check characters in row 0
	sequences += 1
fileHandler.close()
print("Sequences: %s" % sequences)

#INITIALISE DISTANCE MATRIX
distance_matrix = get_square_matrix(sequences);

# open file again for reading in the distance scores now
fileHandler = open(fileName, 'r')
row_num = 0
for line in fileHandler.readlines(): # for every row/line from the read file
	col_num = 0 # current number for the distance score (e.g. if first number extracted then it goes to col_num = 0)
	line_tokens = line.split() # default value is a white space
	for token in line_tokens:
		if (token != '\n'): # if the character found is not a newline char
			distance_matrix[row_num][col_num] = int(token)  # assign the converted integer to its position in the matrix
			col_num += 1
	row_num += 1
fileHandler.close()

print_matrix(distance_matrix, sequences)

# NOW WE EXECUTE UPGMA
clusters = []
for sequence in range(0,sequences): # initialise single clusters in character form
	clusters.append(str(chr(65+sequence)))
# index of every string char/cluster is same as index in matrix

while(len(clusters) != 1): # until all clusters have not merged to become one for the entire tree
	#1. Identify and get smallest D (distance score) from matrix
	current_mp = min_and_pos_in_matrix(distance_matrix, sequences) # current_mp stores 3 element list with minimum and its index in the matrix
	# print(current_mp)
	smallestD = current_mp[0]
	# note that if there were two minimums, we only get the first one here

	#2. Taxa to be joined to form a cluster (suppose A = index 0, B = 1 ...) (T1 = 0 and T2 = 1 means A and B are joined)
	# Get character for every index, use a dictionary, and modify that dictionary over time
	t1_pos = current_mp[1] # current_mp[1] gives the i index of the smallestD corresponding to first taxa
	t2_pos = current_mp[2]

	cluster_string = '('+clusters[t1_pos]+','+clusters[t2_pos]+')'
	print ("New cluster formed: " + cluster_string)
	# merging clusters at indexes t1_pos and t2_pos to form a subtree
	del clusters[t2_pos] # delete 2nd cluster
	new_cluster_pos = t1_pos
	clusters[new_cluster_pos] = cluster_string #replace with merged cluster in first cluster's position

	#3. Calculate distances from this new cluster to other clusters say x (so distance of t1t2 e.g. (A,B) to x e.g. C)
	#e.g. d_(A,B)_C = (d_AC + d_BC) / 2
	#generalizing ... d_t1t2_x = (d_t1x + d_t2x) / 2

	# d_t1t2_x contains the distances from the new cluster to the any other cluster x
	d_t1t2_x = []
	# print(t1_pos, t2_pos)
	for x_pos in range(0, sequences):
		if (x_pos == t1_pos or x_pos == t2_pos): #where x_pos will be all those positions except t1_pos and t2_pos
			continue
		d = (distance_matrix[x_pos][t1_pos] + distance_matrix[x_pos][t2_pos]) / 2
		d_t1t2_x.append(d)
		#print("Distance of cluster %s with %s = %i" % (clusters[new_cluster_pos], clusters[x_pos-1], d)) # -1 for clusters since two of them have merged
	
	#since a cluster has formed of two sequences, there is one less sequence
	sequences -= 1
	old_distance_matrix = distance_matrix
	distance_matrix = get_square_matrix(sequences)
	# (A,B) reside at index 0 or their new_cluster_pos
	for i in range(1,sequences):
		for j in range(0, sequences):
			if (i == new_cluster_pos and j != new_cluster_pos):
				distance_matrix[i][j] = d_t1t2_x[j-1] 
				print("Inserting new score %i at index (%i, %i) in new matrix" % (distance_matrix[i][j],i,j))
			else: # copy same values from old distance matrix in their respective positions	
				distance_matrix[i][j] = old_distance_matrix[i+1][j+1]
	
	print_matrix(distance_matrix, sequences)
# print the final cluster formed for the tree
print("\nTREE BY UPGMA: %s" % clusters[0])