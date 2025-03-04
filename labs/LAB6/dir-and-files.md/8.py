import os

file_path = "examplefordelete.txt"

if os.path.exists(file_path) and os.access(file_path, os.W_OK):
    os.remove(file_path)
    print("Файл удалён!")
else:
    print("Файл не найден или нет разрешения")