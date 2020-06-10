#!/user/bin/env python3
# coding=utf-8
'''
@project : project_test
@author  : anton Wang
@file   : es_client.py
@IDE   : PyCharm
@date  : 2020-03-23
'''
import json
import os

from elasticsearch import Elasticsearch

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print(BASE_DIR)
CONF_DIR = "{}/{}".format(BASE_DIR, "conf/config.json")
with open(CONF_DIR) as f:
    SETTINGS = json.load(f)
    ES_HOST = SETTINGS["ES_settings"]["host"]
    ES_PORT = SETTINGS["ES_settings"]["port"]
#
# REGION = 'us-east-1'
# SERVICE = 'es'
#
# access_key = 'AKIAJMXRXS3QH2LYINKA'
# secret_key = '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'
#
# AWS_AUTH = AWS4Auth(access_key, secret_key,
#                     REGION, SERVICE)
ES_CLIENT = Elasticsearch(
    hosts=[{'host': ES_HOST, 'port': ES_PORT}]
)
