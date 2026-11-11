# BROKEN ON PURPOSE.
# Run it, read the last line, then fix it.

piece = "note=server=east"

# ValueError: too many values to unpack (expected 2, got 3)
# key, value = piece.split("=")

# Fixed
key,value = piece.split('=',1)

print(key,value)
