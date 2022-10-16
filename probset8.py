#!/usr/bin/env python3

import re

def countNucleotides(fasta):
    aCount = []
    gCount = []
    cCount = []
    tCount = []
    with open(fasta, 'rb') as data:
        for line in data:
            if not re.match(r'[agctAGCT]+',line):
                break
            aCount.append(notCount(line,'a'))
            gCount.append(notCount(line,'g'))
            cCount.append(notCount(line,'c'))
            tCount.append(notCount(line,'t'))

def notCount(line, character):
    appearances = 0
    for item in line:
        if item == character:
            appearances += 1
    return appearances

for seq_record in SeqIO.parse('Python_08.fasta', 'fasta'):
	print(seq_record.id)
	print(repr(seq_record.seq))
	print(len(seq_record))
	
        	 
count_nucs = countNucleotides(fasta)
print(count_nucs)
nocount_nucs = notCount(fasta)
print(nocount_nucs)
