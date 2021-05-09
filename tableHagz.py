from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QWidget,QGraphicsDropShadowEffect
from PyQt5.QtCore import pyqtSignal
import win32clipboard
from tableone import Ui_Form as tabone

class tableOne(QWidget, tabone):
    clicked = pyqtSignal()
    def __init__(self):
        super(tableOne, self).__init__()
        QWidget.__init__(self)
        self.setupUi(self)
        self.toolButton.clicked.connect(self.copyToClib)
        self.infobox.setHidden(False)
        self.line.setHidden(False)
        self.showAndHide()
        self.ezhar.clicked.connect(self.showAndHide)
        self.ezhar.clicked.connect(self.clicked)
        self.fon = QFont('Lato',10)
        self.pho = QFont('Fulbo Argenta', 10)
        self.fo = QFont('Almarai', 11)
        self.fonn = QFont('Almarai', 8)
        self.fonn.setBold(True)
        self.font = QFont("Tajawal", 11)
        self.font1 = QFont("Tajawal", 10)
        self.fontAll()
        self.setShadow()

    def setShadow(self):
        lis = [self.groupBox2,self.groupBox6,self.groupBox4,self.groupBox3,self.groupBox7,self.groupBox5]
        for i in lis:
            shadow = QGraphicsDropShadowEffect(blurRadius=3, xOffset=0, yOffset=0)
            i.setGraphicsEffect(shadow)

    def fontAll(self):
        self.rakm.setFont(self.fon)
        self.wakt.setFont(self.fon)
        self.esm.setFont(self.fo)
        self.moak.setFont(self.font)
        self.hagz.setFont(self.font1)
        self.paid.setFont(self.font1)
        self.money.setFont(self.fon)
        self.cost.setFont(self.fon)
        self.tyhagz.setFont(self.font1)
        self.phone.setFont(self.pho)
        self.label.setFont(self.font1)
        self.label3.setFont(self.font1)
        self.label2.setFont(self.font1)
        self.label6.setFont(self.font1)
        self.label11.setFont(self.font1)
        self.label4.setFont(self.font1)
        self.label62.setFont(self.font1)
        self.label8.setFont(self.font1)
        self.bpressure.setFont(self.fon)
        self.height.setFont(self.fon)
        self.diabetes.setFont(self.fon)
        self.weight.setFont(self.fon)
        self.lblood.setFont(self.fon)
        self.temp.setFont(self.fon)
        self.hala.setFont(self.fonn)
        self.groupBox.setFont(self.font1)

    def copyToClib(self):
        s = self.tareef.text()
        try:
            win32clipboard.OpenClipboard()
            win32clipboard.EmptyClipboard()
            win32clipboard.SetClipboardText(s)
            win32clipboard.CloseClipboard()
        except:
            print('Could not copy clipboard data.')

    def showAndHide(self):
        if self.infobox.isHidden() == False :
            self.ezhar.setText('التفاصيل')
            self.infobox.setHidden(True)
            self.line.setHidden(True)
        else:
            self.ezhar.setText('إخفاء')
            self.infobox.setHidden(False)
            self.line.setHidden(False)
