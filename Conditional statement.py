# #IF STATEMENTS   (A conditional statement used to check a condition, and execute if it is true)
# marks=int(input("enter marks: "))
# if(marks<=100 and marks>=80):     #88
#     print("A grade")
# if(marks<80 and marks>=60):       #76
#     print("B grade")
# if(marks<60 and marks>=40):       #57
#     print("C grade")
# if(marks<40):                     #34
#     print("Fail")


# #IF-ELSE STATEMENT  (If the condition is true the if block code is excuted and if the condition is false te else block code is executed)
# num=int(input("enter number"))
# if (num%2==0):
#     print("Even number")       #20  
# else:
#     print("Odd number")        #15


# #IF-ELIF-ELSE LADDER  (This means that if one alternative is true,the other alternatives must be false.Use the if-elif-else statement when te alterntives are mutually exclusive)
# marks=int(input("enter marks: "))
# if(marks<=100 and marks>=80):
#     print("A garde")
# elif(marks<80 and marks>=60):
#     print("B grade")
# elif(marks<60 and marks>40):
#     print("C grade")
# else:
#     print("Fail")



# #NESTED IF (It means the inner if statement will execute only after the outer if statemment has been execued)
# num1=int(input("enter num1 "))     #110
# num2=int(input("enter num2 "))     #120
# num3=int(input("enter num3 "))     #130
# if(num1>=num2):                    
#     if(num1>=num3):      
#         print(num1,"is greatest")
# if(num2>=num1):
#     if(num2>=num3):
#         print(num2,"is greatest")
# if(num3>=num1):
#     if(num3>=num2):
#         print(num3,"is greatest")  #130 is greatest


# #USER GIVEN NUMBER POSITIVE,NEGATIVE OR ZERO
# num=float(input("enter number: "))
# if(num>0):
#     print("Positive number")
# elif(num==0):
#     print("Zero")
# else:
#     print("Negative number")


year=int(input('enter a year: '))
if(year%4==0):
    if(year%100==0):
        if(year%400==0):
              print(year,"is a leap year")
        else:
            print(year,"is not a leap year")
    else:
        print(year,"is a leap year")
else:
    print(year,"is not a leap year")

