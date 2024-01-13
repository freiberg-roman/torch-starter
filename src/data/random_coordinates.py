from dataclasses import dataclass
from typing import List

import torch

from src.data.base import BaseDS
from src.entity.point_cloud import CartesianCoordinates
from src.method.circle_predictor import CircleCoordinates


@dataclass
class SourceCoordinates(CircleCoordinates):
    coords: CartesianCoordinates


class RandomCoordinatesDS(BaseDS):
    def __init__(self, dimensions: int, amount: int):
        self.dimensions = dimensions
        self.amount = amount

    def __getitem__(self, _) -> SourceCoordinates:
        rand_point = torch.randn(size=(self.dimensions,))
        return SourceCoordinates(CartesianCoordinates(rand_point))

    @classmethod
    def collate_fn(cls, batch: List[SourceCoordinates]):
        stacked_coords = torch.stack([s.coords.coordinate for s in batch])
        return SourceCoordinates(CartesianCoordinates(stacked_coords))

    def __len__(self):
        return self.amount
