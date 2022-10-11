#!/usr/bin/env python3

import sys

age = sys.argv[1]

if age < "30" :
   message = "year olds don't know jack"
   print (age, message)
elif age < "40" :
   message = "year olds know the struggle"
   print (age, message)
elif age < "60" :
   message = "year olds wish they were younger"
   print (age, message)
elif age < "90" :
   message = "year olds wish they were dead"
   print (age, message)
elif age > "90" :
   message = "year olds are proabably dead"
   print (age, message)

