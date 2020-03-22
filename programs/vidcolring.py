import cv2
import os
import numpy as np
import matplotlib.pyplot as plt

cap = cv2.VideoCapture('/Users/js/Desktop/test.mp4')
n_rings = 100
nframes = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
everynth = int(nframes/n_rings)
ncaps = nframes // everynth
colours = np.zeros((ncaps, 3))

count = 0
while cap.isOpened():
    count += 1
    ret, frame = cap.read()
    if ret:
        if count % everynth == 0:
            rgb = frame.mean(axis=(0,1))[::-1] / 255
            colours[count // everynth - 1] = rgb
        else:
            continue
    else:
        break

cap.release()
cv2.destroyAllWindows()

ax = plt.gca()
ax.cla()
ax.axis('off')

radii = np.linspace(1e-3, ncaps * 1e-3, ncaps)
for r, c in zip(radii, colours):
    circ = plt.Circle((0, 0), radius=r, fill=None, color=c)
    ax.add_artist(circ)

ax.set_xlim((-1.1 * max(radii)), 1.1 * max(radii))
ax.set_ylim((-1.1 * max(radii)), 1.1 * max(radii))
ax.set_aspect(1)
plt.show()


