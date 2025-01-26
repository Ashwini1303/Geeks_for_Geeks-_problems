def find_union_count(a, b):
    union_set = set(a).union(b)
    return len(union_set)

a1 = [1, 2, 3, 4, 5]
b1 = [1, 2, 3]
print("Output:", find_union_count(a1, b1))  

a2 = [85, 25, 1, 32, 54, 6]
b2 = [85, 2]
print("Output:", find_union_count(a2, b2)) 

a3 = [1, 2, 1, 1, 2]
b3 = [2, 2, 1, 2, 1]
print("Output:", find_union_count(a3, b3))  
