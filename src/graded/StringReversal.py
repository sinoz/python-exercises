input = "Beautiful is better than ugly"
output = ""

destination = -1  # -1 as we subtract 1 from the offset
offset = len(input) - 1 # - 1 to prevent index out of bounds
step = -1 # we're going backwards

for i in range(offset, destination, step):
    output += input[i]

print output