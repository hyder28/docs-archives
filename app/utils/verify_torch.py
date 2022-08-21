import torch
# setting device on GPU if available, else CPU

def check_gpu():
    torch_device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    print('Using device:', torch_device)
    print()

    #Additional Info when using cuda
    if torch_device.type == 'cuda':
        print(torch.cuda.get_device_name(0))