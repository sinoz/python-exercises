def absolute_value(value): # TODO: shorten if/else to a ternary?
   if value <= 0:
       return 0 - value
   else:
       return value

value = -20
print(absolute_value(value))