from PyQt5 import QtWidgets, QtCore, QtGui


class AutoRightBottom1(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(AutoRightBottom1, self).__init__(parent)

        self.layout = QtWidgets.QVBoxLayout(self)
        self.label = QtWidgets.QLabel(self)
        self.layout.addWidget(self.label)
        self.setLayout(self.layout)
        self.label.setText("Auto")