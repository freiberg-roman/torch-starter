import os
from functools import reduce


def go_up_directories(n: int):
    return reduce(lambda dir, _: os.path.dirname(dir), range(n), os.path.dirname(__file__))


PROJECT_DIR = go_up_directories(3)
ASSSET_DIR = os.path.join(PROJECT_DIR, "asset")
DATA_DIR = os.path.join(PROJECT_DIR, "data")
