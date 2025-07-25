import re
haRegex = re.compile(r'(Ha){3,5}?')
mo = haRegex.search('HaHaHaHa')
print(mo.group())