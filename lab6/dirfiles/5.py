#Write a Python program to write a list to a file.
list = ['Aidana', 'JK', 'JM', 'JIN', 'V']

filename=input()

with open(filename, "w") as f:
    for x in list:
        f.write(x + "\n")

print("List was written to", filename)