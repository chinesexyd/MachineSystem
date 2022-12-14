from PyQt5 import QtWidgets, QtCore
from Tool.Methods.ConfigController import con, wRatio, hRatio


class BottomPanel(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super(BottomPanel, self).__init__(parent)

        width = int(con.get("bottom-area", "width")) * wRatio
        height = int(con.get("bottom-area", "height")) * hRatio
        buttonNo = int(con.get("bottom-area", "button-number"))
        buttonWidth = int(con.get("bottom-area", "button-width")) * wRatio

        self.layout = BottomLayout(self, width, height, buttonNo, buttonWidth)
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


class BottomLayout(QtWidgets.QLayout):
    def __init__(self, parent=None, width=1024, height=50, buttonNo=11, buttonWidth=100):
        super(BottomLayout, self).__init__(parent)

        self.parent = parent
        self.width = width
        self.height = height
        self.buttonNo = buttonNo
        self.buttonWidth = buttonWidth

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
        width = self.width
        buttonHeight = self.height
        buttonWidth = self.buttonWidth
        buttonNum = self.buttonNo
        buttonSpace = width / (self.buttonNo - 1) - buttonWidth

        for item in self.itemDict.values():
            button = item.widget()
            if button.index == 0:
                x = 0
                button.setGeometry(x, 0, buttonWidth / 2, buttonHeight)
            elif button.index == buttonNum - 1:
                x = width - buttonWidth / 2
                button.setGeometry(x, 0, buttonWidth / 2, buttonHeight)
            else:
                index = button.index
                x = (index - 0.5) * buttonWidth + (index + 1) * buttonSpace - 2
                button.setGeometry(x, 0, buttonWidth, buttonHeight)
                x += buttonWidth + buttonSpace

        self.setProperty("sHint", QtCore.QSize(width, buttonHeight))

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
