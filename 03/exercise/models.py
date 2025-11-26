import torch
from torch import nn

class ExerciseModel(nn.Module):
    def __init__ (self, out_features=64):
        super().__init__()
        self.conv = nn.Conv2d(in_channels=3, out_channels=256, kernel_size=5, stride=8)
        self.bn = nn.BatchNorm2d(num_features=256)
        self.rulu = nn.ReLU()

        in_features = 256 * 16 * 16
        self.fc = nn.Linear(in_features=in_features, out_features=out_features)

    def forward(self, x):
        x = self.conv(x)
        x = self.bn(x)
        x = self.rulu(x)
        x = torch.flatten(x, 1) #一元化
        x = self.fc(x)
        return x