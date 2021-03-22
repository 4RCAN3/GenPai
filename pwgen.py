from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QHBoxLayout
from itertools import product
import sys
import test



class Settings():

    def __init__(self):
        pass
    

    def LeetCombo(self, password):

        leet = ["A4a","Bb8","Cc", "Dd","Ee3","Ff","Gg6","Hh","Ii","Jj","Kk",
        "Ll","Mm","Nn","Oo0","Pp","Qq","Rr","Ss5","Tt","Uu","Vv",
        "Ww","Xx","Yy","Zz2"]
        
        getPlaces = lambda word: [leet[ord(el.upper()) - 65] for el in word]
        
        all_combs = []
        words = password.split(" ")
        for count, word in enumerate(words):
            for letters in product(*getPlaces(word)):
                words[count] = "".join(letters)
                all_combs.append(" ".join(i for i in words))
        
        return all_combs

    def WordCombos(self, min, max):
        combos = []
        chrs = 'ab'
        min_length, max_length = min, max    
        for n in range(min_length, max_length+1):
            for xs in product(chrs, repeat=n):
                combos.append(''.join(xs))
        
        return combos

    def WritePass(self, combos):
        with open("combs.txt", 'w') as data:
            for word in combos:
                data.write(word + '\n')
            data.close()



class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.setGeometry(200, 200, 300, 300)
        self.setWindowTitle(
            "Password Generator"
        )

        self.RadioButton()
    
    def RadioButton(self):
        layout = QHBoxLayout()
        self.radio = QtWidgets.QRadioButton("Button 1")
        self.radio.setChecked(True)
        self.radio.toggled.connect(self.clicked)
        layout.addWidget(self.radio)
    
    def clicked(self):
        self.label.setText(
            "Clicked"
            )
        self.update()

    def update(self):
        self.label.adjustSize()


def window():
    app = QApplication(sys.argv)
    wind = QMainWindow.setWindowTitle("PWgen")
    win = test.Ui_MainWindow()
    win.setupUi(wind)
    sys.exit(app.exec_())

