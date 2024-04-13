some_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]     # Iterable

for item in some_list:                      # Iteration
    print(item)

print('-=' * 20)

some_list2 = iter([20, 10, 30, 40, 50, 60, 70, 80, 90, 100])    # Interator
# print("first")
# print(next(some_list2))
# print(next(some_list2))
# print(next(some_list2))
# print(next(some_list2))


# while True:
#     try:
#         print(next(some_list2))
#     except StopIteration:
#         print("Done")
#         break


# Generator
def generator():
    some_text = "bla bla bla"
    some_number = 0
    for _ in range(50):
        some_number += 1
        yield f'{some_text} - {some_number}'
        print('Yield Done its job')


for item in generator():
    print(item)
