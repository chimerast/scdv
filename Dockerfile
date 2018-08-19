FROM python:3.6

RUN apt update \
  && apt install -y cmake \
  && apt clean \
  && rm -rf /var/lib/apt/lists/*

WORKDIR /build
RUN git clone https://github.com/facebookresearch/fastText.git

WORKDIR /build/fastText/build
RUN cmake .. -DCMAKE_BUILD_TYPE=Release
RUN make -j8 && make install

WORKDIR /build
RUN wget https://github.com/ku-nlp/jumanpp/releases/download/v2.0.0-rc2/jumanpp-2.0.0-rc2.tar.xz
RUN mkdir jumanpp
RUN tar xf jumanpp-2.0.0-rc2.tar.xz -C jumanpp --strip-components 1
RUN sed -i -e "s/size_t maxInputBytes = 4 \* 1024/size_t maxInputBytes = 20 \* 4 \* 1024/g" /build/jumanpp/src/core/analysis/analyzer.h

WORKDIR /build/jumanpp/build
RUN cmake .. -DCMAKE_BUILD_TYPE=Release
RUN make -j8 && make install

RUN pip install scikit-learn gensim tqdm

WORKDIR /app
COPY . .

CMD ["make"]
