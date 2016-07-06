#!/usr/bin/python
# -*- coding: utf-8 -*-
#hello-chengyu.py
#Author: mpmsimo
#Date Created: 12/10/15

from random import randint
import json

import chengyu_data as cd

def print_chengyu(language, chengyu_id):
    """Prints a chengyu or Chinese proverb alongside the English translation and meaning."""
    if language == 'zh_cn':
        language_format = cd.zh_cn_format
    else:
        language_format = cd.en_format

    jd = json.dumps(cd.chengyu, ensure_ascii=False)
    jl = json.loads(jd)
    output = jl.get(chengyu_id)
    for k, v in output.items():
        print(u'{0}: {1}'.format(k, v))

def randomize():
	"""Generate a random number associated with a chengyu to print to terminal."""
	chengyu_num = randint(1, cd.get_list_length())
	return str(chengyu_num)

def main():
    chengyu_num = randomize()
    print_chengyu('en', chengyu_num)

if __name__ == '__main__':
	main()
