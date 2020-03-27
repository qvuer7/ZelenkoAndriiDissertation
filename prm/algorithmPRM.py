from prm.functions import *



def algorithmPRM(drone):
    a = check_line_interception(drone)

    while a == True :
        pathLines = []
        for i in range(len(drone.path)):
            if i == len(drone.path) - 1:
                pass
            else:
                pathLines.append(
                    get_line(node1=drone.path[i], node2=drone.path[i + 1], dronesize=drone.dronesize, stepx=drone.stepx,
                             stepy=drone.stepy, stepz=drone.stepz))
            drone.pathLines = pathLines
        a = check_line_interception(drone)





