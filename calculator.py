# it is simple program to make calculator

# enter here value
num1=int(input("Enter 1st number :"))
num2=int(input("Enter 2nd number :"))
opr=input("enter here +,-,/,* :")

if opr=='+': #addition
    total=num1+num2
    print("Answer is",total) 

elif opr=='-': #substraction
    total=num1-num2
    print("Answer is",total) 

elif opr=='*': #multiplication
    total=num1*num2
    print("Answer is",total) 

elif opr=='/': #division
    total=num1/num2
    print("Answer is",total)         