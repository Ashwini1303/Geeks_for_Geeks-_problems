my_list = [1, 2, 3, 4, 5]
my_list[0], my_list[-1] = my_list[-1], my_list[0]

print("List after swapping first and last elements:", my_list)

#first and last values in a list using * operand
'''
def swapList(list):
    
    start, *middle, end = list
    list = [end, *middle, start]
    
    return list
    
newList = [12, 35, 9, 56, 24]
print(swapList(newList))'''


# Swap first and last values in a list using Slicing
'''
def swap_first_last_3(lst):
    # Check if list has at least 2 elements
    if len(lst) >= 2:
        # Swap the first and last elements using slicing
        lst = lst[-1:] + lst[1:-1] + lst[:1]
    return lst
inp=[12, 35, 9, 56, 24]
print("The original input is:",inp)
result=swap_first_last_3(inp)
print("The output after swap first and last is:",result)'''
