from omegaconf import DictConfig
from torch.optim.adamw import AdamW

from src.method.base import BaseMethod
def get_optimizer(method: BaseMethod,cfg: DictConfig):
    return AdamW(method.parameters(), lr=cfg.lr, weight_decay=cfg.weight_decay)
