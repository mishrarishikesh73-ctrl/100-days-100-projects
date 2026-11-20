
expenses = []

def add_expense():
    category = input("Enter category (Food/Travel/Shopping/Other): ")
    description = input("Enter description: ")

    try:
        amount = float(input("Enter amount (₹): "))

        if amount <= 0:
            print("Amount must be greater than zero!")
            return

        expense = {
            "category": category,
            "description": description,
            "amount": amount
        }

        expenses.append(expense)
        print("Expense added successfully!")

    except ValueError:
        print("Please enter a valid amount!")


def view_expenses():
    if not expenses:
        print("\nNo expenses recorded!")
        return

    print("\n======= ALL EXPENSES =======")

    for index, expense in enumerate(expenses, start=1):
        print(
            f"{index}. {expense['category']} | "
            f"{expense['description']} | "
            f"₹{expense['amount']:.2f}"
        )


def total_expenses():
    total = sum(expense["amount"] for expense in expenses)
    print(f"\nTotal Expenses: ₹{total:.2f}")


def category_summary():
    if not expenses:
        print("\nNo expenses recorded!")
        return

    summary = {}

    for expense in expenses:
        category = expense["category"].title()
        summary[category] = summary.get(category, 0) + expense["amount"]

    print("\n======= CATEGORY SUMMARY =======")

    for category, amount in summary.items():
        print(f"{category}: ₹{amount:.2f}")


while True:
    print("\n======= EXPENSE TRACKER =======")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Total Expenses")
    print("4. Category Summary")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_expense()
    elif choice == "2":
        view_expenses()
    elif choice == "3":
        total_expenses()
    elif choice == "4":
        category_summary()
    elif choice == "5":
        print("Thank you for using Expense Tracker!")
        break
    else:
        print("Invalid choice! Try again.")
