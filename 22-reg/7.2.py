import re
regtext = re.compile(r'\d{3}-\d{3}-\d{4}')
message = 'Call me at 415-555-1011 tomorrow. 415-555-9999 is my office.'
mo = regtext.search(message)
print('phone number found:' + mo.group())
