import re

emails = ['nothing@gmail.com', 'something.hap.1@example.com', 'anything2021@dot.com', 'everything.at.all@test.com']

for email in emails:
    print(re.search(r'^.*@', email).group()[:-1] + ' - - - ' + re.search(r'@.*', email).group())
