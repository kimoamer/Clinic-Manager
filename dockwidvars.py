from PyQt5.QtWidgets import QDialog,QHeaderView,QApplication
from PyQt5.QtGui import QFont,QRegExpValidator
from PyQt5.QtCore import Qt,QRegExp
from dockwinb import Ui_Form as dockb

class Dialog(QDialog, dockb):
    def __init__(self):
        super(Dialog, self).__init__()
        QDialog.__init__(self)
        self.setupUi(self)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.varsstable.setColumnWidth(0,100)
        self.varsstable.horizontalHeader().setSectionResizeMode(1, QHeaderView.Stretch)
        self.varsstable.horizontalHeader().setSectionResizeMode(2, QHeaderView.Stretch)
        self.varsstable.setColumnWidth(3,0)
        self.varsstable.setColumnWidth(4,40)
        self.varsstable.setColumnHidden(3, True)
        self.font1 = QFont("Tajawal", 10)
        self.tabWidgetmoaml.setFont(self.font1)
        self.varsstable.horizontalHeader().setFont(self.font1)
        validator = QRegExpValidator(QRegExp('-?\d{0,20}(?:\.\d{0,20})?'))
        self.patientvarss.setValidator(validator)
        self.varsshigh.setValidator(validator)
        self.varsslow.setValidator(validator)
        self.patientvarss2.setValidator(validator)