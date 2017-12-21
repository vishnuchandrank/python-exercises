print ("enter first no")
def add (x,y):
    return x+y

def subtract(x,y):
    return x-y
print ("select operation.")
print ("1.add")
print ("2. sub")

choice = input("enter choice (1/2)")

num1 = int (input("enter first no"))
num2 = int (input("enter second no."))
if choice == '1':
    print(num1,"+",num2,"=", add(num1,num2))

elif choice =='2':
    print (num1,"-",num2,"=", subtract(num1,num2))

else :
    print("invalid operation")
