from PyQt5.QtWidgets import QGraphicsDropShadowEffect,QDialog
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from massage import Ui_Dialog as dialog


class Dialog(QDialog, dialog):
    def __init__(self):
        super(Dialog, self).__init__()
        QDialog.__init__(self)
        self.setupUi(self)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        shadow = QGraphicsDropShadowEffect(blurRadius=8, xOffset=0, yOffset=0)
        self.groupBox.setGraphicsEffect(shadow)
        self.font1 = QFont("Tajawal", 12)
        self.font2 = QFont("Tajawal", 10)
        self.fonts()


    def fonts(self):
        self.title.setFont(self.font1)
        self.massage.setFont(self.font2)
        self.okbtn.setFont(self.font2)
        self.nobtn.setFont(self.font2)

