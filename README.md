Build SCDV model using Japanese Wikipedia
====

[![license](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](LICENSE)

## Features

- Build [SCDV](https://dheeraj7596.github.io/SDV/) model
- Using [fastText](https://github.com/facebookresearch/fastText) insted of word2vec
- Using [Juman++ v2](https://github.com/ku-nlp/jumanpp) to tokenize

## Usage

### Build Docker Image

```sh
$ docker-compose build
```

### Build Model

```sh
$ docker-compose run --rm app
```

## Licence

[Apache-2.0](LICENSE)

## Author

[Hideyuki TAKEUCHI (@chimerast)](https://github.com/chimerast)

## Reference

- [SCDV](https://dheeraj7596.github.io/SDV/)
- [Juman++ v2](https://github.com/ku-nlp/jumanpp)
- [fastText](https://github.com/facebookresearch/fastText)
