# -*- coding: utf-8 -*-
"""
@author:XuMing(xuming624@qq.com)
@description:
"""
from collections import defaultdict


def text_segmentate(text, maxlen, seps='\n', strips=None):
    """将文本按照标点符号划分为若干个短句
    """
    text = text.strip().strip(strips)
    if seps and len(text) > maxlen:
        pieces = text.split(seps[0])
        text, texts = '', []
        for i, p in enumerate(pieces):
            if text and p and len(text) + len(p) > maxlen - 1:
                texts.extend(text_segmentate(text, maxlen, seps[1:], strips))
                text = ''
            if i + 1 == len(pieces):
                text = text + p
            else:
                text = text + p + seps[0]
        if text:
            texts.extend(text_segmentate(text, maxlen, seps[1:], strips))
        return texts
    return [text]


def longest_common_substring(source, target):
    """
    LCS substring
    最长公共子串（source和target的最长公共切片区间）
    返回：子串长度, 所在区间（四元组）
    注意：最长公共子串可能不止一个，所返回的区间只代表其中一个。
    """
    c, l, span = defaultdict(int), 0, (0, 0, 0, 0)
    for i, si in enumerate(source, 1):
        for j, tj in enumerate(target, 1):
            if si == tj:
                c[i, j] = c[i - 1, j - 1] + 1
                if c[i, j] > l:
                    l = c[i, j]
                    span = (i - l, i, j - l, j)
    return l, span


def longest_common_subsequence(source, target):
    """
    LCS subsequence
    最长公共子序列（source和target的最长非连续子序列）
    返回：子序列长度, 映射关系（映射对组成的list）
    注意：最长公共子序列可能不止一个，所返回的映射只代表其中一个。
    """
    c = defaultdict(int)
    for i, si in enumerate(source, 1):
        for j, tj in enumerate(target, 1):
            if si == tj:
                c[i, j] = c[i - 1, j - 1] + 1
            elif c[i, j - 1] > c[i - 1, j]:
                c[i, j] = c[i, j - 1]
            else:
                c[i, j] = c[i - 1, j]
    l, mapping = c[len(source), len(target)], []
    i, j = len(source) - 1, len(target) - 1
    while len(mapping) < l:
        if source[i] == target[j]:
            mapping.append((i, j))
            i, j = i - 1, j - 1
        elif c[i + 1, j] > c[i, j + 1]:
            j = j - 1
        else:
            i = i - 1
    return l, mapping[::-1]


def red_color(text):
    return '\033[1;31;40m%s\033[0m' % text


def green_color(text):
    return '\033[1;32;40m%s\033[0m' % text


def text_compare(source, target):
    """
    基于最长公共子序列比较两个字符串差异，高亮差异部分
    refer: https://github.com/bojone/text_compare
    :param source: 句子1
    :param target: 句子2
    :return: 句子1结果，句子2结果，句子1相同字，句子1不同字，句子2相同字，句子2不同字
    """
    common_size, mapping = longest_common_subsequence(source, target)
    source_idxs = set([i for i, j in mapping])
    target_idxs = set([j for i, j in mapping])
    colored_source, colored_target = '', ''
    same_source_ids, diff_source_ids = set(), set()
    same_target_ids, diff_target_ids = set(), set()

    for i, j in enumerate(source):
        if i in source_idxs:
            colored_source += green_color(j)
            same_source_ids.add(i)
        else:
            colored_source += red_color(j)
            diff_source_ids.add(i)
    for i, j in enumerate(target):
        if i in target_idxs:
            colored_target += green_color(j)
            same_target_ids.add(i)
        else:
            colored_target += red_color(j)
            diff_target_ids.add(i)
    print(colored_source)
    print(colored_target)
    return colored_source, colored_target, same_source_ids, diff_source_ids, same_target_ids, diff_target_ids


if __name__ == "__main__":
    a = '关键词仅仅提供了一个维度的信息，我们还可以加入更丰富的信息 (如 词的词性。'
    b = '模型仅仅提供了一个维度的信息，我还可以加入更多其他信息，如:丰富的词性,还有其他特征！'
    colored_source, colored_target, same_source_ids, diff_source_ids, same_target_ids, diff_target_ids = \
        text_compare(a, b)
    # print(colored_source)
    # print(colored_target)
    print(same_source_ids, diff_source_ids, same_target_ids, diff_target_ids)

    t = text_segmentate(b, 6, seps='，:')
    print(t)
