import sys, time
from Base.MainWindow import MainWindow, QtWidgets
from Part.addon import addon
from Tool.Methods.SmallTools import ReadQss

if __name__ == '__main__':
    t1 = time.time()
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = MainWindow()
    t2 = time.time()
    addOn = addon(mainWindow)
    addOn.parseAllScripts()
    addOn.parseAllWidgets()
    t3 = time.time()
    mainWindow.setStyleSheet(ReadQss("../Tool/Qss/default.qss"))
    t4 = time.time()
    print(mainWindow.buttonMsg)
    print("总体启动时间:%.3f秒" % (t4 - t1))
    print("组装所需时间:%.3f秒" % (t3 - t2))
    print("设置样式时间:%.3f秒" % (t4 - t3))
    mainWindow.show()
    sys.exit(app.exec_())
