import math

def circle(figure, diameter):
    output = ""

    radius = diameter / 2
    for y in range(diameter):
        for x in range(diameter):
            x_calc = (x - radius) ** 2
            y_calc = (y - radius) ** 2

            distance = math.sqrt((x_calc + y_calc))
            if distance <= radius:
                output += figure
            else:
                output += " "
        output += "\n"

    return output

figure = input("Insert figure")
diameter = int(input("Insert diameter"))
print(circle(figure, diameter))