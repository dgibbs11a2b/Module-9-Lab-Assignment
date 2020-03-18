#----------------------------------------
#David Gibbs
#March 11, 2020
#
#This program will use a while loop to prompt the user for a number
#It then appends each entered number to a list and adds them together
#until the sum of the list of numbers is greater than 100.
#When the sum totals 100 or more, the program breaks and prints
#the total sum
#----------------------------------------
total_sum = 0

a = int(input("Enter an integer: "))
#assigns "a" to the first integer entered

l = []
#assigns l to an empty list

while a != 0:
    total_sum += a
    if total_sum >= 100:
        print('Total sum is greater than 100. The actual total sum is', total_sum)
        break
    a = int(input("C'mon, enter another integer: "))
    l.append(a)
#appends values to the list 'l'
#the sum that the following line returns doesn't include the first input value.  Did you notice this?!    
    print('The sum of the list is now', l)
#assigns second integer entered to "a"
