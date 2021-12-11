#Define a function named all_equal that takes a list and checks whether all elements in the list are the same.
def all_equal(x):
    l = []
    for i in range(len(x)-1):
        if x[i]==x[i+1]:
            l.append(True)
        elif x[i]!=x[i+1]:
            l.append(False)
    return all(l)

def all_equal_1(x):
    print()

print(all_equal([1, 1, 1, 0]))