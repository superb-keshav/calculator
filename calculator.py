#Simple python program for calculator

num1=int(input("enter ther first number"))          
num2=int(input("enter second number"))
c=input("choose one operator:\n"
            "/,*,-,+\n")
if c=="+" :
    print(num1 +num2)
if c=="-" :
    print(num1-num2)
elif c=="*" :
    print(num1*num2)
elif c=="/" :
    print(num1/num2)
