print("Hello Mr. Eimantas, nice to meet you!")

titel = "Mr."
name = "Eimantas"
print("")

# + Method
print("Hello " + titel + " " + name + ", nice to meet you!")
print("")

# printf method
print("Hello %s %s, nice to meet you! "%(titel,name))
print("")

# str.format()
print("Hello {} {}, nice to meet you! " .format(titel, name))
print("Hello {name} {titel}, nice to meet you! " .format(titel=titel, name=name))
print("Hello {0} {1}, nice to meet you! " .format(titel, name))
print("")

# f-string
print(f"Hello {titel} {name}, nice to meet you!")
print("Hello {titel} {name}, nice to meet you!")
print("")

# rounding
number= 109.7589372589
print(f"{number:.3f}")
print(f"{round(number, 3)}")
