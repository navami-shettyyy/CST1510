# BROKEN ON PURPOSE.
# Run it, read the last line, then fix it.

# FileNotFoundError: [Errno 2] No such file or directory: 'records.txt'
# with open("records.txt") as f:
#    print(f.read())

# Fixed
with open("records.txt","w") as f:
    f.write("R-001,87,100")

with open("records.txt") as f:
    print(f.read())
