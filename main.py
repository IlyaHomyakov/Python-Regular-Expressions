import re

s = '1gL hTW i8r2mVIrjJhtxm3dqtg.DC.oedRNdKPSfhBa1ZT7Jidw55f3N8Fpgsur28G46tsnxS5l5v0QoWHPDG3v7AcluMVxe2I4gv4T'

print(re.search('[0-9][0-9]', s))  # [0-9] find only single dec character, [0-9][0-9] find two characters number, > 22

print(re.search(r'.*', s))  # Matches any single character except newline

print(re.search('\W', s))  # Matches any non-let/num character

print(re.search('^1gL', s))  # Matches any symbols at the begging of the string

print(re.search('4T$', s))  # Matches any symbols at the end of the string

print(re.search(r'\bDC\b', s))  # Matches any words or symbols if there non-let/num symbols in the end or start or both

print(re.search(r'tsnx\BS5', s))  # does the opposite of \b

emails = ['nothing@gmail.com', 'something.hap.1@example.com', 'anything2021@dot.com', 'everything.at.all@test.com']
