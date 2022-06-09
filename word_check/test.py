# -*- coding: utf-8 -*-
import jieba
import re
import itertools
import openpyxl as openpyxl
from collections import Counter

cut_words = []
wordsCout = []

for line in open('result.txt', encoding='gbk'):
    line.strip('\n')
    line = re.sub("[\：\·\—\，\。\“\ ”了]", "", line)
    seg_list = jieba.cut(line, cut_all=True)
    cut_words += seg_list
print(cut_words)
for i in itertools.combinations(cut_words, 2):
    wordsCout.append(i)
print(wordsCout)

counter = Counter()
for x in wordsCout:
    if len(x) > 1 and x != '\r\n':
        counter[x] += 1
print('\n词频统计结果：')
for (k, v) in counter.most_common(20):  # 输出词频最高的前两个词
    print("%s:%d" % (k, v))
