# BMI Calculator + Temperature Converter (Height in cm)

def bmi_calculator():
    print("\n--- BMI Calculator ---")
    weight = float(input("Enter your weight (kg): "))
    height_cm = float(input("Enter your height (cm): "))
    height_m = height_cm / 100  # Convert cm to meters
    bmi = weight / (height_m ** 2)

    print(f"Your BMI is: {bmi:.2f}")

    if bmi < 18.5:
        print("Category: Underweight")
    elif 18.5 <= bmi < 24.9:
        print("Category: Normal weight")
    elif 25 <= bmi < 29.9:
        print("Category: Overweight")
    else:
        print("Category: Obese")


def temperature_converter():
    print("\n--- Temperature Converter ---")
    choice = input("Convert:\n1. Celsius to Fahrenheit\n2. Fahrenheit to Celsius\nChoose 1 or 2: ")

    if choice == "1":
        celsius = float(input("Enter temperature in Celsius: "))
        fahrenheit = (celsius * 9/5) + 32
        print(f"{celsius:.2f}°C = {fahrenheit:.2f}°F")
    elif choice == "2":
        fahrenheit = float(input("Enter temperature in Fahrenheit: "))
        celsius = (fahrenheit - 32) * 5/9
        print(f"{fahrenheit:.2f}°F = {celsius:.2f}°C")
    else:
        print("Invalid choice!")


def main():
    while True:
        print("\n==== Mini Project ====")
        print("1. BMI Calculator")
        print("2. Temperature Converter")
        print("3. Exit")
        option = input("Choose an option: ")

        if option == "1":
            bmi_calculator()
        elif option == "2":
            temperature_converter()
        elif option == "3":
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid option! Try again.")


if __name__ == "__main__":
    main()
