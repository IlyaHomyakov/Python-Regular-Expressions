# todo
#  Write a Python program to find all adverbs and their positions in a given sentence.

import re

text = open('sample_text').read()
a = re.findall(r'\w+ly', text)
print(a, len(a))
