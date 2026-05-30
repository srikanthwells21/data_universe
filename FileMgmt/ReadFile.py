# Read the Example1.txt
example1 = rf"C:\Data_Universe\example1.txt"
file1 = open(example1, "r")

# Print the path of file

print(file1.name)
file1.mode

# Read the file

FileContent = file1.read()
print(FileContent)
print("********************************")
# Print the file with '\n' as a new line

print(FileContent)
print(type(FileContent))

# Close file after finish

file1.close()

# Open file using with

with open(example1, "r") as file2:
    FileContent2 = file2.read()

    # See the content of file

    print(FileContent2)

# Read first four characters

with open(example1, "r") as file3:
    print(file3.read(4))

# Read certain amount of characters

with open(example1, "r") as file4:
    print(file4.read(4))
    print(file4.read(4))
    print(file4.read(7))
    print(file4.read(15))

# Read one line

with open(example1, "r") as file5:
    print("first line: " + file5.readline())

with open(example1, "r") as file6:
    print(file6.readline(20)) # does not read past the end of line
    print(file6.read(20)) # Returns the next 20 chars

# Iterate through the lines

with open(example1,"r") as file7:
        i = 0;
        for line in file7:
            print("Iteration", str(i), ": ", line)
            i = i + 1                    

# Read all lines and save as a list

with open(example1, "r") as file8:
    FileasList8 = file8.readlines()

# Print the first line

    FileasList8[0]                