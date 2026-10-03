# BROKEN ON PURPOSE.
# Run it, read the last line, then fix it.

value = 23.7
limit = 20

# IndentationError: expected an indented block after 'if' statement on line 7
# if value > limit:
# print("OVER")

# Fixed
if value > limit:
    print("OVER")
