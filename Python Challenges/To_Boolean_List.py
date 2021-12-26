#Create a function that converts a word to a bitstring and then to a boolean list based on the following criteria:

#Locate the position of the letter in the English alphabet (from 1 to 26).
#Odd positions will be represented as 1 and even positions will be represented as 0.
#Convert the represented positions to boolean values, 1 for True and 0 for False.
#Store the conversions into an array.

def to_boolean_list(word):
    l = [(ord(letter)-96) for letter in word]
    bin_list = [element%2 for element in l]
    bool_list = [bool(i) for i in bin_list]
    return bool_list


print(to_boolean_list('a'))
print(to_boolean_list("deep"))
print(to_boolean_list("loves"))
print(to_boolean_list("tesh"))