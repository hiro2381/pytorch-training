import torch
from torch import nn

if __name__ == "__main__":
    print("=====problem 1=====")
    _in = torch.ones(32, 1024)
    print(f"_in : {_in.shape}")

    print("=====problem 2=====")
    fc1 = nn.Linear(in_features=1024, out_features=256, bias=True)
    out1 = fc1(_in)
    print(f"out1 : {out1.shape}")

    print("=====problem 3=====")
    fc2 = nn.Linear(in_features=1024, out_features=2048, bias=True)
    out2 = fc2(_in)
    print(f"out2 : {out2.shape}")

    print("=====appendix=====")
    out3 = out1.reshape(32, 16, 16)
    print(f"out3 : {out3.shape}")