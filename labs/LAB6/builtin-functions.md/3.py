def is_palindrome(s):
    s = s.lower().replace(" ", "") 
    return s == s[::-1]  


text = input("Enter the word:")

if is_palindrome(text):
    print("It's a palindrome")
else:
    print("It's not a palindrome.")