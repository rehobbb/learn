import re
batRegex  = re.compile(r'Bat(wo)+man')
mo = batRegex.search('Batman lost a wheel')
print(mo.group())