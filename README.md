Integration of PyMCA (https://github.com/vasole/pymca) and EPICS (https://epics.anl.gov/)

# To run
activate conda environment 
```bash
conda activate pymca
```

if you have modified pymca, from within the conda environment, run 
```bash
pip install .
```
in the top directory of pymca


run python and paste the following lines to open pymca with a specific datafile
```python
from PyMca5.PyMcaGui.pymca.PyMcaMain import PyMcaMain
from PyMca5.PyMcaGui import PyMcaQt as qt
import pyepics

datafile_path = '<ENTER_PATH_HERE>'
app = qt.QApplication([])
wind = PyMcaMain()
wind.sourceWidget.sourceSelector.openSource(datafile_path)
```

a similar script has been provided as run.py

you will need to specify the path to your datafile as indicated

note: you cannot run this from the top directory of pymca, the imports will not work
