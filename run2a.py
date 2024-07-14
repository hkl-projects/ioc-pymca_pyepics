from PyMca5.PyMcaGui.pymca.PyMcaMain import PyMcaMain
from PyMca5.PyMcaGui.pymca.ScanWindowInfoWidget import GraphInfoWidget
from PyMca5.PyMcaGui import PyMcaQt as qt
import epics # pyepics
 
app = qt.QApplication([])
wind = PyMcaMain()

wind.sourceWidget.sourceSelector.openSource('/epics/support/pymca/data/exp798/Datafiles/HB3_exp0798_scan0090.dat') # line 
info = GraphInfoWidget(wind)
print(info.getInfo())

# # OR
# from PyMca5.PyMcaGui.pymca import ScanWindowInfoWidget
# scan = ScanWindowInfoWidget.ScanWindowInfoWidget()
# print(scan.getInfo())
#  
#  
# both show the fields that we want (fwhm, etc), but with empty values, like so:
# #{'scan': {'source': '', 'scan': '', 'hkl': ['', '', '']}, 'graph': {'peak': '', 'peakat': '', 'fwhm': '', 'fwhmat': '', 'com': '', 'mean': '', 'std': '', 'min': '', 'max': '', 'delta': ''}}
