from PyQt5 import QtWidgets, QtCore, QtGui


def ReadQss(qssPath: str) -> str:
    with open(qssPath, "r", encoding="utf-8") as f:
        qssStyle = f.read()
        return qssStyle


