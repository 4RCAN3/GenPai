import MainWindow
import help
import pwgen
from PyQt5 import QtCore, QtGui, QtWidgets



class controller:
    def __init__(self):
        pass

    def after_click(self):
        
        IncLeet = self.ui.IncludeLeetCheck.checkState()
        IncWL = self.ui.IncludeWLCheck.checkState()
        customWord = self.ui.CustomWordsText.toPlainText()
        
        IncComboPS = self.ui.IncludeCombosCheck.checkState()
        prefixText = self.ui.AddPrefixText.toPlainText()
        suffixText = self.ui.AddSuffixText.toPlainText()
        IncNumsPre = self.ui.IncludeNumsPreCheck.checkState()
        IncNumsSuff = self.ui.IncludeNumsSufCheck.checkState()
        prefixNumLen = self.ui.PrefixNumLenCheck.value()
        suffixNumLen = self.ui.SuffixNumLenCheck.value()
        prefixMinNumLen = self.ui.MinPreComboLenCheck.value()
        suffixMinNumLen = self.ui.MinSufComboLenCheck.value()
        addWLPre = self.ui.IncludeWLpreCheck.checkState()
        addWLSuf = self.ui.IncludeWLSufCheck.checkState()

        IncNumsInWL = self.ui.IncludeNumsCheck.checkState()
        UseDefaultCharList = self.ui.DefaultListCheck.checkState()
        customList = self.ui.CustomListText.toPlainText()
        extendList = self.ui.ExtendDefaultListText.toPlainText()
        MinComboLen = self.ui.MinComboLenCheck.value()
        MaxComboLen = self.ui.MaxComboLenCheck.value()

        useDefText = self.ui.UseDefTxtFileCheck.checkState()
        useCustomText = self.ui.UseCustomTxtFileCheck.toPlainText()

        if useCustomText == '':
            txt_file = "combs"
        else:
            txt_file = useCustomText

        settings = pwgen.Settings(txt_file)

        final_combs = []

        chrs = 'abcdefghijklmnopqrstuvwxyz'

        if IncNumsInWL == 2:
            chrs += '1234567890'
        elif customList != '':
            chrs = customList
        elif extendList != '':
            chrs += extendList

        final_combs = settings.LeetCombo(customWord, IncLeet, final_combs)
        final_combs = settings.WordCombos(MinComboLen, MaxComboLen, chrs, IncWL, final_combs)
        
        if prefixText != '':
            prefix = [prefixText]        
            final_combs = settings.AddPrefix(prefix, final_combs, IncComboPS, 2)
        
        if addWLPre == 2:
            prefix = settings.WordCombos(MinComboLen, MaxComboLen, chrs, 2, [])
            print(prefix)
            IncComboPS = 0
            final_combs = settings.AddPrefix(prefix, final_combs, IncComboPS, 2)
        
        if suffixText != '':
            suffix = [suffixText]
            final_combs = settings.AddSuffix(suffix, final_combs, IncComboPS, 2)
        
        if addWLSuf == 2:
            suffix = settings.WordCombos(MinComboLen, MaxComboLen, chrs, 2, [])
            IncComboPS = 0
            final_combs = settings.AddSuffix(suffix, final_combs, IncComboPS, 2)

        final_combs = settings.AddNumPrefix(prefixMinNumLen, prefixNumLen, final_combs, IncNumsPre)
        final_combs = settings.AddNumSuffix(suffixMinNumLen, suffixNumLen, final_combs, IncNumsSuff)
        
        settings.WritePass(final_combs)

        print("Added Combinations")


    def help_show(self):
        '''
        help_show [Shows the main window]
        '''

        self.window = QtWidgets.QMainWindow()
        self.ui =  MainWindow.Ui_PasswordGenerator()
        self.ui.setupUi(self.window)
        self.ui.pushButton.clicked.connect(self.show_help)
        self.ui.GenerateButton.clicked.connect(self.after_click)

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

