def myfunction():          #function definition
    print("Hello World")   
myfunction()               #function calling


##LOCAL VARIABLE
def add():
    a=20                   #Local variable declaration(variables which are defined inside the function)
    b=40                   #Local variable declaration                  
    print("add=",a+b)
add()                      

def add():
    a=25
    b=85
    c=76
    print("a=",a)
    print("b=",b)
    print("c=",c)
    print("Total of a+b+c=",a+b+c)
add()

def subtract():
    a,b,c=25,85,76
    print("a =",a,"b =",b,"c =",c)
    print("Total of a-b-c =",a-b-c)
subtract()

                           
##GLOBAL VARIABLE
x=45                       #Global variable declaration(variables which are defined outside the function)
y=56                       #Global variable declaration
def multiply():
    z=x*y
    print("multiply=",z)
print("x=",x)
print("y=",y)
multiply()

a=30                           #Global variables declaration
b=40
def addition():                #function definition
    a=20                       #Local variables declaration
    b=10
    print("addition =",a+b)    #inside the function
print("addition =",a+b)        #outside the function
addition()                     #function calling


x=240                                          #Global variables declaration
y=4
def divide():
    x=169                                      #Local variables declaration
    y=13
    print("x =",x)
    print("y =",y)
    print("Division of",x,"by",y,"is",x/y)     #inside the function
print("x =",x)
print("y =",y)
print("Division of",x,"by",y,"is",x/y)         #outside the function
divide()

a=5                                            #Global variable declaration
def globalvaluechange():                     
    global a                                  
    a=10                                       #Modified global variable
print("Before call a =",a)                     #5
globalvaluechange()
print("After call a =",a)                      #10


a=10                                                       #global variable declaration
b=2
def myfunction():
    global a                                               #Modified global variable
    a=20
    global b
    b=5
print("Before function call",a,"divided by",b,"is :",a/b)  #5
myfunction()
print("After function call",a,"divided by",b,"is :",a/b)   #4
