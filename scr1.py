import matplotlib.pyplot as plt
import numpy as np
import random
import math

from numpy.lib.function_base import copy

from datetime import datetime
now = datetime.now()


def data_gen(num_points, min, max):
    datapoints = []
    for i in range(num_points):
        X = np.random.randint(low = min, high = max, size = 2)
        Y = (X[0], X[1])
        datapoints.append(Y)
    return datapoints

datapoints = data_gen(15, 0, 200)
N = len(datapoints)


def pointplotter(N, R):
    for i in range(N):
        x = datapoints[i][0]
        y = datapoints[i][1]
        x1 = copy(x)
        y1 = copy(y)
        circ = plt.Circle((x, y), R, fill = False)
        plt.gca().add_patch(circ)
        #area = math.pi * R**2
        #plt.scatter(x, y, s=area, alpha=0.5)
        plt.scatter(x, y, s = 5)


def get_intersections(x0, y0, x1, y1, r):

    d=math.sqrt((x1-x0)**2 + (y1-y0)**2)
    
    # non intersecting
    if d >  2*r :
        return None
    # One circle within other
    if d < 0:
        return None
    # coincident circles
    if d == 0:
        return None
    else:
        M = -(x1-x0)/(y1-y0)
        C = (y0 + y1 - ((x0+x1)*(x0-x1))/((y1-y0)))/2
        A = 1 + M**2
        B = 2*M*C -2*x0 -2*M*y0
        D = y0**2 - x0**2 + C**2 -r**2 -2*C*y0
        
        x3 = (-B + math.sqrt(B**2 - 4 * A * D))/(2*A)
        x4 = (-B - math.sqrt(B**2 - 4 * A * D))/(2*A)
        y3 = M*x3 + C
        y4 = M*x4 + C
    

        
        return (x3, y3, x4, y4)

vals = [5, 10, 15, 20, 50]

def plotter(R):
    for rad in R:
        filename = "foo" + str(rad)
        pointplotter(N, rad)

        for point1 in datapoints:
            for point2 in datapoints:
                if point1 != point2 and get_intersections(point1[0], point1[1], point2[0], point2[1], rad) != None:
                    plt.plot([point1[0], point2[0]], [point1[1], point2[1]])
                else:
                    pass
        plt.savefig(filename)

plotter(vals)