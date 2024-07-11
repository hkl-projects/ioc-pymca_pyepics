# Integration of PyMca into EPICS using pyepics
* https://github.com/vasole/pymca
* https://epics.anl.gov/
* https://pyepics.github.io/pyepics/

## PyMca within conda 
* install conda environment
	* conda env create -f environment.yml

* activate conda environment 
	* conda activate pymca

* if you have modified pymca, from within the conda environment, run 
	* cd pymca
	* pip install .

### conda
* conda env create -f environment.yml
* conda activate pymca
* conda deactivate
* conda env remove -n pymca

## PyMca and pyepics
* https://pyepics.github.io/pyepics/installation.html#getting-started-setting-up-the-epics-environment
* pip install pyepics
* export PYEPICS_LIBCA=/epics/base/lib/linux-x86_64/libca.so
* run python and paste the following lines to open pymca with a specific datafile
	* python
		* test libca.so connection
			* \>>> epics.ca.find_libca()  {-> '/epics/base/lib/linux-x86_64/libca.so'}
	* \>>> from PyMca5.PyMcaGui.pymca.PyMcaMain import PyMcaMain
	* \>>> from PyMca5.PyMcaGui import PyMcaQt as qt
	* \>>> import epics
	* \>>> datafile_path = '/epics/support/pymca/data/exp798/Datafiles/HB3_exp0798_scan0090.dat'
	* \>>> app = qt.QApplication([])
	* \>>> wind = PyMcaMain()
	* \>>> wind.sourceWidget.sourceSelector.openSource(datafile_path)


* provided script: run.py
	* specify the path to your datafile as indicated
	* https://www.pythonguis.com/tutorials/creating-your-first-pyqt-window/
		* wind.show()
		* app.exec()

* note: cannot run this from the top directory of pymca, the imports will not work
