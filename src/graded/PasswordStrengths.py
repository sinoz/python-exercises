# Mutable fields
amt_uppercased = 0
amt_digits = 0
amt_symbols = 0

# Constants
amt_factors = 3

# The actual program
password_input = raw_input("Insert your password")
for i in password_input:
     if not i.isalpha():
         amt_symbols += 1
     elif i.isupper():
         amt_uppercased += 1
     elif i.isdigit():
         amt_digits += 1

strength_lvl = (amt_symbols + amt_uppercased + amt_digits) / amt_factors
if strength_lvl < 2:
    print "Weak"
elif strength_lvl < 6:
    print "Medium"
else:
    print "Strong"
