def is_palindrome(s):
    return s == s[::-1]

print(is_palindrome("abba"))   
print(is_palindrome("abc"))   
print(is_palindrome("a"))     
print(is_palindrome("acbca"))  
