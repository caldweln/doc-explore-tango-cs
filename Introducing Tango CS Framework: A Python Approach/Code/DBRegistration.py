#!/usr/bin/python
#
#database registration
#
import PyTango


d_info = PyTango.DbDevInfo()
d_info.server = "ShiftRegisterDS/test"
d_info._class = "ShiftRegisterDevice"
d_info.name = "virtual/shift_register/test1"

db = PyTango.Database()
db.add_device(d_info)
