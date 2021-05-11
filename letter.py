letter = '''Dear <|NAME|>,
Greetings from ABC coding house. I am happy to tell you about your selection
You are selected!
Have a great day ahead!
Thanks and regards,
Bill
Date: <|DATE|>
'''
name = input("Enter Your Name\n")
date = input("Enter Date\n")
letter = letter.replace("<|NAME|>", name)  #replaces the name with the user input value
letter = letter.replace("<|DATE|>", date)    #replaces the date with the user input value
print(letter)