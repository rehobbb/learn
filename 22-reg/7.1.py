def isPhoneNumber(phone):
    if len(phone) != 12:
        return False
    for i in range(0,3):
        if not phone[i].isdigit():
            return False
    if phone[3] != '-':
        return False
    for i in range(4,7):
        if not phone[i].isdigit():
            return False
    if phone[7] != '-':
        return False
    for i in range(8,12):
        if not phone[i].isdigit():
            return False
    return True
message = 'Call me at 415-555-1011 tomorrow. 415-555-9999 is my office.'
for i in range(len(message)):
    chunk = message[i:i+12]
    if isPhoneNumber(chunk):
        print('phone number found: ' + chunk)
print('done')