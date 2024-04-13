# "r" - read mode (default value).
# "w" - write mode.
# "x" - creation mode. If the file already exists, the operation fails.
# "a" - appending mode.
# "b" - binary mode.
# "t" - text mode (default value).
# "+" - updating mode (read / write).

# f = open("example.txt")
# print(f.readline())

# f.close()

with open("example.txt", "r+") as f:    #without + it is unreadable
    print(f)
    # print(f.readline())
    # f.write("\nLines")
    # f.writelines(["some\n", "New\n", "Text\n", "TO\n", "FILE\n"])

    # print(f.readline()) #if you but lines it will print all lines on the same row
    # print("---------------------------")

    keys = f.readline().strip().split(',')  #name, surname, age
    lines = f.readlines()  # ["Triinu,Niklus,27", "Marken, Piirisalu,7"]
    my_people = []
    for line in lines:
        person = line.strip().split(",") # ["Triinu","Niklus","27"]
        person_dict = {}
        for index, attribute in enumerate(person):
            person_dict[keys[index]] = attribute
        my_people.append(person_dict)

print(my_people)