"Checks if modules are available"
import logging


def main():
    logging.basicConfig(level=logging.INFO)

    try:
        import qgis.core

        qgis_version = qgis.core.Qgis.QGIS_VERSION
        logging.info("QGIS {} is available".format(qgis_version))
    except ImportError:
        logging.error("Import of QGIS failed")

    try:
        import PyQt5

        qt_version = PyQt5.QtCore.QT_VERSION_STR
        logging.info("PyQt5 {} is available".format(qt_version))
    except (ImportError, AttributeError):
        logging.errore("Import of PyQt5 failed")

    try:
        from osgeo import gdal

        gdal_version = gdal.__version__
        logging.info("GDAL {} is available".format(gdal_version))
    except ImportError:
        logging.error("Import of GDAL from OSGEO failed")

    try:
        from osgeo import ogr

        logging.info("OGR is available with {} Drivers".format(ogr.GetDriverCount()))
    except ImportError:
        logging.error("Import of OGR from OSGEO failed")


if __name__ == "__main__":
    main()
