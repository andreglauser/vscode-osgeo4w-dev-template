


def main():
    try:
        import qgis.core
        qgis_version = qgis.core.Qgis.QGIS_VERSION
        print("QGIS {} is available".format(qgis_version))
    except ImportError:
        print("Import of QGIS failed")

    try:
        import PyQt5
        qt_version = PyQt5.QtCore.QT_VERSION_STR
        print("PyQt5 {} is available".format(qt_version))
    except ImportError:
        print("Import of PyQt5 failed")

    try:
        from osgeo import gdal

        gdal_version = gdal.__version__
        print("GDAL {} is available".format(gdal_version))
    except ImportError:
        print("Import of GDAL from OSGEO failed")

    try:
        from osgeo import ogr

        print("OGR is available")
    except ImportError:
        print("Import of OGR from OSGEO failed")


if __name__ == "__main__":
    main()
