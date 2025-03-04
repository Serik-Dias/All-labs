with open("example2.txt", "r") as src, open("destination.txt", "w") as dst: #Этот код копирует содержимое файла "example.txt" в новый файл "destination.txt".
    dst.write(src.read())