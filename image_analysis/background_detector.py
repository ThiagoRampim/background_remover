from utils.math_utils import is_in_rectangle
import numpy as np
import cv2


__image_area: int
__min_area_multiplier = 0.0005
__max_area_multiplier = 0.95
__min_area = None
__max_area = None
__blur = 5
__canny_low = 15
__canny_high = 50
__kernel = np.ones((5, 5), np.uint8)
__morphology_iterations = 5

def setup_background_detector(image_width: float = None, image_height: float = None, image_area: float = None) -> None:
	global __image_area
	global __min_area
	global __max_area

	if image_area != None:
		__image_area = image_area
	else:
		__image_area = image_width * image_height
	
	__min_area = __image_area * __min_area_multiplier
	__max_area = __image_area * __max_area_multiplier

def detect_background(image, focus):
	image_edges = cv2.Canny(image, __canny_low, __canny_high)
	image_edges = cv2.morphologyEx(image_edges, cv2.MORPH_CLOSE, __kernel)

	image_contours = [
		(contour, cv2.contourArea(contour)) for contour in cv2.findContours(image_edges, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)[0]
	]

	blobs_mask = np.zeros(image_edges.shape, dtype = np.uint8)
	for contour in image_contours:
		if contour[1] > __min_area and contour[1] < __max_area:
			blobs_mask = cv2.fillConvexPoly(blobs_mask, contour[0], (255))
	blobs_mask = cv2.morphologyEx(blobs_mask, cv2.MORPH_CLOSE, __kernel, iterations = __morphology_iterations)

	blobs = [
		contour for contour in cv2.findContours(blobs_mask, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)[0]
	]

	objects_mask = np.zeros(blobs_mask.shape, dtype = np.uint8)
	for blob in blobs:
		contour_polygon = cv2.approxPolyDP(blob, 0, True)
		bound_rectangle = cv2.boundingRect(contour_polygon)
		if is_in_rectangle(focus, bound_rectangle):
			objects_mask = cv2.drawContours(objects_mask, [blob], 0, (255), cv2.FILLED)

	objects_mask = cv2.erode(objects_mask, None)

	background_mask = cv2.bitwise_not(objects_mask)

	return (objects_mask, background_mask)
