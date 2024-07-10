from PyMca5.PyMcaGui.pymca.PyMcaMain import PyMcaMain
from PyMca5.PyMcaGui import PyMcaQt as qt
import pyepics

app = qt.QApplication([])
wind = PyMcaMain()
wind.sourceWidget.sourceSelector.openSource('/epics/support/pymca/data/exp798/Datafiles/HB3_exp0798_scan0090.dat')

