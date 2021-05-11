greeting = "Good Morning, "
name = "Vivek"
print(type(name))
#Concatenating two strings
c = greeting + name
print(c)

user = "Vivek"
print(user[4])  #--> Prints the index 4 value only
# user[3] = "d" --> Does not work .We can't change the value in string


print(user[1:4]) #prints values from index 1to3 , it cannot print 4th index value
print(user[:4])  # is same as user[0:4]

v = user[-4:-1] # is same is user[1:4] print(c)
print(user[1:])

intro = "VivekIsGood"
d = intro[0::3]  #skips the two elements and takes the third element and print it ie.Veso is output
e = intro[::-1]  #prints in reverse order
print(d)
print(e)