import os
from Base.BottomPanel import BottomPanel
from Base.RightPanel import RightPanel
from Part.buttonfactory import *


class addon(object):
    """
    组装中心
    将base中的元素实例化并组装在一起
    """
    BOTTOM_AREA = "A_"
    RIGHT_AREA = "B_"
    CENTRAL_AREA = "C_"
    FUNCTION_AREA = "D_"
    CONTROL_AREA = "E_"
    PATTERN_AREA = "F_"
    RUN_AREA = "G_"

    def __init__(self, mainwindow=None):
        self.mainwindow = mainwindow

    """获取组装平台"""

    def getFunctionArea(self):
        return self.mainwindow.leftArea.functionArea

    def getFunctionLayout(self):
        return self.mainwindow.leftArea.functionArea.layout

    def getFunctionButtonGroup(self):
        return self.mainwindow.leftArea.functionArea.buttonGroup

    def getControlArea(self):
        return self.mainwindow.leftArea.controlArea

    def getControlLayout(self):
        return self.mainwindow.leftArea.controlArea.layout

    def getPatternArea(self):
        return self.mainwindow.leftArea.patternArea

    def getPatternLayout(self):
        return self.mainwindow.leftArea.patternArea.layout

    def getPatternButtonGroup(self):
        return self.mainwindow.leftArea.patternArea.buttonGroup

    def getRunArea(self):
        return self.mainwindow.leftArea.runArea

    def getRunLayout(self):
        return self.mainwindow.leftArea.runArea.layout

    def getBottomArea(self):
        return self.mainwindow.bottomArea

    def getBottomLayout(self):
        return self.mainwindow.bottomArea.layout

    def getRightArea(self):
        return self.mainwindow.rightArea

    def getRightLayout(self):
        return self.mainwindow.rightArea.layout

    def getCentralArea(self):
        return self.mainwindow.centralArea

    def getCentralLayout(self):
        return self.mainwindow.centralArea.layout

    """页"""

    def getBottomPanel(self, name: str) -> BottomPanel:
        bottomPanel = self.getBottomArea().findChild(BottomPanel, name)
        return bottomPanel

    def getRightPanel(self, name: str) -> RightPanel:
        rightPanel = self.getRightArea().findChild(RightPanel, name)
        return rightPanel

    """标准化通用化工件生产之中心"""

    def createBottomPageNextButton(self, bottomPageNum, panel):
        faButton = BottomPageNext(bottomPageNum, panel.objectName())
        button = BaseButton(panel, faButton)
        faButton.setupUi(button)
        panel.layout.addWidget(button)

    def createBottomPageUpButton(self, bottomPageNum, panel):
        faButton = BottomPageUp(bottomPageNum, panel.objectName())
        button = BaseButton(panel, faButton)
        faButton.setupUi(button)
        panel.layout.addWidget(button)

    def createRightPageNextButton(self, rightPageNum, panel):
        faButton = RightPageNext(rightPageNum, panel.objectName())
        button = BaseButton(panel, faButton)
        faButton.setupUi(button)
        panel.layout.addWidget(button)

    def createRightPageReturnButton(self, rightPageNum, panel, upbo):
        faButton = RightPageReturn(rightPageNum, panel.objectName(), upbo)
        button = BaseButton(panel, faButton)
        faButton.setupUi(button)
        panel.layout.addWidget(button)

    """私人定制工件及窗口收集之中心"""

    def getScriptsFilePaths(self):
        excluteList = ["../Part/Script/Pattern", "../Part/Script/Function", "../Part/Script/Control",
                       "../Part/Script/Run"]
        scriptsPath = "../Part/Script/"
        scriptsList = self.walkInPath(scriptsPath, excluteList)
        return scriptsList

    def getCentralWidgetPaths(self):
        excluteList = []
        centralPath = "../Part/Widget/"
        centralList = self.walkInPath(centralPath, excluteList)
        return centralList

    def getImportPath(self, filePath: str):
        # ..Part/Script/Machine
        path = filePath.replace("../", "")
        pathList = path.split("/")
        newPath = ".".join(pathList)
        newPathList = newPath.split("\\")
        front = ".".join(newPathList)
        back = front.split(".")[-1]
        front = front + ".{}".format(back)
        return front, back

    def walkInPath(self, path: str, excluteList=None) -> list:
        pathList = []
        for path, dirList, fileList in os.walk(path):
            for dir in dirList:
                filePath = os.path.join(path, dir)
                if filePath not in excluteList and dir != "__pycache__":
                    pathList.append(filePath)
        return pathList

    """将平台与工件实施组装焊接之中心"""

    def parseAllWidgets(self):
        widghtsList = self.getCentralWidgetPaths()
        for filePath in widghtsList:
            front, back = self.getImportPath(filePath)
            exec("from {} import {}".format(front, back))
            widget = eval("{}(self.getCentralArea())".format(back))
            self.getCentralLayout().addWidget(widget)

    def parseAllScripts(self):
        scriptsList = self.getScriptsFilePaths()
        for filePath in scriptsList:
            front, back = self.getImportPath(filePath)
            exec("from {} import {}".format(front, back))
            fakeButton = eval("{}()".format(back))
            area = fakeButton.area

            if area == self.FUNCTION_AREA:
                self.functionAreaManager(fakeButton)

            elif area == self.CONTROL_AREA:
                self.controlAreaManager(fakeButton)

            elif area == self.PATTERN_AREA:
                self.parttenAreaManager(fakeButton)

            elif area == self.RUN_AREA:
                self.runAreaManager(fakeButton)

            elif area == self.BOTTOM_AREA:
                self.bottomAreaManager(fakeButton)

            elif area == self.RIGHT_AREA:
                self.rightAreaManager(fakeButton)

            else:
                print("检查区域设置吧")

    def functionAreaManager(self, fakeButton):
        button = BaseButton(self.getFunctionArea(), fakeButton)
        button.area = fakeButton.area
        button.setCheckable(True)
        self.getFunctionButtonGroup().addButton(button)
        fakeButton.setupUi(button)
        self.getFunctionLayout().addWidget(button)

        bottomPageNum = button.bottomPageNum
        buttonName = button.objectName()

        for i in range(bottomPageNum):
            panel = BottomPanel(self.getBottomArea())
            panelName = buttonName + "B{}".format(i)
            panel.setObjectName(panelName)
            if bottomPageNum > 1:
                self.createBottomPageNextButton(bottomPageNum, panel)

            self.mainwindow.buttonMsg += "\033[32;5m功能按钮 | 创建的\033[0m | \033[31;5m底部页面 | 取用BasePanel值 | {} |      \"{}\"\033[0m\n".format(
                buttonName, panelName)
            self.getBottomLayout().addWidget(panel)

        rightPageNum = button.rightPageNum
        for i in range(rightPageNum):
            panel = RightPanel(self.getRightArea())
            panelName = buttonName + "R{}".format(i)
            panel.setObjectName(panelName)
            if rightPageNum > 1:
                self.createRightPageNextButton(rightPageNum, panel)

            self.mainwindow.buttonMsg += "\033[32;5m功能按钮 | 创建的\033[0m | \033[35;5m右侧页面 | 取用BasePanel值 | {} |       \"{}\"\033[0m\n".format(
                buttonName, panelName)
            self.getRightLayout().addWidget(panel)

    def controlAreaManager(self, fakeButton):
        button = BaseButton(self.getControlArea(), fakeButton)
        fakeButton.setupUi(button)
        self.getControlLayout().addWidget(button)

    def parttenAreaManager(self, fakeButton):
        button = BaseButton(self.getPatternArea(), fakeButton)
        button.setCheckable(True)
        self.getPatternButtonGroup().addButton(button)
        fakeButton.setupUi(button)
        self.getPatternLayout().addWidget(button)

    def runAreaManager(self, fakeButton):
        button = BaseButton(self.getRunArea(), fakeButton)
        fakeButton.setupUi(button)
        self.getRunLayout().addWidget(button)

    def bottomAreaManager(self, fakeButton):
        bottomPanel = self.getBottomPanel(fakeButton.basePanel)
        button = BaseButton(bottomPanel, fakeButton)
        fakeButton.setupUi(button)
        if button.buttonGroup:
            button.setCheckable(True)
            bottomPanel.buttonGroup.addButton(button)
        bottomPanel.layout.addWidget(button)

        buttonName = button.objectName()
        basePanelName = bottomPanel.objectName() + "/" + buttonName

        rightPageNum = button.rightPageNum
        for i in range(rightPageNum):
            panel = RightPanel(self.getRightArea())
            panelName = basePanelName + "R{}".format(i)
            panel.setObjectName(panelName)

            if rightPageNum > 1:
                self.createRightPageNextButton(rightPageNum, panel)

            self.mainwindow.buttonMsg += "\033[31;5m底部按钮 | 创建的\033[0m | \033[35;5m右侧页面 | 取用BasePanel值 | {} |       \"{}\"\033[0m\n".format(
                buttonName, panelName)
            self.getRightLayout().addWidget(panel)

        bottomPageNum = button.bottomPageNum
        for i in range(bottomPageNum):
            panel = BottomPanel(self.getBottomArea())
            panelName = basePanelName + "B{}".format(i)
            panel.setObjectName(panelName)
            self.createBottomPageUpButton(bottomPageNum, panel)
            if bottomPageNum > 1:
                self.createBottomPageNextButton(bottomPageNum, panel)

            self.mainwindow.buttonMsg += "\033[31;5m底部按钮 | 创建的\033[0m | \033[31;5m底部页面 | 取用BasePanel值 | {} |       \"{}\"\033[0m\n".format(
                buttonName, panelName)
            self.getBottomLayout().addWidget(panel)

    def rightAreaManager(self, fakeButton):
        rightPanel = self.getRightPanel(fakeButton.basePanel)
        button = BaseButton(rightPanel, fakeButton)
        fakeButton.setupUi(button)
        if button.buttonGroup:
            button.setCheckable(True)
            rightPanel.buttonGroup.addButton(button)
        rightPanel.layout.addWidget(button)
        buttonName = button.objectName()
        basePanelName = rightPanel.objectName() + "/" + buttonName

        rightPageNum = button.rightPageNum
        for i in range(rightPageNum):
            panel = RightPanel(self.getRightArea())
            panelName = basePanelName + "R{}".format(i)
            panel.setObjectName(panelName)
            if rightPageNum > 1:
                self.createRightPageNextButton(rightPageNum, panel)
                if not button.hasDialog:
                    self.createRightPageReturnButton(rightPageNum, panel, True)
            else:
                self.createRightPageReturnButton(rightPageNum, panel, False)

            self.mainwindow.buttonMsg += "\033[35;5m右侧按钮 | 创建的\033[0m | \033[35;5m右侧页面 | 取用BasePanel值 | {} |       \"{}\"\033[0m\n".format(
                buttonName, panelName)
            self.getRightLayout().addWidget(panel)
