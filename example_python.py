import qgis.core
import PyQt5

qgis_version = qgis.core.Qgis.QGIS_VERSION
print('QGIS {} is available'.format(qgis_version))

qt_version = PyQt5.QtCore.QT_VERSION_STR
print('PyQt5 {} is available'.format(qt_version))
