# This is an attempt at puting GUI in a separate main thread. 
# This does not yet work. The GUI blocks.
# 

from PyMca5.PyMcaGui.pymca.PyMcaMain import PyMcaMain
from PyMca5.PyMcaGui.pymca.ScanWindowInfoWidget import GraphInfoWidget
from PyMca5.PyMcaGui import PyMcaQt as qt
from PyMca5 import PyMcaDataDir
import os
#import time
#import epics # pyepics
import threading

def main():
    app = qt.QApplication([])
    wind = PyMcaMain()

    fname = os.path.join(PyMcaDataDir.PYMCA_DATA_DIR, "/epics/support/pymca/data/exp798/Datafiles/HB3_exp0798_scan0090.dat") 
    wind.sourceWidget.sourceSelector.openSource(fname)
    info = wind.scanWindow.scanWindowInfoWidget
    print(info.getInfo())
    app.exec()  #<---------- code blocks over here !

#app = qt.QApplication([])
#wind = PyMcaMain()
#
#fname = os.path.join(PyMcaDataDir.PYMCA_DATA_DIR, "/epics/support/pymca/data/exp798/Datafiles/HB3_exp0798_scan0090.dat") 
#wind.sourceWidget.sourceSelector.openSource(fname)
#info = wind.scanWindow.scanWindowInfoWidget
#print(info.getInfo())
#app.exec()


#After running the GUI, continue the rest of the application task
t = threading.Thread(target=main)
t.daemon = True
t.start()

print(info.getInfo())


