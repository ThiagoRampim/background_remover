from enum import Enum

class InputCommand(Enum):
	QUIT = ord('q')
	SELECT_NEXT_BACKGROUND = ord('p')
	SELECT_PREVIOUS_BACKGROUND = ord('o')
