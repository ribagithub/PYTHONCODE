# #count all letters,digits and special symbols from the given string
# def count_chars(string):                             #function definition
#     #Initialize counters
#     letter_count=0
#     digit_count=0
#     special_count=0

#     # Iterate through each character in the string
#     for char in string:                             
#         if char.isalpha():                           #check if the character is a letter
#             letter_count += 1                        #8
#         elif char.isdigit():                         #check if the character is a digit
#             digit_count +=1                          #3
#         else:                                        #if the character is not a letter/digit,then consider it as special symbol
#             special_count +=1                        #4  

#     print("Letters= ",letter_count)
#     print("Digits= ",digit_count)
#     print("Special symbols= ",special_count)

# input_string="P@#yn26at^&i5ve"
# count_chars(input_string)                            #function calling


# #Python program to count Uppercase, Lowercase, special character and numeric values in a given string
# def count_values(string):                               #function definition
#     uppercase_count=0                                   
#     Lowercase_count=0                                  
#     digit_count=0                                       
#     special_count=0                                     
#     for value in string:
#         if value.isupper():                             #function definition
#             uppercase_count+=1                        
#         elif value.islower():                          #check the number of lower characters
#             Lowercase_count+=1                         
#         elif value.isdigit():                          #check the number of digits
#             digit_count+=1                            
#         else:                                          #check the number of special characters
#             special_count+=1                         

#     print("Original text: ",text)
#     print("Uppercse counts: ",uppercase_count)          #5
#     print("Lowercase counts: ",Lowercase_count)         #18
#     print("Digits count: ",digit_count)                 #5
#     print("Special characters: ",special_count)         #11

# text= "Hell0 W0rld ! 123 * # welcome to pYtHoN"
# count_values(text)                                  #function calling


# #Python Count vowels in a string
# def counting_vowels(text):                              #function definition
#     vowels="aeiouAEIOU"
#     vowel_counts=0

#     for char in text:
#         if char in vowels:                             #check the number of vowels
#             vowel_counts+=1

#     print("Original string: {}".format(string))
#     print("Vowels: {}".format(vowels))
#     print("No. of vowels: {}".format(vowel_counts))    #8

# string="Welcome to Python Assignment"
# counting_vowels(string)                                  #function calling


#Python program to remove duplicate characters of a given string
def remove_duplicate(string):
    string_list=[]
    result_string=""

    for char in string:
        if char not in string_list:
            string_list.append(char)
            result_string+=char

    return result_string

text="String and String Function"
output=remove_duplicate(text)

print("Before removing duplicate: {}".format(text))
print("After removing duplicate: {}".format(output))










