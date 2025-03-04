items = ["Apple", "Banana", "Cherry"]

with open("example.txt", "w") as file:
    file.write("\n".join(items))