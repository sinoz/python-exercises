# Checks if the given input can be converted to an integer type without throwing a ValueError exception.
# Returns true if this is the case, else returns false if a ValueError was thrown during the process.
def acceptable_input(input):
   try:
       int(input)
       return True
   except ValueError:
       return False

# Converts the given temperature in Celsius to Kelvin.
def celsius_to_kelvin(tempCelsius):
   return tempCelsius + 273.15

# Now for the actual program
userTemperatureInput = raw_input("Temperature in Celsius?")
if acceptable_input(userTemperatureInput):
   tempCelsius = int(userTemperatureInput)

   tempKelvin = celsius_to_kelvin(tempCelsius)
   tempKelvinTwoDecimals = round(tempKelvin, 2)
   if tempKelvinTwoDecimals < 0:
       tempKelvinTwoDecimals = 0

   print "The temperature", tempCelsius, "degrees in celsius converted to degrees in Kelvin: ", tempKelvinTwoDecimals
else:
   print "Invalid user input. Only allows numbers."