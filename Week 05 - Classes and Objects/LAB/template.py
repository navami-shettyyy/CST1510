"""
RECORD CHECK  -  my version
===========================

Name  :  Navami Pradeep Shetty
Lane  :  AI
Date  :  22/10/2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

# ====================================================================== CLASS

class Record:
    over_limit_count = 0

    def __init__(self,label,value,limit):
        """Initializes label, value, and limit for creating objects assigning their values."""
        self.label = label
        self.value = value
        self.limit = limit

    def status(self):
        """Returns the status based on the percentage for one record."""
        percent = (self.value / self.limit) * 100
        if percent >= 100:
            Record.over_limit_count += 1
            return 'OVER LIMIT'
        elif percent >= 90:
            return 'WARNING'
        else:
            return 'OK'

# ==================================================================== RECORDS

def load_records(path):
    """Read label,value,limit lines from a file and return a list of objects."""
    with open(path) as f:
        records = []
        for i in f:
            label,value,limit = i.strip().split(',')
            records.append(Record(label,float(value),float(limit)))
        return records

with open('/Users/navamishetty/Desktop/ /YEAR 1/SEM 1/CST1510 - PROGRAMMING FOR DATA COMMUNICATIONS AND NETWORKS/CST1510/Week 05 - Classes and Objects/LAB/mini_project_data','w') as f:
    f.write('R-001,87,100\n')
    f.write('R-002,120,100\n')
    f.write('R-003,45,100\n')

records = load_records('/Users/navamishetty/Desktop/ /YEAR 1/SEM 1/CST1510 - PROGRAMMING FOR DATA COMMUNICATIONS AND NETWORKS/CST1510/Week 05 - Classes and Objects/LAB/mini_project_data')

# ==================================================================== OUTPUT

for record in records:
    status = record.status()
    print()
    print("=" * 34)
    print(f"  RECORD CHECK  -  {record.label}")
    print("=" * 34)
    print(f'  Label            : {record.label}')
    print(f'  Value            : {record.value}')
    print(f'  Limit            : {record.limit}')
    print(f'  Status           : {status}')
    print("=" * 34)

print(f'Total over limit records: {Record.over_limit_count}')

