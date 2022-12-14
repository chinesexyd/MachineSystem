from Part.basebutton import basebutton


class I(basebutton):

    def __init__(self):
        super(I, self).__init__()
        self.area = self.PATTERN_AREA

    def setupUi(self, button):
        button.setObjectName("I")
        button.setText("1")
        button.setIndex(6)

    def clickSlot(self, checked):
        self.setPattern(self.I)
