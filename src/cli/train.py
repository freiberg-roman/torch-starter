import hydra
from omegaconf import DictConfig
from torch.optim.optimizer import Optimizer
from torch.utils.data.dataloader import DataLoader
from tqdm import tqdm

from src.data.base import BaseDS
from src.data.selector import get_dataset
from src.method.selector import get_method
from src.util.optimizer_selector import get_optimizer


@hydra.main(version_base=None, config_path="conf", config_name="train")
def main(cfg: DictConfig):
    dataset: BaseDS = get_dataset(cfg.data)
    dataloader = DataLoader(dataset, batch_size=32, collate_fn=dataset.collate_fn)
    method = get_method(cfg.method)
    optimizer: Optimizer = get_optimizer(method, cfg.train.opti)

    for epoch in range(cfg.train.num_epochs):
        for _, data in tqdm(enumerate(dataloader)):
            target = data.get_target()
            out = method(data)
            loss = method.compute_loss(out, target)

            optimizer.zero_grad()
            loss.backward()
            optimizer.step()

            to_log = method.pop_logs()

            # Use your logging method here
            print(to_log)

        # Save your model afther each n_th epoch
        save_model = (epoch + 1) % cfg.schedule.save_every_n_epoch == 0
        if save_model:
            print("Saving model...")
            ...


if __name__ == "__main__":
    main()
