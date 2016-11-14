def square(figure, amount_rows):
    output = ""
    for i in range(0, amount_rows):
        for j in range(0, amount_rows):
            output += figure
        output += "\n"
    return output

figure = input("Insert figure")
amount_rows = int(input("Insert amount rows"))

print(square(figure, amount_rows))