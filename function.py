# def addition():          #function defintion
#     a=45                 #addition operator
#     b=28
#     add=a+b
#     print("add= ",add)
# addition()               #function calling


# #function with parameter
# def fruits(name):
#     print("I like",name)  #kiwi,dragonfuit
# fruits("kiwi")
# fruits("dragonfruit")


#function with default parameter
# def my_function(name="Mita",fruit="Mango"):
#     print(name,"likes",fruit)
# my_function()
# my_function("Sneha","Orange")


# #function with return keyword
# def square(n):
#     return n**2
# print("square= ",square(10))


# #passing list as an argument
# def fruit(fruitlist):
#     for i in fruitlist:
#         print("I like",i)
# mylist=["apple","mango","banana"]
# fruit(mylist)


# #arbitory argument
# def fruits(*fruitlist):
#     print("I like",fruitlist[0])
#     print("I like",fruitlist[1])
#     print("I like",fruitlist[2])
# fruits("apple","mango","banana")
# #         0       1        2


# #factorial
# def factorial(num):
#     if(num>1):
#         return num*factorial(num-1)
#     else:
#         return 1
# no=int(input("enter number"))
# factorial(no)
# print("factorial of",no,"is",factorial(no)) 



#function with return keyword
def square(n):
    return n**2
result=square(4)
print("The square of 4 is",result)