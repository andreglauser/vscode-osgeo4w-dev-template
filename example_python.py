"Checks if modules are available"

import logging

logger = logging.getLogger(__name__)


def main() -> None:
    logging.basicConfig(
        level=logging.INFO,
        format="%(levelname)s - %(message)s",
    )

    try:
        import qgis.core

        qgis_version = qgis.core.Qgis.QGIS_VERSION
        logger.info(f"QGIS {qgis_version} is available")
    except ImportError:
        logger.error("Import of QGIS failed")

    try:
        import PyQt5

        qt_version = PyQt5.QtCore.QT_VERSION_STR
        logger.info(f"PyQt5 {qt_version} is available")
    except (ImportError, AttributeError):
        logger.error("Import of PyQt5 failed")

    try:
        from osgeo import gdal

        gdal_version = gdal.__version__
        logger.info(f"GDAL {gdal_version} is available")
    except ImportError:
        logger.error("Import of GDAL from OSGEO failed")

    try:
        from osgeo import ogr

        logger.info(f"OGR is available with {ogr.GetDriverCount()} Drivers")
    except ImportError:
        logger.error("Import of OGR from OSGEO failed")


if __name__ == "__main__":
    main()
