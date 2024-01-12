from typing import List
import torch
from dataclasses import dataclass
from src.data.base import BaseDS

from src.method.circle_predictor import CircleCoordinates

@dataclass
class SourceCoordinates(CircleCoordinates):
    coords: torch.Tensor

class RandomCoordinatesDS(BaseDS):

    def __init__(self, dimensions: int, amount: int):
        self.dimensions = dimensions
        self.amount = amount

    def __getitem__(self, _) -> SourceCoordinates:
        rand_point = torch.randn(size=(self.dimensions,))
        return SourceCoordinates(rand_point)

    @classmethod
    def collate_fn(cls, batch: List[SourceCoordinates]):
        stacked_coords = torch.stack([s.coords for s in batch])
        return SourceCoordinates(stacked_coords)

    def __len__(self):
        return self.amount
