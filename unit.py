 # Unit_Converter

def length_converter():
    print("\nLength Converter (meters ↔ kilometers ↔ miles)")
    print("1: Meters to Kilometers")
    print("2: Kilometers to Meters")
    print("3: Meters to Miles")
    print("4: Miles to Meters")

    choice = input("Choose conversion type (1-4): ")
    value = float(input("Enter value: "))

    if choice == "1":
        print(f"{value} meters = {value / 1000} kilometers")
    elif choice == "2":
        print(f"{value} kilometers = {value * 1000} meters")
    elif choice == "3":
        print(f"{value} meters = {value / 1609.34} miles")
    elif choice == "4":
        print(f"{value} miles = {value * 1609.34} meters")
    else:
        print("Invalid choice!")

def weight_converter():
    print("\nWeight Converter (kg ↔ pounds)")
    print("1: Kilograms to Pounds")
    print("2: Pounds to Kilograms")

    choice = input("Choose conversion type (1-2): ")
    value = float(input("Enter value: "))

    if choice == "1":
        print(f"{value} kg = {value * 2.20462} pounds")
    elif choice == "2":
        print(f"{value} pounds = {value / 2.20462} kg")
    else:
        print("Invalid choice!")

def temperature_converter():
    print("\nTemperature Converter (Celsius ↔ Fahrenheit)")
    print("1: Celsius to Fahrenheit")
    print("2: Fahrenheit to Celsius")

    choice = input("Choose conversion type (1-2): ")
    value = float(input("Enter value: "))

    if choice == "1":
        print(f"{value}°C = {(value * 9/5) + 32}°F")
    elif choice == "2":
        print(f"{value}°F = {(value - 32) * 5/9}°C")
    else:
        print("Invalid choice!")

def main():
    while True:
        print("\nUnit Converter")
        print("1: Length")
        print("2: Weight")
        print("3: Temperature")
        print("4: Exit")

        choice = input("Choose category (1-4): ")

        if choice == "1":
            length_converter()
        elif choice == "2":
            weight_converter()
        elif choice == "3":
            temperature_converter()
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()


