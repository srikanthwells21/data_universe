# Write line to file
exmp2 = 'Example2.txt'
with open(exmp2, 'w') as writefile:
    writefile.write("This is line A\n")
    writefile.write("This is line B\n")

# Read file

with open(exmp2, 'r') as testwritefile:
    print(testwritefile.read())    

# Check whether write to file

with open(exmp2, 'r') as testwritefile:
    print(testwritefile.read())    

# Sample list of text

Lines = ["This is line X\n", "This is line Y\n", "This is line Z\n"]
Lines    

# Write the strings in the list to text file

with open('Example2.txt', 'w') as writefile:
    for line in Lines:
        print(line)
        writefile.write(line)


# Verify if writing to file is successfully executed

with open('Example2.txt', 'r') as testwritefile:
    print(testwritefile.read())        

# with open('Example2.txt', 'w') as writefile:
#     writefile.write("Overwrite\n")
with open('Example2.txt', 'r') as testwritefile:
    print(testwritefile.read())    

# Write a new line to text file

with open('Example2.txt', 'a') as testwritefile:
    testwritefile.write("This is line P\n")
    testwritefile.write("This is line Q\n")
    testwritefile.write("This is line R\n")    

# Verify if the new line is in the text file
with open('Example2.txt', 'r') as testreadfile:
    print(testreadfile.read())

with open('Example3.txt', 'a+') as testwritefile:
    testwritefile.write("This is line E\n")
    print(testwritefile.read())    


with open('Example4.txt', 'a+') as testwritefile:
    print("Initial Location: {}".format(testwritefile.tell()))  

    data = testwritefile.read()
    if (not data):  #empty strings return false in python
            print('Read nothing') 
    else: 
            print(testwritefile.read())
            
    testwritefile.seek(0,0) # move 0 bytes from beginning.
    
    print("\nNew Location : {}".format(testwritefile.tell()))
    data = testwritefile.read()
    if (not data): 
            print('Read nothing') 
    else: 
            print(data)
    
    print("Location after read: {}".format(testwritefile.tell()) )      

    with open('Example4.txt', 'r+') as testwritefile:
        testwritefile.seek(0,0) #write at beginning of file
        testwritefile.write("Line 1" + "\n")
        testwritefile.write("Line 2" + "\n")
        testwritefile.write("Line 3" + "\n")
        testwritefile.write("Line 4" + "\n")
        testwritefile.write("finished\n")
        testwritefile.seek(0,0)
        print(testwritefile.read())

with open('Example4.txt', 'r+') as testwritefile:
    testwritefile.seek(0,0) #write at beginning of file
    testwritefile.write("Line 1" + "\n")
    testwritefile.write("Line 2" + "\n")
    testwritefile.write("Line 3" + "\n")
    testwritefile.write("Line 4" + "\n")
    testwritefile.write("finished\n")
    #Uncomment the line below
    testwritefile.truncate()
    testwritefile.seek(0,0)
    print(testwritefile.read())      


# Copy file to another

with open('Example4.txt','r') as readfile:
    with open('Example5.txt','w') as writefile:
          for line in readfile:
                writefile.write(line)      

# Verify if the copy is successfully executed

with open('Example5.txt','r') as testwritefile:
    print(testwritefile.read())                


#Run this prior to starting the exercise
from random import randint as rnd

memReg = 'members.txt'
exReg = 'inactive.txt'
fee =('yes','no')

def genFiles(current,old):
    with open(current,'w+') as writefile: 
        writefile.write('Membership No  Date Joined  Active  \n')
        data = "{:^13}  {:<11}  {:<6}\n"

        for rowno in range(20):
            date = str(rnd(2015,2020))+ '-' + str(rnd(1,12))+'-'+str(rnd(1,25))
            writefile.write(data.format(rnd(10000,99999),date,fee[rnd(0,1)]))


    with open(old,'w+') as writefile: 
        writefile.write('Membership No  Date Joined  Active  \n')
        data = "{:^13}  {:<11}  {:<6}\n"
        for rowno in range(3):
            date = str(rnd(2015,2020))+ '-' + str(rnd(1,12))+'-'+str(rnd(1,25))
            writefile.write(data.format(rnd(10000,99999),date,fee[1]))


genFiles(memReg,exReg)    