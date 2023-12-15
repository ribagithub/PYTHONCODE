#use of break statement in while loop
num=int(input("enter number: "))  #10
i=2
while(i<num):                     #2<7,3<7,4<7,5<7,6<7
    if i==7:                      #7==7 (if the break condition satisfies it will not get printed) 
        break
    else:
        print(i)                  
        i+=1                      #i=i+1
else:
    print("This is else part")    #else part will be executed in case the loop fails to satisfy
