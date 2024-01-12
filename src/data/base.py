from abc import abstractmethod
from typing import List
from torch.utils.data.dataloader import Dataset

from src.method.base import DataRaw


class BaseDS(Dataset):

    @abstractmethod
    @classmethod
    def collate_fn(cls, batch: List[DataRaw]):
        pass
