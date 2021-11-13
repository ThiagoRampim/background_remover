import numpy as np


def distance(position_1, position_2):
	position_1 = np.array(np.int64(position_1[0]), np.int64(position_1[1]))
	position_2 = np.array(np.int64(position_2[0]), np.int64(position_2[1]))
	return np.sqrt(np.sum((position_1 - position_2) ** 2))

def is_in_circle(dot, circle) -> bool:
	return distance(dot, circle[0]) <= circle[1]

def is_in_rectangle(dot, rectangle) -> bool:
	return (dot[0] >= rectangle[0] and dot[0] <= rectangle[0] + rectangle[2]) \
		and (dot[1] >= rectangle[1] and dot[1] <= rectangle[1] + rectangle[3])
