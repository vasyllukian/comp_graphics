from matplotlib import pyplot as plt
import numpy as np
fig, ax = plt.subplots()
fig.set_size_inches(10, 5.625)
f = open("D:\\the work\sem3 exclusive\comp graphics and multimedia\lab2\DS7.txt")
xs = []
ys = []
for line in f:
    y,x = line.split(" ")
    xs.append(x)
    ys.append(y)
f.close()
npxs = np.array(xs, 'int16') 
npys = np.array(ys, 'int16')
plt.xlim(0,960)
plt.ylim(0,540)
lines = plt.plot(npxs,npys)
plt.setp(lines, linestyle = '') 
ax.scatter(npxs, npys, s=1)
plt.show()