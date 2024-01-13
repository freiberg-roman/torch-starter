from dataclasses import dataclass

import torch


@dataclass
class CartesianCoordinates:
    coordinate: torch.Tensor

    def __post_init__(self):
        assert self.coordinate.shape[-1] == 2

    def to(self, device: torch.device):
        self.coordinate = self.coordinate.to(device)
