from Part.basebutton import basebutton


class System(basebutton):

    def __init__(self):
        super(System, self).__init__()
        self.area = self.FUNCTION_AREA

    def setupUi(self, button):
        button.setObjectName("System")
        button.setText("System")
        button.setIndex(5)
        button.setBottomPageNum(1)

    def clickSlot(self, checked):
        self.setBottomCurrentPanel("SystemB0")
