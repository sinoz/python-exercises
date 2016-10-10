def build_square(figure, amount_rows):
    output = ""
    for i in range(0, amount_rows):
        for j in range(0, amount_rows):
            output += figure
        output += "\n"
    return output

figure = raw_input("Insert figure")
amount_rows = int(raw_input("Insert amount rows"))

print build_square(figure, amount_rows)