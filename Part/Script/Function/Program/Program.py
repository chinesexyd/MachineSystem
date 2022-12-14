from Part.basebutton import basebutton


class Program(basebutton):

    def __init__(self):
        super(Program, self).__init__()
        self.area = self.FUNCTION_AREA

    def setupUi(self, button):
        button.setObjectName("Program")
        button.setText("Prog")
        button.setIndex(1)
        button.setBottomPageNum(2)

    def clickSlot(self, checked):
        self.setBottomCurrentPanel("ProgramB0")
        self.setRightCurrentPanel("ProgramR0")

