#!/usr/bin/python
#
#device server testing
#

import PyTango

d = PyTango.DeviceProxy("virtual/shift_register/test1")
d.registerValue
d.shiftBit("1")
d.shiftBit("1")
d.shiftBit("0")
d.shiftBit("0")
d.shiftBit("1")
d.shiftBit("0")
d.shiftBit("1")
d.shiftBit("0")
d.registerValue
