# #even numbers using for loop
# n=int(input("enter number"))  #20
# for i in range(2,n,2):        #start,stop,step  2 4 6 8 10 12 14 16 18 
#     print(i)


# #odd numbers using for loop
# n=int(input("enter number"))  #20
# for i in range(1,n,2):        #1 3 5 7 9 11 13 15 17 19
#     print(i)

# n=5                      #initial value
# for x in range(5,10,2):  #5 7 9
#     print(x)

# #reverse number series using for loop
# n=int(input("enter number"))  #10
# for i in range(n,2,-2):       #10 8 6 4 
#     print(i)

# #no. of even and odds in one series using for loop
# n=int(input("enter number"))  #20
# for i in range(n,0,-3):       #20 17 14 11 8 5 2
#     print(i)


# #for loop with string
# str='Priya'    
# for x in str:    #x will execute all the letters stored in str variable
#     print(x)


# #for loop with list
# fruit_list=["Apple","Mango","Banana","Pineapple"]
# for i in fruit_list:
#         print(i)


# def new_func():                                        #function definition
#     fruit_list=["Apple","Mango","Banana","Pineapple"]
#     for i in fruit_list:
#         print(i)
# new_func()                                             #function calling

# #for loop with table
# num=int(input("enter number")) #7
# for x in range(1,11):          #7 14 21 28 35 42 49 56 63 70
#      print(num*x)


# #for loop with else part
# fruit_list=["Appe","Mango","Banana"]
# for i in fruit_list:
#     print(i)
# else:
#     print("This is else block")


# #for loop with break and else
# Student=["Rohit","Sima","Geeta","Vishal"]
# for i in Student:
#     if i=="Geeta":
#         break
#     else:
#         print(i)
# else:
#     print("This is else part")


# #n-1
# num=int(input("enter number")) #5
# i=num                          #5
# while(i>=1):                   #5>=1,4>=1,3>=1,2>=1,1>=1
#     print(i)
#     i-=1                       #i=i-1 ->5-1=4-1=3-1=2-1=1-1=0


#factorial
num=int(input("enter number")) #10
fact=1
i=1
while(i<=num):
    fact=fact*i
    i+=1
print("factorial of digit ",num,"is",fact) #3628800


# #while with else
# num=int(input("enter number"))  #12
# i=2
# while(i<=num):                  #2<=12,4<=12,6<=12,8<=12,10<=12,12<=12
#     print(i)
#     i+=2                        #i=i+2 ->2+2=4+2=6+2=8+2=10+2=12
# else:
#     print("This is else part")


# #while loop with break
# num=int(input("enter number")) #5
# i=1
# while(i<num):                  #1<5,2<5,3<5,4<5         
#     if i==3:                   #3==3 condition satisfying
#         break
#     else:
#         print(i)               #1,2
#         i+=1                   #2,3           
# else:
#     print("This is else part")


# #while loop with string
# str="Python"
# print("length=",len(str))
# i=0
# while i<len(str):
#     print(str[i])          #P y t h o n
#     i+=1                   #i=i+1


# #while loop with list
# li=["Apple","Banana","Guava"]
# #     0       1         2
# i=0
# while(i<len(li)):
#     print(li[i])
#     i+=1                          #i=i+1


# #list with for loop using len function
# items_list=["pen","pencil","copy","eraser","board"]     #list
# print("The list of items are:")                         
# for i in range(len(items_list)):                        #length in range starts from zero
    #  print(i,items_list[i])
    
                    