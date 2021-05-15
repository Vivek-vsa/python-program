def remove_and_split(string, word):
    newStr = string.replace(word, "")
    return newStr.strip()

this = "     vivek is a good      "
print(this)                             #before removing and spliting
n = remove_and_split(this, "vivek")
print(n)                                #after removing and spliting
# print(this)
# print(this.strip())
