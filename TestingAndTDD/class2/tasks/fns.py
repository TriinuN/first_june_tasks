# Task 1
def add(a, b):
    return a + b


# Task 2
def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True


# Task 3
def reverse_string(example_text):
    example_text = example_text[::-1]
    return example_text


# Task dec
def is_palindrome(s):
    return s == s[::-1]


# Task 5
def factorial(n):
    return 1 if (n == 1 or n == 0) \
        else n * factorial(n - 1)


# Task 6
def find_max(a):
    if not a:
        return None
    return max(a)


# Task 7
def is_leap_year(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


# Task 8
def remove_duplicates(dup_list):
    return list(set(dup_list))


# Task 9
def are_anagrams(first, second):
    if sorted(first) == sorted(second):
        return True
    return False


if __name__ == "__main__":
    text1 = input("Enter the first word: ")
    text2 = input("Enter the second word: ")

    if are_anagrams(text1, text2):
        print("Anagram")
    else:
        print("Not Anagram")


# Task 10
def celsius_to_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32





