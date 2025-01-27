def reverseWords(s):
    s = s.strip()
    words = s.split()
    words.reverse()
    result = " ".join(words)
    return result

s1 = " i like this program very much "
print(reverseWords(s1))  

s2 = " pqr mno "
print(reverseWords(s2))  

s3 = " a "
print(reverseWords(s3)) 
