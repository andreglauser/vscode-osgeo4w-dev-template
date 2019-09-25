# VS Code OsGeo4W Template with QGIS LTR

**How to start? Click [open_vscode.cmd](open_vscode.cmd)**

...this template is work in progress and not tested seriously.

## Requirements

- [OSGeo4W Network Installer (64 bit)](https://www.qgis.org/en/site/forusers/download.html)
  - QGIS LTR

## Important Files

- [open_vscode.cmd](open_vscode.cmd) : Opens VS Code in current directory with OsGeo4W and QGIS-LTR environment settings.
- [.vscode](/.vscode/) : Important VS Code and Debugger settings.
- [.pylintrc](.pylintrc#L28-L31) : Settings for pylint (extension-pkg-whitelist=PyQt5,qgis)
- [hello.py](hello.py) : Shows import from qgis and PyQt5

---------------------------------------------------------------------------------------

## Common Developing Tasks for Plugins

### Create Plugin

Create Plugin with **Plugin Builder 3** [ [GitHub]() | [QGIS](https://plugins.qgis.org/plugins/pluginbuilder3/) ] inside ```%appdata%\QGIS\QGIS3\profiles\default\python\plugins```

### Debugging

1. Install debugvs-Plugin [ [GitHub](https://github.com/lmotta/debug_vs_plugin/wiki) | [QGIS](https://plugins.qgis.org/plugins/debug_vs) ]  in QGIS
2. Install the Python debugger package for use Visual Studio Code with ```pip3 install ptvsd``` (Works with Terminal inside VS Code)
3. Enable Debug for Visual Studio in QGIS
4. Start Debugger ```Python: Remote Attach```
5. Run Plugin-functions from inside QGIS

### Make and reload Changes

1. Search & Install QGIS-Plugin **Plugin Reloader** [[GitHub](https://github.com/borysiasty/plugin_reloader) | [QGIS](https://plugins.qgis.org/plugins/plugin_reloader) ] (flagged as experimental)
2. Make changes inside Plugin and reload it.
3. If the order of the toolbars inside QGIS gets messed up, reload it again.
