FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

def convert_to_celsius(fahrenheit):
    total = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return f"{fahrenheit}°F is {total}°C"

def convert_to_fahrenheit(celsius):
    total = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
    return f"{celsius}°C is {total}°F"

try:
    temperature = float(input("Enter the temperature to convert: "))
    unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ")

    if unit == "C":
        print(convert_to_fahrenheit(temperature))
    elif unit == "F":
        print(convert_to_celsius(temperature))
    else:
        print("Invalid unit. Choose C or F")
except ValueError:
    print("Invalid temperature. Please enter a numeric value.")
