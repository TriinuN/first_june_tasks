# String Manipulation:
# Write a function that accepts a string and replaces all spaces with underscores.
# Additionally,convert the string to lowercase. Display the modified string.


text = "Cupcake ipsum dolor sit amet toffee cupcake. Cheesecake bonbon jelly beans macaroon toffee danish cake. Cake pudding lemon drops pudding liquorice pie dragée ice cream. Powder I love I love tootsie roll jelly beans muffin. I love sweet bear claw liquorice shortbread dessert. Chocolate marshmallow sesame snaps fruitcake gingerbread chocolate cake. Toffee cake dragée pastry souffle jelly-o lemon drops. Marshmallow cupcake danish chupa chups halvah."


def modify(original):
    return original.replace(" ", "_").lower()



print(modify(text))