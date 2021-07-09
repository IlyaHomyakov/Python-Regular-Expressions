# todo
#  Write a Python program that matches a string that has an a followed by three 'b'.

import re

strings = ['eryuabbb', 'ureiytajdkghlaa', 'rtab8u4f', 're7y834tnj&!^kfshgabbbb', '&*uygu2387ay&*']

for string in strings:
    print(re.search(r'a\Bbbb', string))