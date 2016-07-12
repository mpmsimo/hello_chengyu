#!/usr/bin/python
# -*- coding: utf-8 -*-
#chengyu-data.py
#Author: mpmsimo
#Date Created: 12/11/15

import json

en_format = ["Chinese meaning", "English meaning", "English equivalent"]
zh_format = ["中文意思", "英文意思", "英文等同于"]

# chengyu - pinyin
# [5-7] are values from then language format list, listed sequentially.
# [2-4] are values from the chengyu dict that was passed to the program. 
printcy = u"""{0} - {1}
{5}: {2}
{6}: {3}
{7}: {4}"""

chengyu = {'1': {
		"chengyu": "通权达变",
		"pinyin": "tōng quán dá biàn",
		"zh_meaning": "To be capable of versatility",
		"en_meaning": "To adapt to any situation",
		"en_equivalent": "placeholder"},
        '2': {
		"chengyu": "一窍不通",
		"pinyin": "yī qiào bù tōng",
		"zh_meaning": "I don't understand a word",
		"en_meaning": "It's all Greek to me",
		"en_equivalent": "placeholder"}}

def get_list_length():
	"""Gets the length of the dictionary."""
	list_length = len(chengyu.keys())
	return list_length
