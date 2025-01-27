def combine_strings(a, b):
    if len(a) < len(b):
        return a + b + a 
    else:
        return b + a + b
    
a = "Hi"
b = "There"
print(combine_strings(a, b))  

a = "Hello"
b = "Go"
print(combine_strings(a, b))  
