"""
RECORD CHECK  -  my version
===========================

Name  :  Navami Pradeep Shetty
Lane  :  AI
Date  :  09/11/2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

record_count = 0
flagged_count = 0

# =================================================================== FUNCTIONS    

def parse_line(raw_line):
    """Turn one messy raw status line into a clean dict."""
    line = raw_line.strip()
    survey_part,rest = line.split(',', 1)
    survey = survey_part.strip().lower()

    fields = {}
    for i in rest.split(','):
        key,value = i.split('=')
        fields[key.strip().lower()] = float(value.strip())

    return {'survey' : survey,'rating' : fields['rating'],'age' : fields['age']}

def status_of(rating,warning_at = 3):
    """Return FLAGGED or OK based on the survey rating threshold."""
    if rating <= warning_at:
        return 'FLAGGED'
    else:
        return 'OK'

# ====================================================================== INPUT

with open('mini_project.txt') as f:
    for raw_record in f:

# =============================================================== PROCESS + OUTPUT

        record = parse_line(raw_record)
        status = status_of(record['rating'])
        print(record,status)
        record_count += 1
        if status == 'FLAGGED':
            flagged_count += 1

print(f'Summary: {record_count} records processed, {flagged_count} flagged.')