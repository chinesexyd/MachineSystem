from Part.basebutton import basebutton


class Channel(basebutton):

    def __init__(self):
        super(Channel, self).__init__()
        self.area = self.CONTROL_AREA

    def setupUi(self, button):
        button.setObjectName("Channel")
        button.setText("Chan")
        button.setIndex(0)

    def clickSlot(self, checked):
        pass
