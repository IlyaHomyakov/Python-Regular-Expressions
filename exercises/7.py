# todo
#  Write a Python program to find the substrings within a string.

import re

string = 'Some few words with different duplicates and quick program working with them will be written in a few secs'
finder = input('Needed word? ')
for match in re.findall(finder, string):
    print('There\'s ' + match + ' in >' + string)
