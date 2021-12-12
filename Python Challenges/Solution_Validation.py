#The aim of this challenge is to write code that can analyze code submissions.
#Write a function named validate that takes code represented as a string as its only parameter.

#My Solution: Line 5 and Line 12 for making sure no empty parentheses
code = """l = [i[0] for i in S.split("(")]
    if "def" not in S:
        return "missing def"
    elif ":" not in S:
        return "missing :"
    elif "(" and ")" not in S:
        return "missing paren"   
    elif ")" in l:
        return "missing param"
    elif "    " not in S:
        return "missing indent"
    elif "validate" not in S:
        return "wrong name"
    elif "return" not in S:
        return "missing return"
    else:
        return True"""

code2="""if "def" not in S:
        return "missing def"
    elif ":" not in S:
        return "missing :"
    elif "(" and ")" not in S:
        return "missing paren"   
    elif "(" + ")" in l")":
        return "missing param"
    elif "    " not in S:
        return "missing indent"
    elif "validate" not in S:
        return "wrong name"
    elif "return" not in S:
        return "missing return"
    else:
        return True"""

def validate(S):
    l = [i[0] for i in S.split("(")]
    if "def" not in S:
        return "missing def"
    elif ":" not in S:
        return "missing :"
    elif "(" and ")" not in S:
        return "missing paren"   
    elif ")" in l:
        return "missing param"
    elif "    " not in S:
        return "missing indent"
    elif "validate" not in S:
        return "wrong name"
    elif "return" not in S:
        return "missing return"
    else:
        return True

print(validate(code))
print(validate(code2))