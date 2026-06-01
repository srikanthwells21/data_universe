# Create a new file Example2.txt for writing
with open('Example1.txt', 'w') as file1:
    writemgmt = file1.write("This is line A\n")
    writemgmt = file1.write("This is line B\n")
    # file1 is automatically closed when the 'with' block exits

    print(writemgmt)