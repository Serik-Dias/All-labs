import os
path = str(input("Enter the directory path: "))  #/Users/diastursynbek/Downloads/KBTU/PP2/PYTHON/     покажет содержимые папки и файлы

if os.access(path, os.F_OK):
    list = os.listdir(path)
    print("Files and Folders")
    for i in list:
        print(i)
else:
    print("path is wrong! ")