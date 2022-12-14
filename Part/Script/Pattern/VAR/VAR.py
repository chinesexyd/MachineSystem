from Part.basebutton import basebutton


class VAR(basebutton):

    def __init__(self):
        super(VAR, self).__init__()
        self.area = self.PATTERN_AREA

    def setupUi(self, button):
        button.setObjectName("VAR")
        button.setText("VAR")
        button.setIndex(7)

    def clickSlot(self, checked):
        self.setPattern(self.VAR)
