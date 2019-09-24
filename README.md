# VS Code OsGeo4W Template with QGIS LTR

**Work in progress not tested seriously.**

## Requirements

- [OSGeo4W Network Installer (64 bit)](https://www.qgis.org/en/site/forusers/download.html)
  - QGIS LTR

## Important Files

- [open_vscode.cmd](open_vscode.cmd) : Opens VS Code in current directory with OsGeo4W and QGIS-LTR environment settings.
- [.vscode](/.vscode/) : Important VS Code and Debugger settings.
- [.pylintrc](.pylintrc#L31) : Settings for pylint (extension-pkg-whitelist=PyQt5,qgis)
- [hello.py](hello.py) : Shows import from qgis and PyQt5
