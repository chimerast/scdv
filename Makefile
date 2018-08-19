SHELL := /bin/bash
PATH := src:$(PATH)

BASENAME = corpus/wikipedia
NUM_CLUSTERS = 60
DIMENSION = 300

all: $(BASENAME).pvec

$(BASENAME).pvec: $(BASENAME).proba
	proba_wordvecs.py $(NUM_CLUSTERS) $(DIMENSION) $(BASENAME).proba

$(BASENAME).proba: $(BASENAME).vec
	idx_proba_dict.py $(NUM_CLUSTERS) $(BASENAME).vec

$(BASENAME).vec: $(BASENAME).norm
	fasttext skipgram -dim $(DIMENSION) -epoch 10 -minCount 20 -input $(BASENAME).norm -output $(BASENAME)

$(BASENAME).norm: $(BASENAME).txt
	word_idf_dict.py $(BASENAME).txt

clean:
	rm $(BASENAME).{pvec,proba,vec,bin,norm,idf}
