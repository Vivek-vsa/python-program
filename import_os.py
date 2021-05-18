import os

oldname = "sample2.txt"    #file that is saved in your folder with this name and this file will delete
newname = "renamed_by_python.txt"  #file name that you want to be by replacing the old name 
with open(oldname) as f:
    content = f.read()

with open(newname, "w") as f:
    f.write(content)

os.remove(oldname)