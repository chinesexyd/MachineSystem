from Part.basebutton import basebutton


class Alarm(basebutton):

    def __init__(self):
        super(Alarm, self).__init__()
        self.area = self.FUNCTION_AREA

    def setupUi(self, button):
        button.setObjectName("Alarm")
        button.setText("Alarm")
        button.setIndex(3)
        button.setBottomPageNum(1)

    def clickSlot(self, checked):
        self.setBottomCurrentPanel("AlarmB0")
