'''Ask for a number (n) as an input from user. Using the use input (n), write a program to generate a dictionary that contains
 (i, i*i) where i is key and i*i is a value for numbers between the range 1 and n (both included). and then
 the program should print the dictionary.'''
reqnumber=int(input("enter your required number:"))
dictionary = dict()

for i in range(1,( reqnumber+1)):
    dictionary[i] = i*i

print(dictionary)