print ("Logi  c Gate Simulation")
class gate
    
class andgate():
    def AND (a,b):
 
        if a == 1 and b == 1:
            return 1
        else:
            return 0

'''
class notgate():
    def logic(self):
        self.output = not self.
'''
class notgate():
    def NOT(a):
        if a == 1:
            return 1
        else:
            return 0
    
class orgate():
    def OR(a,b):
        if a == 1:
            return 1
        elif b == 1:
            return 1
        else:
            return 0
class norgate(orgate,notgate):
    
    def NOR(a,b):
        x = orgate.OR(a,b)
        y = notgate.NOT(x)
        return y
class nandgate(orgate,notgate):
    
    def NAND(a,b):
        x = andgate.AND(a,b)
        y = notgate.NOT(x)
        return y

A=input("what type of gate do you want to simulate - OR, AND ,NOT,NAND  or NOR?")

if A == 'AND':
    a = int(input("enter value for input 1"))
    b = int(input("enter value for input 2"))
    x= andgate.AND(a,b)
    print (x)



elif A == 'OR':
    a = int(input("enter value for input 1"))
    b = int(input("enter value for input 2"))
    x= orgate.OR(a,b)
    print (x)

elif A == 'NOT':
    a = bool(input("enter value for input 1"))
    
    x= notgate.NOT(a)
    print (x)
    
elif A == 'NOR':
    a = int(input("enter value for input 1"))
    b = int(input("enter value for input 2"))
    Y= norgate.NOR(a,b)
    print (Y)

elif A == 'NAND':
    a = int(input("enter value for input 1"))
    b = int(input("enter value for input 2"))
    Y= nandgate.NAND(a,b)
    print (Y)

    

    

