def include_hollowness(figure, amountRows):
    output = figure
    for i in range(1, amountRows):
        output += " "
    output += figure
    output += "\n"

    return output

def include_border(figure, amountRows):
    output = ""
    for i in range(0, (amountRows + 1)):
        output += figure
    output += "\n"

    return output

def build_hollow_square(figure, amountRows):
    output = include_border(figure, amountRows)
    for i in range(amountRows):
        output += include_hollowness(figure, amountRows)
    output += include_border(figure, amountRows)

    return output

figure = raw_input("Insert figure")
amountRows = int(raw_input("Insert amount rows"))

print build_hollow_square(figure, amountRows)