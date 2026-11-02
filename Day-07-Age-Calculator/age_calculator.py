from datetime import date


def calculate_age(dob, today):

    years = today.year - dob.year

    if (today.month, today.day) < (dob.month, dob.day):
        years -= 1

    last_birthday = date(
        today.year - (1 if (today.month, today.day) < (dob.month, dob.day) else 0),
        dob.month,
        dob.day
    )

    next_birthday = date(today.year, dob.month, dob.day)

    if next_birthday < today:
        next_birthday = date(today.year + 1, dob.month, dob.day)

    days_lived = (today - dob).days
    days_remaining = (next_birthday - today).days

    return years, days_lived, days_remaining


print("================================")
print("         AGE CALCULATOR")
print("================================")

try:

    dob_input = input("Enter DOB (YYYY-MM-DD): ")

    dob = date.fromisoformat(dob_input)

    today = date.today()

    if dob > today:
        print("Date of birth cannot be in the future.")

    else:

        age, days_lived, days_remaining = calculate_age(
            dob, today
        )

        print("\n========== YOUR RESULT ==========")

        print(f"Date of Birth: {dob}")
        print(f"Age: {age} years")
        print(f"Total Days Lived: {days_lived} days")
        print(f"Next Birthday In: {days_remaining} days")

        print("================================")

except ValueError:
    print("Invalid date! Please use YYYY-MM-DD format.")