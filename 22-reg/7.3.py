import re
regtext = re.compile(r'(\d{3})-(\d{3})-(\d{4})')
message = 'Call me at 415-555-1011 tomorrow. 415-555-9999 is my office.'
mo = regtext.search(message)
print('phone number :' + mo.group())
print('area code:' + mo.group(1))
print('main number:' + mo.group(2))
print('subscriber number:' + mo.group(3))
area,main,sub = mo.groups()
print(area)
print(main)
print(sub)

