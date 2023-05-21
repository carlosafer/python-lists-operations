# Creating a list
names = ["Joao", "Maria", "Ana", "Julia", "Pedro"]

# Printing on console
print("List:", names, "\n")

# Assigning variable 's' to store the list size
s = len(names)
print(s, "\n")

# Scrolling through the list
print("Elements printed one by one:")
for x in names:
    print(x)
print()

# Acessing the element number 2 of a list
z = names[2]
print("Element number 2: ", z, "\n")

# Adding a element
names.append('Marco')
print("Marco was added to the list: ", names, "\n")

# Removing a element
names.remove('Joao')
print("Joao was removed from the list: ",  names, "\n")

# Removing a element by index
names.pop(1)
print("Element 1 was removed: ", names, "\n")

# Filtering elements witch start with the letter 'M'
filtered_names = [name for name in names if name.startswith("M")]
print("Names filtered starting with letter 'M': ", filtered_names)


