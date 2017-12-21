print ("Logic Gate Simulation")

def AND (a,b):

    if a == 1 and b == 1:
        return 1
    else:
        return 0



def NOT (a):
    if a == 1:
        return 0
    else:
        return 1


def OR(a,b):
    if a == 1:
        return 1
    elif b == 1:
        return 1
    else:
        return 0

A=input("what type of gate do you want to simulate - OR, AND  or NOT?")

if A == 'AND':
    a = input("enter value for input 1")
    b = input("enter value for input 2")
    x= AND(a,b)
    print (x)



elif A == 'OR':
    a = input("enter value for input 1")
    b = input("enter value for input 2")
    x= OR(a,b)
    print (x)
    
elif A == 'NOT':
    a = input("enter value for input 1")
    x= NOT(a)
    print (x)

    

