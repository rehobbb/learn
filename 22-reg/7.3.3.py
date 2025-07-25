import re
batRegex = re.compile(r'Bat(wo)?man')
mo = batRegex.search('Batwoman lost a wheel')
print(mo.group())
mo = batRegex.search('Batman lost a wheel')
print(mo.group())