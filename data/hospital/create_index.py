#!/user/bin/env python3
# coding=utf-8
'''
@project : project_test
@author  : anton Wang
@file   : create_index.py
@IDE   : PyCharm
@date  : 2020-03-23
'''
from text_similarity.conf.es_client import ES_CLIENT

Index = "hospital_names"


def create_index():
    setting = {
        "settings": {
            "number_of_replicas": 0,
            "number_of_shards": 1
        },
        "mappings": {
            "properties": {
                "code": {
                    "type": "keyword"
                },
                "name": {
                    "type": "keyword"
                },
                "address": {
                    "type": "text"
                },
                "name_vector": {
                    "type": "dense_vector",
                    "dims": 300
                }
            }
        }
    }
    ES_CLIENT.indices.create(index=Index, body=setting)
    print("end create index")


if __name__ == '__main__':
    create_index()
