def convert_length(value,choice):
  if choice == "1" :
    return value * 0.621371
  elif choice == "2":
    return value * 1000
  elif choice == "3":
    return value * 3.288084


def convet_weigth(value,choice):
  if choice == "1":
    return value * 2.20462
  elif choice == "2":
   return value * 1000


def convert_time(value,choice):
   if choice == "1":
     return value * 60
   elif choice == "2":
    return value * 60




print("=======UNIT CONVERTER====")
print("1. Length")
print("2. Weigth")
print("3. Time")

category = input("Choose category(1-3):")

try:
  value = float(input("Enter value:"))


  if value < 0:
    print("Please enter a non-nagative value")
  elif category == "1":

    print("\n1. Kilometer to Miles ")
    print("2. Kilometer to Meter")
    print("3. Meters to Feet")


    choice = input("Choose conversion:")

    if choice in ("1","2","3"):
      result = convert_length(value , choice)
      print(f"Result :{result : 2f}")
    else:
      print("Invalid conversion choice.")
  elif category == "2":
    print("\n1. Kilogrmas to pounds")
    print("2. Kilogrmas to Grams")

    choice = input("Choose conversion:")
    if choice in ("1","2"):
      result = convert_time(value ,choice)
      print(f"Result : {result:.2f}")
    else:
      print("Invalid conversion choice.")

  else :
    print("Invalid category.")
except ValueError:
  print("Please enter a valid number")          



 

    