class BackgroundFile(enumerate):
	BEACH_1 = "backgrounds/beach_1.mp4"
	BEACH_2 = "backgrounds/beach_2.mp4"
	FARM_1 = "backgrounds/farm_1.mp4"

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
