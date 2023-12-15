
#factorial using a while loop
num=int(input("enter digit= "))                  #7
fact=1                                           #1 is assigned into the variable
i=1
while(i<=num):
    fact=fact*i                                  
    i+=1                                         #i=i+1
print("The factorial of digit",num,"is= ",fact)  #5040
