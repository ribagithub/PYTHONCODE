#NESTED IF (It means the inner if statement will execute only after the outer if statemment has been execued)
num1=int(input("enter num1 "))     #110
num2=int(input("enter num2 "))     #120
num3=int(input("enter num3 "))     #130
if(num1>=num2):                    
    if(num1>=num3):      
        print(num1,"is largest")
if(num2>=num1):
    if(num2>=num3):
        print(num2,"is largest")
if(num3>=num1):
    if(num3>=num2):
        print(num3,"is largest")  #130 is largest