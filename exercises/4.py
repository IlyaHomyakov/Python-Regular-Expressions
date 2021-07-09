# todo
#  Write a Python program to find sequences of lowercase letters joined with a underscore.

import re

strings = ['28374g_h_g_h8hd', 'whuuhagd_yg_gygu', 'g_6_6_6y^7y&*^%_', 'fl_*ki*iI8', '&*uygu2_87ay&*']

for string in strings:
    print(re.search(r'[a-z]+_[a-z]', string))
