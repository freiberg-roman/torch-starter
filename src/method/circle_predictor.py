from dataclasses import dataclass
from typing import Tuple

import torch
from omegaconf import DictConfig
from torch.nn.functional import mse_loss

from src.entity.point_cloud import CartesianCoordinates
from src.method.base import BaseMethod, DataIn, DataInference, DataOut, DataRaw, DataTarget
from src.model.encoder import SinusoidalPosEmb
from src.model.mlp import MLP

@dataclass
class CircleData(DataIn):
    coords: CartesianCoordinates


@dataclass
class CirclePrediction(DataOut):
    confidence: torch.Tensor

@dataclass
class CircleTarget(DataTarget):
    is_inside: torch.Tensor


@dataclass
class CircleCoordinates(DataRaw, DataInference):
    coords: CartesianCoordinates


class LearnCircleMethod(BaseMethod):
    def __init__(self, cfg: DictConfig):
        super().__init__()
        self.encoder = SinusoidalPosEmb(**cfg.encoder)
        self.mlp = MLP(**cfg.nerf)

        self.logging = {}

    def forward(self, circle_data: CircleData) -> CirclePrediction:
        assert isinstance(circle_data, CircleData)  # save guard

        x = self.encoder(circle_data.coords)
        out = self.mlp(x)

        self.logging = {"in_circle_confidence": out.detach().mean().cpu().numpy()}

        return out

    def compute_loss(self, model_out: CirclePrediction, target: CircleTarget) -> torch.Tensor:
        return mse_loss(model_out.confidence, target.is_inside)

    def pop_logs(self):
        out = self.logging
        self.logging = {}
        return out

    def pre_process(self, data: CircleCoordinates) -> Tuple[CircleData, CircleTarget]:
        input = CircleData(data.coords)
        # yes, this is a bit over-engineered for such a small example
        is_inside = torch.sum(data.coords.coordinate ** 2, dim=-1) < 1.0
        target = CircleTarget(is_inside)
        return input, target

    def inference(self, circle_data: CircleCoordinates):
        input = CircleData(circle_data.coords)
        return self.forward(input).confidence > 0.5
