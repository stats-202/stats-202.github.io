#!python3
from absl import app
from absl import logging
import os


def main(argv):
  del argv
  assert os.path.exists("../results"), "results folder not found."
  assert os.path.exists("../data"), "data folder not found."

  from questions.ch3_ex9 import ch3_ex9
  ch3_ex9()

  from questions.ch3_ex14 import ch3_ex14
  ch3_ex14()

  from questions.ch10_ex9 import ch10_ex9
  ch10_ex9()

  logging.info("Run successful. Shutting down...")
  return 0


if __name__ == '__main__':
  app.run(main)
