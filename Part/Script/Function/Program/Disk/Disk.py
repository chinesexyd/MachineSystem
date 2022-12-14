from Part.Script.Function.Program.Program import Program


class Disk(Program):
    def __init__(self):
        super(Disk, self).__init__()
        self.area = self.BOTTOM_AREA
        self.basePanel = "ProgramB0"

    def setupUi(self, button):
        button.setObjectName("Disk")
        button.setText("Disk")
        button.setIndex(2)
        button.setShortcut("F2")
        button.setRightPageNum(3)
        button.setBottomPageNum(3)
        button.setButtonGroup(True)

    def clickSlot(self, checked):
        self.setCentralCurrentWidget("ProgramDisk")
        self.setBottomCurrentPanel("ProgramB0/DiskB0")
        self.setRightCurrentPanel("ProgramB0/DiskR0")
