from typing import List

from torch.utils.data.dataloader import Dataset

from src.method.base import DataRaw


class BaseDS(Dataset):
    @classmethod
    def collate_fn(cls, batch: List[DataRaw]):
        assert batch is not None
        raise NotImplementedError
