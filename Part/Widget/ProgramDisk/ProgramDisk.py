import shutil, os, psutil
from PyQt5 import QtWidgets, QtCore, QtGui, Qsci

LOCAL_PATH = "computer:/"


class ProgramDisk(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(ProgramDisk, self).__init__(parent)
        self.setObjectName("ProgramDisk")
        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setSpacing(0)

        self.treeView = ATreeView(self)
        self.treeView.sourceModel.setRootPath(LOCAL_PATH)
        self.treeView.setRootIndex(self.treeView.model.mapFromSource(self.treeView.sourceModel.index(LOCAL_PATH)))
        self.previewWidget = ProgramPreviewWidget(self)
        self.previewWidget.close()
        self.searchWidget = SearchWidget(self)
        self.searchWidget.close()
        self.layout.addWidget(self.treeView)
        self.layout.addWidget(self.searchWidget)
        self.layout.addWidget(self.previewWidget)

        self.setLayout(self.layout)


class SearchWidget(QtWidgets.QWidget):
    def __init__(self, parent):
        super(SearchWidget, self).__init__(parent)
        self.setFixedHeight(200)
        self.setObjectName("ProgramDiskSearchWidget")
        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setSpacing(0)
        self.labelTitle = QtWidgets.QLabel(self)
        self.labelTitle.setObjectName("ProgramLabel")
        self.labelTitle.setFixedHeight(25)
        self.listView = QtWidgets.QListView(self)
        self.layout.addWidget(self.labelTitle)
        self.layout.addWidget(self.listView)
        self.listModel = QtCore.QStringListModel(self)
        self.listView.setModel(self.listModel)

        self.listView.setEditTriggers(QtWidgets.QListView.NoEditTriggers)
        self.listView.clicked.connect(self.showResultFromListViewToTreeView)

    def showResultFromListViewToTreeView(self):
        filePath = self.listModel.itemData(self.listView.currentIndex())[0]
        index = self.parent().treeView.model.mapFromSource(self.parent().treeView.sourceModel.index(filePath))
        self.parent().treeView.scrollTo(index)
        self.parent().treeView.setCurrentIndex(index)


class ProgramPreviewWidget(QtWidgets.QWidget):
    def __init__(self, parent):
        super(ProgramPreviewWidget, self).__init__(parent)
        self.setFixedHeight(200)
        # self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setObjectName("ProgramPreviewWidget")
        self.setWindowTitle("Preview")
        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setSpacing(0)
        self.label = QtWidgets.QLabel(self)
        self.label.setObjectName("ProgramLabel")
        # self.label.setStyleSheet("border:1px solid black;")
        self.label.setFixedHeight(25)
        self.layout.addWidget(self.label)

        self.textEdit = NcPreview(self)
        self.textEdit.setReadOnly(True)
        self.layout.addWidget(self.textEdit)

        self.setLayout(self.layout)
        # self.setStyleSheet("border:1px solid gray;")


class NcPreview(Qsci.QsciScintilla):
    """class NcEdit"""

    def __init__(self, parent=None):
        super(NcPreview, self).__init__(parent)
        self.setUtf8(True)  # ??????utf-8??????
        self.setFont(QtGui.QFont("Consolas", 12))  # ??????????????????
        self.setMarginsFont(QtGui.QFont("Consolas", 12))
        # ??????????????????
        self.setMarginType(0, Qsci.QsciScintilla.NumberMargin)
        self.setMarginLineNumbers(0, True)
        self.setMarginsBackgroundColor(QtGui.QColor("#cccccc"))
        #  ???????????????????????????
        self.setCaretLineVisible(True)
        self.setCaretLineBackgroundColor(QtCore.Qt.lightGray)
        self.lineMarginWidth = 10

        self.linesChanged.connect(self.updateLineWidthSlot)

    def updateLineWidthSlot(self):
        """??????????????????"""
        line = str(self.lines())
        width = len(line)
        if self.lineMarginWidth != width:
            self.setMarginWidth(0, width * 10)


class ATreeView(QtWidgets.QTreeView):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.sourceModel = AFileSystemModel(parent)
        self.model = ASortFilterProxyModel(parent)
        self.model.setSourceModel(self.sourceModel)
        self.parent = parent
        self.setAnimated(False)  # ????????????
        self.setAlternatingRowColors(False)  # ????????????????????????
        self.setEditTriggers(QtWidgets.QTreeView.NoEditTriggers)  # ????????????????????????
        self.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)  # ????????????????????????
        self.customContextMenuRequested.connect(self.showContextMenu)  # ???????????????????????????
        self.setModel(self.model)

        self.setColumnWidth(0, 400)  # ?????????????????????
        self.sortByColumn(0, QtCore.Qt.AscendingOrder)

        self.doubleClicked.connect(self.doubleClickedSlot)

    def doubleClickedSlot(self, index: QtCore.QModelIndex):
        currentIndex = self.model.mapToSource(index)
        isDir = self.sourceModel.isDir(currentIndex)
        if not isDir:
            appWin = EAction.get_main_window()
            autoAction = appWin.findChild(GsGuiAction, "AutoAction")
            machineAction = appWin.findChild(GsGuiAction, "Mach__AF1ToolsPanelAction")
            autoAction.trigger()
            machineAction.trigger()
            SIG.programToMachineAutoLoadSignal.emit(self.sourceModel.filePath(currentIndex))

    def showContextMenu(self, pos):
        currentIndex = self.currentIndex()
        if self.indexAt(pos) == currentIndex and self.sourceModel.type(
                self.model.mapToSource(currentIndex)) != "Drive":  # ??????????????????????????????????????????????????????
            self.getFileMenu(QtCore.QPoint(pos.x(), pos.y() + 25))

    def getFileMenu(self, pos):
        self.actionCopy = QtWidgets.QAction(self)
        self.actionCopy.setText("copy")
        self.actionCopy.setObjectName("copy")
        self.actionCopy.triggered.connect(self.copy)

        self.actionPaste = QtWidgets.QAction(self)
        self.actionPaste.setText("paste")
        self.actionPaste.setObjectName("paste")
        self.actionPaste.triggered.connect(self.paste)

        self.actionRename = QtWidgets.QAction(self)
        self.actionRename.setText("rename")
        self.actionRename.setObjectName("rename")
        self.actionRename.triggered.connect(self.rename)

        self.actionDelete = QtWidgets.QAction(self)
        self.actionDelete.setText("delete")
        self.actionDelete.setObjectName("delete")
        self.actionDelete.triggered.connect(self.delete)

        self.actionCut = QtWidgets.QAction(self)
        self.actionCut.setText("cut")
        self.actionCut.setObjectName("cut")
        self.actionCut.triggered.connect(self.cut)

        self.menu = QtWidgets.QMenu(self)  # ??????????????????

        self.menu.addAction(self.actionCopy)
        self.menu.addAction(self.actionCut)
        self.menu.addAction(self.actionPaste)
        self.menu.addAction(self.actionDelete)
        self.menu.addSeparator()
        self.menu.addAction(self.actionRename)
        self.menu.exec(self.mapToGlobal(pos))

    def rename(self):
        self.edit(self.model.index(self.currentIndex().row(), 0, self.model.parent(self.currentIndex())))

    def copy(self):
        currentIndex = self.model.mapToSource(self.currentIndex())
        sourceFilePath = self.sourceModel.filePath(currentIndex)

        clipBoard = QtGui.QGuiApplication.clipboard()
        clipBoard.clear()
        clipBoard.setText("Copy+---+---+" + sourceFilePath)

    def paste(self):
        clipBoard = QtGui.QGuiApplication.clipboard()
        sourceFilePath = clipBoard.text()
        clipBoard.clear()
        try:
            tip = sourceFilePath.split("+---+---+")[0]
            sourcePath = sourceFilePath.split("+---+---+")[1]
        except Exception as e:
            QtWidgets.QMessageBox.warning(self.parent, "Warning", "The paste board has no associated path!")

        currentIndex = self.model.mapToSource(self.currentIndex())
        if self.sourceModel.isDir(currentIndex):
            newPathIndex = currentIndex
        else:
            newPathIndex = self.sourceModel.parent(currentIndex)
        newPath = self.sourceModel.filePath(newPathIndex)

        if tip == "Copy":
            try:
                if self.sourceModel.isDir(self.sourceModel.index(sourcePath)):
                    sourcePathName = sourcePath.split("/")[-1]
                    newPath += "/" + sourcePathName

                    shutil.copytree(sourcePath, newPath)
                else:
                    shutil.copy(sourcePath, newPath)
            except Exception as e:
                QtWidgets.QMessageBox.warning(self.parent, "Warning", str(e))
        elif tip == "Cut":
            try:
                shutil.move(sourcePath, newPath)
            except Exception as e:
                QtWidgets.QMessageBox.warning(self.parent, "Warning", str(e))

    def delete(self):
        currentIndex = self.model.mapToSource(self.currentIndex())
        filePath = self.sourceModel.filePath(currentIndex)

        import sys
        if sys.platform == "win32":
            from win32com.shell import shell, shellcon
            debug = False
            if not debug:
                res = shell.SHFileOperation((0, shellcon.FO_DELETE, filePath, None,
                                             shellcon.FOF_SILENT | shellcon.FOF_ALLOWUNDO | shellcon.FOF_NOCONFIRMATION,
                                             None, None))  # ????????????????????????
                if not res[1]:
                    os.system('del ' + filePath)
        elif not bool(self.sourceModel.fileInfo(currentIndex).baseName()):  # ?????????????????????
            QtWidgets.QMessageBox.warning(self, "Delete warning!",
                                          "The system disk character cannot perform the delete operation!!!!!!",
                                          QtWidgets.QMessageBox.Yes)
        else:

            boolDel = QtWidgets.QMessageBox.warning(self, "Delete warning!!!",
                                                    "The file or folder deleted by this operation is not in the recycle bin. Are you sure you want to delete this file or folder?",
                                                    QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
            if boolDel == QtWidgets.QMessageBox.No:
                pass
            elif boolDel == QtWidgets.QMessageBox.Yes:
                self.sourceModel.remove(currentIndex)

    def cut(self):
        currentIndex = self.model.mapToSource(self.currentIndex())
        sourceFilePath = self.sourceModel.filePath(currentIndex)
        clipBoard = QtGui.QGuiApplication.clipboard()
        clipBoard.clear()
        clipBoard.setText("Cut+---+---+" + sourceFilePath)


class AFileSystemModel(QtWidgets.QFileSystemModel):
    def __init__(self, parent):
        super().__init__(parent)

        self.setReadOnly(False)  # ??????
        # self.setIconProvider(AFileIconProvider())
        # self.setFilter(QtCore.QDir.NoFilter)
        # self.setNameFilters(["*.NC"])  # ?????????????????????NC??????
        # self.setNameFilterDisables(False)  # ?????????????????????????????????
        self.sort(0, QtCore.Qt.DescendingOrder)

    def data(self, index, role=None):
        data = super(AFileSystemModel, self).data(index, role)
        if role == QtCore.Qt.DisplayRole and QtCore.QDir.isRoot(
                QtCore.QDir(self.filePath(index))) and index.column() == 0:
            changedData = self.filePath(index).replace("/", "")
            return changedData
        else:
            return data


class ASortFilterProxyModel(QtCore.QSortFilterProxyModel):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.localDriveList = []
        self.searchLocalDrive()

    def searchLocalDrive(self):
        part = psutil.disk_partitions()
        for i in range(len(part)):
            drivePath = part[i].device.replace("\\", "/")
            tmpList = part[i].opts.split(",")
            if len(tmpList) == 2 and tmpList[1] == "fixed":
                self.localDriveList.append(drivePath)

    def lessThan(self, left, right):
        if self.sortColumn() == 0:
            model = self.sourceModel()
            boolLeftDir = model.fileInfo(left).isDir()
            boolRightDir = model.fileInfo(right).isDir()
            if boolLeftDir != boolRightDir:
                return boolLeftDir
        return super(ASortFilterProxyModel, self).lessThan(left, right)

    def filterAcceptsRow(self, row, parent):
        model = self.sourceModel()
        index = model.index(row, 0, parent)

        filePath = model.filePath(index)
        isDrive = QtCore.QDir.isRoot(QtCore.QDir(filePath))
        if isDrive:
            if filePath in self.localDriveList:
                return True
            else:
                return False
        else:
            return True
