#!/usr/bin/env python3
# -*- Coding: utf-8 -*-

import sys
import os
import signal
import pickle
import gensim
import numpy as np
from mecab import MeCab
from jumanpp import Jumanpp

signal.signal(signal.SIGINT, signal.SIG_DFL)

num_clusters = int(sys.argv[1])
dimension = int(sys.argv[2])

wikiFile = sys.argv[3]
baseFile = os.path.splitext(wikiFile)[0]
probaVecFile = baseFile + '.pvec'

analyzer = MeCab()

proba_wordvecs = pickle.load(open(probaVecFile, 'rb'))

def scdv(sentence):
  words = analyzer.analysis(sentence)

  vec = np.zeros(num_clusters * dimension, dtype=np.float32)

  for word in words:
    if word in proba_wordvecs:
      vec += proba_wordvecs[word]

  return vec
