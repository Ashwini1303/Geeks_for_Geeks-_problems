def trim(input_str):
    return input_str.strip()

def exists(input_str, x):
    return input_str.find(x)

def titleIt(input_str):
    return input_str.title()

def casesSwap(input_str):
    return input_str.swapcase()

str = " hello "  
x = "llo"

trimmed_str = trim(str)
index_of_x = exists(trimmed_str, x)
titled_str = titleIt(trimmed_str)
swapped_str = casesSwap(trimmed_str)

print(trimmed_str)
print(index_of_x)   
print(titled_str)   
print(swapped_str) 
