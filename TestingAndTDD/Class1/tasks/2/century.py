def get_century(year):
    if year < 1:
        return "Nice! You are not even in a first century yet!"
    else:
        return f"You are in the {((year - 1) // 100) + 1} century"


if __name__ == "__main__":
    user_input = int(input("Enter the year: "))
    print(get_century(user_input))

