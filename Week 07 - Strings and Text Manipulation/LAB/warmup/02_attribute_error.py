# BROKEN ON PURPOSE.
# Run it, read the last line, then fix it.

value_text = "87"

# AttributeError: 'float' object has no attribute 'strip'
# value = float(value_text)

# cleaned = value.strip()
# print(cleaned)

# Fixed
cleaned = value_text.strip()

value = float(cleaned)
print(value)
