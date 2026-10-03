# BROKEN ON PURPOSE.
# Run it, read the last line, then fix it.

limit = 20
value = input("Value: ")

# TypeError: '>' not supported between instances of 'str' and 'int'
# if value > limit:

# Fixed
if float(value) > limit:
    print("OVER")
else:
    print("OK")
