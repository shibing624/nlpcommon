# -*- coding: utf-8 -*-
"""
@author:XuMing(xuming624@qq.com)
@description: 
"""
__version__ = "0.1.1"

from nlpcommon.data import load_list, stopwords, symbols
from nlpcommon.log import logger, get_logger, set_log_level
from nlpcommon import tokenizer
from nlpcommon.text import text_segmentate, text_compare, longest_common_substring, longest_common_subsequence
