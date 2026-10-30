def calculate_interest(principal, rate, time):

    interest = (principal * rate * time) / 100

    total_amount = principal + interest

    return interest, total_amount


print("==============================")
print("   SIMPLE INTEREST CALCULATOR")
print("==============================")

try:
    principal = float(input("Enter principal amount: "))
    rate = float(input("Enter annual interest rate (%): "))
    time = float(input("Enter time in years: "))

    if principal < 0 or rate < 0 or time < 0:
        print("Please enter non-negative values.")

    else:
        interest, total = calculate_interest(
            principal, rate, time
        )

        print("\n--------- RESULT ---------")
        print(f"Principal Amount: ₹{principal:.2f}")
        print(f"Interest Rate: {rate:.2f}%")
        print(f"Time: {time:.2f} years")
        print(f"Simple Interest: ₹{interest:.2f}")
        print(f"Total Amount: ₹{total:.2f}")

except ValueError:
    print("Invalid input! Please enter numeric values.")