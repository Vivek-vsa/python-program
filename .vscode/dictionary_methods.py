myDict = {
    "fast": "In a Quick Manner",
    "Vicky": "A developer",
    "marks": [1, 2, 5],
    "anotherdict": {'Vicky': 'Player'},
    1: 2
}

# Dictionary Methods
print(list(myDict.keys())) # Prints the keys of the dictionary
print(myDict.values()) # Prints the keys of the dictionary 
print(myDict.items()) # Prints the (key, value) for all contents of the dictionary 
print(myDict)
updateDict = {
    "Lovish": "Friend",
    "Divya": "Friend",
    "Shubham": "Friend",
    "Vicky": "A Dancer"
}
myDict.update(updateDict) # Updates the dictionary by adding key-value pairs from updateDict
print(myDict)

print(myDict.get("Vicky")) # Prints value associated with key "Vicky"
print(myDict["Vicky"]) # Prints value associated with key "Vicky"

# The difference between .get and [] sytax in Dictionaries?
print(myDict.get("Vicky2")) # Returns None as Vicky2 is not present in the dictionary
print(myDict["Vicky2"]) # throws an error as Vicky2 is not present in the dictionary