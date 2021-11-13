import cv2
import dlib
from classes.face import Face


__FACE_DETECTOR = dlib.get_frontal_face_detector()
__FACE_DETAILS_DETECTOR = dlib.shape_predictor('image_analysis/shape_predictor_68_face_landmarks.dat')

def get_faces_from(image) -> list[Face]:
	image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
	face_positions = __FACE_DETECTOR(image_rgb)
	
	faces: list[Face] = []
	for face_position in face_positions:
		faces.append(Face(face_position, None))
	return faces

def get_faces_landmark_from(image) -> list[Face]:
	image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
	face_positions = __FACE_DETECTOR(image_rgb)

	faces: list[Face] = []
	for face_position in face_positions:
		face_landmark = __FACE_DETAILS_DETECTOR(image_rgb, face_position)
		faces.append(Face(face_position, face_landmark))

	return faces
