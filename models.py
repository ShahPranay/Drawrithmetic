import torch
import torch.nn as nn
import torch.nn.functional as F

class InfixClassifier(nn.Module):
  def __init__(self):
    super().__init__()
    self.conv1 = nn.Conv2d(1,32,5)
    self.layer1 = nn.Linear(12*12*32,32)
    #self.layer2 = nn.Linear(32,32)
    #self.layer3 = nn.Linear(32,32)
    self.output = nn.Linear(32,2)

  def forward(self,x):
    x = F.relu(self.conv1(x))
    x = F.max_pool2d(x,2,2)
    x = x.view(-1,12*12*32)
    x=F.relu(self.layer1(x))
    #x=F.relu(self.layer2(x))
    #x=F.relu(self.layer3(x))
    x = self.output(x)
    return torch.sigmoid(x)

class OperatorClassifier(nn.Module):
  def __init__(self):
    super().__init__()
    self.conv1 = nn.Conv2d(1,32,5)
    self.conv2 = nn.Conv2d(32,64,5)
    self.layer1 = nn.Linear(4*4*64,32)
    #self.layer2 = nn.Linear(32,32)
    #self.layer3 = nn.Linear(32,32)
    self.output = nn.Linear(32,4)

  def forward(self,x):
    x = F.relu(self.conv1(x))
    x = F.max_pool2d(x,2,2)
    x = F.relu(self.conv2(x))
    x = F.max_pool2d(x,2,2)
    x = x.view(-1,4*4*64)
    x = F.relu(self.layer1(x))
    #x=F.relu(self.layer2(x))
    #x=F.relu(self.layer3(x))
    x = self.output(x)
    return torch.sigmoid(x)

class DigitsClassifier(nn.Module):
  def __init__(self):
    super().__init__()
    self.conv1 = nn.Conv2d(1,32,5)
    self.conv2 = nn.Conv2d(32,64,5)
    self.layer1 = nn.Linear(4*4*64,64)
    self.layer2 = nn.Linear(64,32)
    #self.layer3 = nn.Linear(32,32)
    self.output = nn.Linear(32,10)

  def forward(self,x):
    x = F.relu(self.conv1(x))
    x = F.max_pool2d(x,2,2)
    x = F.relu(self.conv2(x))
    x = F.max_pool2d(x,2,2)
    x = x.view(-1,4*4*64)
    x = F.relu(self.layer1(x))
    x=F.relu(self.layer2(x))
    #x=F.relu(self.layer3(x))
    x = self.output(x)
    return torch.sigmoid(x)
