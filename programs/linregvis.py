import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import torch
from torch import nn, optim
import seaborn as sns
from sklearn import linear_model
from sklearn.metrics import mean_squared_error

fig, ax1 = plt.subplots(1, figsize=(12, 6))

pts = 250
max_x = 40
m, b = np.random.randint(0, 100, 1), np.random.randint(0, 100, 1)
noise = m * np.random.randn(pts, 1)

x = max_x * np.random.rand(pts, 1)
y = m * x + b + noise
sns.regplot(x.squeeze(), y.squeeze())

reg = linear_model.LinearRegression()
reg.fit(x, y)
pred = reg.predict(x)
print(mean_squared_error(y, pred))


model = nn.Sequential(nn.Linear(1, 1))
loss_fn = nn.MSELoss()
optimizer = optim.SGD(model.parameters(), lr=2e-4)

line, = ax1.plot([], [], c='firebrick')

x, y = torch.from_numpy(x), torch.from_numpy(y)

def run_epoch(x, y):
    optimizer.zero_grad()
    output = model(x.float())
    loss = loss_fn(output, y.float())
    loss.backward()
    optimizer.step()
    params = list(model.parameters())
    weight, bias = params[0].item(), params[1].item()
    output, label = output.detach().numpy(), y.detach().numpy()
    return loss, weight, bias, output, y

def init():
    line.set_data([], [])
    return line,

def animate(i):
    loss, weight, bias, feature, label = run_epoch(x, y)
    print(loss.item())
    line.set_data([0, max_x], [bias, max_x * weight + bias])
    return line,

ani = animation.FuncAnimation(fig, animate, init_func=init, interval=100)
plt.show()
