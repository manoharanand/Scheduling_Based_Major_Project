import matplotlib.pyplot as plt
import numpy as np

# x axis values
#Graph plot
# x = [100,200,300,400,500,600,700,800,900]
# # corresponding y axis values
# y = [25.833333333333336, 45.14285714285714, 65.5, 53.35714285714286, 67.3125, 65.84210526315789, 64.16666666666667, 71.24000000000001, 65.03571428571429]
# y2 = [23.400000000000002, 36.4, 64.2, 83.39999999999999, 83.39999999999999, 83.39999999999999, 83.39999999999999, 83.39999999999999, 83.39999999999999]
# y3 = [24.0, 29.799999999999997, 29.799999999999997, 40.0, 48.199999999999996, 48.199999999999996, 51.0, 51.0, 62.8]
# # plotting the points
# plt.plot(x, y, label = 'Sequential')
# plt.plot(x, y2, label = 'best fit')
# plt.plot(x,y3, label = 'worse fit')
#
# # setting x and y axis range
# plt.ylim(0, 100)
# plt.xlim(0, 1000)
#
# # naming the x axis
# plt.xlabel('x - axis')
# # naming the y axis
# plt.ylabel('y - axis')
#
# # giving a title to my graph
# plt.title('Cpu Utilization Comparison')
# plt.legend()
# # function to show the plot
# plt.show()

#Bar plot
x = [100,200,300,400,500,600,700,800,900]
# corresponding y axis values
#sequential
y1 = [36.26, 57.5125, 54.825, 68.84666666666666, 74.21052631578947, 70.56363636363636, 72.7695652173913, 74.51538461538462, 74.47241379310346]
#LeastLoaded
y2 = [46.36, 50.739999999999995, 53.879999999999995, 56.56, 56.56, 58.120000000000005, 58.120000000000005, 58.120000000000005, 58.120000000000005]
#bestFit
y3 = [41.959999999999994, 59.760000000000005, 79.17999999999999, 84.88, 88.56, 91.10000000000001, 91.10000000000001, 91.10000000000001, 92.56]
# plotting the points
# plt.plot(x, y1, label = 'Sequential')
# plt.plot(x, y2, label = 'best fit')
# plt.plot(x,y3, label = 'worse fit')
#
# # setting x and y axis range
# plt.ylim(0, 100)
# plt.xlim(0, 1000)

# # naming the x axis
# plt.xlabel('x - axis')
# # naming the y axis
# plt.ylabel('y - axis')
#
# # giving a title to my graph
# plt.title('Cpu Utilization Comparison')
# plt.legend()
# # function to show the plot
# plt.show()

# set height of bar
barWidth = 0.2
sequential = [i for i in y1]
best_fit = [i for i in y2]
least_loaded = [i for i in y3]

# Set position of bar on X axis
br1 = np.arange(len(sequential))
br2 = [x + barWidth + 0.05 for x in br1]
br3 = [x + barWidth + 0.05 for x in br2]

# Make the plot
plt.bar(br1, sequential, color='g', width=barWidth,
        edgecolor='grey', label='sequential')
plt.bar(br2, best_fit, color='r', width=barWidth,
        edgecolor='grey', label='best_fit')
plt.bar(br3, least_loaded, color='b', width=barWidth,
        edgecolor='grey', label='least_loaded')

# # Adding Xticks
# plt.xlabel('Scheduler', fontweight='bold', fontsize=15)
# plt.ylabel('Count', fontweight='bold', fontsize=15)
# plt.xticks([r + barWidth for r in range(len(sequential))],
#            ['sequential', 'best_fit', 'least_loaded'])

plt.xlabel('Number of Requests', fontweight ='bold', fontsize = 15)
plt.ylabel('Memory Utilization(%)', fontweight ='bold', fontsize = 15)
plt.xticks([r + barWidth for r in range(len(sequential))],
           [100, 200, 300, 400, 500, 600, 700, 800, 900])

plt.savefig('C:/Users/1997m/OneDrive/Desktop/Scheduling_Based_Major_Project/Memory_utilization.png')
plt.legend()
plt.show()

# plt.savefig('C:/Users/1997m/OneDrive/Desktop/Scheduling_Based_Major_Project/request_comparison.png')