import sys
from PyQt5.QtWidgets import QApplication

from latihan2 import *
if __name__ =='__main__':
    a = QApplication(sys.argv)
    minform = latihan2()
    minform.show()
    a.exec_()
