import cv2
import os
import subprocess
import numpy as np
import matplotlib.pyplot as plt

cap = cv2.VideoCapture('/Users/js/Desktop/test.mp4')
savedir = '/Users/js/Desktop/testing'
n_rings = 2000
nframes = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
everynth = nframes // n_rings
ncaps = nframes // everynth
colours = np.zeros((ncaps, 3))
print(ncaps)

count = 0
while cap.isOpened():
    count += 1
    ret, frame = cap.read()
    if ret:
        if count % everynth == 0:
            rgb = frame.mean(axis=(0,1))[::-1] / 256
            colours[count // everynth - 1] = rgb
            print(count // everynth - 1)
        else:
            continue
    else:
        break

cap.release()
cv2.destroyAllWindows()

np.savetxt(f'{savedir}/cols.csv', colours, delimiter=',')

radii = np.linspace(1e-3, ncaps * 1, ncaps)

ax = plt.gca()
ax.cla()
ax.axis('off')
ax.set_xlim((-1.1 * max(radii)), 1.1 * max(radii))
ax.set_ylim((-1.1 * max(radii)), 1.1 * max(radii))
ax.set_aspect(1)

for idx, (r, c) in enumerate(zip(radii, colours)):
    circ = plt.Circle((0, 0), radius=r, fill=None, color=c)
    ax.add_artist(circ)
    plt.savefig(f'{savedir}/%d.png' % idx)

subprocess.call(['ffmpeg', '-start_number', '0', '-i', f'{savedir}/%d.png', '-vcodec', 'mpeg4', '-q:v', '1', f'{savedir}/out.avi'])

for i in range(len(radii) - 1):
    subprocess.call(['rm', f'{savedir}/{i}.png'])
