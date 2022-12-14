from Part.basebutton import basebutton


class AUTO(basebutton):

    def __init__(self):
        super(AUTO, self).__init__()
        self.area = self.PATTERN_AREA

    def setupUi(self, button):
        button.setObjectName("AUTO")
        button.setText("AUTO")
        button.setIndex(0)

    def clickSlot(self, checked):
        self.setPattern(self.AUTO)
