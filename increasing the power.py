def printIncreasingPower(x):
    power = 1  
    while power <= 5:  
        print(x ** power, end=" ") 
        power += 1 
x = int(input("Enter the number: "))
printIncreasingPower(x)

