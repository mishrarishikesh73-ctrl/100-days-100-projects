def celsius_to_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32


def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9


def celsius_to_kelvin(celsius):
    return celsius + 273.15


def kelvin_to_celsius(kelvin):
    return kelvin - 273.15


print("================================")
print("     TEMPERATURE CONVERTER")
print("================================")

print("\n1. Celsius → Fahrenheit")
print("2. Fahrenheit → Celsius")
print("3. Celsius → Kelvin")
print("4. Kelvin → Celsius")

choice = input("\nChoose an option (1-4): ")

try:
    temperature = float(input("Enter temperature: "))

    if choice == "1":
        result = celsius_to_fahrenheit(temperature)
        print(f"\nResult: {result:.2f} °F")

    elif choice == "2":
        result = fahrenheit_to_celsius(temperature)
        print(f"\nResult: {result:.2f} °C")

    elif choice == "3":
        result = celsius_to_kelvin(temperature)
        print(f"\nResult: {result:.2f} K")

    elif choice == "4":
        result = kelvin_to_celsius(temperature)

        if result < -273.15:
            print("\nInvalid temperature!")

        else:
            print(f"\nResult: {result:.2f} °C")

    else:
        print("\nInvalid choice!")

except ValueError:
    print("\nPlease enter a valid number.")