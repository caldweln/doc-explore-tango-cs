#!/usr/bin/python
#
#shift register device class
#
import PyTango
from PyTango.server import server_run, Device, DeviceMeta, device_property
from PyTango.server import attribute, AttrWriteType, command

from ShiftRegister import ShiftRegister

class ShiftRegisterDevice(PyTango.server.Device):
    __metaclass__ = PyTango.server.DeviceMeta
 
    #init device
    def init_device(self):
        try:
            PyTango.server.Device.init_device(self)

            #self.get_device_properties(self.get_device_class())
            self.RegisterSize = 8#device_property(dtype=int, default_value=8)
            self.info_stream("ShiftRegisterDevice.init_device() - initializing register of size", self.RegisterSize)
            self.d = ShiftRegister(self.RegisterSize)
        
        except:
            self.error_stream("ShiftRegisterDevice.init_device() - Error on getting device properties")
            self.set_state(PyTango.DevState.FAULT)
            self.set_status("Error on initializing device - get_device_device_properties failed")
            
        
        self.info_stream("ShiftRegisterDevice.init_device() - success, device ready for input")
        self.set_state(PyTango.DevState.STANDBY)
        self.set_status("Ready for input")


    #attributes
    registerValue = PyTango.server.attribute(label="RegisterValue", dtype=str, access=PyTango.AttrWriteType.READ, fget="readRegister", unit="BASE-2")
    
    def readRegister(self):
        return self.d.readRegister()

    #commands
    
    @PyTango.server.command(dtype_in=str)
    def ShiftBit(self, data):
        self.set_state(PyTango.DevState.MOVING)
        self.set_status("Shifting input to register")
        self.info_stream("ShiftRegisterDevice.ShiftBit() - shifting input", data)

        try:
            self.d.shiftBit(data)
            self.set_status("Successful bit shift")
            
            if self.d.isRegisterValid():
                self.set_state(PyTango.DevState.STANDBY)
                self.set_status(self.get_status()+" - Valid Register")
            else:
                self.warn_stream("ShiftRegisterDevice.ShiftBit() - register holds an invalid value")
                self.set_state(PyTango.DevState.FAULT)
                self.set_status(self.get_status()+" - Invalid Regsiter")
                
        except ValueError:
            error_desc = "Input bit to shift has an invalid value"
            self.error_stream("ShiftRegisterDevice.ShiftBit() - "+error_desc, data)
            self.set_state(PyTango.DevState.FAULT)
            self.set_status("Unsccessful bit shift - Invalid Register")
            PyTango.Except.throw_exception('DATA_OUT_OF_RANGE', error_desc,'ShiftRegisterDevice.ShiftBit()', PyTango.ErrSeverity.ERR)
            

if __name__ == "__main__":
    try:
        PyTango.server.server_run([ShiftRegisterDevice])
    except DevFailed, e:
            self.error_stream("ShiftRegisterDS __main__ - Received a DevFailed exception")
            PyTango.Except.print_exception(e)
    except:
            self.error_stream("ShiftRegisterDS __main__ - Unknown error has occured")
        


