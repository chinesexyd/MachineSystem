from Part.basebutton import basebutton
from Base.BaseButton import BaseButton
from PyQt5 import QtCore, QtGui


class BottomPageNext(basebutton):
    """底部下一页按键"""

    def __init__(self, bottomPageNum, panelObjectName):
        super(BottomPageNext).__init__()
        self.area = self.BOTTOM_AREA
        self.panelObjectName = panelObjectName
        self.bottomPageNum = bottomPageNum

    def setupUi(self, button: BaseButton):
        button.setIndex(10)
        button.setShortcut(QtCore.Qt.Key_D)
        button.setObjectName("NEXT")
        button.setIcon(QtGui.QIcon(QtGui.QPixmap("../Tool/Resource/NEXT.svg")))
        button.setIconSize(QtCore.QSize(button.height() * 1.3, button.height() * 1.3))

    def clickSlot(self, check):
        baseName = self.panelObjectName[:-1]
        index = int(self.panelObjectName[-1])
        if index == self.bottomPageNum - 1:
            toIndex = 0
        else:
            toIndex = index + 1
        toPanelName = baseName + str(toIndex)
        self.setBottomCurrentPanel(toPanelName)
        self.setBottomIndicatorById(toIndex)


class BottomPageUp(basebutton):
    """底部返回上一层按键"""

    def __init__(self, bottomPageNum, panelObjectName):
        super(BottomPageUp).__init__()
        self.area = self.BOTTOM_AREA
        self.panelObjectName = panelObjectName
        self.bottomPageNum = bottomPageNum

    def setupUi(self, button: BaseButton):
        button.setIndex(0)
        button.setShortcut(QtCore.Qt.Key_W)
        button.setObjectName("UP")
        button.setIcon(QtGui.QIcon(QtGui.QPixmap("../Tool/Resource/UP.svg")))
        button.setIconSize(QtCore.QSize(button.height() * 1.3, button.height() * 1.3))

    def clickSlot(self, check):
        nameList = self.panelObjectName.split("/")
        name1 = nameList[-1]
        name2 = nameList[-2]
        parentPanelName = "/".join(nameList[:-1])  # returnPanelName
        parentParentButtonName = name2[:-2]
        parentParentPanelName = "/".join(nameList[:-2])
        parentPanelIndex = int(name1[-1])
        self.setBottomCurrentPanel(parentPanelName)
        if parentParentPanelName:
            parentParentButton = self.getBottomButton(parentParentPanelName, parentParentButtonName)
        else:
            parentParentButton = self.getFunctionButtonByName(parentParentButtonName)
        pageNum = parentParentButton.bottomPageNum
        self.getBottomIndicatorArea().setButtonNum(pageNum)
        self.setBottomIndicatorById(parentPanelIndex)


class RightPageNext(basebutton):
    """右侧下一页按键"""

    def __init__(self, rightPageNum, panelObjectName):
        super(RightPageNext).__init__()
        self.area = self.RIGHT_AREA
        self.panelObjectName = panelObjectName
        self.rightPageNum = rightPageNum

    def setupUi(self, button: BaseButton):
        button.setIndex(10)
        button.setShortcut(QtCore.Qt.Key_Right)
        button.setObjectName("NEXT")
        button.setIcon(QtGui.QIcon(QtGui.QPixmap("../Tool/Resource/NEXT.svg")))
        button.setIconSize(QtCore.QSize(button.height() * 1.3, button.height() * 1.3))

    def clickSlot(self, check):
        panelBaseName = self.panelObjectName[:-1]
        panelCurrentIndex = int(self.panelObjectName[-1])
        if panelCurrentIndex == self.rightPageNum - 1:
            panelToIndex = 0
        else:
            panelToIndex = panelCurrentIndex + 1
        toPanelName = panelBaseName + str(panelToIndex)
        self.setRightCurrentPanel(toPanelName)
        self.setRightIndicatorById(panelToIndex)


class RightPageReturn(basebutton):
    """右侧返回上一层按键"""

    def __init__(self, rightPageNum, panelObjectName, upbo):
        super(RightPageReturn).__init__()
        self.area = self.RIGHT_AREA
        self.panelObjectName = panelObjectName
        self.rightPageNum = rightPageNum
        self.upbo = upbo

    def setupUi(self, button: BaseButton):
        if self.upbo:
            button.setIndex(9)
        else:
            button.setIndex(10)
        button.setObjectName("RETURN")
        button.setIcon(QtGui.QIcon(QtGui.QPixmap("../Tool/Resource/RETURN.svg")))
        button.setIconSize(QtCore.QSize(button.height() * 1.3, button.height() * 1.3))

    def clickSlot(self, check):
        nameList = self.panelObjectName.split("/")
        name1 = nameList[-1]
        name2 = nameList[-2]
        name3 = nameList[-3]
        parentPanelName = "/".join(nameList[:-1])  # returnPanelName
        parentParentButtonName = name2[:-2]
        parentParentPanelName = "/".join(nameList[:-2])
        parentPanelIndex = int(name1[-1])
        self.setRightCurrentPanel(parentPanelName)
        if "B" in name3:
            parentParentButton = self.getBottomButton(parentParentPanelName, parentParentButtonName)
        else:
            parentParentButton = self.getRightButton(parentParentPanelName, parentParentButtonName)
        pageNum = parentParentButton.rightPageNum
        self.getRightIndicatorArea().setButtonNum(pageNum)
        self.setRightIndicatorById(parentPanelIndex)
