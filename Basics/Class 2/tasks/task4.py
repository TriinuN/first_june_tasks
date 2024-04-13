# Create a list with 5 names in it. Append one name, insert one name at the start of the list, sort and reverse
# the list. Print out the indexes of these added names.

names = ["Mari", "Liis", "Mart", "Karl", "John"]
names.append('Johanna')
names.insert(0, 'Alizee')
names.sort()
print(names)
names.reverse()
print(names)
index_of_Johanna = names.index('Johanna')
print(f"The index of Johanna in this list is: {names.index('Johanna')}")
index_of_Alizee = names.index('Alizee')
print(f"The index of Alizee in this list is: {names.index('Alizee')}")