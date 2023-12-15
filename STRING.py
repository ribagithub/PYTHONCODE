# #access the string
# my_string='Hello World!'
# #H E L L O   W O R L D !
# #0 1 2 3 4 5 6 7 8 9 10 11               #Positive indexing starts from 0(front counting)
# print("my_string[0]=",my_string[0])      
# print("len(my_string)=",len(my_string))
# print("my_string[7]=",my_string[7])

# #Negative index
# str="Hello World!"
# print("str[-1]=",str[-1])       #negative indexing starts from -1(back counting)
# print("str[=12]=",str[-12])


# #Slicing
# str="Hello World!"
# print("str[:]=",str[:])       #if no start and end point is present then after slicing it will print the whole string 
# print("str[:5]=",str[:5])     #if the end point is mentioned it will take upto n-1 starting from 0 
# print("str[6:]=",str[6:])     #if the start point is mentioned it will start from that point and continue till the end of string
# print("str[:8:2]=",str[:8:2]) #if the ennd point & step size is mentioned it will print the string from start maintaining a gap


# #string length
# my_string="Hello, World!"
# length=len(my_string)             #13
# print("Length of string=",length)


# #iterating over characters
# my_string="Hello, World!"
# for char in my_string:
#     print(char)            #printing (Hello, World!) vertically downward 

# #end="" function used to print the string horizontally
# my_string="Hello, World!"
# for char in my_string:
#     print(char,end="")       #printing (Hello, World!) horizontally


# #concatnation
# str1="Hello "
# str2="World!"
# result= str1+str2                    #Joing two variables to create a single result
# #the result will "Hello World!"
# print("after concatenation=",result)


#len and split function
# string_sentence="To change the overall look of your document.To change the look availability in the gallary"
# length=len(string_sentence)                #{}braces mens place holder
# print(string_sentence,"\nlength of sentence= ",length)        #\n means newline
# string_split=string_sentence.split(" ")
# print("After split: ",string_split)


#count the occurances of each word in a given sentence
# def word_count(str):                                  #function definition
#     counts=dict()
#     words=str.split()                                 #splitting the words with quotation
#     for word in words:
#         if word in counts:
#             counts[word]+=1
#         else:
#             counts[word]=1
#     return counts
# print(word_count("To change the overall look of your document.To change the look availability in the gallary")) #function calling


# #Python program to remove a newline in Python
# String="\nBest\nDeeptech\nPython\nTraining\n"     #\n means newline
# replace_string=String.replace("\n"," ")           #replace is a function of string (replacing \n with space)
# print("replacing with space:",replace_string)


# #Python program to reverse words in a string
# def reverse_words(string):                      #function definition
#     words=string.split(' ')                     #split is a function of string
#     reverse=' '.join(reversed(words))           #join is a function of string
#     return reverse
# str="Deeptech Python Training"
# print("reverse of string:",reverse_words(str))  #Training Python Deeptech


#Python program to count and display the vowels of a given text
# def count_and_display(text):
#     vowels='aeiouAEIOU'
#     vowels_count=0
#     vowel_list=[]
#     for char in text:
#         if char in vowels:
#             vowels_count+=1
#             vowel_list.append(char)
#     print("Original text: {}".format(text))
#     print("Number of vowels: {}".format(vowels_count))
#     print("Vowels: {}".format(", ".join(vowel_list)))
# text="Welcome to python Training"
# count_and_display(text)


#another method
def vowel(text):
    vowels="aeiouAEIOU"
    print("original text: ",text)
    print("no. of vowels: ",len([letter for letter in text if letter in vowels]))
    print("vowel alphabets: ",[letter for letter in text if letter in vowels])
vowel("Welcome to python Training")








