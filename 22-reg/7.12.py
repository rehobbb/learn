import re
nameRegex = re.compile(r'Agent \w+')
mo = nameRegex.sub('CENSORED','Agent Alice gave the secret documents to Agent Bob.')
print(mo)
starRegex = re.compile(r'Agent (\w)\w*')
mo2 = starRegex.sub(r'\1****','Agent Alice told Agent Bob that Agent Carol was a spy.')
print(mo2)