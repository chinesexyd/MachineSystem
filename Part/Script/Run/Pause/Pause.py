from Part.basebutton import basebutton


class Pause(basebutton):
    def __init__(self):
        super(Pause, self).__init__()
        self.area = self.RUN_AREA

    def setupUi(self, button):
        button.setObjectName("Pause")
        button.setText("Pause")
        button.setIndex(2)

    def clickSlot(self, checked):
        print("Pause")
