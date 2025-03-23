FAHRENHEIT_TO_CELSIUS_FACTOR = (5/9)
CELSIUS_TO_FAHRENHEIT_FACTOR = (9/5) 
def convert_to_celsius(fahrenheit): 
        """converts a temperature from Fahrenheit to Celsius. """
        celsius = (fahrenheit - 32) * fahrenheit_to_celsius_factor
        return celsius
def convert_to_fahrenheit(celsius): 
        """converts a temperature from Celsius to Fahrenheit. """
        fahrenheit = (celsius * celsius_to_fahrenheit_factor) + 32 
        return fahrenheit
def main():
    try:
        temperature = float(input("enter the temperature: "))
        unit = input("enter the unit (c for celsius, f for fahrenheit): ").strip().upper()
        if unit == "f":
            converted_temp = convert_to_celsius(temperature)
            print(f"{temperature} °f is equal to {converted_temp:.2f}°c")
        elif unit == "c":
            converted_temp = convert_to_fahrenheit(temperature)
            print(f"{temperature}°c is equal to {converted_temp:.2f}°f")
        else:
            raise ValueError("Invalid unit. please enter 'c' for celsius or 'f' for fahrenheit. ")
    except ValueError as e:
        print(f"Error: {e}")
if __name__ == "__main__":
    main()

