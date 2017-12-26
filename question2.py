'''Write a program that accepts a comma separated sequence of words as input and prints the words in a comma-separated
sequence after sorting them alphabetically.'''
any=str(input("enter any string:"))
any=any.split(",")
any=sorted(any)
print("," .join(any))