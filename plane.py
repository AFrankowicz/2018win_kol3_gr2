class Plane():
	def __init__(self, orientation):
		self.orientation = orientation
		self.prev_orientation = 0
		self.correction = 0
		self.const_max_correction = 1

	def tilt(self, tilt):
		self.prev_orientation = self.orientation
		self.orientation += tilt

	def correct(self):
		diff = self.prev_orientation - self.orientation
		correction = abs(0.1 * diff + 0.9 * self.orientation)
		correction = min([self.const_max_correction, correction])
		
		if(self.orientation < 0):
			self.correction = correction
		if(self.orientation > 0):
			self.correction = -correction
			
		self.orientation += self.correction
			
	def get_orientation(self):
		return self.orientation
		
	def get_correction(self):
		return self.correction
			
