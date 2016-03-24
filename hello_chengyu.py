#!/usr/bin/python
# -*- coding: utf-8 -*-
#hello-chengyu.py
#Author: mpmsimo
#Date Created: 12/10/15

import random imort randint
import json

import chengyu_data as cd

def select_language(language = None):
	if language != 'en' or language != 'zh_cn':
		print("Please select 'en' (English) or 'zh_cn' (Simplified Chinese).")
	return language

def print_chengyu(language, chengyu_id):
	"""Prints a chengyu or Chinese proverb alongside the English translation and meaning."""
	pass
	if language == 'en':
		language_format = cd.en_format
	elif language == 'zh_cn':
		language_format = cd.zh_cn_format
	output_format.format(chengyu_id["chengyu"], chengyu_id["pinyin"],
						language_format[0], language_format[1],
						language_format[2], chengyu_id["zh_cn_meaning"],
						chengyu_id["en_meaning"], chengyu_id["en_equivalent"])
	print(output_format)

def randomize():
	"""Generate a random number associated with a chengyu to print to terminal."""
	chengyu_num = randint(0, cd.get_list_length())
	return chengyu_num

def main():
	language = select_language()
	chengyu_num = randomize()
	print_chengyu(language, chengyu_num)
	
if __name__ == '__main__':
	main()