def find_min_and_max(arr):
    if not arr:
        return None, None
    minimum = maximum = arr[0]
    for num in arr:
        if num < minimum:
            minimum = num
        if num > maximum:
            maximum = num
    return minimum, maximum

arr1 = [3, 2, 1, 56, 10000, 167]
arr2 = [1, 345, 234, 21, 56789]
arr3 = [56789]

print("Output:", find_min_and_max(arr1)) 
print("Output:", find_min_and_max(arr2))  
print("Output:", find_min_and_max(arr3))  
