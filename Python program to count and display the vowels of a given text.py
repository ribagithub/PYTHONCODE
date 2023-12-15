#Python program to count and display the vowels of a given text
def count_and_display(text):                      #function defintiion
    vowels='aeiouAEIOU'                           
    vowels_count=0                                #initialize
    vowel_list=[]
    for char in text:
        if char in vowels:
            vowels_count+=1                       #vowels_count=vowels_count+1
            vowel_list.append(char)               #append means to add value at the end of the list
    print("Original text: {}".format(text))       #{}braces mens place holder
    print("Number of vowels: {}".format(vowels_count))
    print("Vowels: {}".format(", ".join(vowel_list)))
text="Welcome to python Training"
count_and_display(text)                           #function calling


#another method
def vowel(text):                                  #function definition
    vowels="aeiouAEIOU"
    print("original text: ",text)
    print("no. of vowels: ",len([letter for letter in text if letter in vowels]))
    print("vowel alphabets: ",[letter for letter in text if letter in vowels])
vowel("Welcome to python Training")                #function calling