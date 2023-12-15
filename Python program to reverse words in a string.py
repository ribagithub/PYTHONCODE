#Python program to reverse words in a string
def reverse_words(string):                      #function definition
    words=string.split(' ')                     #split is a function of string
    reverse=' '.join(reversed(words))           #join is a function of string
    return reverse
str="Deeptech Python Training"
print("reverse of string:",reverse_words(str))  #Training Python Deeptech