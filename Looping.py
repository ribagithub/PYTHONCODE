# #Looping means repeating something over and over until a particular condition is satisfied


# #USING WHILE LOOP FOR COUNTING INTEGERS
# count=0               #function of python used to count integers
# while count<5:        #while loop
#     print(count)
#     count+=1          #count=count+1 [Assignment operator]


# #CODE USING RANGE FUNCTION
# n=int(input("enter number")) #5 last element excluded [n-1]
# for i in range(n):           #0,1,2,3,4   [In general range starts from 0 if any element is not specified]
#     print(i)                 #i is a variable


# n=int(input("enter number")) #starting from 8
# for d in range(8,n):         #begins from the mentioned value and continues upto n-1
#     print(d) 


# n=int(input("enter number")) #any number starting from 0
# for i in range(n,8):         #begins from the user input and continues upto 8-1
#     print(i) 


# #SQUARRING A NUMBER
# n=int(input("enter number"))
# def square():                        #function definition
#     squarring=n*n
#     print("squarring: ",squarring) 
# square()                             #function calling
# square()


# # Manupulation [Adding a number into the list]
# list=[1,2,3,4,5,6]             #list is immutable
# print("before added",list)
# list.append(7)                 #append is an object of the list function used to add an element at the last in a sequence
# print("after added",list)


# #BREAK & CONTINUE
# for i in range(10):  #[0-9]
#     if(i==5):
#         break
#     if(i==30):
#         continue
#     print(i)         #0



# def square(n):
#     return n**3             #n is 2 means 2 to the power 3 
# print("square: ",square(2)) #8


# try:
#     result=10/0
#     print("result: ",result)
# except ZeroDivisionError as e:
#     print("error: ",e)


for i in range(4):

  print("Hello world!")