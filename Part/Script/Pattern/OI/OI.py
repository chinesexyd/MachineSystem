from Part.basebutton import basebutton


class OI(basebutton):

    def __init__(self):
        super(OI, self).__init__()
        self.area = self.PATTERN_AREA

    def setupUi(self, button):
        button.setObjectName("OI")
        button.setText("0.1")
        button.setIndex(5)

    def clickSlot(self, checked):
        self.setPattern(self.OI)
