def getlinesListFrom(startStr): # get all lines starting from the keyword 'startStr' as a list
	global fileList
	linesList = []
	for line in fileList:
		lineList = line.split(' ')
		if lineList[0]  == startStr:
			linesList.append(line)
	return linesList

def printList(listx): # test print function for ease
	for line in listx:
		print(line)

def getAAsequence():
	global fileList
	seqrList = getlinesListFrom("SEQRES") # get list of lines starting from SEQRES
	AAseq = ""
	currentCI = seqrList[0][11] # chain identifier current
	for seqrline in seqrList:
		sll = seqrline.split() # to copy as codons
		newCI = seqrline[11]
		if newCI != currentCI:
			AAseq += '\n'

		for codon in sll[4:]:
			AAseq += codon + " "
		currentCI = newCI

	return AAseq

def numberHydrophobicResidues(aa): # aa sequence given for residues
	hydrophobicResidues = ['GLY','ALA','VAL','LEU','ILE','PRO','PHE','MET','TRP']
	#the nine amino acids that have hydrophobic side chains	
	nHR = 0
	resList = aa.split()
	print("Total number of residues: ", len(resList))
	for res in resList:
		if res in hydrophobicResidues: # if a res found is a hydrophobic res, increment count
			nHR += 1
	return nHR

def numberProteinChains():
	global fileList
	seqrList = getlinesListFrom("SEQRES") # get list of lines starting from SEQRES
	uniqueChainIdentifiers = []  # add all unique chain IDs found in these lines to this list
	for seqrline in seqrList:
		current_chain_id = seqrline[11]
		if not current_chain_id in uniqueChainIdentifiers:
			uniqueChainIdentifiers.append(current_chain_id)
		
	print("Unique Chain Identifiers found: ", uniqueChainIdentifiers)
	return len(uniqueChainIdentifiers) # length of this list == number desired

def numberHelices():
	global fileList
	helixList = getlinesListFrom("HELIX")  # get list of lines starting from HELIX
	uniqueHelixIdentifiers = [] # add all unique helix IDs found in these lines to this list
	for hline in helixList:
		hll = hline.split()
		current_helix_id = hll[2]
		if not current_helix_id in uniqueHelixIdentifiers:
			uniqueHelixIdentifiers.append(current_helix_id) # length of this list == number desired
	
	print("Unique Helix Identifiers found: ", uniqueHelixIdentifiers)
	return len(uniqueHelixIdentifiers)

def numberSheets():
	global fileList
	sheetList = getlinesListFrom("SHEET")  # get list of lines starting from HELIX
	uniqueSheetIdentifiers = [] # add all unique helix IDs found in these lines to this list
	for sline in sheetList:
		sll = sline.split()
		current_sheet_id = sll[2]
		if not current_sheet_id in uniqueSheetIdentifiers:
			uniqueSheetIdentifiers.append(current_sheet_id) # length of this list == number desired
	
	print("Unique Sheet Identifiers found: ", uniqueSheetIdentifiers)
	return len(uniqueSheetIdentifiers)

fileHandler = open(input("Enter PDB filename (example.pdb): "), "r")
fileList = fileHandler.read().split('\n')
fileHandler.close()

helixList = getlinesListFrom("HELIX")
a = getAAsequence()
print()
print("Amino acid sequence with line breaks according to protein chains:")
print(a,"\n")
b = numberHydrophobicResidues(a) # give amino acid sequence (residues) to check and return number of residues that are hydrophobic
print("Number of hydrophobic residues: ", b)
print()
c = numberProteinChains()
d = numberHelices()
e = numberSheets()
print("Number of protein chains:", c)
print("Number of helices:", d)
print("Number of sheets:", e)
