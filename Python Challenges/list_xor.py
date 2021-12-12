#Define a function named list_xor. Your function should take three parameters: n, list1 and list2.
#Your function must return whether n is exclusively in list1 or list2. 

def list_xor(n,list1,list2): #My original solutin
    if n in list1 and n in list2 or n not in list1 and n not in list2:
        return False
    elif n in list1 and n not in list2 or n not in list1 and n in list2:
        return True

def list_xor_2(n,list1,list2): #After being prompted on use of ^ operator
    return (n in list1) ^ (n in list2)

print(list_xor(1, [1, 2, 3], [4, 5, 6]))
print(list_xor(1, [0, 2, 3], [1, 5, 6]))
print(list_xor(1, [1, 2, 3], [1, 5, 6]))
print(list_xor(1, [0, 0, 0], [4, 5, 6]))

print(list_xor_2(1, [1, 2, 3], [4, 5, 6]))
print(list_xor_2(1, [0, 2, 3], [1, 5, 6]))
print(list_xor_2(1, [1, 2, 3], [1, 5, 6]))
print(list_xor_2(1, [0, 0, 0], [4, 5, 6]))