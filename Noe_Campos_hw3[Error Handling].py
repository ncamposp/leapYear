import sys

year = input('Year:\n') #grab input from cmd
#before we proceed, lets verify what we have is an int
try:
   year = int(year) #cast the string to int
except ValueError:
   print(year, "is not an integer")
   print("Program will now terminate.")
   sys.exit(1)

#check 1: divisible by 4 and NOT divisible by 100
if (year % 4 == 0) and (year % 100 != 0): 
  print(year, "is a leap year")
#check 2: what if it is divisible by 4, not by 100, but yes by 400?
elif(year % 4 == 0) and (year % 400 == 0): 
  print(year, "is a leap year")
#if we are down here then it is definitely NOT a leap year
else:
  print(year, "is NOT leap year")