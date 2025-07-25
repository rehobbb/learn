import re
phoneNumRegex = re.compile(r'(\d{3})-(\d{3})-(\d{4})')
mo = phoneNumRegex.findall('Call me at 415-555-1011 tomorrow. 415-555-9999 is my office.')
for m in mo:
    print(m)