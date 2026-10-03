# BROKEN ON PURPOSE.
# Run it, read the last line, then fix it.

# TypeError: can only concatenate str (not "int") to str
# value = input("Value: ")

# Fixed
value = int(input("Value: "))
print(value + 1)
