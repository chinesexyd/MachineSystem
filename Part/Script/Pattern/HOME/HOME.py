from Part.basebutton import basebutton


class HOME(basebutton):

    def __init__(self):
        super(HOME, self).__init__()
        self.area = self.PATTERN_AREA

    def setupUi(self, button):
        button.setObjectName("HOME")
        button.setText("HOME")
        button.setIndex(9)

    def clickSlot(self, checked):
        self.setPattern(self.HOME)
