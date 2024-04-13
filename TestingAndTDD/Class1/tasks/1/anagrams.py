def is_anagram(first, second):
    if sorted(first) == sorted(second):
        return True
    return False

if __name__ == "__main__":
    text1 = input("Enter the first word: ")
    text2 = input("Enter the second word: ")

    if is_anagram(text1, text2):
        print("Anagram")
    else:
        print("Not Anagram")


# (angel, glean), (dusty, study),  (cat, act)