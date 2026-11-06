import secrets
import string


def generate_password(length):

    characters = (
        string.ascii_letters
        + string.digits
        + string.punctuation
    )

    password = ''.join(
        secrets.choice(characters)
        for _ in range(length)
    )

    return password


print("================================")
print("       PASSWORD GENERATOR")
print("================================")

while True:

    user_input = input(
        "\nEnter password length (or exit): "
    )

    if user_input.lower() == "exit":
        print("Thank you for using Password Generator!")
        break

    try:

        length = int(user_input)

        if length < 8:
            print("Password must be at least 8 characters.")
            continue

        password = generate_password(length)

        print("\n--------- GENERATED PASSWORD ---------")
        print(password)
        print("--------------------------------------")

    except ValueError:

        print("Invalid input! Please enter a number.")