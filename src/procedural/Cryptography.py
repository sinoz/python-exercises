textInput = input("Insert text to shift")
amtToShift = int(input("Insert amount of decimal values to shift characters to"))

output = ""
for original in textInput:
    asciiDecimal = ord(original)
    shiftedResult = chr(asciiDecimal + amtToShift)

    # we fall back to the original character if the result is a non-letter type
    if original.isalpha() and shiftedResult.isalpha():
        # lowercased characters remain lowercased and same goes for uppercased
        if original.islower():
            shiftedResult = shiftedResult.lower()
        elif original.isupper():
            shiftedResult = shiftedResult.upper()
        output += shiftedResult
    else:
        output += original

print(output)
