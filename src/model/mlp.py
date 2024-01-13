import torch
from torch import nn
from torch.nn.functional import gelu


class MLP(nn.Module):
    def __init__(self, in_dim, out_dim, hidden_dim=16, hidden_layers=4):
        super().__init__()
        self.input_layer = nn.Linear(in_features=in_dim, out_features=hidden_dim)
        self.layers = nn.ModuleList(
            [
                nn.Linear(in_features=hidden_dim, out_features=hidden_dim)
                for _ in range(hidden_layers)
            ]
        )
        self.ouput_layer = nn.Linear(in_features=hidden_dim, out_features=out_dim)

    def forward(self, input: torch.Tensor) -> torch.Tensor:
        x = self.input_layer(input)
        x = gelu(x)

        for layer in self.layers:
            x = gelu(layer(x))

        out = self.ouput_layer(x)
        return out
