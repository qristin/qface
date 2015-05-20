"""
Bar chart demo with pairs of bars grouped for easy comparison.
"""
import numpy as np
import matplotlib.pyplot as plt



def gethistogram(ax, v, n):
    N = len(v)
    menMeans = v

    ind = np.arange(N)  # the x locations for the groups
    width = 0.35       # the width of the bars

    fig, ax = plt.subplots()
    rects1 = ax.bar(ind, menMeans, width, color='r')


    # add some text for labels, title and axes ticks
    ax.set_ylabel('Scores')
    ax.set_title('Scores by group and gender')
    ax.set_xticks(ind+width)
    ax.set_xticklabels( ('G1', 'G2', 'G3', 'G4', 'G5') )

    plt.show()

values = (16, 35, 12, 71, 27)
names = ('Name A', 'Name B', 'Name C', 'Name D', 'Name E')



gethistogram(values, names)

