# OSGeo4W Python Project-Template with QGIS LTR, uv and VS Code

Template for the creation of virtual environments for the use of [OSGeo4W](https://www.qgis.org/download/) and QGIS-LTR Python functionalities with [uv](https://docs.astral.sh/uv/).

## How to use it

Create the virtual environment with uv for simple management of additional dependencies. After executing the following commands reopen the terminal or restart VS Code. If the setup is successful [example_python.py](example_python.py) will execute without error messages.

```cmd
SET OSGEO_ROOT=C:\OSGeo4W
SET OSGEO_PYTHON=%OSGEO_ROOT%\apps\Python312\python.exe

rem To enable system site packages the venv has to be created explicitly
uv venv --system-site-packages --python %OSGEO_PYTHON%

rem Adds the QGIS LTR directories to the virtual environment
echo %OSGEO_ROOT%\apps\qgis-ltr\python > .venv\qgis-ltr.pth
echo %OSGEO_ROOT%\apps\qgis-ltr\python\plugins >> .venv\qgis-ltr.pth

rem use the dependencies from the existing pyproject.toml
rem Project Metadata in pyproject.toml has to be changed manually
uv sync --dev
rem OR create a new project and pyproject.toml whitout predefined dependencies
uv init
```

For the usage of the functionalities from the `OSGeo4W Shell` check in [.vscode\settings.json](.vscode\settings.json) the path settings and modify it if `OSGeo4W` in the default location.


...this template is work in progress and not tested seriously.

### Important Files

- [.vscode](/.vscode/) : Important VS Code and Debugger settings.
- [example_python.py](example_python.py) : Shows usage of qgis.core and PyQt5
- [example_gdal.cmd](example_gdal.cmd) : Shows usage of gdal

## Recommended Installations

- OSGeo4W Network Installer (64 bit) [ [Download](https://www.qgis.org/en/site/forusers/download.html) ]
  - QGIS LTR
- Visual Studio Code [ [Download](https://code.visualstudio.com/Download) | [Documentation](https://code.visualstudio.com/docs) ]
- QGIS Plugins for plugin-creation and debugging
  - Plugin Builder 3 [ [GitHub](http://g-sherman.github.io/Qgis-Plugin-Builder/) | [QGIS](https://plugins.qgis.org/plugins/pluginbuilder3/) ]
  - debugvs-Plugin [ [GitHub](https://github.com/lmotta/debug_vs_plugin/wiki) | [QGIS](https://plugins.qgis.org/plugins/debug_vs) ]
  - Python debugger package for use Visual Studio Code [ [GitHub](https://github.com/microsoft/ptvsd) ]  
  --> `python3 -m pip install --upgrade ptvsd` inside VS Code terminal
  - Plugin Reloader [ [GitHub](https://github.com/borysiasty/plugin_reloader) | [QGIS](https://plugins.qgis.org/plugins/plugin_reloader) ] (flagged as experimental)
- pb_tools `python3 -m pip install --upgrade pb_tool`


## Common Developing Tasks for Plugins

### Useful Tools / Informations

- [pb_tool (Plugin Builder Tool)](http://g-sherman.github.io/plugin_build_tool/)
- [Quick Guide to Getting Started with PyQGIS 3 on Windows](http://spatialgalaxy.net/2018/02/13/quick-guide-to-getting-started-with-pyqgis-3-on-windows/)

### Create Plugin

- Create Plugin with **Plugin Builder 3** inside this directory.
- Edit the new created `pb_tool.cfg` and define the plugin_path for the deploy (real path without %appdata%): `%appdata%\QGIS\QGIS3\profiles\default\python\plugins`. It be a good idea to work in a clean qgis-profile.
- run `pb_tool compile` or `pyrcc5 -o resources.py resources.qrc`

### Debugging

1. Define the remoteRoot path-mappings in the debugger-settings `.vscode\settings.json`
2. Install and enable debugvs-Plugin and ptvsd
3. Enable Debug for Visual Studio in QGIS (Button in QGIS)
4. Start Debugger `Python: Remote Attach` inside VS Code
5. Run Plugin-functions from inside QGIS and use breakpoints inside VS Code.

### Make and reload Changes

1. Make changes inside Plugin
2. run `pb_tool deploy --no-confirm` and the plugin gets deployed to the qgis plugin-folder
3. reload it with the Plugin Reloader.
4. If the order or layout of the toolbars inside QGIS gets messed up, reload it again.
5. Test the changes.

### Known difficulties

pb_tool compile or pyrcc5 throws a pyt4 error -> load environments

``` cmd
rem load necessary envs
o4w_env
py3_env
qt5_env
```

If debugger throws an error like `Error while enumerating installed packages` update `importlib-metadata` with the following command in the osgeo4w shell:

```cmd
python -m pip install --upgrade importlib-metadata
```
