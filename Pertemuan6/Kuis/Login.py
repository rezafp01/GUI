import sys

from PyQt5.QtGui import*
from PyQt5.QtCore import*
from PyQt5.QtWidgets import*
from Pendaftaran import *

class Login(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi()

    def setupUi(self):
        self.resize(250,80)
        self.move(400,200)
        self.setWindowTitle('Kuis Pemrograman GUI ')

        self.label1 = QLabel('Username')
        self.edit1 = QLineEdit()

        self.label2 = QLabel('Password')
        self.edit2 = QLineEdit()
        self.edit2.setEchoMode(QLineEdit.Password)

        self.button1 = QPushButton('Login')
        self.button2 = QPushButton('Clear')

        layout = QGridLayout()
        layout.addWidget(self.label1, 0,0)
        layout.addWidget(self.edit1, 0,1,1,2)
        layout.addWidget(self.label2, 1,0)
        layout.addWidget(self.edit2, 1,1,1,2)
        layout.addWidget(self.button1,2,1,1,1)
        layout.addWidget(self.button2,2,2)
        self.setLayout(layout)


        self.button1.setParent(self)
        self.button1.clicked.connect(self.button1Click)
        self.button2.clicked.connect(self.button2Click)

    def button1Click(self):
        user = self.edit1.text()
        pw = self.edit2.text()

        if not user or not pw :
            QMessageBox.information(self,'Perhatian','Username atau password tidak boleh kosong')
        else:
            if user == '17104014' and pw =='reza':
                self.form = Pendaftaran()
                self.form.show()
                self.close()
            else:
                QMessageBox.information(self,'Perhatian','Username atau password Salah')


    def button2Click(self):
        self.edit1.clear()
        self.edit2.clear()

if __name__ == '__main__':
     a = QApplication(sys.argv)

     form = Login()
     form.show()

     a.exec_()
