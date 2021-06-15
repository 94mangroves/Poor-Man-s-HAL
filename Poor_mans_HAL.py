

# This will import math module
import math

# This section will have the converstation

name = input("Hi there, what is your name? ")
activity = input("Hello " + name + ", nice to meet you. What would you like to do today? ")
print("Sorry " + name + ", I can't " + activity + " today.\n")
place = input("Where are you from? ")
print("I hear " + place + " is nice this time of year" )

# This section will ask for number from user and find the sqaure root

num = float(input('What is your favorite number? '))
num_sqrt = num ** 0.5
print(name + ', the square root of %0.3f is %0.3f'%(num ,num_sqrt))

# This section concludes the converstion

print("Goodbye " + name) 