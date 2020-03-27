from rrt.algorithmRRT import rrt
import matplotlib.pyplot as plt
from input.input import drones, colors
from mpl_toolkits.mplot3d import Axes3D, axes3d
import sys

def main():
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')



    while True:
        check = []
        for j in range(len(drones)):
            rrt(drone = drones[j], target=drones[j].finish)
            check.append(drones[j].RRTfinished)

        if all(check) : break



    for j in range(len(drones)):
        for k in range(len(drones[j].path)):
            ax.scatter(drones[j].path[k][0],drones[j].path[k][1], drones[j].path[k][2], color = colors[j])



    plt.show()

if __name__ == "__main__":
    main()