#!/usr/bin/env python3
# -*- Coding: utf-8 -*-

import sys
import os
import signal
import pickle
import gensim
import numpy as np

signal.signal(signal.SIGINT, signal.SIG_DFL)

num_clusters = int(sys.argv[1])
dimension = int(sys.argv[2])

wikiFile = sys.argv[3]
baseFile = os.path.splitext(wikiFile)[0]
idfFile = baseFile + '.idf'
modelFile = baseFile + '.vec'
probaFile = baseFile + '.proba'
probaVecFile = baseFile + '.pvec'

model = gensim.models.KeyedVectors.load_word2vec_format(modelFile, binary=False)
idx_proba_dict = pickle.load(open(probaFile, 'rb'))
word_idf_dict = pickle.load(open(idfFile, 'rb'))

proba_wordvecs = {}
for word in idx_proba_dict:
  proba_wordvecs[word] = np.zeros(num_clusters * dimension, dtype=np.float32)
  if word in model and word in idx_proba_dict and word in word_idf_dict:
    for index in range(0, num_clusters):
      proba_wordvecs[word][index*dimension:(index+1)*dimension] = model[word] * idx_proba_dict[word][index] * word_idf_dict[word]

with open(probaVecFile, 'wb') as f:
  pickle.dump(proba_wordvecs, f)
