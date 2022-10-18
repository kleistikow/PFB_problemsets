#!/usr/bin/env python3

import re
with open ('Python_07_nobody.txt', 'r') as raw:
	for line in raw:
		for match in re.finditer(r'Nobody', line):
			start = match.start() +1
			end = match.end()
			print( "Line: {}\tstart:{}\tend:{}".format(start,end))			
			 	
with open('Python_07_nobody.txt', 'r') as raw:
	for line in raw:
		line = line.rstrip()
		line = re.sub(r'Nobody','Everybody', line)
		print(line)


with open("Python_07.fasta") as raw:
	for line in raw:
		if re.search(r"^>",line):
			print(line.rstrip()) 

with open("Python_07.fasta") as raw:
	for line in raw:
		line = line.rstrip()
		if re.search(r"^>",line):
			for found in re.finditer(r"^>(\S*)? (.*)$", line):
				ID = found.group(1)
				Desc = found.group(2)
				print(ID,"\t",Desc) 


seqdict = {}
with open("Python_07.fasta") as raw:
	seq = ''
	for line in raw:
		line = line.rstrip()
		if re.search(r"^>", line):
            		header = line
            		seq = ''
		else:
			seq += line
			seqdict[header] = seq
seqdict[header] = seq
print (seqdict)


seq = ''
with open("Python_07_ApoI.fasta") as raw:
    for line in raw:
        seq += line

for match in re.finditer(r"[A|G]AATT[C|T]",seq):
    print (match)


seq = ''
with open("Python_07w_ApoI.fasta") as raw:
    for line in raw:
        seq += line
newseq = re.sub(r"([A|G])(AATT[C|T])",r"\1^\2",seq)
print (newseq)


seq = ''

with open("Python_07_ApoI.fasta") as raw:
    for line in raw:
        seq += line

newseq = re.sub(r"([A|G])(AATT[C|T])",r"\1^\2",seq)

fragList = []
for match in re.findall(r"\^(\w+)[\^\n]", newseq):
    fragList.append(match)
fragList = sorted(fragList, key=len, reverse=True)

for frag in fragList:
    fragLen = len(frag)
    print("Length: {}\tFragment: {}".format(fragLen, frag))

with open("bionet.txt", 'r') as raw:
    for n in range(1,10):
        next(raw)
    for line in raw:
            line = line.rstrip()
            if re.match(r"^\w",line):
                cleanline = re.sub(r" {2,}", r"\t",line)
                splitline = cleanline.split('\t')
                enzymeDict[splitline[0]]=splitline[1]

print(enzymeDict)
