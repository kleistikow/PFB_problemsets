#! usr/bin/env python3

with open ('Python_06.txt', 'r') as raw:
	for line in raw:
		line_upper = line.upper()
		print(line_upper)

with open ('Python_06.txt', 'r') as raw: 
	with open('Python_06.uc.txt', 'w') as new_file:
		for line in raw:
			new_file.write(line)

fa_dict={}
with open ('Python_06.seq.txt', 'r') as raw:
	for line in raw:
		line_list = line.split()
		fa_dict[line_list[0]] = line_list[1].rstrip()
		print(fa_dict)

for k,v in fa_dict.items():
	print('>'+ k + '\n' + v + '\n')

with open('Python_06.fastq', 'r') as raw:
	for line in raw:
		line = line.rstrip() 
		print(line)  
