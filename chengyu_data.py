#!/usr/bin/python
# -*- coding: utf-8 -*-
#chengyu-data.py
#Author: mpmsimo
#Date Created: 12/11/15

import json

output_format = ("""{0} | {1}
{2}: {5}
{3}: {6}
{4}: {7}""") #Chengyu, Pinyin 

en_format = ["Chinese meaning", "English meaning", "English equivalent"]
zh_cn_format = ["中文意思", "英文意思", "英文等同于"]

chengyu = {1: {
		"chengyu": "通权达变",
		"pinyin": "tōng quán dá biàn",
		"zh_cn_meaning": "To be capable of versatility",
		"en_meaning": "To adapt to any situation",
		"en_equivalent": "placeholder"},
		"chengyu": "一窍不通",
		"pinyin": "yī qiào bù tōng",
		"zh_cn_meaning": "I don't understand a word",
		"en_meaning": "It's all Greek to me",
		"en_equivalent": "placeholder"}}

def get_list_length():
	"""Gets the length of the dictionary."""
	list_length = len(chengyu.keys())
	return list_length