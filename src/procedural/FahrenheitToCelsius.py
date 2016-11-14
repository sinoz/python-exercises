# Checks if the given input can be converted to an integer type without throwing a ValueError exception.
# Returns true if this is the case, else returns false if a ValueError was thrown during the process.
def is_number(input):
   try:
       int(input)
       return True
   except ValueError:
       return False

# Converts the given temperature in Fahrenheit to Celsius.
def fahrenheit_to_celsius(tempFahrenheit):
   return (tempFahrenheit - 32) / 1.8

# Now for the actual program
userTemperatureInput = input("Temperature in Fahrenheit?")
if is_number(userTemperatureInput):
   tempFahrenheit = int(userTemperatureInput)

   tempCelsius = fahrenheit_to_celsius(tempFahrenheit)
   tempCelsiusTwoDecimals = round(tempCelsius, 2)

   print("The temperature", tempFahrenheit, "degrees in fahrenheit converted to degrees in celsius: ", tempCelsiusTwoDecimals)
else:
   print("Invalid user input. Only allows numbers.")