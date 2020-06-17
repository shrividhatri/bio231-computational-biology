print("Q2. Write a program that takes protein sequence  as  input, and \
predicts the helices in the sequence using Chou-Fasman algorithm.")

name_list = ["Alanine", "Arginine", "Aspartic Acid", "Asparagine", "Cysteine", "Glutamic Acid", "Glutamine", "Glycine", "Histidine",\
"Isoleucine", "Leucine", "Lysine", "Methionine", "Phenylalanine", "Proline", "Serine", "Threonine", "Trpytophan", "Tyrosine", "Valine"]
AA1_list = "ARDNCEQGHILKMFPSTWYV"
p_a = [142, 98, 101, 67, 70, 151, 111, 57, 100, 108, 121, 114, 145, 113, 57, 77, 83, 108, 69, 106]
p_b = [83, 93, 54, 89, 119, 37, 110, 75, 87, 160, 130, 74, 105, 138, 55, 75, 119, 137, 147, 170]
'''
p_turn = [66, 95, 146, 156, 119, 74, 98, 156, 95, 47, 59, 101, 60, 60, 152, 143, 96, 96, 114, 50]
f_i = [0.06,0.070,0.147,0.161,0.149,0.056,0.074,0.102,0.140,0.043,0.061,0.055,0.068,0.059,0.102,0.120,0.086,0.077,0.082,0.062]
f_ip1 = [0.076,0.106,0.110,0.083,0.050,0.060,0.098,0.085,0.047,0.034,0.025,0.115,0.082,0.041,0.301,0.139,0.108,0.013,0.065,0.048]
f_ip2 = [0.035,0.099,0.179,0.191,0.117,0.077,0.037,0.190,0.093,0.013,0.036,0.072,0.014,0.065,0.034,0.125,0.065,0.064,0.114,0.028]
f_ip3 = [0.058,0.085,0.081,0.091,0.128,0.064,0.098,0.152,0.054,0.056,0.070,0.095,0.055,0.065,0.068,0.106,0.079,0.167,0.125,0.053]

collection = [name_list, p_a, p_b, p_turn, f_i, f_ip1, f_ip2, f_ip3]
while(True):
	print("\n")
	myAA = input("Enter amino acid 1-letter abbreviation to check details: ")
	if myAA in AA1_list:
		i = AA1_list.index(myAA)
		for somelist in collection:
			print(somelist[i], end=" ")
	else:
		print("Not found. Retry.")
'''

# propensity for a given amino acid to adopt alpha helices is its p(a) value -- p(Ala, Helix) = [N(Ala, helix)/N(aa in helix)]/[N(Ala)/N(aa)]
aa_sequence = "YSPYAELMRSYG" # length = 12
#aa_sequence = "APAFSVSLASGA"
#aa_sequence = "QAWIRGCRL"
#aa_sequence = "RWWCNDGRTPGSRNLCNIPCSALLSSDITASVNCAKKIVSDGNGMNAWVAWRNRCKGTDV"
#aa_sequence = input("Enter an amino acid sequence: ") 
h_markers = [] # will contain the markers 'H' for helix regions
for i in range(len(aa_sequence)): # same length as given aa_sequence
	h_markers.append(' ') # but for now we initialize it as empty

# Initiation
# assign parameters to all the residues
print(">> Assigning parameters to residues: ")
residue_parameters = []
residue_parametersb = []
for aa in aa_sequence:
	print(aa, end="    ")
	i = AA1_list.index(aa)
	residue_parameters.append(p_a[i])	
	residue_parametersb.append(p_b[i])


print("")
for p in residue_parameters:
	if(p < 100):
		print(p, end="   ")
	else:
		print(p, end="  ")

print("")
for p in residue_parametersb:
	if(p < 100):
		print(p, end="   ")
	else:
		print(p, end="  ")

print("")

markerDistance = 6-1
# list of window indexes from which helix regions start
helix_nuclei_indices = []

#since we are doing chou-fasmanI, we take windows of 6 contiguous AA to scan the peptide sequence, until we find a region where exactly 4 have p(a) > 100
#first window == 0-5, then 1-6.. until.. last window = 6-11, if length = 12, last index == 6 (length-6)
for window_index in range(len(aa_sequence)-markerDistance):
	h_residues = 0
	for res_index in range(window_index, window_index+6): # entire window where each index corresponds to a residue
		if residue_parameters[res_index] > 100: # check the corresponding p_a value
			h_residues += 1 # alpha helix residue found
	
	if h_residues == 4:
		print(f"Alpha-helix region found at window index {window_index}.")
		for i in range(window_index, window_index+6):
			print(aa_sequence[i], end=" ")
		print("")
		helix_nuclei_indices.append(window_index)

# propagation
print("Initiation complete.\n>> Propagation - Extending helixes until 4 contiguous residues have \naverage p(a) < 100 = until ends of helix found.")
for i in range(len(helix_nuclei_indices)):
	leftMark = helix_nuclei_indices[i] # left mark marks the left-most amino acid/character/index in the window chosen for the alpha-helix region
	rightMark = helix_nuclei_indices[i]+markerDistance # marks the right-most amino acid/index
	print(f"\nExtending region {i}...")
	print("Left extension...")
	#LEFT EXTENSION
	while(leftMark >= 1):
		avg_of_4pa = 0
		for r in range(leftMark-1, leftMark+3): # if leftMark is 2 then window of 1,2,3,4
			avg_of_4pa += residue_parameters[r]

		avg_of_4pa /= 4.0
		print (avg_of_4pa)
		if (avg_of_4pa < 100):
			break
		leftMark -= 1

	print("Right extension...")
	#RIGHT EXTENSION
	while(rightMark < len(aa_sequence)-1):
		avg_of_4pa = 0
		for r in range(rightMark-2, rightMark+2): # if rightMark is 7, then window of 5,6,7,8
			avg_of_4pa += residue_parameters[r]	

		avg_of_4pa /= 4.0
		print(avg_of_4pa)
		if (avg_of_4pa < 100):
			break
		rightMark += 1

	segment_p_a = 0
	segment_p_b = 0
	print("Final extended segment: ")
	for i in range(leftMark, rightMark+1):
		segment_p_a += residue_parameters[i]
		segment_p_b += residue_parametersb[i]
		print(aa_sequence[i], end=" ")

	if (segment_p_a > segment_p_b):
		print("\nNow marking this segment as an alpha-helix region.")
		for i in range(leftMark, rightMark+1):
			h_markers[i] = 'H'

print("Propagation complete.\n\n>> Printing entire amino acid sequence with helix prediction markers: ")
for aa in aa_sequence:
	print(aa, end="")
print("")
for marker in h_markers:
	print(marker, end="")
print("")
