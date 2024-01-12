from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Dict, Tuple

import torch


@dataclass
class DataRaw:
    pass


@dataclass
class DataIn:
    pass


@dataclass
class DataOut:
    pass


@dataclass
class DataTarget:
    pass


@dataclass
class DataInference:
    pass


class BaseMethod(ABC, torch.nn.Module):
    @abstractmethod
    def pre_process(self, data: DataRaw) -> Tuple[DataIn, DataTarget]:
        pass

    @abstractmethod
    def compute_loss(self, out: DataOut, target: DataTarget) -> torch.Tensor:
        pass

    @abstractmethod
    def inference(self, data: DataInference):
        pass

    @abstractmethod
    def pop_logs() -> Dict:
        pass
