from Part.basebutton import basebutton


class Data(basebutton):

    def __init__(self):
        super(Data, self).__init__()
        self.area = self.FUNCTION_AREA

    def setupUi(self, button):
        button.setObjectName("Data")
        button.setText("Data")
        button.setShortcut("F3")
        button.setIndex(2)
        button.setBottomPageNum(1)

    def clickSlot(self, checked):
        self.setBottomCurrentPanel("DataB0")
