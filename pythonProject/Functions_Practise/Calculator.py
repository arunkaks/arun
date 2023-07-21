# Addition of two numbers
def Addition(n1,n2):
    return n1+n2
# Subtraction of  two numbers
def Subtraction(n1,n2):
    return n1-n2
# Multiplication of  two numbers
def Multiplication(n1,n2):
    return n1*n2
# Division of two numbers
def Divsion(n1 ,n2):
    return n1/n2
print("' Select the Operator -\n"
      "1.Addition\n"
      "2.Subtraction\n"
      "3.Multipliaction\n"
      "4.Division\n")

#  Taking input from the users
operator=int(input("Select the operator from 1 to 4:"))
num_1=int(input("Enter the first number: "))
num_2=int(input("Enter the second number: "))

if operator == 1:
    print(num_1,"+",num_2,"=",Addition(num_1,num_2))

elif operator == 2:
    print(num_1,"-",num_2,"=",Subtraction(num_1,num_2))

elif operator == 3:
    print(num_1,"*",num_2,"=",Multiplication(num_1,num_2))

elif operator == 4:
    print(num_1,"/",num_2,"=",Divsion(num_1,num_2))

else:
    print("Invalid")

