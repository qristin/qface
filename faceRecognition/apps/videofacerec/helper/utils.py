

def weighted_nearest_neighbours(prediction):
	# labels = prediction[1].labels
	# distances = prediction[1].distances

	

	return prediction[0]

def get_text(prediction, names):
	labels = prediction[1]['labels']
	distances = prediction[1]['distances']
	out = []
	for i in range(0,len(labels)):
		out.append(names[labels[i]] + ', ' + str(distances[i]))
	return out
