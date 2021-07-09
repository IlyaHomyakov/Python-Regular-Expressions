# todo
#  Write a Python program to check that a string contains only
#  a certain set of characters (in this case a-z, A-Z and 0-9).

import re

strings = ['ricthiuyrg9845798hfdgn4yt35784ygfd', 'jug8053ht@#&&*//okeoijf4!@&#*^']

for string in strings:
    if re.search(r'[a-zA-Z0-9]*', string).group() == string:
        print(string + ' consists only from a-z, A-Z, 0-9')
    else:
        print(string + ' does\'not consists only from a-z, A-Z, 0-9')
