#!/user/bin/env python3
# coding=utf-8
'''
@project : project_test
@author  : anton Wang
@file   : load_data_to_es.py
@IDE   : PyCharm
@date  : 2020-03-23
'''

import json

import numpy as np
from elasticsearch.helpers import bulk
from gensim.models import doc2vec

from text_similarity.conf.es_client import ES_CLIENT
from text_similarity.data.vectorLoader import vectors
from text_similarity.word_segmentation.segmentation import segment

# load hospital data(hospital_base.json) to es index(hospital)
Index = "hospital_v01"


# text to vector
def embed_text(sentences):
    """
    将所有的句子转化为向量
    """
    model = doc2vec.Doc2Vec.load("model/doc2vec.model")
    resp = []
    for s in sentences:
        resp.append(model.infer_vector(segment(s)).tolist())
    return resp


def compute_text_vector(features):
    """
    通过向量词典计算文本向量值
    :param text:
    :return:
    """
    vecs = []
    for item in features:
        try:
            words = segment(item)
            wordsVec = []
            for word in words:
                v = vectors.get(word)
                if v:
                    wordsVec.append(v)
                else:
                    additonal_vecs = [vectors.get(i) for i in word]
                    wordsVec += additonal_vecs
            # 存在一些字不在预训练向量集中 暂时忽略这些字
            while None in wordsVec:
                wordsVec.remove(None)
            x = np.array(wordsVec)
            vec = np.mean(x, axis=0)  # axis=0，计算每一列的均值
            vecs.append(vec.tolist())
        except Exception as e:
            print(item)
    return vecs


def bulk_index_data():
    """
        将数据索引到es中，且其中包含描述的特征向量字段
        """
    print("begin embed index data to vector")
    with open("../data/hospital/hospital_base.json", encoding='utf-8') as file:
        load_dict = json.load(file)
    features = [doc["name"] for doc in load_dict]
    print("number of lines to embed:", len(features))
    features_vectors = compute_text_vector(features)
    print("begin index data to es")
    requests = []
    for i, doc in enumerate(load_dict):
        request = {'_op_type': 'index',  # 操作 index update create delete
                   '_index': Index,  # index
                   # '_id': doc["code"],
                   '_source':
                       {
                           'code': doc["code"],
                           'name': doc["name"],
                           'address': doc["address"],
                           'name_vector': features_vectors[i],
                       }
                   }
        requests.append(request)
    bulk(ES_CLIENT, requests)
    print("end index data to es")


def bulk_index_data1():
    """
    将数据索引到es中，且其中包含描述的特征向量字段
    """
    print("begin embed index data to vector")
    with open("../data/hospital/hospital_base_bak.json", encoding='utf-8') as file:
        load_dict = json.load(file)
    features = [doc["name"] for doc in load_dict]
    print("number of lines to embed:", len(features))
    features_vectors = embed_text(features)
    print("begin index data to es")
    requests = []
    for i, doc in enumerate(load_dict):
        request = {'_op_type': 'index',  # 操作 index update create delete
                   '_index': Index,  # index
                   # '_id': doc["code"],
                   '_source':
                       {
                           'code': doc["code"],
                           'name': doc["name"],
                           'address': doc["address"],
                           'name_vector': features_vectors[i],
                       }
                   }
        requests.append(request)
    bulk(ES_CLIENT, requests)
    print("end index data to es")


if __name__ == '__main__':
    bulk_index_data1()
    # x = "上海中智医院"
    # vecs = []
    # words = segment(x)
    # wordsVec = [vectors.get(i) for i in words]
    # print(type(wordsVec))
    # x = np.array(wordsVec)
    # print(type(x))
    # print(x)
    # vec = np.mean(x, axis=0).tolist()  # axis=0，计算每一列的均值
    # print(type(vec))
    # print(vec)
    # vecs.append(vec)
