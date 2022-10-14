#!usr/bin/env python3
#krl 10-12-22

num = int(input("enter a number: "))
 
fac = 1
i = 1
 
while i <= num:
  fac = fac * i
  i = i + 1
 
print("factorial of ", num, " is ", fac)
