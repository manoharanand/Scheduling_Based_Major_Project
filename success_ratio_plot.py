# import os os.environ['MPLCONFIGDIR'] = os.getcwd() + "/configs/"

import matplotlib.pyplot as plt
import numpy as np

x = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]
y1 = [0.98, 0.66, 0.04666666666666667, 0.34, 0.295, 0.243, 0.1934, 0.153, 0.1132]
y2 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
# Bar plot


# set height of bar
barWidth = 0.2
without_autoscaling = [i for i in y1]
with_autoscaling = [i for i in y2]


# Set position of bar on X axis
br1 = np.arange(len(with_autoscaling))
br2 = [x + barWidth + 0.05 for x in br1]


# Make the plot
plt.bar(br1, without_autoscaling, color='g', width=barWidth,
        edgecolor='grey', label='without_autoscaling')
plt.bar(br2, with_autoscaling, color='r', width=barWidth,
        edgecolor='grey', label='with_autoscaling')


# # Adding Xticks
# plt.xlabel('Scheduler', fontweight='bold', fontsize=15)
# plt.ylabel('Count', fontweight='bold', fontsize=15)
# plt.xticks([r + barWidth for r in range(len(sequential))],
#            ['sequential', 'best_fit', 'least_loaded'])

plt.xlabel('Number of Requests', fontweight='bold', fontsize=15)
plt.ylabel('Success Ratio(%)', fontweight='bold', fontsize=15)
plt.xticks([r + barWidth for r in range(len(with_autoscaling))],
           [100, 200, 300, 400, 500, 600, 700, 800, 900])
plt.legend()
plt.savefig('/home/pgcse/PycharmProjects/Scheduling_Based_Major_Project/success_ratio.png')

# plt.show()
