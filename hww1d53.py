def get_temperature():
    while True:
        temperature_str = input("Please enter the temperature in Fahrenheit (or 'exit' to quit): ")
        if temperature_str == 'exit':
            return None
        try:
            temperature = float(temperature_str)
            return temperature
        except ValueError:
            print("Invalid input! Please enter a valid numerical temperature.")

def convert_to_celsius(temperature):
    celsius = (temperature - 32) * 5 / 9
    return celsius

def main():
    print("Welcome to the Weather Forecast Application!")
    while True:
        temperature = get_temperature()
        if temperature is None:
            break
        try:
            celsius = convert_to_celsius(temperature)
        except Exception as e:
            print("Error occured during temperature conversion:", e)
        else:
            print(f"The temperature in Celsius is: {celsius:.2f}°C")
        finally:
            print("Thank you for using the Weather Forecast Application!")
main()




































