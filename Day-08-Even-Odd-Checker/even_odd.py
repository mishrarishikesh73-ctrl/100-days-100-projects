def even_odd(number):
    if number == 0:
        number_type = "Zero"
    elif number > 0:
        number_type = "Postive"
    else: 
        number_type = "negtive"


    if number % 2 == 0:
        parity = "Even"
    else:
        parity = "odd"
    return number_type,parity
print("======================")
print("      EVEN ODD CHECKER")
print("=======================")

while True:
    user_input = input(
        "\n Enter a number (or type exit):"

    ) 
    if user_input.lower() == "exit":
        print("Thank you for using the program!")

    try:
        number = int(user_input)   
        number_type,parity = even_odd(number)
        print("\n----------RESULT--------")
        print(f"Number:{number}")
        print(f"Type:{number_type}")
        print(f"Parity:{parity}")
        print("-------------------")
    except ValueError:
        print("Invalid input! Please enter an integer.")    
        





        
