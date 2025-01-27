def are_anagrams(s1, s2):
    return sorted(s1) == sorted(s2)

print(are_anagrams("geeks", "kseeg"))      
print(are_anagrams("allergy", "allergic")) 
print(are_anagrams("g", "g"))              
