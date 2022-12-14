from Part.Script.Function.Program.Disk.Disk import Disk


class Copy(Disk):
    def __init__(self):
        super(Disk, self).__init__()
        self.area = self.RIGHT_AREA
        self.basePanel = "ProgramB0/DiskR0"

    def setupUi(self, button):
        button.setObjectName("Copy")
        button.setText("Copy")
        button.setIndex(8)
        button.setShortcut("Ctrl + F3")
        button.setRightPageNum(2)
        button.setHasDialog(False)

    def clickSlot(self, checked):
        self.setRightCurrentPanel("ProgramB0/DiskR0/CopyR0")
