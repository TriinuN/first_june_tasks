def process_payment(amount):
    card_number = input("Please submit your card number: ")
    expiry_date = input("Please enter the expiry date: ")
    cvv = input("Enter your cvv: ")
    if len(card_number) == 5 and expiry_date and cvv:
        return True
    else:
        return False


def make_payment():
    while True:
        amount = float(input("Please enter the amount to be paid: $"))
        if process_payment(amount):
            print("Payment successful.")
            break
        else:
            print("Payment failed. Try again.")
        choice = input("Do you want to cancel payment? ")
        if choice == "yes":
            print("Payment cancelled.")
            break


make_payment()
