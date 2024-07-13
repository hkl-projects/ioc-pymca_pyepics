from PyMca5.PyMcaGui.pymca.PyMcaMain import PyMcaMain
from PyMca5.PyMcaGui import PyMcaQt as qt
import epics # pyepics
#import time

app = qt.QApplication([])
wind = PyMcaMain(debug=True)
wind.sourceWidget.sourceSelector.openSource('/epics/support/pymca/data/exp798/Datafiles/HB3_exp0798_scan0090.dat')
#ddict =
#ddict["selection"] = {'cols': {'y': [1], 'x': [0]}} # line 1198 in PyMcaMain.py 
#wind.dispatcherAddSelectionSlot(ddict) # line 517 in PyMcaMain.py
#wind.dispatcherReplaceSelectionSlot(ddict) # line 687 in PyMcaMain.pyi
print(wind.getConfig())
wind.show()
#time.sleep(7.5)
app.exec()

