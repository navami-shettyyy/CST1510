"""
RECORD CHECK  -  my version
===========================

Name  :  Navami Pradeep Shetty
Lane  :  AI
Date  :  08/10/2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

over_limit = 0

# =================================================================== FUNCTIONS

def status_of(percent):
    """Returns status based on the percentage."""
    if percent >= 100:
        return 'OVER LIMIT'
    elif percent >= 90:
        return 'WARNING'
    else:
        return 'OK'

def check(value,limit):
    """Returns the difference and percentage."""
    difference = limit - value
    percent = (value / limit) * 100
    return difference,percent

def print_report(label,value,limit,difference,percent,status):
    """Prints the formatted report."""
    print()
    print('=' * 34)
    print(f'  RECORD CHECK  -  {label}')
    print('=' * 34)
    print(f'  Rows loaded      : {value:>10.2f}')
    print(f'  Rows expected    : {limit:>10.2f}')
    print(f'  Difference       : {difference:>+10.2f}')
    print(f'  Percentage       : {percent:>10.2f} %')
    print(f'  Status           : {status:>10}')
    print('=' * 34)

# ==================================================================== INPUT

while True:
    label = input("Enter dataset name or type 'quit' to stop: ") 
    if label == 'quit':
        break   
    value = float(input('Enter number of rows loaded: '))     
    limit = float(input('Enter number of rows expected: '))

# ================================================================== PROCESS

    difference,percent = check(value,limit)
    status = status_of(percent)
    if status == 'OVER LIMIT':
        over_limit += 1

# =================================================================== OUTPUT

    print_report(label,value,limit,difference,percent,status)

print(f'Total over limit records: {over_limit}')