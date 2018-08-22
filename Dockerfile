FROM python:3.6

RUN apt update \
  && apt install -y cmake mecab mecab-ipadic-utf8 libmecab-dev \
  && apt clean \
  && rm -rf /var/lib/apt/lists/*

## MeCab
WORKDIR /build
RUN git clone --depth 1 https://github.com/neologd/mecab-ipadic-neologd.git

WORKDIR /build/mecab-ipadic-neologd
RUN ./bin/install-mecab-ipadic-neologd -y -n -p /var/lib/mecab/dic/ipadic-utf8-neologd
RUN rm /etc/alternatives/mecab-dictionary \
  && ln -s /var/lib/mecab/dic/ipadic-utf8-neologd /etc/alternatives/mecab-dictionary

## fastText
WORKDIR /build
RUN git clone --depth 1 https://github.com/facebookresearch/fastText.git

WORKDIR /build/fastText/build
RUN cmake .. -DCMAKE_BUILD_TYPE=Release && make -j8 && make install

## Juman++ v2
WORKDIR /build
RUN wget https://github.com/ku-nlp/jumanpp/releases/download/v2.0.0-rc2/jumanpp-2.0.0-rc2.tar.xz \
  && mkdir jumanpp \
  && tar xf jumanpp-2.0.0-rc2.tar.xz -C jumanpp --strip-components 1 \
  && rm jumanpp-2.0.0-rc2.tar.xz
RUN sed -i -e "s/size_t maxInputBytes = 4 \* 1024/size_t maxInputBytes = 20 \* 4 \* 1024/g" /build/jumanpp/src/core/analysis/analyzer.h

WORKDIR /build/jumanpp/build
RUN cmake .. -DCMAKE_BUILD_TYPE=Release && make -j8 && make install

RUN pip install scikit-learn gensim tqdm

WORKDIR /app
COPY . .

CMD ["/bin/bash"]
