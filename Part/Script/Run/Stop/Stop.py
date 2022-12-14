from Part.basebutton import basebutton


class Stop(basebutton):
    def __init__(self):
        super(Stop, self).__init__()
        self.area = self.RUN_AREA

    def setupUi(self, button):
        self.button = button
        button.setObjectName("Stop")
        button.setText("Stop")
        button.setIndex(1)

    def clickSlot(self, checked):
        print(self.button)
