import torch
from torch import nn

class MyModule(nn.Module):
    def __init__(self, tensor_shape=(10,), add: float = 0.0, mul: float = 1.0):
        super().__init__()
        self.mytensor: torch.Tensor = torch.zeros(tensor_shape, dtype=torch.float32)
        self.elem_add: torch.Tensor = torch.tensor(add, dtype=torch.float32)
        self.elem_multiply: torch.Tensor = torch.tensor(mul, dtype=torch.float32)

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        return x + self.mytensor + (self.elem_add * self.elem_multiply)
    
if __name__ == "__main__":
    MyModule = MyModule(tensor_shape=(3, 3), add=2.0, mul=1.0)
    input_tensor = torch.ones((3, 3), dtype=torch.float32)
    output_tensor = MyModule(input_tensor)
    print("Input Tensor:\n", input_tensor)
    print("Output Tensor:\n", output_tensor)