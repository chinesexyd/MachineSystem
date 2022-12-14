from PyQt5 import QtWidgets, QtCore, QtGui


class JogRightBottom(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(JogRightBottom, self).__init__(parent)

        self.layout = QtWidgets.QVBoxLayout(self)
        self.label = QtWidgets.QLabel(self)
        self.layout.addWidget(self.label)
        self.setLayout(self.layout)
        self.label.setText("Jog")