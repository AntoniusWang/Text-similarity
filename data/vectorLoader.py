#!/user/bin/env python3
# coding=utf-8
'''
@project : project_test
@author  : anton Wang
@file   : vectorLoader.py
@IDE   : PyCharm
@date  : 2020-04-07
'''
# file = "sgns.wiki.char"
# f = open(file, 'r', encoding="utf-8")
# first = f.readline()
# print(first)
# lines = f.readlines()[1:]
# res = {}
# for line in lines:
#     key, *vec = line.split(" ")
#     res[key] = vec
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
file = "data/sgns.wiki.char"
CONF_DIR = "{}/{}".format(BASE_DIR, file)
class VecLoader():
    def __init__(self):
        self.vector = {}
        self.load()

    def load(self):
        f = open(CONF_DIR, 'r', encoding="utf-8")
        first = f.readline()
        print(first)
        lines = f.readlines()[1:]
        for line in lines:
            key, *vec = line.strip().split(" ")
            self.vector[key] = list(map(float, vec))

vecLoader = VecLoader()
vectors = vecLoader.vector
if __name__ == '__main__':

    x = vectors.get("上海")
    print(x)
    print(len(x))