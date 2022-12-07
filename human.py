import matplotlib.pyplot as plt
import numpy as np

def read(filename):
    with open(filename) as f:
        lines = f.readlines()

    duration = float(lines[2].split()[2])
    samples = np.asarray(lines[4:], dtype=int)
    
    return samples, duration, len(samples)

data = read("anton2.txt")[0]

plt.plot(data)
plt.show()