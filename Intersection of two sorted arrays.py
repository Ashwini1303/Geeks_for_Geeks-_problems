def find_intersection_count(a, b):
    intersection_set = set(a).intersection(b)
    return len(intersection_set)

a1 = [1, 2, 3, 4, 5]
b1 = [1, 2, 3]
print("Output:", find_intersection_count(a1, b1))  

a2 = [85, 25, 1, 32, 54, 6]
b2 = [85, 2]
print("oUTPUT: ",find_intersection_count(a2, b2)) 

a3 = [1, 2, 1, 1, 2]
b3 = [2, 2, 1, 2]
print("Output: ",find_intersection_count(a3, b3))
