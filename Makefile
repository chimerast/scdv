BASENAME = corpus/wikipedia
N = 60

all: $(BASENAME).proba

$(BASENAME).proba: $(BASENAME).vec
	./src/idx_proba_dict.py $(N) $(BASENAME).vec

$(BASENAME).vec: $(BASENAME).norm
	fasttext skipgram -dim 300 -epoch 10 -minCount 20 -input $(BASENAME).norm -output $(BASENAME)

$(BASENAME).norm: $(BASENAME).txt
	./src/word_idf_dict.py $(BASENAME).txt

clean:
	rm $(BASENAME).proba $(BASENAME).vec $(BASENAME).bin $(BASENAME).norm $(BASENAME).idf
