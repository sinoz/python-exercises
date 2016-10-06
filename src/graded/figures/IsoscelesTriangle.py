def iso_triangle(figure, amountRows):
    output = ""
    figure_record = ""

    # we start at 1 as we have only one asterisk at the top
    offset = 1
    destination = (amountRows + 1)

    for row in range(offset, destination):
        # calculate the amount of spaces to include from the left side based on the current row
        amt_spaces = (amountRows - row)
        for col in range(amt_spaces):
            output += " "

        # Adds two figures to the output for every row that comes after the first (top to bottom)
        output += figure_record + figure_record + figure
        figure_record += figure

        output += "\n"

    return output

figure = raw_input("Insert figure")
amountRows = int(raw_input("Insert amount rows"))

print iso_triangle(figure, amountRows)