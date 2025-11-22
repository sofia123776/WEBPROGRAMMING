#This is a simple calculator python program

#the method block

def Add(a,b):
    return a+b

def Subtract(a,b):
    return a-b

def Multiply(a,b):
    return a*b

def Divide(a,b):
    if b==0:
        return "Error division by 0"
    return a/b

#making a method for the operator's choice
def Calculator():
    print("Choose an operator")
    print("1.Add")
    print("2.Subtract")
    print("3.Multiply")
    print("4.Divide")


#Asking the user to choose an operator

choice = input("Enter choice(1/2/3/4): ")

if choice in ('1', '2' ,'3' ,'4'):
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        if choice == '1':
            print("Result:",Add(num1,num2))
        elif choice == '2':
            print("Result:",Subtract(num1,num2))
        elif choice == '3':
            print("Result:",Multiply(num1,num2))
        elif choice == '4':
            print("Result:",Divide(num1,num2))
        
    except ValueError:
        print("Invalid input!Please enter a number")
else:
    print("Invalid choice please select a valid operator")
if __name__=="__main__":
    Calculator()
                             


    
    



        




    