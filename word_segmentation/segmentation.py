#!/user/bin/env python3
# coding=utf-8
'''
@project : project_test
@author  : anton Wang
@file   : segmentation.py
@IDE   : PyCharm
@date  : 2020-03-17
'''
import os

import jieba

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
file_DIR = "{}/{}".format(BASE_DIR, "data/ChineseStopWords.txt")
# 停用词
stopwords = [line.strip() for line in open(file_DIR, encoding='UTF-8').readlines()]


def segment(sentence: str):
    """
    结巴分词，并去除停用词
    """
    resp = []
    sentence_depart = jieba.cut(sentence.strip())
    for word in sentence_depart:
        if word not in stopwords:
            if word != "":
                resp.append(word)
    return resp
if __name__ == '__main__':
    str1="上海古美医院"
    x = jieba.cut(str1, cut_all=True)
    y= jieba.cut(str1)
    print(" /".join(x))
    print(" /".join(y))