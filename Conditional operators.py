# #Conditionl operators(ternary operator)
# age=int(input("enter the age"))                                               #userinput
# voting_crteria= "eligible for vote" if age>=18 else "not elogible for vote"   #conditional statement in one line
# print(voting_crteria)   


# age=5
# adult="True" if age>=18 else "False"     #conditional statement in one line
# print(adult)



# sun_direction=input("The sun rises in the: ")             
# if sun_direction=="east":
#     print("true")
# else:
#     print("false")



from unicodedata import east_asian_width


sun_direction=input("The sun rises in the: ")         
sun="True" if sun_direction=="east" else "False"
print(sun)