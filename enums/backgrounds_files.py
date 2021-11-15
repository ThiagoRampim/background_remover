from enum import Enum

class BackgroundFile(Enum):
	PURE_WHITE = "backgrounds/pure_white.mp4"

	def next(self):
		members = list(self.__class__)

		next_index = members.index(self) + 1
		if next_index >= len(members):
			next_index = 0
		
		return members[next_index]

	def previous(self):
		members = list(self.__class__)

		previous_index = members.index(self) - 1
		if previous_index < 0:
			previous_index = len(members) -1
		
		return members[previous_index]
