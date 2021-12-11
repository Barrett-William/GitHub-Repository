#Define a function named all_equal that takes a list and checks whether all elements in the list are the same.
import timeit

def all_equal(x): #My first solution
    l = []
    for i in range(len(x)-1):
        if x[i]==x[i+1]:
            l.append(True)
        elif x[i]!=x[i+1]:
            l.append(False)
    return all(l)

def all_equal_2(x): # My second solution
    return len([True for i in x if x[0]==i]) == len(x)

def all_equal_3(items): # Online solution 1
    for item1 in items:
        for item2 in items:
            if item1 != item2:
                return False
    return True

def all_equal_4(items): # Online solution 2
    return all(item1 == item2 for item1 in items for item2 in items)

import random
input = []
r = random.randint(0,15)
for i in range(0,r):
    n = random.randint(1,9)
    input.append(n)
print(input)

print("Method 1",all_equal(input))
print(timeit.timeit('all_equal(input)', globals=globals()))
print("Method 2", all_equal_2(input))
print(timeit.timeit('all_equal_2(input)', globals=globals()))
print("Method 3", all_equal_3(input))
print(timeit.timeit('all_equal_2(input)', globals=globals()))
print("Method 4", all_equal_4(input))
print(timeit.timeit('all_equal_2(input)', globals=globals()))