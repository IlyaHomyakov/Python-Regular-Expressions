# todo
#  Write a Python program that matches a string that has an 'a' followed by anything, ending in 'b'

import re

strings = ['283b74g_h_g_h8ahbd', 'whuuhagd_yg_gygb', 'g_6_6a_6y^7y&*^%_b', 'fl_a*ki*ibI8', '&*uaygu2_87ay&*']

for string in strings:
    print(re.search(r'[a]+.*\Bb$', string))
