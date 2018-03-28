from PyQt4 import QtGui
# from mainwindow import Ui_MainWindow

class Login(QtGui.QDialog):
    def __init__(self, parent=None):
        super(Login, self).__init__(parent)
        self.setWindowTitle("Team jarvis") 
        self.textName = QtGui.QLineEdit(self)
        self.textPass = QtGui.QLineEdit(self)
        self.buttonLogin = QtGui.QPushButton('Login', self)
        self.buttonLogin.clicked.connect(self.handleLogin)
        layout = QtGui.QVBoxLayout(self)
        layout.addWidget(self.textName)
        layout.addWidget(self.textPass)
        layout.addWidget(self.buttonLogin)


    def handleLogin(self):
        if (self.textName.text() == 'bhanu' and
            self.textPass.text() == 'jamwal'):
            self.accept()
        else:
            QtGui.QMessageBox.warning(
                self, 'Error', 'Bad user or password')

class Window(QtGui.QMainWindow):
    def __init__(self, parent=None):
        super(Window, self).__init__(parent)
        # self.ui = Ui_MainWindow()
        # self.ui.setupUi(self)
        self.setWindowTitle("Team jarvis")
        

        def file_open(self):
            name=QtGui.QfileDialog.getopenfileName(self,'openfile')
            file=open(name,'r')
            self.editor()
            with file:
                text=file.read()
                self.textEdit.settext(text)

if __name__ == '__main__':
    import sys
    app = QtGui.QApplication(sys.argv)
    login = Login()

    if login.exec_() == QtGui.QDialog.Accepted:
        window = Window()
        window.show()
        sys.exit(app.exec_())
