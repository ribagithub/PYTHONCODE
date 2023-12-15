#PROGRAM THAT DETERMINES IF A GIVEN YEAR IS A LEAP YEAR OR NOT
year=int(input('enter a year: '))
if(year%4==0):                              #always divisible by 4
    if(year%100==0):                        #not always divisible by 100
        if(year%400==0):                    #if divisile by 100 checks whether divisible by 4 or not 
              print(year,"is a leap year")
        else:
            print(year,"is not a leap year")
    else:
        print(year,"is a leap year")
else:
    print(year,"is not a leap year")
