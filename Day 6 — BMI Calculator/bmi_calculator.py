def bmi_calculator(weight,Height):
    bmi = weight /(Height ** 2)
    return bmi


def get_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25:
        return "Healthy Weight"
    elif bmi < 30:
        return "Overweight"
    else :
        return "Obesity"


print("=========================")
print("        BMI CALCULATOR") 
print("=========================")

try:
    weight = float(input("Enter your weigth(kg): "))
    Heigth = float(input("Enter your Heigth(meters: "))

    if weight <= 0 or Heigth <= 0:
        print("Please enter postive Values.")
    else:
        bmi = bmi_calculator(weight , Heigth)
        category  = get_category(bmi)
        print("\n=========RESULT ======")
        print(f"Weight:{weight} Kg")
        print(f"Heigth:{Heigth} meters")
        print(f"BMI:{bmi:2f}")
        print(f"Category:{category}")
except ValueError:
    print("Invalid input! Please enter number")




