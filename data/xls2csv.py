#!/user/bin/env python3
# coding=utf-8
'''
@project : project_test
@author  : anton Wang
@file   : xls2csv.py
@IDE   : PyCharm
@date  : 2020-03-13
'''
import json

import numpy as np
import xlrd

workbook = xlrd.open_workbook("./hospital/hospital_info.xls")
names = workbook.sheet_names()
print(names)  # ['Sheet1']

# 通过sheet索引获得sheet对象
worksheet = workbook.sheet_by_index(0)
# print(worksheet)

# 通过sheet名获得sheet对象
# worksheet = workbook.sheet_by_name("Sheet1")
# print(worksheet)

# 由上可知，workbook.sheet_names() 返回一个list对象，可以对这个list对象进行操作
# sheet0_name = workbook.sheet_names()[0]  # 通过sheet索引获取sheet名称
# print(sheet0_name)

nrows = worksheet.nrows  # 获取该表总行数
print(nrows)  # 32

# ncols = worksheet.ncols  # 获取该表总列数


# for i in range(nrows):  # 循环打印每一行
#     code =worksheet.cell(i,0).value
#     name =worksheet.cell(i,2).value

# row_values = worksheet.row_values(0) # 获取第一行内容
# col_data = worksheet.col_values(0)  # 获取第一列的内容

codes = worksheet.col_values(0)
names = worksheet.col_values(2)
address = worksheet.col_values(7)
# res=dict(zip(codes,names))
len = codes.__len__()
res = []
# 忽略表头
for i in range(1, len):
    item = {
        "name":names[i],
        "code":codes[i],
        "address":address[i]
    }
    res.append(item)

# 写文件
res_filename = "hospital_base.json"

with open(res_filename, 'w', encoding="utf-8") as f:
    json.dump(res, f, ensure_ascii=False, indent=4)

# names model train data
train_data = "hospital_name.csv"
with open(train_data, 'w', encoding="utf-8") as f:
    for item in names:
        f.write("{}\n".format(item))
