# Word Count:
# Write a function that takes a sentence as input and returns the count of each word in the sentence.
# Use a dictionary to store the word counts. Allow the user to input a sentence and display the word
# count results.
import json

text = "Cupcake ipsum dolor sit amet toffee cupcake. Cheesecake bonbon jelly beans macaroon toffee danish cake. Cake pudding lemon drops pudding liquorice pie dragée ice cream. Powder I love I love tootsie roll jelly beans muffin. I love sweet bear claw liquorice shortbread dessert. Chocolate marshmallow sesame snaps fruitcake gingerbread chocolate cake. Toffee cake dragée pastry souffle jelly-o lemon drops. Marshmallow cupcake danish chupa chups halvah."
words_counter = {}

words_list = text.split()

for word in words_list:
    if words_counter.get(word.strip(".")):
        words_counter[word.strip(".")] += 1
        # print("In")
    else:
        words_counter[word.strip(".")] = 1
        # print("Not in")

print(json.dumps(words_counter, indent=2))