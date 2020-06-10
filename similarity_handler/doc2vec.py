#!/user/bin/env python3
# coding=utf-8
'''
@project : project_test
@author  : anton Wang
@file   : doc2vec.py
@IDE   : PyCharm
@date  : 2020-03-23
'''
import dill
import gensim
import jieba
from gensim.models.doc2vec import Doc2Vec
from gensim.models.word2vec import Word2Vec

# 停用词
stopwords = [line.strip() for line in open('../data/ChineseStopWords.txt', encoding='UTF-8').readlines()]


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


def read_corpus(f_name):
    """
    读数据
    """
    with open(f_name, encoding="utf-8") as f:
        for i, line in enumerate(f):
            yield gensim.models.doc2vec.TaggedDocument(segment(line), [i])


# def train_doc2vec():
#     """
#     训练 Doc2Vec 模型
#     """
#     train_file = "../data/hospital_name.csv"
#     train_corpus = list(read_corpus(train_file))
#     model = Doc2Vec(vector_size=300, min_count=2, epochs=10)
#     print(len(train_corpus))
#     model.build_vocab(train_corpus)
#     model.train(train_corpus, total_examples=model.corpus_count, epochs=model.epochs)
#     # model.save(".model/doc2vec.model")
#
#     # save your model as
#     with open('model/doc2vec.model', 'wb') as f:
#         dill.dump(model, f)

    # later load the model as
    # model = gensim.models.Doc2vec.load('file-name')


def train(type, modelFile):
    """
    训练模型文件
    :param type:  modle 类型
    :param modelFile 模型文件名
    """
    train_file = "../data/hospital_name.csv"
    train_corpus = list(read_corpus(train_file))
    if type == "doc":
        model = Doc2Vec(vector_size=300, min_count=2, epochs=10)
        print(len(train_corpus))
        model.build_vocab(train_corpus)
        model.train(train_corpus, total_examples=model.corpus_count, epochs=model.epochs)
    elif type == "word":
        return
        # model =  Word2Vec(common_texts, size=100, window=5, min_count=1, workers=4)
    else:
        print("unknow model type {}".format(type))
        return

    # model.save(".model/doc2vec.model")

    # save your model as
    with open(modelFile, 'wb') as f:
        dill.dump(model, f)


if __name__ == '__main__':
    train("doc","model/doc2vec.model")
    # train("word","model/word2vec.model")
