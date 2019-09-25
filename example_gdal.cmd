@echo off
rem load osgeo4w environments (not neccesary if executed inside vscode)
SET OSGEO4W_ROOT="C:/OSGeo4W64"
call %OSGEO4W_ROOT%/bin/o4w_env.bat

rem your code comes here, examples with gdal...
ogrinfo --version
ogr2ogr --version
gdal_translate --version