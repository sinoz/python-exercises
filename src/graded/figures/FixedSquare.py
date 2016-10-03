def build_square(figure, amountRows):
    output = ""
    for i in range(0, amountRows):
        for j in range(0, amountRows):
            output += figure
        output += "\n"
    return output

figure = raw_input("Insert figure")
amount = int(raw_input("Insert amount rows"))

print build_square(figure, amount)