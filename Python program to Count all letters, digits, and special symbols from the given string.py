    #Python program to Count all letters, digits, and special symbols from the given string
def count_chars(string):                             #function definition
    #Initialize counters
    letter_count=0
    digit_count=0
    special_count=0

    for char in string:                             
        if char.isalpha():                           #check if the character is a letter
            letter_count += 1                        #8
        elif char.isdigit():                         #check if the character is a digit
            digit_count +=1                          #3
        else:                                        #if the character is not a letter/digit,then consider it as special symbol
            special_count +=1                        #4  
    print("Original string: {}".format(input_string))
    print("Letters= ",letter_count)
    print("Digits= ",digit_count)
    print("Special symbols= ",special_count)

input_string="P@#yn26at^&i5ve"
count_chars(input_string)                            #function calling