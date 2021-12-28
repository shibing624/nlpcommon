# -*- coding: utf-8 -*-
"""
@author:XuMing(xuming624@qq.com)
@description:
"""
import unittest
import sys

sys.path.append('..')
from nlpcommon import stopwords


class BaseTestCase(unittest.TestCase):
    def test_classifier(self):
        self.assertEqual(len(stopwords), 2438)


if "__main__" == __name__:
    unittest.main()
