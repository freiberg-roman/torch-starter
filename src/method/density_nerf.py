import torch
from omegaconf import DictConfig
from torch import nn

from src.entity.point_cloud import CartesianCoordinates
from src.model.encoder import SinusoidalPosEmb
from src.model.mlp import MLP


class DensityNerf(nn.Module):
    def __init__(self, cfg: DictConfig):
        super().__init__()
        self.encoder = SinusoidalPosEmb(**cfg.encoder)
        self.mlp = MLP(**cfg.nerf)

        self.logging = {}

    def forward(self, coords: CartesianCoordinates) -> torch.Tensor:
        x = self.encoder(coords.coordinates)
        out = self.mlp(x)
        return out

    def pop_logs(self):
        out = self.logging
        self.logging = {}
        return out
