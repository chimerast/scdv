#!/usr/bin/env python3
# -*- Coding: utf-8 -*-

import sys
import os
import signal
import pickle
import gensim
from sklearn.mixture import GaussianMixture

signal.signal(signal.SIGINT, signal.SIG_DFL)

num_clusters = int(sys.argv[1])

wikiFile = sys.argv[2]
baseFile = os.path.splitext(wikiFile)[0]
modelFile = baseFile + '.vec'
probaFile = baseFile + '.proba'

model = gensim.models.KeyedVectors.load_word2vec_format(modelFile, binary=False)

clf = GaussianMixture(n_components=num_clusters, covariance_type='tied', init_params='kmeans', max_iter=50)
clf.fit(model.vectors)

idx_proba = clf.predict_proba(model.vectors)
idx_proba_dict = dict(zip(model.index2word, idx_proba))

pickle.dump(idx_proba_dict, open(probaFile, 'wb'))
