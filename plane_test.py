import unittest
from plane import Plane
from task import simulator


#https://github.com/mic19/kol1_gr2
class PlaneTest(unittest.TestCase):
	def setUp(self):
		self.orientation = 0
		self.test_instance = Plane(self.orientation)

	def test_init(self):
		self.assertEqual(self.test_instance.orientation, self.orientation)
		self.assertEqual(self.test_instance.prev_orientation, 0)
		self.assertEqual(self.test_instance.correction, 0)
		self.assertEqual(self.test_instance.const_max_correction, 1)

	def test_tilt(self):
		prev_orientation = self.test_instance.prev_orientation
		self.test_instance.tilt(1)
		self.assertEqual(self.test_instance.prev_orientation, prev_orientation)
		self.assertEqual(self.test_instance.orientation, prev_orientation+1)

	def test_correct(self):
		self.test_instance.tilt(1)
		self.test_instance.correct()
		self.assertGreater(self.test_instance.orientation, self.test_instance.prev_orientation)

	def test_get_orientation(self):
		orientation = self.test_instance.orientation
		self.assertEqual(orientation, self.test_instance.get_orientation())

	def test_get_correction(self):
		correction = self.test_instance.correction
		self.assertEqual(correction, self.test_instance.get_correction())
