#This is a basic code dealing with I/O basic functions in Python
#Specifically, it is meant to work with .txt files

#First, oppening a txt file
myfile = open("myfile.txt")

#Now, it is common to read what is written on it
print(myfile.read())

#It is important to know that the cursor will not reset automatically.
#So, if you want to read it again, the result would be a blank space.
print(myfile.read())

#In order to read it from the beginning:
myfile.seek(0)
print(myfile.read())
myfile.seek(0)

#It is possible to store the values inside of a txt file on a variable:
contents = myfile.read()
print(contents)

#The next step is read just a specific line:
myfile.seek(0)
print(myfile.readlines())

#Best practices for opening files:

#When you are not working with the .txt file, it is a good practice closing it
#Imagine you want to delete this file on your PC.
#If you try to do that, the Python will be using. So you will not be able.
#So, you can use:
myfile.close()

#It is also a good method using the statement 'with'.
#Using it, it will run a block of code and, when finished, it will automatically close the file.
with open("myfile.txt",mode='r') as myfile:
    contents = myfile.read()
    print(contents)

#Oppening modes for .txt files
#mode = 'r' is read only
#mode = 'w' is write only (will overwrite files or create new!)
#mode = 'a' is append only (will add on to file)
#mode = 'r+' is reaading and writing
#mode = 'w+' is writing and reading (Overwrites wxisting files or creates a new file!)

with open("my_new_file.txt",mode='r') as f:
    print(f.read())

with open("my_new_file.txt",mode='a') as f:
    f.write('\nFOUR ON FOURTH')

with open("my_new_file.txt",mode='r') as f:
    print(f.read())

with open("njirwiohriu.txt", mode='w') as f1:
    f1.write("BRUNO GM ALVES")


