import re
xmasRegex = re.compile(r'\d+\s\w+')
text = xmasRegex.findall('12 days of Christmas, 25 th December')
print(text)