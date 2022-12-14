from Part.basebutton import basebutton


class Machine(basebutton):

    def __init__(self):
        super(Machine, self).__init__()
        self.area = self.FUNCTION_AREA

    def setupUi(self, button):
        button.setObjectName("Machine")
        button.setText("Mach")
        button.setShortcut("F3")
        button.setIndex(0)
        button.setBottomPageNum(3)
        button.setRightPageNum(2)

    def clickSlot(self, checked):
        self.setCentralCurrentWidget("MachineWidgets")
        self.setBottomCurrentPanel("MachineB0")
        self.setRightCurrentPanel("MachineR0")
        pattern = self.getCurrentPattern()
        print(pattern)
        if pattern == self.AUTO:
            pass
        elif pattern == self.MDI:
            pass
        elif pattern == self.JOG:
            pass
        elif pattern == self.OOOI:
            pass
        elif pattern == self.OOI:
            pass
        elif pattern == self.OI:
            pass
        elif pattern == self.I:
            pass
        elif pattern == self.VAR:
            pass
        elif pattern == self.MPG:
            pass
        elif pattern == self.HOME:
            pass
        else:
            raise TypeError("ERROR Pattern!")
