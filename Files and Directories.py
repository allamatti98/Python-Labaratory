#Check if a directory exists, create a directory, remove a directory.
#Print out all Python files in currenct directory, then print out all files in current directory.
from pathlib import Path
p1 = Path()
print(p1.exists())
for file in p1.glob("*"):
    print(file)










"""
from pathlib import Path


path1 = Path() #If you dont parse an argument it parses the current directory.
path2 = Path("Speed") #Can use a string to reference directory
print(path1.exists())
print(path2.exists())
#path3 = Path("Maverick")
#path3.mkdir() Create directory
#path4 = Path("Bossman")
#path4.rmdir() #To remove directory


path5 = Path()
for file in path5.glob("*.py"):
    print(file)

path6 = Path()
for file in path6.glob("*"):
    print(file)
"""