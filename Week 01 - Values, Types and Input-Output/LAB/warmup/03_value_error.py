# BROKEN ON PURPOSE.
# Run it, type 23.7 when asked, read the last line, then fix it.

# ValueError: invalid literal for int() with base 10: '23.7'
# value = int(input("Value: "))

# Fixed
value = float(input("Value: "))

print(value)

