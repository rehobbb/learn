import re
anyRegex = re.compile(r'First name: (.*) Last name: (.*)')
mo = anyRegex.search('First name: Al Last name: Sweigart')
print(mo.group(1))
print(mo.group(2))
nogreedyRegex = re.compile(r'<.*?>')
mo = nogreedyRegex.search('<to server> and <to client>')
print(mo.group())