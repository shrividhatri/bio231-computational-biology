print("Q1. Write a program that takes DNA sequence as input and output six reading \
frames, and their amino acid sequence.")

# inserting a new key value pair by just assigning e.g. dict["a"] = "b"
# dict.pop("somekey"), dict.popitem() -- last item inserted is popped, del "somekey" same as pop
# changing is same as in list, lookup with key -- if "yourkey" in dict: 
# len(dict) gives length, clear() empties the dictionary, to copy -- yourdict = mydict.copy() or yourdict = dict(mydict)
# dict() constructor, update() dictionary with k-v pairs, values() return all values in a list, like keys()

base_list = ['T','C','A','G']
codon_list = []
for base1 in base_list:
	for base2 in base_list:
		for base3 in base_list:
			codon_list.append(base1+base2+base3)
# codon_list has all the codons now possible in the correct order of the table to be generated, UUU, UUC, UUA...
# 3 letter abbreviations from http://www.hgmd.cf.ac.uk/docs/cd_amino.html
AA3_list = ["Phe","Phe","Leu","Leu","Ser","Ser","Ser","Ser","Tyr","Tyr","Ter","Ter","Cys","Cys","Ter","Trp","Leu",\
"Leu","Leu","Leu","Pro","Pro","Pro","Pro","His","His","Gln","Gln","Arg","Arg","Arg","Arg","Ile","Ile","Ile","Met",\
"Thr","Thr","Thr","Thr","Asn","Asn","Lys","Lys","Ser","Ser","Arg","Arg","Val","Val","Val","Val","Ala","Ala","Ala",\
"Ala","Asp","Asp","Glu","Glu","Gly","Gly","Gly","Gly"] #amino acid list for the AA in the same order as their codons
AA1_list = "FFLLSSSSYY**CC*WLLLLPPPPHHQQRRRRIIIMTTTTNNKKSSRRVVVVAAAADDEEGGGG" # 1-length abbreviations
#dictionary

aaLen = int(input("Generate 1-length or 3-length abbreviations for amino acids? [Enter 1 or 3]: "))

codon_table = {}
if (aaLen == 1):
	for i in range(len(codon_list)):
		codon_table[codon_list[i]] = AA1_list[i]
	# combine key,value pairs and add in dictionary, where the key is the codon, and the value is its corresponding amino acid
if (aaLen == 3):
	for i in range(len(codon_list)):
		codon_table[codon_list[i]] = AA3_list[i]

print(">> Reading single 5' to 3' DNA sequence strand from 'dna.txt'")
DNA_File = open("dna.txt", "r")
main_strand = DNA_File.read()
main_strand = main_strand.replace(' ', '') # removing any spaces
main_strand = main_strand.replace('\n', '') # removing any \n characters
comp_strand = main_strand.replace('T','1') # replacing bases with temp characters (1,2,3,4), then later swapping the complement bases to get the complement strand
comp_strand = comp_strand.replace('A','2')
comp_strand = comp_strand.replace('C','3')
comp_strand = comp_strand.replace('G','4')
comp_strand = comp_strand.replace('1','A')
comp_strand = comp_strand.replace('2','T')
comp_strand = comp_strand.replace('3','G')
comp_strand = comp_strand.replace('4','C')
# complement strand now ready as well in 3'-5'direction for the given DNA strand in 5'-3'
# need to reverse comp_strand for the 5' to 3' direction, convert it from string to list first
comp_strand = comp_strand[::-1] # slice starts at end and iterates backwards

dna_reading_frames = []
for i in range(3): # generating frames 1,2,3
	dna_reading_frames.append([main_strand[c:c+3] for c in range(0, len(main_strand), 3)]) # list comprehension to generate smaller split strings of 3 length each
	main_strand = main_strand[1:] # truncate first DNA base every time

for j in range(3): # generating frames -1,-2,-3
	dna_reading_frames.append([comp_strand[c:c+3] for c in range(0, len(comp_strand), 3)]) # list comprehension to generate smaller split strings of 3 length each
	comp_strand = comp_strand[1:] # truncate first DNA base every time

print("\n>> Printing the six reading frames from 5' to 3': ")
counter = 1
for reading_frame in dna_reading_frames:
	print(counter, end=" = ")
	for codon in reading_frame:
		print(codon, end=" ")
	print ("")
	counter += 1

print("\n>> Printing amino acid sequences produced by these frames: ")
counter = 1
for reading_frame in dna_reading_frames:
	print(counter, end=" = ")
	for codon in reading_frame:
		if len(codon) == 3:
			print(codon_table[codon], end=" ")
		elif aaLen == 1:
			print("X", end=" ")
	print ("")
	counter += 1
