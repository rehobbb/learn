import re
starRegex = re.compile(r'.at')
mo = starRegex.findall('The cat sat on the mat.')
print(mo)