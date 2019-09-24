import qgis.core
import PyQt5

qgis_v = qgis.core.Qgis.QGIS_VERSION
print('hello {}'.format(qgis_v))

qt_v = PyQt5.QtCore.QT_VERSION_STR
print(qt_v)