#!/user/bin/env python3
# coding=utf-8
'''
@project : project_test
@author  : anton Wang
@file   : handler.py
@IDE   : PyCharm
@date  : 2020-03-17
'''
import difflib


def simple_diff(query_str, diff_s):
    ratio = difflib.SequenceMatcher(None, query_str, diff_s).quick_ratio()
    return ratio
