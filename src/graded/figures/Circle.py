import math

def circle(radius):
    width = radius ** 2
    height = radius ** 2

    output = ""

    for y in range(height):
        for x in range(width):
            a = (x - radius) ** 2
            b = (y - radius) ** 2

            z = math.sqrt(a + b)
            if z < radius:
                output += "#"
            else:
                output += " "
        output += "\n"
    return output

radius = int(raw_input("Insert radius"))
print(circle(radius))