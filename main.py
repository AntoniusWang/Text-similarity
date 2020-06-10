#!/user/bin/env python3
# coding=utf-8
'''
@project : project_test
@author  : anton Wang
@file   : main.py
@IDE   : PyCharm
@date  : 2020-03-13
'''
import os
import json
import numpy as np
from gensim.models.doc2vec import Doc2Vec

from text_similarity.conf.es_client import ES_CLIENT
from text_similarity.data.vectorLoader import vectors
from text_similarity.word_segmentation.segmentation import segment

Index = "hospital"

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
print(BASE_DIR)
model_dir = "{}/{}".format(BASE_DIR, "similarity_handler/model/doc2vec.model")


def test():
    model = Doc2Vec.load(model_dir)
    while True:
        try:
            query = input("Enter query: ")
            input_vector = model.infer_vector(segment(query)).tolist()
            resp = ES_CLIENT.search(index=Index, body={
                "_source": ["name", "name_vector"],
                "query": {
                    "script_score": {
                        "query": {
                            "match_all": {}
                        },
                        "script": {
                            "source": "cosineSimilarity(params.queryVector, doc['name_vector'])+1",
                            "params": {
                                "queryVector": input_vector
                            }
                        }
                    }
                }
            })
            print("关联的医院：", end=" ")
            for hit in resp["hits"]["hits"]:
                print(hit["_source"]["name"], end="\t")
            print("\n")
        except KeyboardInterrupt:
            return


def test01():
    while True:
        try:
            query = input("Enter query: ")
            words = segment(query)
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
            input_vector = vec.tolist()
            resp = ES_CLIENT.search(index=Index, body={
                "_source": ["name", "name_vector"],
                "query": {
                    "script_score": {
                        "query": {
                            "match_all": {}
                        },
                        "script": {
                            "source": "cosineSimilarity(params.queryVector, doc['name_vector'])+1",
                            "params": {
                                "queryVector": input_vector
                            }
                        }
                    }
                }
            })
            print("关联的医院：", end=" ")
            for hit in resp["hits"]["hits"]:
                print(hit["_source"]["name"], end="\t")
            print("\n")
        except KeyboardInterrupt:
            return


if __name__ == '__main__':
    test01()
    # s = "中治职工"
    # model = Doc2Vec.load(model_dir)
    # input_vector = model.infer_vector(segment(s)).tolist()
    # body = {
    #     "_source": ["name", "name_vector"],
    #     "query": {
    #         "script_score": {
    #             "query": {
    #                 "match_all": {}
    #             },
    #             "script": {
    #                 "source": "cosineSimilarity(params.queryVector, doc['name_vector'])+1",
    #                 "params": {
    #                     "queryVector": input_vector
    #                 }
    #             }
    #         }
    #     }
    # }
    # print(json.dumps(body))