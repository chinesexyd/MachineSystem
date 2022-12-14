from Part.basebutton import basebutton


class OOI(basebutton):

    def __init__(self):
        super(OOI, self).__init__()
        self.area = self.PATTERN_AREA

    def setupUi(self, button):
        button.setObjectName("OOI")
        button.setText("0.01")
        button.setIndex(4)

    def clickSlot(self, checked):
        self.setPattern(self.OOI)
