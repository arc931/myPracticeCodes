import torch

if torch.cuda.is_available():
    print("1")
    device=torch.device("cuda")
else:
    device = torch.device("cpu")
    print("2")