import numpy as np
import operator as op

def getHistValues(prediction, names):
	length = 5
	labels = prediction[1]['labels']
	distances = prediction[1]['distances']
	# print names
	my_dict = {}
	my_counts = {}
	for x in range(0, len(labels)):
		name = names[labels[x]]
		if name in my_dict:
			my_dict[name] += [1/(distances[x])]
			my_counts[name] += 1
		else:
			my_dict[name] = 1/(distances[x])
			my_counts[name] = 1

	for key in my_counts:
		my_dict[key] = my_counts[key] * my_dict[key]
	if len(my_dict) < length:
		for x in range(0, length-len(my_dict)):
			name = "none"+str(x)
			my_dict[name] = 0
	#print my_counts
	return my_dict

def getKeyByValue(list, lookValue):
	willKey = ''
	for key, value in list.iteritems():
		if value == lookValue:
			willKey = key
	return willKey

def getWeightedPrediction(prediction,names):
	dict = getHistValues(prediction,names)
	value = max(dict, key=op.itemgetter(1))
	if (dict[value] > 0.015):
		return getKeyByValue(names,value)
	else: 
		return 0

def get_text(prediction, names):
	labels = prediction[1]['labels']
	distances = prediction[1]['distances']
	out = []
	for i in range(0,len(labels)):
		out.append(names[labels[i]] + ', ' + str(distances[i]))
	return out

def get_Name(prediction,names):
	dict = getHistValues(prediction,names)
	value = max(dict, key=op.itemgetter(1))
	if (dict[value] > 0.015):
		return ('Hello ' + str(value))
	else: 
		return ('Hello ' + str(value))


def gethistogram(ax, values, names):
    N = len(values)

    ind = np.arange(N)  # the x locations for the groups
    width = 0.35       # the width of the bars

    rects1 = ax.bar(ind, values, width, color='m')
    ax.axhline(0.015, color='blue', linewidth=2)

    # add some text for labels, title and axes ticks
    ax.set_ylabel('Scores')
    ax.set_title('Scores by group and gender')
    ax.set_xticks(ind+width)
    ax.set_xticklabels( names )
    ax.set_ylim([0,0.02])