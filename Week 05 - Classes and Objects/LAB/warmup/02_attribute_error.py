# BROKEN ON PURPOSE.
# Run it, read the last line, then fix it.

# AttributeError: 'Record' object has no attribute 'value'
#class Record:
#    def __init__(self, label, value, limit):
#        self.label = label
#        self.amount = value    # stored as "amount", not "value"
#        self.limit = limit

# Fixed
class Record:
    def __init__(self, label, value, limit):
        self.label = label
        self.value = value
        self.limit = limit

r = Record("R-001", 87.0, 100.0)
print(r.value)
