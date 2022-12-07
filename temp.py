import matplotlib.pyplot as plt
import numpy as np

def read(filename):
    with open(filename) as f:
        lines = f.readlines()

    duration = float(lines[2].split()[2])
    samples = np.asarray(lines[4:], dtype=int)
    
    return samples, duration, len(samples)
x = np.linspace(0, 113, 113)*10
data = read("anton2.txt")[0]
data = data[810:923]
k = 45/112
for i in range(len(data)):
    data[i] -= k*(112-i)
plt.plot(x, data)
plt.grid()
plt.show()
print(len(x), len(data))