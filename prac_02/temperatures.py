"""Temperature conversion program"""

def main():
   """Get temperature and convert between Celsius and Fahrenheit"""
   celsius = float(input("Enter temperature in Celsius: "))
   fahrenheit = celsius_to_fahrenheit(celsius)
   print(f"{celsius}C is {fahrenheit}F")

   fahrenheit = float(input("Enter temperature in Fahrenheit: "))
   celsius = fahrenheit_to_celsius(fahrenheit)
   print(f"{fahrenheit}F is {celsius}C")

def celsius_to_fahrenheit(celsius):
   """Convert Celsius to Fahrenheit"""
   return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
   """Convert Fahrenheit to Celsius"""
   return (fahrenheit - 32) * 5/9

main()