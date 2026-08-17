                                                                        
#Simple calculator
#Author:Sshivani Karthikeyan
print("Calculator")
print("1.Addition")
print("2.Subtreaction")
print("3.Multiplication")
print("4.Division")
ch=int(input("Enter your choice:"))
num1=float(input("Enter number 1:"))
num2=float(input("Enter number 2:"))

if(ch==1):
    sum=num1+num2
    print("Addition of numbers is:",sum)
elif(ch==2):
    if(num1>num2):
        diff=num1-num2
    else:
        diff=num2-num1
    print("Subtraction of two numbers is:",diff)
elif(ch==3):
    mul=num1*num2
    print("Multiplication two numbers is:",mul)
elif(ch==4):
    div=num1/num2
    print("Division of two numbers is:",div)
else:
    print("Invalid choice")
