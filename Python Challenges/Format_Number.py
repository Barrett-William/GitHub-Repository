#Write a function named format_number that takes a non-negative number as its only parameter.

#Your function should convert the number to a string and add commas as a thousands separator.

#For example, calling format_number(1000000) should return "1,000,000".

def format_number(x):
    t_x = str(x)
    first = len(t_x)%3 #remainder = where comma from left side goes
    step = (len(t_x)//3) #number of commas (will need to change ,xxx,xxx)
    l=0
    for i in range(step):
        t_x = t_x[:first+l+i*3] + "," + t_x[first+l+i*3:]
        l +=1
    if t_x[0]==",":
        return t_x[1:]       
    else:
        return t_x
    
print(format_number(10000000000000))
print(format_number(1000000))
print(format_number(100000))
print(format_number(10000))