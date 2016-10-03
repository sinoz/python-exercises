def build_rect_triangle(figure, amountRows):
    output = ""
    previous = figure

    for i in range(0, amountRows):
        output += previous
        previous += figure

        output += "\n"

    return output

figure = raw_input("Insert figure")
amountRows = int(raw_input("Insert amount rows"))

print build_rect_triangle(figure, amountRows)