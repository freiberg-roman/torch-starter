from dataclasses import dataclass

import torch


@dataclass
class CartesianCoordinates:
    coordinates: torch.Tensor

    def __post_init__(self):
        assert self.coordinates.shape[-1] == 3

    def to(self, device: torch.device):
        self.coordinates = self.coordinates.to(device)


@dataclass
class PointCloud:
    position: torch.Tensor
    color: torch.Tensor

    def __post_init__(self):
        assert self.position.shape[-1] == 3
        assert self.color.shape[-1] == 3
        assert self.position.device == self.color.device

    def to(self, device: torch.device):
        self.position = self.position.to(device)
        self.color = self.color.to(device)
