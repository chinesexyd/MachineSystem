# -*- coding: utf-8 -*-
from Base.MainWindow import MainWindow, QtWidgets
from Base.BaseButton import BaseButton


class basebutton(object):
    BOTTOM_AREA = "A_"
    RIGHT_AREA = "B_"
    CENTRAL_AREA = "C_"
    FUNCTION_AREA = "D_"
    CONTROL_AREA = "E_"
    PATTERN_AREA = "F_"
    RUN_AREA = "G_"

    AUTO = "AUTO"
    MDI = "MDI"
    JOG = "JOG"
    OOOI = "OOOI"
    OOI = "OOI"
    OI = "OI"
    I = "I"
    VAR = "VAR"
    MPG = "MPG"
    HOME = "HOME"

    def __init__(self):
        """
        1.设置按钮区域
        """
        self.area = ""
        """
        2.使用频率高的控件给子类继承，对象重用，不用重新查找
        """

    def setupUi(self, button: BaseButton):
        """设置按钮属性"""
        pass

    def clickSlot(self, check):
        """点击事件"""
        pass

    def getCentralCurrentWidget(self) -> QtWidgets.QWidget:
        """获取Central区域当前Widget"""
        currentWidget = MainWindow.getMainWindow().centralArea.layout.getCurrentWidget()
        return currentWidget

    def getBottomPanel(self, name: str):
        """获取底部按钮页"""
        bottomArea = MainWindow.getMainWindow().bottomArea
        bottomPanel = bottomArea.findChild(QtWidgets.QWidget, name)
        return bottomPanel

    def getBottomButton(self, name: str, index: int or str = None) -> QtWidgets.QPushButton:
        """获取底部按钮"""
        bottomPanel = self.getBottomPanel(name)
        if isinstance(index, str):
            button = bottomPanel.getButtonByName(index)
        elif isinstance(index, int):
            button = bottomPanel.getButtonByIndex(index)
        else:
            raise TypeError("请填写正确的参数")
        return button

    def setBottomCurrentPanel(self, name: str) -> None:
        """设置要显示的底部按钮页"""
        bottomLayout = MainWindow.getMainWindow().bottomArea.layout
        bottomPanel = self.getBottomPanel(name)
        bottomLayout.setCurrentWidget(bottomPanel)

    def setBottomIndicatorById(self, id):
        MainWindow.getMainWindow().bottomIndicatorArea.setButtonCheckedById(id)

    def getFunctionButtonById(self, id: int) -> BaseButton:
        button = MainWindow.getMainWindow().leftArea.functionArea.layout.itemAt(id).widget()
        return button

    def getFunctionButtonByName(self, name: str) -> BaseButton:
        functionArea = MainWindow.getMainWindow().leftArea.functionArea
        button = functionArea.findChild(BaseButton, name)
        return button

    def setPattern(self, pattern):
        MainWindow.getMainWindow().setProperty("pattern", pattern)

    def getCurrentPattern(self):
        pattern = MainWindow.getMainWindow().property("pattern")
        return pattern

    def setCentralCurrentWidget(self, name: str) -> None:
        centralArea = MainWindow.getMainWindow().centralArea
        centralLayout = centralArea.layout
        currentWidget = centralArea.findChild(QtWidgets.QWidget, name)
        centralLayout.setCurrentWidget(currentWidget)

    def getBottomIndicatorArea(self):
        return MainWindow.getMainWindow().bottomIndicatorArea

    def setRightCurrentPanel(self, name: str):
        rightArea = MainWindow.getMainWindow().rightArea
        currentPanel = rightArea.findChild(QtWidgets.QWidget, name)
        rightArea.layout.setCurrentWidget(currentPanel)

    def setRightIndicatorById(self, id):
        MainWindow.getMainWindow().rightIndicatorArea.setButtonCheckedById(id)

    def getRightIndicatorArea(self):
        return MainWindow.getMainWindow().rightIndicatorArea

    def getRightPanel(self, name: str) -> QtWidgets.QWidget:
        rightArea = MainWindow.getMainWindow().rightArea
        rightPanel = rightArea.findChild(QtWidgets.QWidget, name)
        return rightPanel

    def getRightButton(self, name: str, index: int or str = None) -> BaseButton:
        rightPanel = self.getRightPanel(name)
        if isinstance(index, str):
            button = rightPanel.getButtonByName(index)
        elif isinstance(index, int):
            button = rightPanel.getButtonByIndex(index)
        else:
            raise TypeError("请填写正确的参数")
        return button


