from PyQt5.QtWidgets import QWidget, QLabel, QApplication

class latihan2(QWidget):
    def __init__(self):
        super(latihan2, self).__init__()
        self.setupUi()

    def setupUi(self):
        self.resize(400, 200)
        self.move(300, 300)
        self.setWindowTitle('Implementasi Tag HTML')

        self.label = QLabel('<h1>Rekayasa<font color = red> Perangkat</font><font color = blue> Lunak</font></h1>')
        self.label.move(10, 10)
        self.label.setParent(self)

        self.label2 = QLabel('<h3>Peserta Praktikum Pemrograman GUI</h3>')
        self.label2.move(10, 50)
        self.label2.setParent(self)

        self.label3 = QLabel('\t1. Monkey D. Luffy \n\t2. Roronoa Zoro \n\t3. Sanji Vinsmoke')
        self.label3.setWordWrap(True)
        self.label3.move(10, 70)
        self.label3.setParent(self)
