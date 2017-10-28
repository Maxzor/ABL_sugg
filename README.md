# ABL_sugg
Demonstration app with sqlite and pyqt, for an ERP extension about botanics. (french in there!) 

Tab2 let you browse, from top to bottom, a mapping between the official Open Tree of Life taxonomy and the current ERP botanic articles.

Tab3 consists of suggestions for botanic-data-model improvements of the ERP (atomicization, meta-caracterization).

_External dependencies_: Sqlite3, Python3 and PyQT5 + CxFreeze for Windows packaging.

_Installation (Linux)_ :
- Create the db from dump with "cat sqlite3_dump.sql | sqlite3 as.db"
- Launch the demo "sudo python3 main.py"

Upon modification of the .ui with Qtcreator, translate and override .py with "sudo pyuic5 mainwindow.ui -o mainwindow.py"

_Windows packaging_ : run cxfreeze python script and export build directory to windows. Run main.exe there.
