#!/usr/bin/python
# -*- coding: utf-8 -*-
#chengyu-data.py
#Author: mpmsimo
#Date Created: 12/11/15

import json

output_header = ("{0} | {1}")
output_format = ("""{0}:
{1}:
{2}:""")

en_format = output_format.format("Chinese meaning", "English meaning", "English equivalent")
zh_cn_format = output_format.format("placeholder", "placeholder", "placeholder")

'''
json_schema = {"id": {
				"chengyu": chengyu,
				"pinyin": pinyin,
				"zh_cn_meaning": zh_cn_translation,
				"en_meaning": en_translation,
				"en_equivalent": en_equivalent }
			}
'''

chengyu = {"id": {
		"chengyu": "通权达变",
		"pinyin": "tōng quán dá biàn",
		"zh_cn_meaning": "To be capable of versatility",
		"en_meaning": "To adapt to any situation",
		"en_equivalent": "placeholder"
}
