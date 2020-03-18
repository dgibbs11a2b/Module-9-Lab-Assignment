#----------------------------------------
#David Gibbs
#March 10, 2020
#
#This program will use a while loop to append the current
#value of the current counter variable to the list and
#then increase the counter by 1. The while loop then stops
#once the counter value is greater than 10.
#----------------------------------------

l = [0,1,2,3,4,5,6,7,8,9,10]


counter_value = 0
#sets counter value

counter_max = 10
#sets counter maximum

while counter_value <= counter_max:
    l.append(counter_value)
    counter_value += 1
#while statement which appens incremented counter values to list "l"
  
print('The updated list is: ', l)
#Updated List

#x = 0
#L = []

#while x < 11:
#	L.append(x)
#	x += 1
	
#print(L)
