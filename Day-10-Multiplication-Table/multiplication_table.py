def generate_table(number, limit):

    print(f"\nMultiplication Table of {number}")
    print("--------------------------------")

    for i in range(1, limit + 1):

        result = number * i

        print(f"{number} x {i} = {result}")

    print("--------------------------------")


print("================================")
print("   MULTIPLICATION TABLE GENERATOR")
print("================================")

while True:

    user_input = input("\nEnter a number (or exit): ")

    if user_input.lower() == "exit":
        print("Thank you for using the program!")
        break

    try:

        number = int(user_input)

        limit = int(input("Enter table limit: "))

        if limit <= 0:
            print("Please enter a positive limit.")
            continue

        generate_table(number, limit)

    except ValueError:

        print("Invalid input! Please enter integers.")