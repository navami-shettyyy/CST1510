# BROKEN ON PURPOSE.
# Run it, read the last line, then fix it.

# NameError: name 'status' is not defined
# def check(value, limit):
#   status = "OVER LIMIT" if value > limit else "OK"

# check(87, 100)

# print(status)

# Fixed
def check(value, limit):
    status = "OVER LIMIT" if value > limit else "OK"
    return status

result = check(87, 100)
print(result)