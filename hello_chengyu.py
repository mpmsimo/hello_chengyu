#!/usr/bin/python
# -*- coding: utf-8 -*-
#hello-chengyu.py
#Author: mpmsimo
#Date Created: 12/10/15

import json
import chengyu_data as cd

def select_language(language = 'en'):
	if language != 'en' or language != 'zh_cn':
		print("Please select 'en' (English) or 'zh_cn' (Simplified Chinese).")
	return language

def format_output(language):
	if language == 'en':
		return cd.en_format
	elif language == 'zh_cn':
		return cd.zh_cn_format

def print_chengyu(chengyu_data):
	"""Prints a chengyu or Chinese proverb alongside the English translation and meaning."""
	pass

def main():
	language = select_language()
	output = format_output(language)
	print_chengyu(chengyu_data)
	

if __name__ == '__main__':
	main()