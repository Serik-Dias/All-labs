def count_letters(s):
    uppercase_count = sum(1 for c in s if c.isupper())      #1++
    lowercase_count = sum(1 for c in s if c.islower())      #1++
    return uppercase_count, lowercase_count
text = input("Input: ")

upper, lower = count_letters(text)

print(f"Upper: {upper}, Lower: {lower}")