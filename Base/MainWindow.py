from PyQt5 import QtWidgets, QtCore, QtGui
from Tool.Methods.ConfigController import con, wRatio, hRatio
import math


class MainWindow(QtWidgets.QWidget):
    """主窗口"""

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.buttonMsg = ""
        self.setObjectName("MainWindow")
        self.setProperty("pattern", "AUTO")  # 默认模式

        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        # self.setAttribute(QtCore.Qt.WA_TranslucentBackground)  # 透明

        self.width = int(con.get("main", "width"))
        self.height = int(con.get("main", "height"))
        self.setFixedSize(self.width, self.height)

        self.layout = QtWidgets.QGridLayout(self)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setSpacing(0)

        self.topArea = TopArea(self)
        self.leftArea = LeftArea(self)
        self.bottomArea = BottomArea(self)
        self.centralArea = CentralArea(self)
        self.statusBar = StatusBar(self)
        self.bottomIndicatorArea = BottomIndicatorArea(self)
        self.rightIndicatorArea = RightIndicatorArea(self)
        self.rightArea = RightArea(self)

        self.layout.addWidget(self.topArea, 0, 0, 1, 3)
        self.layout.addWidget(self.leftArea, 1, 0, 4, 1)
        self.layout.addWidget(self.bottomArea, 5, 0, 1, 3)
        self.layout.addWidget(self.centralArea, 1, 1, 2, 1)
        self.layout.addWidget(self.statusBar, 3, 1, 1, 1)
        self.layout.addWidget(self.bottomIndicatorArea, 4, 1, 1, 1)
        self.layout.addWidget(self.rightIndicatorArea, 1, 2, 1, 1)
        self.layout.addWidget(self.rightArea, 2, 2, 3, 1)

        self.layout.setColumnStretch(0, int(con.get("left-area", "width")))
        self.layout.setColumnStretch(1, int(con.get("central-area", "width")))
        self.layout.setColumnStretch(2, int(con.get("right-area", "width")))

        self.layout.setRowStretch(0, int(con.get("top-area", "height")))
        self.layout.setRowStretch(1, int(con.get("right-indicator-area", "height")))
        self.layout.setRowStretch(2, int(con.get("central-area", "height")) - int(
            con.get("right-indicator-area", "height")))
        self.layout.setRowStretch(3, int(con.get("status-bar", "height")))
        self.layout.setRowStretch(4, int(con.get("bottom-indicator-area", "height")))
        self.layout.setRowStretch(5, int(con.get("bottom-area", "height")))

        self.setLayout(self.layout)

        MainWindow.mainWindow = self

    @staticmethod
    def getMainWindow():
        return MainWindow.mainWindow

    def mouseMoveEvent(self, e: QtGui.QMouseEvent):  # 重写移动事件
        self._endPos = e.pos() - self._startPos
        self.move(self.pos() + self._endPos)

    def mousePressEvent(self, e: QtGui.QMouseEvent):
        if e.button() == QtCore.Qt.LeftButton:
            self._isTracking = True
            self._startPos = QtCore.QPoint(e.x(), e.y())

    def mouseReleaseEvent(self, e: QtGui.QMouseEvent):
        if e.button() == QtCore.Qt.LeftButton:
            self._isTracking = False
            self._startPos = None
            self._endPos = None


# ----------静止-------------
class TopArea(QtWidgets.QWidget):
    """顶部显示当前模式 操作路径 时间 设置 关闭软件等信息"""

    def __init__(self, parent=None):
        super(TopArea, self).__init__(parent)
        self.setObjectName("TopArea")

        self.layout = QtWidgets.QGridLayout(self)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setSpacing(0)

        self.label1 = QtWidgets.QLabel(self)
        self.label1.setObjectName("TOP")
        self.label2 = QtWidgets.QLabel(self)
        self.label2.setObjectName("TOP")
        self.label3 = QtWidgets.QLabel(self)
        self.label3.setObjectName("TOP")
        self.label4 = QtWidgets.QLabel(self)
        self.label4.setObjectName("TOP")
        self.label5 = QtWidgets.QLabel(self)
        self.label5.setObjectName("TOP")
        self.label5.setAlignment(QtCore.Qt.AlignCenter)
        self.button6 = QtWidgets.QPushButton(self)
        self.button6.setObjectName("TOP")
        self.button6.setText("EXIT")
        self.label7 = QtWidgets.QLabel(self)
        self.label7.setObjectName("TOP")
        self.label8 = QtWidgets.QLabel(self)
        self.label8.setObjectName("TOP")
        self.label9 = QtWidgets.QLabel(self)
        self.label9.setObjectName("TOP")
        self.label10 = QtWidgets.QLabel(self)
        self.label10.setObjectName("TOP")

        self.layout.addWidget(self.label1, 0, 0, 1, 1)
        self.layout.addWidget(self.label2, 0, 1, 1, 1)
        self.layout.addWidget(self.label3, 0, 2, 1, 1)
        self.layout.addWidget(self.label4, 0, 3, 1, 1)
        self.layout.addWidget(self.label5, 0, 4, 1, 1)
        self.layout.addWidget(self.button6, 0, 5, 1, 1)
        self.layout.addWidget(self.label7, 1, 0, 1, 1)
        self.layout.addWidget(self.label8, 1, 1, 1, 1)
        self.layout.addWidget(self.label9, 1, 2, 1, 1)
        self.layout.addWidget(self.label10, 1, 3, 1, 3)

        self.layout.setColumnStretch(0, 100)
        self.layout.setColumnStretch(1, 100)
        self.layout.setColumnStretch(2, 100)
        self.layout.setColumnStretch(3, 524)
        self.layout.setColumnStretch(4, 100)
        self.layout.setColumnStretch(5, 100)

        self.setLayout(self.layout)

        self.timer = QtCore.QTimer(self)
        self.timer.start(1000)
        self.timer.timeout.connect(self.showDateTimeSlot)

        self.button6.clicked.connect(self.parent().close)

    def showDateTimeSlot(self):
        nowDateTimeStr = QtCore.QDateTime.currentDateTime().toString("MM/dd hh:mm")
        self.label5.setText(nowDateTimeStr)


class LeftArea(QtWidgets.QWidget):
    """左侧按钮栏，包含功能按钮区域、控制切换区域、模式区域、控制程序运行与否区域"""

    def __init__(self, parent=None):
        super(LeftArea, self).__init__(parent)
        self.setObjectName("LeftArea")

        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setSpacing(6)

        self.functionArea = FunctionArea(self)
        self.controlArea = ControlArea(self)
        self.patternArea = PatternArea(self)
        self.runArea = RunArea(self)

        self.layout.addWidget(self.functionArea)
        self.layout.addWidget(self.controlArea)
        self.layout.addWidget(self.patternArea)
        self.layout.addWidget(self.runArea)

        self.layout.setStretch(0, int(con.get("function-area", "height")))
        self.layout.setStretch(1, int(con.get("control-area", "height")))
        self.layout.setStretch(2, int(con.get("pattern-area", "height")))
        self.layout.setStretch(3, int(con.get("run-area", "height")))

        self.setLayout(self.layout)


class ColumnLayout(QtWidgets.QLayout):
    def __init__(self, parent: QtWidgets.QWidget = None, column: int = 2, width: int = 100):
        super(ColumnLayout, self).__init__(parent)

        self.setContentsMargins(0, 0, 0, 0)
        self.setSpacing(0)

        self.column = column
        self.width = width

        self.setProperty("sHint", QtCore.QSize())
        self.itemList = list()

    def addItem(self, newItem: QtWidgets.QLayoutItem) -> None:
        self.itemList.append(newItem)

    def removeWidget(self, w: QtWidgets.QWidget) -> None:
        if bool(self.itemList) and isinstance(w, QtWidgets.QWidget):
            for i, item in enumerate(self.itemList):
                if w == item.widget():
                    del self.itemList[i]

    def setGeometry(self, rect: QtCore.QRect = None) -> None:
        width = self.width
        column = self.column
        buttonWidth = buttonHeight = width / column
        height = math.ceil(len(self.itemList) / column) * buttonHeight
        for item in self.itemList:
            i = item.widget().index
            x = i % column * buttonWidth
            y = math.floor(i / column) * buttonHeight
            item.widget().setGeometry(x, y, buttonWidth, buttonHeight)

        self.setProperty("sHint", QtCore.QSize(width, height))

    def sizeHint(self):
        if self.property("sHint") is None:
            return QtCore.QSize(0, 0)
        self.setGeometry()
        return self.property("sHint")

    def count(self):
        return len(self.itemList)

    def itemAt(self, p_int):
        if len(self.itemList) == 0 or p_int < 0 or p_int >= len(self.itemList):
            return None
        return self.itemList[p_int]

    def minimumSize(self):
        return self.sizeHint()


class FunctionArea(QtWidgets.QWidget):
    """功能区域，包含机床、程序、诊断、报警信息等等"""

    def __init__(self, parent=None):
        super(FunctionArea, self).__init__(parent)
        self.setObjectName("FunctionArea")

        column = int(con.get("function-area", "column"))
        width = int(con.get("function-area", "width")) * wRatio
        self.layout = ColumnLayout(self, column, width)
        self.setLayout(self.layout)

        self.buttonGroup = QtWidgets.QButtonGroup(self)


class ControlArea(QtWidgets.QWidget):
    """控制切换区域，切换通道，重新设置等"""

    def __init__(self, parent=None):
        super(ControlArea, self).__init__(parent)
        self.setObjectName("ControlArea")

        column = int(con.get("control-area", "column"))
        width = int(con.get("control-area", "width")) * wRatio
        self.layout = ColumnLayout(self, column, width)
        self.setLayout(self.layout)


class PatternArea(QtWidgets.QWidget):
    """模式区域，包含自动、手动等模式"""

    def __init__(self, parent=None):
        super(PatternArea, self).__init__(parent)
        self.setObjectName("PatternArea")

        column = int(con.get("pattern-area", "column"))
        width = int(con.get("pattern-area", "width")) * wRatio
        self.layout = ColumnLayout(self, column, width)
        self.setLayout(self.layout)

        self.buttonGroup = QtWidgets.QButtonGroup(self)


class RunArea(QtWidgets.QWidget):
    """包含三个按钮，控制已加载程序运行与否"""

    def __init__(self, parent=None):
        super(RunArea, self).__init__(parent)
        self.setObjectName("RunArea")

        width = int(con.get("run-area", "width")) * wRatio
        self.layout = RunLayout(self, width)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setSpacing(0)
        self.setLayout(self.layout)


class RunLayout(QtWidgets.QLayout):
    def __init__(self, parent=None, width=100):
        super(RunLayout, self).__init__(parent)
        self.setContentsMargins(0, 0, 0, 0)
        self.setSpacing(0)

        self.width = width

        self.setProperty("sHint", QtCore.QSize())
        self.itemList = list()
        self.setProperty("itemList", self.itemList)

    def addItem(self, newItem: QtWidgets.QLayoutItem) -> None:
        self.itemList.append(newItem)
        self.setProperty("itemList", self.itemList)

    def removeWidget(self, w: QtWidgets.QWidget) -> None:
        if bool(self.itemList) and isinstance(w, QtWidgets.QWidget):
            for i, item in enumerate(self.itemList):
                if w == item.widget():
                    del self.itemList[i]
                    return

    def setGeometry(self, rect: QtCore.QRect = None) -> None:
        buttonWidth = self.width
        buttonHeight = buttonWidth / 2
        for item in self.itemList:
            index = item.widget().index
            x = 0
            y = index * buttonHeight
            item.widget().setGeometry(x, y, buttonWidth, buttonHeight)

        self.setProperty("sHint", QtCore.QSize(self.width, self.width * 1.5))

    def sizeHint(self):
        if self.property("sHint") is None:
            return QtCore.QSize(0, 0)
        self.setGeometry()
        return self.property("sHint")

    def count(self):
        return len(self.itemList)

    def itemAt(self, p_int):
        if len(self.property("itemList")) == 0 or p_int < 0 or p_int >= len(self.itemList):
            return None
        return self.itemList[p_int]

    def minimumSize(self):
        return self.sizeHint()


class CentralArea(QtWidgets.QWidget):
    """主要信息展示区域"""

    def __init__(self, parent=None):
        super(CentralArea, self).__init__(parent)
        self.setObjectName("CentralArea")

        self.layout = QtWidgets.QStackedLayout(self)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setSpacing(0)
        self.setLayout(self.layout)


class StatusBar(QtWidgets.QStatusBar):
    """状态栏：用于展示提示信息"""

    def __init__(self, parent=None):
        super(StatusBar, self).__init__(parent)
        self.height = int(con.get("status-bar", "height")) * hRatio
        self.setFixedHeight(self.height)


class BottomIndicatorArea(QtWidgets.QWidget):
    """页码展示灯"""

    def __init__(self, parent=None):
        super(BottomIndicatorArea, self).__init__(parent)
        self.setObjectName("Indicator")

        self.height = int(con.get("bottom-indicator-area", "height")) * hRatio
        self.width = int(con.get("bottom-indicator-area", "width")) * wRatio
        self.setFixedHeight(self.height)
        self.setFixedWidth(self.width)
        self.layout = QtWidgets.QHBoxLayout(self)
        self.layout.setContentsMargins(int(con.get("bottom-indicator-area", "margin-left")) * wRatio, 0,
                                       int(con.get("bottom-indicator-area", "margin-right")) * wRatio, 0)
        self.layout.setSpacing(int(con.get("bottom-indicator-area", "spacing")) * wRatio)

        self.setLayout(self.layout)

        self.buttonNum = 1
        self.buttonGroup = QtWidgets.QButtonGroup(self)

        buttonFirst = self.createButton()
        buttonFirst.setChecked(True)
        buttonFirst.index = 0
        self.buttonDict = {0: buttonFirst}

    def createButton(self):
        button = BottomIndicatorButton(self)
        button.setProperty("area", "bottom-indicator")
        self.buttonGroup.addButton(button)
        self.layout.addWidget(button)
        button.setCheckable(True)
        return button

    def setButtonNum(self, num: int) -> None:
        if num > self.buttonNum:
            for i in range(self.buttonNum, num):
                self.buttonDict[i] = self.createButton()
                self.buttonDict[i].index = i
        elif num < self.buttonNum:
            for i in range(num, self.buttonNum):
                self.buttonGroup.removeButton(self.buttonDict[i])
                self.layout.removeWidget(self.buttonDict[i])
                self.buttonDict[i].deleteLater()
        self.buttonNum = num
        self.buttonDict[0].setChecked(True)

    def setButtonCheckedById(self, id: int) -> None:
        if 0 <= id < self.buttonNum:
            checkedButton = self.buttonDict[id]
            checkedButton.setChecked(True)


class BottomIndicatorButton(QtWidgets.QPushButton):
    """页码提示 灯"""

    def __init__(self, parent=None):
        super(BottomIndicatorButton, self).__init__(parent)
        self.setObjectName("Indicator")
        self.clicked.connect(self.jumpPage)

    def jumpPage(self):
        mainwindow = MainWindow.getMainWindow()
        bottomArea = mainwindow.bottomArea
        nowBaseObjectName = bottomArea.layout.currentWidget().objectName()[:-1]
        toObjectName = nowBaseObjectName + str(self.index)
        toBottomPanel = bottomArea.findChild(QtWidgets.QWidget, toObjectName)
        bottomArea.layout.setCurrentWidget(toBottomPanel)

    def paintEvent(self, event: QtGui.QPaintEvent) -> None:
        painter = QtGui.QPainter(self)
        painter.begin(self)
        painter.setRenderHints(QtGui.QPainter.Antialiasing | QtGui.QPainter.TextAntialiasing)
        if self.isChecked():
            brush = QtGui.QBrush(QtCore.Qt.green)
        else:
            brush = QtGui.QBrush(QtCore.Qt.lightGray)
        painter.setBrush(brush)
        painter.drawRoundedRect(self.rect(), 2.5, 2.5)
        painter.end()


class BottomArea(QtWidgets.QWidget):
    """底部二级菜单"""

    def __init__(self, parent=None):
        super(BottomArea, self).__init__(parent)
        self.setObjectName("BottomArea")

        self.layout = QtWidgets.QStackedLayout(self)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setSpacing(0)
        self.setLayout(self.layout)


class RightArea(QtWidgets.QWidget):
    """右侧三级菜单"""

    def __init__(self, parent=None):
        super(RightArea, self).__init__(parent)
        self.setObjectName("RightArea")

        self.layout = QtWidgets.QStackedLayout(self)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setSpacing(0)
        self.setLayout(self.layout)


class RightIndicatorArea(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(RightIndicatorArea, self).__init__(parent)
        self.setObjectName("Indicator")

        self.width = int(con.get("right-indicator-area", "width")) * wRatio
        self.height = int(con.get("right-indicator-area", "height")) * hRatio
        self.setFixedWidth(self.width)
        self.setFixedHeight(self.height)

        self.layout = QtWidgets.QHBoxLayout(self)
        self.layout.setContentsMargins(int(con.get("right-indicator-area", "margin-left")) * wRatio, 0,
                                       int(con.get("right-indicator-area", "margin-right")) * wRatio, 0)
        self.layout.setSpacing(int(con.get("right-indicator-area", "spacing")) * wRatio)

        self.setLayout(self.layout)

        self.buttonNum = 1
        self.buttonGroup = QtWidgets.QButtonGroup(self)

        buttonFirst = self.createButton()
        buttonFirst.setChecked(True)
        buttonFirst.index = 0
        self.buttonDict = {0: buttonFirst}

    def createButton(self):
        button = RightIndicatorButton(self)
        button.setProperty("area", "right-indicator")
        self.buttonGroup.addButton(button)
        self.layout.addWidget(button)
        button.setCheckable(True)
        return button

    def setButtonNum(self, num: int) -> None:
        if num > self.buttonNum:
            for i in range(self.buttonNum, num):
                self.buttonDict[i] = self.createButton()
                self.buttonDict[i].index = i
        elif num < self.buttonNum:
            for i in range(num, self.buttonNum):
                self.buttonGroup.removeButton(self.buttonDict[i])
                self.layout.removeWidget(self.buttonDict[i])
                self.buttonDict[i].deleteLater()
        self.buttonNum = num
        self.buttonDict[0].setChecked(True)

    def setButtonCheckedById(self, id: int) -> None:
        if 0 <= id < self.buttonNum:
            checkedButton = self.buttonDict[id]
            checkedButton.setChecked(True)


class RightIndicatorButton(QtWidgets.QPushButton):
    """页码提示 灯"""

    def __init__(self, parent=None):
        super(RightIndicatorButton, self).__init__(parent)
        self.setObjectName("Indicator")
        self.clicked.connect(self.jumpPage)

    def jumpPage(self):
        mainwindow = MainWindow.getMainWindow()
        rightArea = mainwindow.rightArea
        nowBaseObjectName = rightArea.layout.currentWidget().objectName()[:-1]
        toObjectName = nowBaseObjectName + str(self.index)
        toRightPanel = rightArea.findChild(QtWidgets.QWidget, toObjectName)
        rightArea.layout.setCurrentWidget(toRightPanel)

    def paintEvent(self, event: QtGui.QPaintEvent) -> None:
        painter = QtGui.QPainter(self)
        painter.begin(self)
        painter.setRenderHints(QtGui.QPainter.Antialiasing | QtGui.QPainter.TextAntialiasing)
        if self.isChecked():
            brush = QtGui.QBrush(QtCore.Qt.green)
        else:
            brush = QtGui.QBrush(QtCore.Qt.lightGray)
        width = self.width()
        height = self.height()
        painter.setBrush(brush)
        painter.drawRoundedRect(0, 0, width, height, 2.5, 2.5)
        painter.end()
