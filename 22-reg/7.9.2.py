import re
dotRegex = re.compile(r'.*')
dotRegex2 = re.compile(r'.*',re.DOTALL)
msg = 'This is a test string.\n It has multiple lines.'
mo = dotRegex.search(msg)
print(mo.group())
mo2 = dotRegex2.search(msg)
print(mo2.group())