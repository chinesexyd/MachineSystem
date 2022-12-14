from PyQt5 import QtWidgets, QtGui, QtCore


class BaseButton(QtWidgets.QPushButton):
    BOTTOM_AREA = "A_"
    RIGHT_AREA = "B_"
    CENTRAL_AREA = "C_"
    FUNCTION_AREA = "D_"
    CONTROL_AREA = "E_"
    PATTERN_AREA = "F_"
    RUN_AREA = "G_"

    def __init__(self, parent=None, fakeButton=None):
        super(BaseButton, self).__init__(parent)
        self.area = fakeButton.area
        self.fakeButton = fakeButton
        self.index = None
        self.hasPage = False
        self.bottomPageNum = 0
        self.hasBottomPage = False
        self.rightPageNum = 0
        self.hasRightPage = False
        self.hasDialog = False
        self.buttonGroup = False
        self.clicked.connect(self.clickSlot)

    def clickSlot(self, checked):
        mainWindow = self.parent().parent().parent()
        if self.hasBottomPage:
            bottomIndicatorArea = mainWindow.bottomIndicatorArea
            bottomIndicatorArea.setButtonNum(self.bottomPageNum)
        if self.hasRightPage:
            rightIndicatorArea = mainWindow.rightIndicatorArea
            rightIndicatorArea.setButtonNum(self.rightPageNum)
        self.showButtonAreaOnAppTop()

        self.fakeButton.clickSlot(checked)

    def setIndex(self, index: int):
        self.index = index

    def setBottomPageNum(self, num: int):
        if num > 0:
            self.hasPage = True
            self.bottomPageNum = num
            self.hasBottomPage = True

    def setRightPageNum(self, num: int):
        if num > 0:
            self.hasPage = True
            self.rightPageNum = num
            self.hasRightPage = True

    def setButtonGroup(self, bo: bool):
        self.buttonGroup = bo

    def setHasDialog(self, bo: bool):
        self.hasDialog = bo

    def showButtonAreaOnAppTop(self):
        if self.area in [self.BOTTOM_AREA, self.RIGHT_AREA]:
            buttonPathList = self.fakeButton.basePanel.split("/")
            function = buttonPathList[0][:-2]
            other = "\\".join([i[:-2] for i in buttonPathList[1:]])
            if other:
                other += "\\" + self.objectName()
            else:
                other = self.objectName()
            print(function, other)
        elif self.area == self.FUNCTION_AREA:
            print(self.objectName())

    def paintEvent(self, event: QtGui.QPaintEvent):
        super().paintEvent(event)
        if self.area == self.RIGHT_AREA or self.area == self.BOTTOM_AREA or self.area == self.RUN_AREA:
            self.drawShortCutIcon()
        if self.area == self.PATTERN_AREA:
            self.drawlight()
        # if self.objectName() in ["RETURN", "NEXT", "UP"]:
        #     self.drawDirectionIcon()

    def drawShortCutIcon(self) -> None:
        painter = QtGui.QPainter(self)
        painter.begin(self)
        painter.setRenderHints(QtGui.QPainter.Antialiasing | QtGui.QPainter.TextAntialiasing)
        if self.area == self.RIGHT_AREA:
            text = "CF" + str(self.index + 1)
            painter.setPen(QtGui.QPen(QtCore.Qt.blue))
        elif self.area == self.BOTTOM_AREA:
            text = "F" + str(self.index)
            painter.setPen(QtGui.QPen(QtCore.Qt.darkGray))
        else:
            if self.objectName() in ["Start", "Stop"]:
                text = "F" + str(self.index + 10)
            else:
                text = "Pause"
            painter.setPen(QtGui.QPen(QtCore.Qt.red))

        rect = QtCore.QRect(5, 5, self.width(), self.height())
        align = QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(8)
        painter.setFont(font)
        painter.drawText(rect, align, text)
        painter.end()

    def drawPageDownIcon(self) -> None:
        painter = QtGui.QPainter(self)
        painter.begin(self)
        painter.setRenderHints(QtGui.QPainter.Antialiasing | QtGui.QPainter.TextAntialiasing)
        width = self.width()
        height = self.height()
        x1 = width - height / 2 - height / 4
        y1 = height / 6
        x2 = width - height / 2
        y2 = height / 6 * 5
        p1 = QtCore.QPoint(width - height / 3, height / 3)
        p2 = QtCore.QPoint(width - height / 3, height / 3 * 2)
        p3 = QtCore.QPoint(width - height / 6, height / 2)
        brush = QtGui.QBrush(QtCore.Qt.darkBlue)
        painter.setBrush(brush)
        painter.setPen(QtGui.QPen(0))
        painter.drawRect(QtCore.QRect(QtCore.QPoint(x1, y1), QtCore.QPoint(x2, y2)))
        painter.drawPolygon(QtGui.QPolygon([p1, p2, p3]))
        painter.end()

    def drawlight(self) -> None:
        painter = QtGui.QPainter(self)
        painter.begin(self)
        painter.setRenderHints(QtGui.QPainter.Antialiasing | QtGui.QPainter.TextAntialiasing)
        width = self.width()
        rect = QtCore.QRect(5, 0, width - 10, 5)
        if self.isChecked():
            brush = QtGui.QBrush(QtCore.Qt.green)
        else:
            brush = QtGui.QBrush(QtCore.Qt.lightGray)
        painter.setBrush(brush)
        painter.drawRoundedRect(rect, 2.5, 2.5)
        painter.end()
