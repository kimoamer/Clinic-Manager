from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QWidget
from patlist import Ui_Form as patlis

class listwidget(QWidget, patlis):
    def __init__(self):
        super(listwidget, self).__init__()
        QWidget.__init__(self)
        self.setupUi(self)
        font = QFont("Tajawal", 9)
        self.patName.setFont(font)
