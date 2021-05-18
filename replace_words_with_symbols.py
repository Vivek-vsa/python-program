with open("sample.txt") as f:
    content = f.read()

content = content.replace("donkey", "$%^@$^#")  #it replaces the donkey with censored content, values, symbols

with open("sample.txt", "w") as f:
    f.write(content)