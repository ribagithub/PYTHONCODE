#Python program to count Uppercase, Lowercase, special character and numeric values in a given string
def count_values(string):                               #function definition
    uppercase_count=0                                   
    Lowercase_count=0                                  
    digit_count=0                                       
    special_count=0                                     
    for value in string:
        if value.isupper():                             #function definition
            uppercase_count+=1                        
        elif value.islower():                          #check the number of lower characters
            Lowercase_count+=1                         
        elif value.isdigit():                          #check the number of digits
            digit_count+=1                            
        else:                                          #check the number of special characters
            special_count+=1                         

    print("Original text: ",text)
    print("Uppercse counts: ",uppercase_count)          #5
    print("Lowercase counts: ",Lowercase_count)         #18
    print("Digits count: ",digit_count)                 #5
    print("Special characters: ",special_count)         #11

text= "Hell0 W0rld ! 123 * # welcome to pYtHoN"
count_values(text)                                  #function calling