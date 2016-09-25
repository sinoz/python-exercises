textInput = raw_input("Insert text to shift")
amtToShift = int(raw_input("Insert amount of decimal values to shift characters to"))

output = ""
for i in textInput:
    asciiDecimal = ord(i)
    shiftedCharacter = chr(asciiDecimal + amtToShift)

    # TODO: check if number or uppercased character

    output += shiftedCharacter

print output

