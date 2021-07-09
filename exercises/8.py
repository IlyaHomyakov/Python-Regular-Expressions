# todo
#  Write a Python program to extract year, month and date from an url.

import re

sample_url = 'https://people.onliner.by/2021/07/09/luchshie-uchebnye-zavedeniya'


def extract_url(url):
    print(re.findall(r'/(\d{4})/(\d{1,2})/(\d{1,2})/', url))


extract_url(sample_url)
