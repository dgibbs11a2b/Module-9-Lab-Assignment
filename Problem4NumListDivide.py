#----------------------------------------
#David Gibbs
#March 11, 2020
#
#This program will use a while loop to initialize a counter at 0.
#As processes, it will max out to a value of 50. if it finds a value that is
#divisible by 10, it will append that value to the list and
#then generate a list showing the numbers from that list called "tens".
#----------------------------------------

tens = []
#assigns variable to an empty list

count = 0
#initializes count at 0

while count <= 50:
  if count % 10 == 0:
    tens.append(count)
  count += 1
#counts up to 50 and kicks out values that are divisible by ten
#to the "tens" list

print('''Between the numbers 0 and 50, here are the list of numbers
that are evenly divisble by ten''', tens)

#prints final list of numbers evenly divisible by 10
