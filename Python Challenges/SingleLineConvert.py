#Define a function named convert that takes a list of numbers as its only parameter and returns a list of each number converted to a string.

def convert(x):
    return([str(i) for i in x])
    
print(convert([1, 2, 3]))