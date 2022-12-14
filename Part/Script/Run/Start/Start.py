from Part.basebutton import basebutton


class Start(basebutton):
    def __init__(self):
        super(Start, self).__init__()
        self.area = self.RUN_AREA

    def setupUi(self, button):
        button.setObjectName("Start")
        button.setText("Start")
        button.index = 0

    def clickSlot(self, checked):
        print("Start")
