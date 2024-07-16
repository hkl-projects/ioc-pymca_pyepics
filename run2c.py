from PyMca5.PyMcaGui.pymca.PyMcaMain import PyMcaMain
from PyMca5.PyMcaGui.pymca.ScanWindowInfoWidget import GraphInfoWidget
from PyMca5.PyMcaGui import PyMcaQt as qt
from PyMca5 import PyMcaDataDir
import os
#import time
#import epics # pyepics

app = qt.QApplication([])
wind = PyMcaMain()

fname = os.path.join(PyMcaDataDir.PYMCA_DATA_DIR, "/epics/support/pymca/data/exp798/Datafiles/HB3_exp0798_scan0090.dat") 
wind.sourceWidget.sourceSelector.openSource(fname)
info = wind.scanWindow.scanWindowInfoWidget
print(info.getInfo())
app.exec()

