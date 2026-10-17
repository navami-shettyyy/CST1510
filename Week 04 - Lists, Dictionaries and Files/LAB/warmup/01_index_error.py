# BROKEN ON PURPOSE.
# Run it, read the last line, then fix it.

labels = ["R-001", "R-002", "R-003"]

# IndexError: list index out of range
# print(labels[3])

# Fixed
print(labels[-1])
