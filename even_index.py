def stringjumper(string):
    for i in range(len(string)):
        if i % 2 == 0:  
            print(string[i], end=" ")  
string = input("Enter the string: ")
stringjumper(string)


