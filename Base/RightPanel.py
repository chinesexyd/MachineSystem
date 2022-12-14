from PyQt5 import QtWidgets, QtCore
from Tool.Methods.ConfigController import con,wRatio,hRatio


class RightPanel(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(RightPanel, self).__init__(parent)

        width = int(con.get("right-area", "width"))*wRatio
        height = int(con.get("right-area", "height"))*hRatio
        buttonNum = int(con.get("right-area", "button-number"))
        buttonHeight = int(con.get("right-area", "button-height"))*hRatio

        self.layout = RightLayout(self, width, height, buttonNum, buttonHeight)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setSpacing(0)
        self.setLayout(self.layout)

        self.buttonGroup = QtWidgets.QButtonGroup(self)

    def getButtonByName(self, name: str) -> QtWidgets.QPushButton:
        button = self.findChild(QtWidgets.QPushButton, name)
        return button

    def getButtonByIndex(self, index: int) -> QtWidgets.QPushButton:
        if 0 <= index < len(self.layout.itemDict):
            button = self.layout.itemDict[index].widget()
            return button


class RightLayout(QtWidgets.QLayout):
    def __init__(self, parent=None, width=100, height=668, buttonNo=11, buttonHeight=100):
        super(RightLayout, self).__init__(parent)

        self.parent = parent
        self.width = width
        self.height = height
        self.buttonNo = buttonNo
        self.buttonHeight = buttonHeight

        self.itemDict = dict()
        for i in range(self.buttonNo):
            button = QtWidgets.QPushButton(self.parent)
            button.index = i
            button.setEnabled(False)
            self.itemDict[i] = QtWidgets.QWidgetItem(button)

    def addItem(self, item: QtWidgets.QWidgetItem) -> None:
        button = self.itemDict[item.widget().index].widget()
        self.itemDict[item.widget().index] = item
        button.deleteLater()

    def removeWidget(self, w: QtWidgets.QWidget) -> None:
        if w.index in self.itemDict:
            if self.itemDict[w.index] == w:
                self.itemDict.pop(w.index)

    def setGeometry(self, rect: QtCore.QRect = None) -> None:
        height = self.height
        buttonHeight = self.buttonHeight
        buttonWidth = self.width
        buttonSpace = height / self.buttonNo - buttonHeight

        for item in self.itemDict.values():
            button = item.widget()
            index = button.index
            y = index * (buttonHeight + buttonSpace)
            button.setGeometry(0, y, buttonWidth, buttonHeight)

        self.setProperty("sHint", QtCore.QSize(buttonWidth, height))

    def sizeHint(self):
        if self.property("sHint") is None:
            return QtCore.QSize(0, 0)
        self.setGeometry()
        return self.property("sHint")

    def count(self):
        return len(self.itemDict)

    def itemAt(self, p_int):
        if len(self.itemDict) == 0 or p_int < 0 or p_int >= len(self.itemDict):
            return None
        return self.itemDict[p_int]

    def minimumSize(self):
        return self.sizeHint()



