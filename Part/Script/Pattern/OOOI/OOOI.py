from Part.basebutton import basebutton


class OOOI(basebutton):

    def __init__(self):
        super(OOOI, self).__init__()
        self.area = self.PATTERN_AREA

    def setupUi(self, button):
        button.setObjectName("OOOI")
        button.setText("0.001")
        button.setIndex(3)

    def clickSlot(self, checked):
        self.setPattern(self.OOOI)
