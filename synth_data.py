import random
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure


seed = 46
random.seed(seed)
np.random.seed(seed)
figure(figsize=(12, 8), dpi=80)

def synth_imaginary(n):



        distrib = 0.5
        start_value = 80

        max_step = 0.05
        min_step = 0.001

        arr = [80]
        for i in range(1, n):
            checker = random.random() - distrib > 0
            if checker:
                arr.append(arr[i - 1] + arr[i - 1] * random.uniform(min_step, max_step))
                max_step += random.uniform(0.001, 0.005)
                min_step += random.uniform(0.001, 0.005)
                distrib += random.uniform(0.01, 0.05)

            else:
                arr.append(arr[i - 1] - arr[i - 1] * random.uniform(min_step, max_step))
                max_step -= random.uniform(0.001, 0.005)
                min_step -= random.uniform(0.001, 0.005)
                distrib -= random.uniform(0.01, 0.05)

            if distrib > 0.55 or distrib < 0.45:
                distrib = 0.5
                max_step = 0.05
                min_step = 0.001
        return arr
y = synth_imaginary(1000)
plt.plot(range(0, 1000), y)
plt.show()