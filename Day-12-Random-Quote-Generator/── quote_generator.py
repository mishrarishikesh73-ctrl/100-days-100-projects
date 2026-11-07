import random


def generate_quote():

    quotes = [
        "Believe in yourself and your abilities.",
        "Great things take time.",
        "Never stop learning.",
        "Success starts with hard work.",
        "Dream big and work hard.",
        "Consistency is the key to success.",
        "Every day is a new opportunity.",
        "Failure is the first step towards success.",
        "Stay focused and never give up.",
        "Your future depends on what you do today."
    ]

    return random.choice(quotes)


print("================================")
print("      RANDOM QUOTE GENERATOR")
print("================================")

while True:

    print("\n1. Generate Quote")
    print("2. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "1":

        quote = generate_quote()

        print("\n--------- YOUR QUOTE ---------")
        print(quote)
        print("------------------------------")

    elif choice == "2":

        print("Thank you for using Quote Generator!")
        break

    else:

        print("Invalid choice! Please select 1 or 2.")