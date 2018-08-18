#!/usr/bin/env python3
# -*- Coding: utf-8 -*-

import subprocess
from subprocess import PIPE

class Jumanpp:
  def __init__(self, command='jumanpp'):
    try:
      self.process = subprocess.Popen([command], stdin=PIPE, stdout=PIPE, universal_newlines=True)
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
      elif line[0] == '@' or line[0] == ' ':
        pass
      else:
        cols = line.split()
        try:
          if cols[2] == '*':
            result.append(cols[0])
          elif cols[4] == '1' or cols[4] == '9':
            pass
          else:
            result.append(cols[2])
        except IndexError:
          print(line)
          raise
    return result
