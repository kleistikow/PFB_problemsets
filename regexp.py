#!/usr/bin/env python3

import re
with open ('Python_07_nobody.txt', 'r') as raw:
	for line in raw:
		line = line.rstrip()
		print(line)

nobody = len(re.findall(r'Nobody', line))
print(nobody)
