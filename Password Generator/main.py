from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import sys, random, string

lower = string.ascii_lowercase
upper = string.ascii_uppercase
num   = string.digits
symbols = string.punctuation


class PasswordGenerator(QMainWindow):
    
    def __init__(self):
        super().__init__()
        self.top = 600
        self.left = 100
        self.height=250
        self.width = 360
        self.UI_init()
        
        
    def UI_init(self):
        
        self.Mainlabel = QLabel(self)
        self.Mainlabel.setText('Password Generator')
        self.Mainlabel.setAlignment(Qt.AlignCenter)
        self.Mainlabel.setFont(QFont('Arial', 15))
        self.Mainlabel.setGeometry(QRect(80, 10, 200, 20))
        
        self.Lengthlabel = QLabel(self)
        self.Lengthlabel.setText('Enter Length')
        self.Lengthlabel.setFont(QFont('Arial', 9))
        self.Lengthlabel.setGeometry(QRect(40, 50, 80, 15))
        
        self.pass_len=QLineEdit(self)
        self.pass_len.setGeometry(QRect(40, 70, 130, 20))
        self.pass_len.setValidator(QIntValidator(1,99,self))
        
        self.radioWeak=QRadioButton(self)
        self.radioWeak.setGeometry(QRect(250, 60, 80, 15))
        self.radioWeak.setText('Weak')
        self.radioWeak.setChecked(True)
        
        self.radioMedium=QRadioButton(self)
        self.radioMedium.setGeometry(QRect(250, 90, 80, 15))
        self.radioMedium.setText('Medium')
        
        self.radioStrong=QRadioButton(self)
        self.radioStrong.setGeometry(QRect(250, 120, 80, 15))
        self.radioStrong.setText('Strong')
        
        self.PassLabel = QLabel(self)
        self.PassLabel.setFont(QFont('Arial', 9))
        self.PassLabel.setGeometry(QRect(40, 120, 160, 20))
        self.PassLabel.setText('Password Generated')
        
        self.Pass_gen = QLineEdit(self)
        self.Pass_gen.setGeometry(QRect(40, 140, 160, 20))
        self.Pass_gen.setReadOnly(True)
        
        self.StateLabel = QLabel(self)
        self.StateLabel.setGeometry(QRect(40, 160, 160, 20))
        #self.StateLabel.setText('Password Generated')
        
        
        
        self.generate_button = QPushButton(self)
        self.generate_button.setGeometry(QRect(70, 200, 75, 20))
        self.generate_button.setText('Generate')
        self.generate_button.clicked.connect(self.generate_password)
        
        self.exit_button = QPushButton(self)
        self.exit_button.setGeometry(QRect(215, 200, 75, 20))
        self.exit_button.setText('Exit')
        self.exit_button.clicked.connect(self.gui_exit)
        
        self.copy_button = QPushButton(self)
        self.copy_button.setIcon(QIcon('Password Generator\copy.png'))  # Replace 'icon.png' with your image file
        self.copy_button.setIconSize(self.copy_button.sizeHint())  # Set icon size to button size
        self.copy_button.setGeometry(QRect(210, 130, 30, 30))
        #self.copy_button.setText('copy')
        self.copy_button.clicked.connect(self.copyPassword)

        
        self.title = 'Password Generator'
        
        self.setWindowTitle(self.title)
        self.setGeometry(self.top, self.left, self.width, self.height)
        self.show()
        
    def gui_exit(self):
        sys.exit()
        
        
    def check_radio(self):
        if self.radioWeak.isChecked():
            chars = lower
        elif self.radioMedium.isChecked():
            chars = lower + upper
        elif self.radioStrong.isChecked():
            chars = lower + upper + num + symbols
            
        return chars
        
        
    def generate_password(self):
        
        pass_cur = ""
        number = int(self.pass_len.text())
        chars = self.check_radio()
        self.StateLabel.setText('')
        
        pass_cur += ''.join(random.sample(chars, number))
        self.pass_cur = pass_cur  # Store pass_cur as an instance attribute
        self.Pass_gen.setText(pass_cur)
        
        
    def copyPassword(self):
        if hasattr(self, 'pass_cur') and self.pass_cur:  # Check if pass_cur is defined
            clipboard = QApplication.clipboard()
            clipboard.setText(self.pass_cur)
            self.StateLabel.setText('Password is copied to clipboard')
        else:
            self.StateLabel.setText('Please, Generate a Password !!!!')
        
        
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = PasswordGenerator()
    sys.exit(app.exec_())