f = open('poems.txt')
t = f.read()            #you have to create a poems.txt file before runs the program
if 'twinkle' in t:
    print("Twinkle is present")
else:
    print("Twinkle is not present")
f.close()