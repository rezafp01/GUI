from PyQt5.QtGui import*
from PyQt5.QtCore import*
from PyQt5.QtWidgets import*

class Pendaftaran(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi()

    def setupUi(self):
        self.resize(300, 200)
        self.move(400, 200)
        self.setWindowTitle('Form Pendaftaran')
        self.label1 = QLabel('<b>Pendaftaran Calon Anggota Avengers</b>')
        self.label2 = QLabel('Nama')
        self.edit1 = QLineEdit()

        self.label3 = QLabel('Jenis Kelamin')
        self.radio1 = QRadioButton()
        self.radio1.setText('Laki-Laki')
        self.radio1.setChecked(True)
        self.radio2 = QRadioButton()
        self.radio2.setText('Perempuan')

        self.label4 = QLabel('Tanggal Lahir')
        self.date = QDateEdit()
        self.date.setDisplayFormat('dd/MM/yyyy')

        self.label5 = QLabel('Hobi')
        self.combo = QComboBox()
        self.combo.addItem('basket')
        self.combo.addItem('sepak bola')
        self.combo.addItem('voli')
        self.combo.addItem('catur')
        self.combo.addItem('lainny')

        self.label6 = QLabel('Alamat')
        self.text = QTextEdit()

        self.button1 = QPushButton('Submit')
        self.button2 = QPushButton('Cancel')

        layout = QGridLayout()
        layout.addWidget(self.label1,0,1,1,2)
        layout.addWidget(self.label2, 1,0)
        layout.addWidget(self.edit1,  1,1,1,2)
        layout.addWidget(self.label3, 2,0)
        layout.addWidget(self.radio1, 2,1,1,2)
        layout.addWidget(self.radio2, 3,1,1,2)
        layout.addWidget(self.label4, 4,0)
        layout.addWidget(self.date,   4,1,1,2)
        layout.addWidget(self.label5, 5,0)
        layout.addWidget(self.combo,  5,1,1,2)
        layout.addWidget(self.label6, 6,0)
        layout.addWidget(self.text,   6,1,1,2)
        layout.addWidget(self.button1,7,1,1,1)
        layout.addWidget(self.button2,7,2)
        self.setLayout(layout)

        self.button1.clicked.connect(self.CSubmit)
        self.button2.clicked.connect(self.CCancel)

    def CSubmit(self):
        nama = str(self.edit1.text())
        tlahir = str(self.date.date().toString())
        hobi = str(self.combo.currentText())
        alamat = str(self.text.toPlainText())

        if self.radio1.isChecked():
                QMessageBox.information(self, 'Pendaftaran Berhasil',
                'Nama :' + nama +'\n'+
                'Jenis Kelamin : Laki Laki' + '\n'+
                'Tanggal Lahir :' +tlahir + '\n'+
                'Hobi :'+ hobi +'\n'+
                'Alamat :' +alamat +'\n' )
        else:
                QMessageBox.information(self, 'Pendaftaran Berhasil',
                'Nama :' + nama +'\n'+
                'Jenis Kelamin : Perempuan' + '\n'+
                'Tanggal Lahir :' +tlahir + '\n'+
                'Hobi :' + hobi +'\n'+
                'Alamat :' +alamat +'\n' )

    def CCancel(self):
        self.close()
