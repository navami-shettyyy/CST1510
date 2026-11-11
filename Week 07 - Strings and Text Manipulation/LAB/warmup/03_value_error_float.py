# BROKEN ON PURPOSE.
# Run it, read the last line, then fix it.

# ValueError: could not convert string to float: 'unknown'
# raw_line = "srv-01,used=unknown,total=100"

# Fixed
raw_line = "srv-01,used=87,total=100"
hostname_part, rest = raw_line.split(",", 1)

for piece in rest.split(","):
    key, value = piece.split("=")
    print(key, float(value))
