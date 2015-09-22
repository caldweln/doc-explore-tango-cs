import unittest
from ShiftRegister import ShiftRegister

class ShiftRegisterTestCase(unittest.TestCase):
			
	seed_size = 8
	seed_word = "11001010"
		
	def setUp(self):
		self.d = ShiftRegister(self.seed_size)		
		
	def tearDown(self):
		pass
		
	def test_Init(self):
		#test init
		self.assertEqual(len(self.d.readRegister()), self.seed_size)
		
	def test_ShiftBits(self):
		#test shiftBit
		for i in range(len(self.seed_word)):
			self.d.shiftBit(self.seed_word[i])
			
		#test readRegister
		self.assertEqual(self.d.readRegister(), self.seed_word)


if __name__ == '__main__':
    unittest.main()
