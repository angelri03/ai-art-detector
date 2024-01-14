import torch.nn as nn

class Net(nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = nn.Sequential(
            nn.Conv2d(1, 64, 2, 1, 1),
            nn.MaxPool2d(2, 2, 1),
            nn.ReLU(),
            
            nn.Conv2d(64, 128, 2, 1, 1),
            nn.MaxPool2d(2, 2, 1),
            nn.ReLU(),

            nn.Conv2d(128, 256, 2, 1, 1),
            nn.MaxPool2d(2, 2, 1),
            nn.ReLU(),
        )

        self.fc = nn.Sequential(
            nn.Flatten(),
            nn.Linear(4096*2*2, 128),
            nn.ReLU(),
            nn.Linear(128, 1),
            nn.Sigmoid()
        )

    def forward(self, x):
        x = self.conv(x)
        x = x.view(x.size(0), -1)
        x = self.fc(x)

        return x