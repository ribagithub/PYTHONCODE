#Python Count vowels in a string
def counting_vowels(text):                              #function definition
    vowels="aeiouAEIOU"
    vowel_counts=0

    for char in text:
        if char in vowels:                             #check the number of vowels
            vowel_counts+=1

    print("Original string: {}".format(string))
    print("Vowels: {}".format(vowels))
    print("No. of vowels: {}".format(vowel_counts))    #8

string="Welcome to Python Assignment"
counting_vowels(string)                                  #function calling
