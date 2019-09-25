# VS Code OsGeo4W Template with QGIS LTR

**How to start? Click [open_vscode.cmd](open_vscode.cmd)**

...this template is work in progress and not tested seriously.

## Requirements / Installation

- OSGeo4W Network Installer (64 bit) [ [Download](https://www.qgis.org/en/site/forusers/download.html) ]
  - QGIS LTR
- Visual Studio Code [ [Download](https://code.visualstudio.com/Download) | [Documentation](https://code.visualstudio.com/docs) ]
- QGIS Plugins for plugin-creation and debugging
  - Plugin Builder 3 [ [GitHub](http://g-sherman.github.io/Qgis-Plugin-Builder/) | [QGIS](https://plugins.qgis.org/plugins/pluginbuilder3/) ]
  - debugvs-Plugin [ [GitHub](https://github.com/lmotta/debug_vs_plugin/wiki) | [QGIS](https://plugins.qgis.org/plugins/debug_vs) ]
  - Python debugger package for use Visual Studio Code [ [GitHub](https://github.com/microsoft/ptvsd) ]  
  --> ```pip3 install ptvsd``` inside VS Code terminal
  - Plugin Reloader [ [GitHub](https://github.com/borysiasty/plugin_reloader) | [QGIS](https://plugins.qgis.org/plugins/plugin_reloader) ] (flagged as experimental)

## Important Files

- [open_vscode.cmd](open_vscode.cmd) : Opens VS Code in current directory with OsGeo4W and QGIS-LTR environment settings.
- [.vscode](/.vscode/) : Important VS Code and Debugger settings.
- [.pylintrc](.pylintrc#L28-L31) : Settings for pylint (extension-pkg-whitelist=PyQt5,qgis)
- [hello.py](hello.py) : Shows import from qgis and PyQt5

---------------------------------------------------------------------------------------

## Common Developing Tasks for Plugins

### Create Plugin

Create Plugin with **Plugin Builder 3** inside ```%appdata%\QGIS\QGIS3\profiles\default\python\plugins```

### Debugging

1. Install and enable debugvs-Plugin and ptvsd
2. Enable Debug for Visual Studio in QGIS (Button in QGIS)
3. Start Debugger ```Python: Remote Attach``` inside VS Code
4. Run Plugin-functions from inside QGIS and use breakpoints inside VS Code.

### Make and reload Changes

1. Make changes inside Plugin and reload it with the Plugin Reloader.
2. If the order of the toolbars inside QGIS gets messed up, reload it again.
3. Test the changes.
