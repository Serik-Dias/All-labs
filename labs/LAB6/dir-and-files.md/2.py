import os
path = str(input("Enter the directory path: "))   #input --> example.txt
print(os.access(path, os.F_OK)) # Existence
print(os.access(path, os.R_OK)) # Readability
print(os.access(path, os.W_OK)) # Writeability
print(os.access(path, os.X_OK)) # Executeability