import cv2

from enums.input_commands_enum import InputCommand
from enums.backgrounds_files import BackgroundFile
from image_analysis.face_detector import get_faces_from
from image_analysis.background_detector import setup_background_detector, detect_background


__selected_background: BackgroundFile = BackgroundFile.PURE_WHITE
__background_video = cv2.VideoCapture(__selected_background.value)

__camera_video = cv2.VideoCapture(0)
__camera_video_width = __camera_video.get(3)
__camera_video_heigth = __camera_video.get(4)
__camera_video_horizontal_center = __camera_video_width / 2
__camera_video_vertical_center = __camera_video_heigth / 2

setup_background_detector(__camera_video_width, __camera_video_heigth)

while True:
	_, frame = __camera_video.read()
	background_video_finished, background = __background_video.read()
	if not background_video_finished:
		__background_video.set(cv2.CAP_PROP_POS_FRAMES, 0)
		_, background = __background_video.read()

	faces = get_faces_from(frame)
	object_mask, background_mask = detect_background(frame, faces[0].center()) if len(faces) > 0 \
			else detect_background(frame, (__camera_video_horizontal_center, __camera_video_vertical_center))
	
	background = cv2.resize(background, (int(__camera_video_width), int(__camera_video_heigth)))

	frame = cv2.bitwise_and(frame, frame, mask = object_mask)
	background = cv2.bitwise_and(background, background, mask = background_mask)
	frame = cv2.add(background, frame)

	cv2.imshow('Frame', frame)

	key_input = cv2.waitKey(1) & 0xFF
	if key_input == InputCommand.QUIT.value:
		break
	elif key_input == InputCommand.SELECT_NEXT_BACKGROUND.value:
		__selected_background = __selected_background.next()
		__background_video = cv2.VideoCapture(__selected_background.value)
	elif key_input == InputCommand.SELECT_PREVIOUS_BACKGROUND.value:
		__selected_background = __selected_background.previous()
		__background_video = cv2.VideoCapture(__selected_background.value)

__camera_video.release()
cv2.destroyAllWindows()
