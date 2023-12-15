# #count the occurances of each word in a given sentence
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


sentence="To change the overall look of your document.To change the look availability in the gallary"
count=sentence.count("To change the overall look of your document.To change the look availability in the gallary")
print("count of words:",count)
