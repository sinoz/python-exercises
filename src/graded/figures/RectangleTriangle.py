def build_rect_triangle(figure, amount_rows):
    output = ""
    previous = figure

    for i in range(0, amount_rows):
        output += previous
        previous += figure

        output += "\n"

    return output

figure = raw_input("Insert figure")
amount_rows = int(raw_input("Insert amount rows"))

print build_rect_triangle(figure, amount_rows)