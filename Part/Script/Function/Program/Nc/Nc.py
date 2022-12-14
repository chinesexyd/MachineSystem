from Part.Script.Function.Program.Program import Program


class Nc(Program):
    def __init__(self):
        super(Nc, self).__init__()
        self.area = self.BOTTOM_AREA
        self.basePanel = "ProgramB0"

    def setupUi(self, button):
        button.setObjectName("NC")
        button.setText("NC")
        button.setIndex(1)
        button.setShortcut("F1")
        button.setRightPageNum(1)
        button.setButtonGroup(True)

    def clickSlot(self, checked):
        self.setRightCurrentPanel("ProgramB0/NCR0")
        self.setCentralCurrentWidget("ProgramNc")
