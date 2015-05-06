"""
Bar chart demo with pairs of bars grouped for easy comparison.
"""
import numpy as np
import matplotlib.pyplot as plt



def gethistogram(v, n):
    n_groups = 5


    means_men = v


    fig, ax = plt.subplots()

    index = np.arange(n_groups)
    bar_width = 0.5

    opacity = 0.5
    error_config = {'ecolor': '0.3'}

    rects1 = plt.bar(index, means_men, bar_width,
                     alpha=opacity,
                     color='c',
                     error_kw=error_config,
                     label='Qers')

    plt.xlabel('Group')
    plt.ylabel('Scores')
    plt.title('Scores by person')
    plt.xticks(index + bar_width, n)
    plt.legend()

    plt.tight_layout()
    plt.show()

    return plt.figure()

values = (16, 35, 12, 71, 27)
names = ('Name A', 'Name B', 'Name C', 'Name D', 'Name E')



gethistogram(values, names)

