#!/usr/bin/python
#
#shift register device client 
#

import sys
from PyQt4 import Qt    #from taurus.external.qt import Qt
from taurus.qt.qtgui.application import TaurusApplication
from taurus.qt.qtgui.panel import TaurusForm
from taurus.qt.qtgui.panel import TaurusCommandsForm

app = TaurusApplication(sys.argv)
panel = Qt.QWidget()
layout = Qt.QHBoxLayout()
panel.setLayout(layout)

attrForm = TaurusForm()
attrs = [ 'State', 'Status', 'registerValue' ]
attrForm.setModel([ 'virtual/shift_register/test1/%s' % attr for attr in attrs ])
attrForm.withButtons = False

cmdForm = TaurusCommandsForm()
cmdForm.setModel('virtual/shift_register/test1')
cmdForm.setViewFilters([lambda x: ('ShiftBit' == x.cmd_name)])
        
layout.addWidget(attrForm)
layout.addWidget(cmdForm)
panel.show()

sys.exit(app.exec_())
