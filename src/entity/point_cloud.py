from dataclasses import dataclass

import torch


@dataclass
class CartesianCoordinates:
    coordinate: torch.Tensor

    def __post_init__(self):
        assert self.coordinates.shape[-1] == 3

    def to(self, device: torch.device):
        self.coordinates = self.coordinates.to(device)
