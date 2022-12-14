from Part.basebutton import basebutton


class MDI(basebutton):

    def __init__(self):
        super(MDI, self).__init__()
        self.area = self.PATTERN_AREA

    def setupUi(self, button):
        button.setObjectName("MDI")
        button.setText("MDI")
        button.setIndex(1)

    def clickSlot(self, checked):
        self.setPattern(self.MDI)
