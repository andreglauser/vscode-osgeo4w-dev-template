@echo off
SET OSGEO4W_ROOT=C:\OSGeo4W
SET PYTHON_VERSION=Python39

call "%OSGEO4W_ROOT%"\bin\o4w_env.bat

path %PATH%;%OSGEO4W_ROOT%\apps\qgis-ltr\bin
path %PATH%;%OSGEO4W_ROOT%\apps\Qt5\bin
path %PATH%;%OSGEO4W_ROOT%\apps\%PYTHON_VERSION%\Scripts

set PYTHONPATH=%PYTHONPATH%;%OSGEO4W_ROOT%\apps\qgis-ltr\python\
set PYTHONPATH=%PYTHONPATH%;%OSGEO4W_ROOT%\apps\qgis-ltr\python\qgis
set PYTHONPATH=%PYTHONPATH%;%OSGEO4W_ROOT%\apps\qgis-ltr\python\qgis\PyQt5
set PYTHONPATH=%PYTHONPATH%;%OSGEO4W_ROOT%\apps\qgis-ltr\python\qgis\core

set PYTHONHOME=%OSGEO4W_ROOT%\apps\%PYTHON_VERSION%

start "VS Code with PyQGIS and OsGeo4W" /B "%LOCALAPPDATA%\Programs\Microsoft VS Code\Code.exe" .