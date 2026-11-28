
def add(a,b):
    return a+b

def multiply(a,b):
    return a*b

def subs(a,b):
    return a-b

# def divide(a,b):
#     return a/b // does'nt work for reminder 0

def divide(a, b):
    if b == 0:
        raise ValueError("b should not be zero")
    return a / b

