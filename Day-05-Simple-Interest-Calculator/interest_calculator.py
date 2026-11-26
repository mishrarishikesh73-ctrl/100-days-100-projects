def calculate_interest(P,R,T):
    interest = (P*R*T)/100
    total_amount = P+interest
    return interest,total_amount


print("===========================")
print(" SIMPLE INTEREST CALCULATOR")
print("===========================")


try:
    P = float(input("Enter p amount"))
    R = float(input("Enter annual interest rate(%)"))
    T = float(input("Enter time in year"))

    if P <0 or R < 0 or T <0:
        print("Please enter non-nagtive value.")
    else:
        interest ,total = calculate_interest(
            P , R , T
        )    

        print("\n--------- RESULT ---------")
        print(f"Principal Amount: ₹{P:.2f}")
        print(f"Interest Rate: {R:.2f}%")
        print(f"Time: {T:.2f} years")
        print(f"Simple Interest: ₹{interest:.2f}")
        print(f"Total Amount: ₹{total:.2f}")
except ValueError:
    print("Invalid input! please enter numeric values")        


    