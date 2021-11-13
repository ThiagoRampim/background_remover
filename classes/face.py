class Face:

	def __init__(self, position, landmark) -> None:
		self.position = position
		self.landmark = landmark

	def detach_position(self) -> tuple[int, int, int, int]:
		x_min = self.position.left()
		y_min = self.position.top()
		x_max = self.position.right()
		y_max = self.position.bottom()
		return int(x_min), int(y_min), int(x_max), int(y_max)
	
	def center(self):
		x_min, y_min, x_max, y_max = self.detach_position()
		return (
			(x_min + x_max) / 2,
			(y_min + y_max) / 2
		)
