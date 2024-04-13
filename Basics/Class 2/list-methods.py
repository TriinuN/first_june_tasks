cars = ["VW", "Audi", "BMW"]

# Adding values to the list
cars.append("Mazda")
cars.append("Volvo")
cars.append("Cupra")
# Joining lists
cars.extend(["Nissan", "Zap", "Opel", "VW"])
# Length of cars list
print(len(cars))
# Sort the list
cars.sort()
# Get a count of certain cars
print(f'Amount Volkswagens in the list: {cars.count("VW")}')
# Get the index of certain record
index_of_coupra = cars.index('Cupra')
print(f"The index of Cupra in this list is: {cars.index('Cupra')}")
# Inserting at a certain index
cars.insert(index_of_coupra, "Opel")
print(cars)
# Remove item from the list at the index
cars.pop(index_of_coupra)
# Remove the last item from the list
cars.pop()
# Reverse the list
cars.reverse()
# Clear the list
cars.clear()

print(cars)
