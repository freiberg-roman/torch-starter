import hydra
from omegaconf import DictConfig
from torch.optim.optimizer import Optimizer
from torch.utils.data.dataloader import DataLoader
from tqdm import tqdm

from src.data.base import BaseDS
from src.data.selector import get_dataset
from src.method.selector import get_method
from src.util.optimizer_selector import get_optimizer


@hydra.main(version_base=None, config_path="config", config_name="train")
def main(cfg: DictConfig):
    dataset: BaseDS = get_dataset(cfg.data)
    dataloader = DataLoader(dataset, batch_size=32, collate_fn=dataset.collate_fn)
    method = get_method(cfg.method)
    optimizer: Optimizer = get_optimizer(method, cfg.optimizer)

    for epoch in range(cfg.schedule.epochs):
        for _, data in tqdm(enumerate(dataloader)):
            model_in, target = method.pre_process(data)
            out = method(model_in)
            loss = method.compute_loss(out, target)

            optimizer.zero_grad()
            loss.backward()
            optimizer.step()

            # Use your logging method here
            # to_log = method.pop_logs()

        # Save your model afther each n_th epoch
        save_model = (epoch + 1) % cfg.schedule.save_every_n_epochs == 0
        if save_model:
            print("Saving model...")
            ...


if __name__ == "__main__":
    main()
