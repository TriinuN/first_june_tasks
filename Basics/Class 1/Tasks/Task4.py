# This equation x2 + y2 + z2 – 3xyz formula: (x + y + z)(x2 + y2 + z2 – xy – yz -xz)
print("Let's solve equation ;) ")
x = int(input("Please enter numberx"))
y = int(input("Please enter numbery"))
z = int(input("Please enter numberz"))
Equation = x**2 + y**2 + z**2 -3*x*y*z
print("The result of this equation is: ", Equation)
print("Now let's try with formula")
Formula = (x + y + z) * (x**2 + y**2 - x * y - y * z - x * z)
print("The result of this equation is: ", Formula)