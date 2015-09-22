#!/usr/bin/python
#
#shift register 
#

import string
import re
		
class ShiftRegister:
	
	def __init__(self, size=8):
		self._register = "0" * size						#register represented by string
				
	def shiftBit(self, bit):
		if len(bit) != 1:								#one char per shift
			self._register = self._register[1:] + "x"	#invalid input represented by 'x'
			raise ValueError, bit
		if (ord(bit) not in range(ord("0"),ord("2"))):	#register is of base-2 form
			self._register = self._register[1:] + "x"
			raise ValueError, bit
			
		self._register = self._register[1:] + bit		#shift input to LSB
			
	def readRegister(self):
		return self._register
		
	def isRegisterValid(self):
		return bool(re.compile('^[0-1]+\Z').match(self._register))


#class - ShiftRegister
