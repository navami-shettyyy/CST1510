# BROKEN ON PURPOSE.
# Run it, read the last line, then fix it.

# KeyError: 'status'
# record = {"label": "R-001", "value": 87.0, "limit": 100.0}

# Fixed
record = {"label": "R-001", "value": 87.0, "limit": 100.0, "status": "OK"}

print(record["status"])
