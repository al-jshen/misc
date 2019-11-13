import numpy as np
import torch
from torch import nn, optim
from torchvision import transforms, datasets, models
from PIL import Image
import json
import matplotlib.pyplot as plt
from collections import OrderedDict


data_dir = '/home/js/flower_data'
train_dir = data_dir + '/train'
val_dir = data_dir + '/valid'


data_transforms = transforms.Compose([
    transforms.Resize(320),
    transforms.TenCrop(299),
    transforms.Lambda(lambda crops: torch.stack([transforms.ToTensor()(crop) for crop in crops]))
])

train_dat = datasets.ImageFolder(train_dir, transform=data_transforms)
val_dat = datasets.ImageFolder(val_dir, transform=data_transforms)

train_loader = torch.utils.data.DataLoader(train_dat, batch_size=16, shuffle=True, num_workers=4)
val_loader = torch.utils.data.DataLoader(val_dat, batch_size=16, shuffle=True, num_workers=4)


print(len(train_dat))
print(len(val_dat))

print(len(train_loader))
print(len(val_loader))

print(next(iter(train_loader))[0].shape)
print(next(iter(train_loader))[1].shape)


with open('cat_to_name.json', 'r') as f:
    cat_to_name = json.load(f)


model = models.inception_v3(pretrained=True)
model





for param in model.parameters():
    param.requires_grad = False


class net(nn.Module):
    def __init__(self, in_dims, out_dims):
        super(net, self).__init__()
        self.fc1 = nn.Linear(in_dims, 1024)
        self.fc2 = nn.Linear(1024, 512)
        self.fc3 = nn.Linear(512, out_dims)
        self.lsm = nn.LogSoftmax()
        self.lrelu = nn.LeakyReLU()
        self.drop = nn.Dropout(p=0.3)

    def forward(self, x):
        x = self.drop(self.lrelu(self.fc1(x)))
        x = self.drop(self.lrelu(self.fc2(x)))
        x = self.drop(self.lrelu(self.fc3(x)))
        x = self.lsm(x)
        return(x)


clf = net(2048, 102)
aux_clf = net(768, 102)

model.fc = clf
model.AuxLogits.fc = aux_clf

model



if torch.cuda.is_available():
    model = model.cuda()
    print('Using GPU')
else:
    print('Using CPU')



loss_fn = nn.NLLLoss()
optimizer = optim.Adam(model.parameters(), lr=1e-2)



feature, label = next(iter(train_loader))
feature, label = feature.cuda(), label.cuda()
batch_size, n_crops, channels, height, width = feature.shape
flattened = feature.view(-1, channels, height, width)
output, aux_output = model.forward(flattened)
output = output.view(batch_size, n_crops, -1).mean(1)
aux_output = aux_output.view(batch_size, n_crops, -1).mean(1)
loss1 = loss_fn(output, label)
loss2 = loss_fn(aux_output, label)
loss = loss1 + 0.35 * loss2
print(loss.item())





epochs = 3

for e in range(epochs):
    train_loss = 0
    model.train()
    for feature, label in train_loader:
        if torch.cuda.is_available():
            feature, label = feature.cuda(), label.cuda()
        optimizer.zero_grad()
        batch_size, n_crops, channels, height, width = feature.shape
        flattened = feature.view(-1, channels, height, width)
        output, aux_output = model(flattened)
        output = output.view(batch_size, n_crops, -1).mean(1)
        aux_output = aux_output.view(batch_size, n_crops, -1).mean(1)
        loss1 = loss_fn(output, label)
        loss2 = loss_fn(aux_output, label)
        loss = loss1 + 0.35 * loss2
        loss.backward()
        optimizer.step()
        train_loss += loss.item()

    test_loss = 0
    model.eval()
    for feature, label in test_loader:
        if torch.cuda.is_available():
            feature, label = feature.cuda(), label.cuda()
        batch_size, n_crops, channels, height, width = feature.shape
        flattened = feature.view(-1, channels, height, width)
        output = model(flattened)
        output = output.view(batch_size, n_crops, -1).mean(1)
        loss = loss_fn(output, label)
        test_loss += loss.item()

    print(f"Epoch: {e+1}/{epochs}  |  Training loss: {train_loss:.6f}  |  Testing loss: {test_loss:.6f}")






