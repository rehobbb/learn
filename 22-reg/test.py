import re
numRegex = re.compile(r'''
                      (Alice|Bob|Carol)
                      (eats|pets|throws)
                      (apples|cats|baseballs)\.
                      ''', re.VERBOSE|re.I)