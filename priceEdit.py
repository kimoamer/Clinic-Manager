from PyQt5.QtWidgets import QDialog,QGraphicsDropShadowEffect
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from priceeditd import Ui_Dialog as priceedit

class Dialog(QDialog, priceedit):
    def __init__(self):
        super(Dialog, self).__init__()
        QDialog.__init__(self)
        self.setupUi(self)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.shadow = QGraphicsDropShadowEffect(blurRadius=8, xOffset=0, yOffset=0)
        self.groupBox_3.setGraphicsEffect(self.shadow)
        self.font1 = QFont("Tajawal", 10)
        self.font2 = QFont("Tajawal", 9)
        self.groupBox.setFont(self.font1)
        self.label.setFont(self.font2)
        self.label_4.setFont(self.font2)
        self.label_3.setFont(self.font2)
        self.label_2.setFont(self.font2)
        self.label_7.setFont(self.font2)
        self.label_8.setFont(self.font2)
        self.label_6.setFont(self.font2)
        self.label_5.setFont(self.font2)
        self.groupBox_2.setFont(self.font1)
