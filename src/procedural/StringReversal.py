val = input("Insert string value to have reversed")
output = ""

destination = -1  # -1 as we subtract 1 from the offset
offset = len(val) - 1 # - 1 to prevent index out of bounds
step = -1 # we're going backwards

for i in range(offset, destination, step):
    output += val[i]

print(output)