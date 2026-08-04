def Celsius_to_Fahrenheit_Converter(Celsius):
    print("Celsius to Fahrenheit Converter")
    return (Celsius * 9 / 5) + 32


def Celsius_to_Kelvin_Converter(Celsius):
    print("Celsius to Kelvin Converter")
    return Celsius + 273.15


def Kelvin_to_Celsius_Converter(Kelvin):
    print("Kelvin to Celsius Converter")
    return Kelvin - 273.15


print("\n------------Welcome To The Temperature Converter------------\n")

while True:
    print("\nChoose Temperature Converter\n")
    print("1. Celsius to Fahrenheit Converter")
    print("2. Celsius to Kelvin Converter")
    print("3. Kelvin to Celsius Converter")
    print("4. Exit")

    try:
        choice = int(input("\nEnter Your Choice: 1, 2, 3, 4: "))

        if choice == 1:
            celsius = float(input("Enter Temperature in Celsius: "))
            fahrenheit = Celsius_to_Fahrenheit_Converter(celsius)
            print(celsius, "°C =", fahrenheit, "°F")

        elif choice == 2:
            celsius = float(input("Enter Temperature in Celsius: "))
            kelvin = Celsius_to_Kelvin_Converter(celsius)
            print(celsius, "°C =", kelvin, "K")

        elif choice == 3:
            kelvin = float(input("Enter Temperature in Kelvin: "))
            celsius = Kelvin_to_Celsius_Converter(kelvin)
            print(kelvin, "K =", celsius, "°C")

        elif choice == 4:
            print("Exiting the program. Thank You for Using !")
            break

        else:
            print("Invalid Choice")

    except ValueError:
        print("Invalid Input. Please enter a valid number.")

