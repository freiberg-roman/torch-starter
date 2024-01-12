from omegaconf import DictConfig
from src.data.random_coordinates import RandomCoordinatesDS


def get_dataset(cfg: DictConfig):
    return RandomCoordinatesDS(cfg.dimensions, cfg.amount)
