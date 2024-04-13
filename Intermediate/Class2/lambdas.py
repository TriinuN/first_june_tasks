# def function_sum(x):: See rida defineerib funktsiooni nimega function_sum, mis võtab ühe argumendi x.
def function_sum(x):
    # return x + 5: See rida ütleb funktsioonile, mida tagastada. Antud juhul see lihtsalt lisab argumendile x väärtusele 5
    # ja tagastab selle tulemuse.
    return x + 5

# function_sum(9): Siin kutsutakse funktsiooni function_sum argumentiga 9. Seejärel tagastab funktsioon 9 + 5, mis on 14
function_sum(9)
# l_sum = lambda x: x + 5: See rida defineerib lambda funktsiooni, mis teeb täpselt sama asja, mis function_sum
# They are the same thing
# funktsioon - see lisab 5 argumendile x. Seejärel määratakse see lambda funktsioon muutujasse l_sum.
l_sum = lambda x: x + 5
# l_sum(9): Siin kutsutakse lambda funktsiooni l_sum argumentiga 9. Nagu eelnevalt mainitud, teeb see sama asja mis
# function_sum(9), tagastades 9 + 5, mis on jällegi 14.
l_sum(9)
# (lambda x: x * 9)(2): See on lambdafunktsiooni otse kasutamine. See loob lambdafunktsiooni, mis korrutab argumendi x
# 9-ga ja seejärel kohe kutsutakse seda argumendiga 2, tagastades 2 * 9, mis on 18.
# print((lambda x: x * 9)(2)): See trükib eelnevalt mainitud lambda funktsiooni tulemuse, mis on 18.
print((lambda x: x * 9)(2))

print('')
example_list = [5, 2, 3, 4, 6, 7, 8, 9]
# Function filter
filter_result = list(filter(lambda x: x % 2 == 0, example_list))

print(filter_result)
print('')
# Function math
map_result = list(map(lambda x: x + 2, example_list))
list_method = [x + 2 for x in example_list]

print(map_result)
print(list_method)
print('')
# Sorting (esimese nr järgi)
example_list_sort = [[1, 3], [3, 1], [4, 2], [2, 4]]
simple_sorted = sorted(example_list_sort)

print(simple_sorted)
# Teise järgi sorteerimine
smarter_sorted = sorted(example_list_sort, key=lambda x: x[1])
print('')
print(smarter_sorted)
