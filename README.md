# nlpcommon

[![PyPI version](https://badge.fury.io/py/nlpcommon.svg)](https://badge.fury.io/py/nlpcommon)
[![Contributions welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg)](CONTRIBUTING.md)
[![GitHub contributors](https://img.shields.io/github/contributors/shibing624/nlpcommon.svg)](https://github.com/shibing624/nlpcommon/graphs/contributors)
[![License Apache 2.0](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](LICENSE)
[![python_vesion](https://img.shields.io/badge/Python-3.5%2B-green.svg)](requirements.txt)
[![GitHub issues](https://img.shields.io/github/issues/shibing624/nlpcommon.svg)](https://github.com/shibing624/nlpcommon/issues)
[![Wechat Group](http://vlog.sfyc.ltd/wechat_everyday/wxgroup_logo.png?imageView2/0/w/60/h/20)](#Contact)


nlpcommon, Python Text Tool. Python3开发。


**Guide**

- [Feature](#Feature)
- [Install](#install)
- [Usage](#usage)
- [Dataset](#Dataset)
- [Contact](#Contact)
- [Cite](#Cite)
- [Reference](#reference)

# Feature

**nlpcommon** is a python Open Source Toolkit for text classification. The goal is to implement
text analysis algorithm, so as to achieve the use in the production environment.

**nlpcommon** has the characteristics
of clear algorithm, high performance and customizable corpus.

Functions：
### Classifier
  - [x] LogisticRegression
  - [x] Random Forest
  - [x] Decision Tree
  - [x] K-Nearest Neighbours
  - [x] Naive bayes
  - [x] Xgboost
  - [x] Support Vector Machine(SVM)
  - [x] TextCNN
  - [x] TextRNN_Att
  - [x] Fasttext
  - [x] Bert

### Cluster
  - [x] MiniBatchKmeans

While providing rich functions, **nlpcommon** internal modules adhere to low coupling, model adherence to inert loading, dictionary publication, and easy to use.

# Install

- Requirements and Installation

```
pip3 install nlpcommon
```

or

```
git clone https://github.com/shibing624/nlpcommon.git
cd nlpcommon
python3 setup.py install
```


# Usage
## data

### Stopwrods

[examples/base_demo.py](examples/base_demo.py):


```python
import sys

sys.path.append('..')
from nlpcommon import stopwords

if __name__ == '__main__':
    print(len(stopwords), stopwords)
```

output:

```shell
2438 {'．', '大家', '孰知', '至于', './', '知道', '二话没说', '一何', '从宽', 'especially' ... }
```


# Contact

- Issue(建议)：[![GitHub issues](https://img.shields.io/github/issues/shibing624/nlpcommon.svg)](https://github.com/shibing624/nlpcommon/issues)
- 邮件我：xuming: xuming624@qq.com
- 微信我：加我*微信号：xuming624*, 进Python-NLP交流群，备注：*姓名-公司名-NLP*
<img src="http://42.193.145.218/github_data/xm_wechat_erweima.png" width="200" />


# Cite

如果你在研究中使用了nlpcommon，请按如下格式引用：

```latex
@software{nlpcommon,
  author = {Xu Ming},
  title = {nlpcommon: A Tool for Text NLP},
  year = {2021},
  url = {https://github.com/shibing624/nlpcommon},
}
```

# License


授权协议为 [The Apache License 2.0](LICENSE)，可免费用做商业用途。请在产品说明中附加nlpcommon的链接和授权协议。


# Contribute
项目代码还很粗糙，如果大家对代码有所改进，欢迎提交回本项目，在提交之前，注意以下两点：

 - 在`tests`添加相应的单元测试
 - 使用`python setup.py test`来运行所有单元测试，确保所有单测都是通过的

之后即可提交PR。


# Reference

- pytextclassifier
