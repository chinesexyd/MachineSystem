from Part.basebutton import basebutton


class Reset(basebutton):

    def __init__(self):
        super(Reset, self).__init__()
        self.area = self.CONTROL_AREA

    def setupUi(self, button):
        button.setObjectName("Reset")
        button.setText("Reset")
        button.setIndex(1)

    def clickSlot(self, checked):
        pass
