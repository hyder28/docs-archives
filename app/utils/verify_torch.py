import torch


def get_torch_device():
    torch_device = 'cuda' if torch.cuda.is_available() else 'cpu'

    return torch_device
