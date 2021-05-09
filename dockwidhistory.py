from PyQt5.QtWidgets import QDialog
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
from dockwina import Ui_Form as docka

class Dialog(QDialog, docka):
    def __init__(self):
        super(Dialog, self).__init__()
        QDialog.__init__(self)
        self.setupUi(self)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.font1 = QFont("Tajawal", 9)
        self.label2.setFont(self.font1)
        self.label7.setFont(self.font1)
        self.label3.setFont(self.font1)
        self.label5.setFont(self.font1)
        self.label6.setFont(self.font1)
        self.label.setFont(self.font1)
