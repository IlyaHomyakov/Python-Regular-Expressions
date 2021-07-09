# todo
#  Write a Python program that matches a word at the end of string, with optional punctuation.

import re

strings = ['The quick brown fox jumps over the lazy dog.',
           'The quick brown fox jumps over the lazy dog. ',
           'The quick brown fox jumps over the lazy dog ']

for string in strings:
    print(re.search(r'\w+\S*$', string))
