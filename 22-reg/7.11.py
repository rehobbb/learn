import re
ignoreRegex = re.compile(r'robocop',re.I)
mo = ignoreRegex.search('Robocop is part of the movie.')
print(mo.group())