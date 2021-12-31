# -*- coding: utf-8 -*-
"""
@author:XuMing(xuming624@qq.com)
@description: 
"""
import os
import sys

sys.path.append('..')
pwd_path = os.path.abspath(os.path.dirname(__file__))
default_stopwords_path = os.path.join(pwd_path, 'data/stopwords.txt')
default_symbol_path = os.path.join(pwd_path, 'data/sentence_symbol.txt')


def load_list(path):
    return [word for word in open(path, 'r', encoding='utf-8').read().split()]


stopwords = set(load_list(default_stopwords_path))
symbols = set(load_list(default_symbol_path))
sentence_symbols = {'？', '?', '！', '!', '。', '；', '……', '…'}
