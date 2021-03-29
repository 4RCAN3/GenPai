import MainWindow
import help
import pwgen
from PyQt5 import QtCore, QtGui, QtWidgets




class controller:
    def __init__(self):
        pass

    def help_show(self):
        '''
        help_show [Shows the main window]
        '''

        self.window = QtWidgets.QMainWindow()
        self.ui =  MainWindow.Ui_PasswordGenerator()
        self.ui.setupUi(self.window)
        self.ui.pushButton.clicked.connect(self.show_help)

        self.window.show()
    
    def show_help(self):
        '''
        show_help [Shows the felp window]
        '''

        self.help_window = QtWidgets.QMainWindow()
        self.ui = help.Ui_MainWindow()
        self.ui.setupUi(self.help_window)
        
        self.help_window.show()



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    control = controller()
    control.help_show()
    sys.exit(app.exec_())

