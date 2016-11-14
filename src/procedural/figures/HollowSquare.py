def hollow(figure, amount_rows):
    output = figure
    for i in range(1, amount_rows):
        output += " "
    output += figure
    output += "\n"

    return output

def top_and_bottom(figure, amount_rows):
    output = ""
    for i in range(0, (amount_rows + 1)):
        output += figure
    output += "\n"

    return output

def hollow_square(figure, amount_rows):
    output = top_and_bottom(figure, amount_rows)
    for i in range(amount_rows):
        output += hollow(figure, amount_rows)
    output += top_and_bottom(figure, amount_rows)

    return output

figure = input("Insert figure")
amount_rows = int(input("Insert amount rows"))

print(hollow_square(figure, amount_rows))