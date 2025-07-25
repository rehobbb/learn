import re
mo = re.compile(r'[a-jA-J.13]')
text = mo.findall('A quick. brown1 fox13 jumps over the lazy dog')
print(text)

