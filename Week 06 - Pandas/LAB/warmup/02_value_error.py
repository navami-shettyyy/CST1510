# BROKEN ON PURPOSE.
# Run it, read the last line, then fix it.

import pandas as pd

# ValueError: All arrays must be of the same length
# df = pd.DataFrame({
#    "label": ["R-001", "R-002", "R-003"],
#    "value": [87, 120],
# })

# Fixed
df = pd.DataFrame({
    "label": ["R-001", "R-002", "R-003"],
    "value": [87, 120,45]
})