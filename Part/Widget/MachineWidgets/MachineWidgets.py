from PyQt5 import QtWidgets, QtCore, QtGui
from Tool.Methods.ConfigController import con, wRatio, hRatio
from Part.Widget.MachineWidgets.AutoLeftTop1 import AutoLeftTop1
from Part.Widget.MachineWidgets.AutoRIghtTop1 import AutoRightTop1
from Part.Widget.MachineWidgets.AutoLeftBottom1 import AutoLeftBottom1
from Part.Widget.MachineWidgets.AutoRightBottom1 import AutoRightBottom1
from Part.Widget.MachineWidgets.JogLeftBottom1 import JogLeftBottom
from Part.Widget.MachineWidgets.JogRightBottom1 import JogRightBottom


class MachineWidgets(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(MachineWidgets, self).__init__(parent)
        self.setObjectName("MachineWidgets")

        self.layout = QtWidgets.QGridLayout(self)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setSpacing(0)

        self.leftTopArea = LeftTopArea(self)
        self.rightTopArea = RightBottomArea(self)
        self.leftBottomArea = LeftBottomArea(self)
        self.rightBottomArea = RightBottomArea(self)

        self.layout.addWidget(self.leftTopArea, 0, 0, 1, 1)
        self.layout.addWidget(self.rightTopArea, 0, 1, 1, 1)
        self.layout.addWidget(self.leftBottomArea, 1, 0, 1, 1)
        self.layout.addWidget(self.rightBottomArea, 1, 1, 1, 1)

        self.layout.setColumnStretch(0, int(con.get("left-top-area", "width")))
        self.layout.setColumnStretch(1, int(con.get("right-bottom-area", "width")))

        self.layout.setRowStretch(0, int(con.get("left-top-area", "height")))
        self.layout.setRowStretch(1, int(con.get("left-bottom-area", "height")))

        self.setLayout(self.layout)


class LeftTopArea(QtWidgets.QWidget):
    """左上角"""

    def __init__(self, parent=None):
        super(LeftTopArea, self).__init__(parent)

        self.width = int(con.get("left-top-area", "width")) * wRatio
        self.height = int(con.get("left-top-area", "height")) * hRatio

        self.layout = QtWidgets.QStackedLayout(self)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setSpacing(0)


class RightTopArea(QtWidgets.QWidget):
    """右上角"""

    def __init__(self, parent=None):
        super(RightTopArea, self).__init__(parent)

        self.width = int(con.get("right-top-area", "width")) * wRatio
        self.height = int(con.get("right-top-area", "height")) * hRatio

        self.layout = QtWidgets.QStackedLayout(self)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setSpacing(0)


class LeftBottomArea(QtWidgets.QWidget):
    """左下角"""

    def __init__(self, parent=None):
        super(LeftBottomArea, self).__init__(parent)

        self.width = int(con.get("left-bottom-area", "width")) * wRatio
        self.height = int(con.get("left-bottom-area", "height")) * hRatio

        self.layout = QtWidgets.QStackedLayout(self)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setSpacing(0)


class RightBottomArea(QtWidgets.QWidget):
    """右下角"""

    def __init__(self, parent=None):
        super(RightBottomArea, self).__init__(parent)

        self.width = int(con.get("right-bottom-area", "width")) * wRatio
        self.height = int(con.get("right-bottom-area", "height")) * hRatio

        self.layout = QtWidgets.QStackedLayout(self)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setSpacing(0)
