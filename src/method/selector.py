from omegaconf import DictConfig

from src.method.base import BaseMethod
from src.method.circle_predictor import LearnCircleMethod


def get_method(cfg: DictConfig) -> BaseMethod:
    return LearnCircleMethod(cfg)
