from Part.basebutton import basebutton


class MPG(basebutton):

    def __init__(self):
        super(MPG, self).__init__()
        self.area = self.PATTERN_AREA

    def setupUi(self, button):
        button.setObjectName("MPG")
        button.setText("MPG")
        button.setIndex(8)

    def clickSlot(self, checked):
        self.setPattern(self.MPG)
