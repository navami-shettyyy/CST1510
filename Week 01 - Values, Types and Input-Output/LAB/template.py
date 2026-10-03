"""
RECORD CHECK  -  my version
===========================

Name  :  Navami Pradeep Shetty
Lane  :  AI      
Date  :  24/09/2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

# ==================================================================== INPUT

label = input('Enter dataset name: ')
first = float(input('Enter number of rows loaded: '))
second = float(input('Enter number of rows expected: '))

# ================================================================== PROCESS

difference = second - first
percent = (first / second * 100)

# Extra useful calculation: Shows the percentage of rows that failed to load
percent_failed = (difference / second * 100)

# =================================================================== OUTPUT

print()
print('=' * 34)
print(f'  RECORD CHECK  -  {label}')
print('=' * 34)
print(f'  Rows loaded   : {first:>10.2f}')
print(f'  Rows expected : {second:>10.2f}')
print(f'  Difference    : {difference:>+10.2f}')
print(f'  Percentage    : {percent:>10.2f} %')
print(f'  Failed %      : {percent_failed:>10.2f} %')
print('=' * 34)