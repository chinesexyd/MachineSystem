from Part.basebutton import basebutton


class JOG(basebutton):

    def __init__(self):
        super(JOG, self).__init__()
        self.area = self.PATTERN_AREA

    def setupUi(self, button):
        button.setObjectName("JOG")
        button.setText("JOG")
        button.setIndex(2)

    def clickSlot(self, checked):
        self.setPattern(self.JOG)
