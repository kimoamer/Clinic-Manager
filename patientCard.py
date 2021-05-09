from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QWidget
from paticard import Ui_Form as paticar


class listwidget(QWidget, paticar):
    def __init__(self):
        super(listwidget, self).__init__()
        QWidget.__init__(self)
        self.setupUi(self)
        self.font = QFont("Tajawal", 10)
        self.logofont = QFont('Crimson Text', 15)
        self.fonts()

    def fonts(self):
        self.hagz.setFont(self.font)
        self.tarekh.setFont(self.font)