from Part.basebutton import basebutton


class Diagnose(basebutton):

    def __init__(self):
        super(Diagnose, self).__init__()
        self.area = self.FUNCTION_AREA

    def setupUi(self, button):
        button.setObjectName("Diagnose")
        button.setText("Diag")
        button.setIndex(4)
        button.setBottomPageNum(1)

    def clickSlot(self, checked):
        self.setBottomCurrentPanel("DiagnoseB0")
