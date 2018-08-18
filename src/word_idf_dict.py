#!/usr/bin/env python3
# -*- Coding: utf-8 -*-

import sys
import os
import re
import pickle
from tqdm import tqdm
import numpy as np
from jumanpp import Jumanpp
from sklearn.feature_extraction.text import TfidfVectorizer

wikiFile = sys.argv[1]
baseFile = os.path.splitext(wikiFile)[0]
normFile = baseFile + '.norm'
idfFile = baseFile + '.idf'

wikiStartTag = re.compile('^<doc[^>]*>$')
wikiEndTag = re.compile('^</doc>$')

jumanpp = Jumanpp()

def tokenize(path):
    file_size = os.path.getsize(path)
    pbar = tqdm(total=file_size)

    with open(path, 'r', encoding='utf-8') as file:
        doc = []
        skip = True

        for line in file:
            pbar.update(len(line.encode()))
            line = line.rstrip()
            if wikiStartTag.match(line):
                doc = []
                if 'title="Wikipedia:' in line:
                    skip = True
            elif wikiEndTag.match(line):
                if not skip:
                    yield doc
                else:
                    skip = False
            elif not skip:
                doc.append(jumanpp.analysis(line))

    pbar.close()

def extract(path, file):
    for doc in tokenize(path):
        lines = [' '.join(line) for line in doc]
        file.write('\n'.join(lines) + '\n')
        yield ' '.join(lines)

vec = TfidfVectorizer(lowercase=False, dtype=np.float32)

with open(normFile, 'w') as f:
    vec.fit_transform(extract(wikiFile, f))

words = vec.get_feature_names()
idf = vec._tfidf.idf_

word_idf_dict = dict(zip(words, idf))

with open(idfFile, 'wb') as f:
    pickle.dump(word_idf_dict, f)
