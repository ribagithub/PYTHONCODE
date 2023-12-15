#Python program to remove duplicate characters of a given string
def remove_duplicate(string):                #function definition
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
print("After removing duplicate: {}".format(output)) #String adFuco