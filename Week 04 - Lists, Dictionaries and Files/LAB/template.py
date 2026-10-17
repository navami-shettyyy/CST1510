"""
RECORD CHECK  -  my version
===========================

Name  :  Navami Pradeep Shetty
Lane  :  AI
Date  :  15/10/2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

over_limit_count = 0

# =================================================================== FUNCTIONS

def load_records(path):
    """Read label,value,limit lines from a file and return a list of dicts."""
    try:
        records = []
        with open(path) as f:
            for i in f:
                label,value,limit = i.strip().split(',')
                records.append({'label' : label,'value' : float(value),'limit' : float(limit)})
            return records
    except FileNotFoundError:
        print(f"Error: The file '{path}' was not found.")
        return []
    
def check_record(value,limit):
    """Returns the difference, percentage, and status based on the percentage for one record."""
    difference = limit - value
    percent = (value / limit) * 100
    if percent >= 100:
        status = 'OVER LIMIT'
    elif percent >= 90:
        status = 'WARNING'
    else:
        status = 'OK'
    return difference,percent,status

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

# ====================================================================== STORE
with open('/Users/navamishetty/Desktop/ /YEAR 1/SEM 1/CST1510 - PROGRAMMING FOR DATA COMMUNICATIONS AND NETWORKS/CST1510/Week 04 - Lists, Dictionaries and Files/LAB/mini_project_data','w') as f:
    f.write('R-001,87,100\n')
    f.write('R-002,120,100\n')
    f.write('R-003,45,100\n')

mini_project = load_records('/Users/navamishetty/Desktop/ /YEAR 1/SEM 1/CST1510 - PROGRAMMING FOR DATA COMMUNICATIONS AND NETWORKS/CST1510/Week 04 - Lists, Dictionaries and Files/LAB/mini_project_data')

with open('/Users/navamishetty/Desktop/ /YEAR 1/SEM 1/CST1510 - PROGRAMMING FOR DATA COMMUNICATIONS AND NETWORKS/CST1510/Week 04 - Lists, Dictionaries and Files/LAB/mini_project_result','w') as f:
    for i in mini_project:
        difference,percent,status = check_record(i['value'],i['limit'])
        f.write(f'{i['label']},{status}\n')

with open('/Users/navamishetty/Desktop/ /YEAR 1/SEM 1/CST1510 - PROGRAMMING FOR DATA COMMUNICATIONS AND NETWORKS/CST1510/Week 04 - Lists, Dictionaries and Files/LAB/mini_project_result') as f:
      text = f.read()

# =============================================================== PROCESS + OUTPUT

print(text)

for i in mini_project:
    difference,percent,status = check_record(i['value'],i['limit'])
    print_report(i['label'],i['value'],i['limit'],difference, percent,status)
    if status == 'OVER LIMIT':
            over_limit_count += 1

print(f'Total over limit records: {over_limit_count}')