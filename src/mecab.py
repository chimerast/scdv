#!/usr/bin/env python3
# -*- Coding: utf-8 -*-

import subprocess
from subprocess import PIPE

class MeCab:
  def __init__(self, command='mecab'):
    try:
      self.process = subprocess.Popen([command, '-b', '81920', '-F', '%t\t%f[6]\n'], stdin=PIPE, stdout=PIPE, universal_newlines=True)
      self.stdin = self.process.stdin
      self.stdout = self.process.stdout
    except OSError:
      raise

  def __del__(self):
    self.process.stdin.close()
    try:
      self.process.kill()
      self.process.wait()
    except (OSError, TypeError, AttributeError):
      pass

  def analysis(self, sentence):
    self.stdin.write(sentence.lower() + '\n')
    self.stdin.flush()

    result = []
    while True:
      line = self.stdout.readline().rstrip()
      if line == 'EOS':
        break
      else:
        cols = line.split('\t')
        try:
          if cols[0] == '6' or cols[0] == '3':
            pass
          elif len(cols) == 2:
            result.append(cols[1].lower())
        except IndexError:
          print(line)
          raise
    return result
