from PyQt5.QtWidgets import QDialog,QHeaderView,QGraphicsDropShadowEffect,QPushButton,QTableWidgetItem
from PyQt5.QtCore import Qt,QDateTime,QRegExp
from PyQt5.QtGui import QFont,QIcon,QRegExpValidator
from adddialog import Ui_Dialog as editdailog

class Dialog(QDialog, editdailog):
    def __init__(self):
        super(Dialog, self).__init__()
        QDialog.__init__(self)
        self.setupUi(self)
        self.handleprocess()
        self.tabWidget.tabBar().setVisible(False)
        self.hideWidget()
        self.onrun()
        self.numfont = QFont("CrashNumberingGothic", 20)
        self.font1 = QFont("Tajawal", 12)
        self.font2 = QFont("Tajawal", 10)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        shadow = QGraphicsDropShadowEffect(blurRadius=8, xOffset=0, yOffset=0)
        self.maingroup.setGraphicsEffect(shadow)
        self.setfont()
        self.sumall.setFont(self.numfont)
        self.allsum.setFont(self.numfont)
        self.setShadow()
        self.moaddateEdit.setDateTime(QDateTime.currentDateTime())
        self.savebtn.setEnabled(True)



    def setfont(self):
        self.radiokashf.setFont(self.font1)
        self.radioest.setFont(self.font1)
        self.priceb.setFont(self.font1)
        self.labelpainfo.setFont(self.font2)
        self.labelpatdata.setFont(self.font2)
        self.adad.setFont(self.font2)
        self.egmaly.setFont(self.font2)
        self.labelpatientname.setFont(self.font2)
        self.labelage.setFont(self.font2)
        self.labelgender.setFont(self.font2)
        self.labelhala.setFont(self.font2)
        self.labelphone.setFont(self.font2)
        self.labeladdress.setFont(self.font2)
        self.labelheight.setFont(self.font2)
        self.labelweight.setFont(self.font2)
        self.labelsuger.setFont(self.font2)
        self.labelpressure.setFont(self.font2)
        self.label9.setFont(self.font2)
        self.label14.setFont(self.font2)
        self.label20.setFont(self.font2)
        self.hagzway.setFont(self.font2)
        self.mosbkdaf.setFont(self.font2)
        self.takedhagz.setFont(self.font2)
        self.labelerror.setFont(self.font2)

    def checkViewbtn(self):
        if self.hide.isChecked():
            self.view.setChecked(True)
            self.tabWidget.setCurrentIndex(0)
            self.hide.setChecked(False)
            self.onoff.setStyleSheet('QGroupBox{background-color:#f93537;border-radius:15px;border:0px;}')
        else:
            self.view.setChecked(False)
            self.tabWidget.setCurrentIndex(1)
            self.hide.setChecked(True)
            self.onoff.setStyleSheet('QGroupBox{background-color:#35bb40;border-radius:15px;border:0px;}')

    def checkHidebtnn(self):
        if self.view.isChecked():
            self.view.setChecked(False)
            self.tabWidget.setCurrentIndex(1)
            self.hide.setChecked(True)
            self.onoff.setStyleSheet('QGroupBox{background-color:#35bb40;border-radius:15px;border:0px;}')
        else:
            self.view.setChecked(True)
            self.tabWidget.setCurrentIndex(0)
            self.hide.setChecked(False)
            self.onoff.setStyleSheet('QGroupBox{background-color:#f93537;border-radius:15px;border:0px;}')

    def setShadow(self):
        lis = [self.mokhass]
        for i in lis:
            shadow = QGraphicsDropShadowEffect(blurRadius=8, xOffset=0, yOffset=0)
            i.setGraphicsEffect(shadow)

    def hideWidget(self):
        if self.priceb.isChecked() == False:
            self.view.setChecked(True)
            self.hide.setChecked(False)
            self.onoff.setStyleSheet('QGroupBox{background-color:#f93537;border-radius:15px;border:0px;}QGroupBox:disabled{background-color:rgb(194, 194, 194);}')
            self.tabWidget.setCurrentIndex(0)
        else:
            self.view.setChecked(False)
            self.hide.setChecked(True)
            self.onoff.setStyleSheet('QGroupBox{background-color:#35bb40;border-radius:15px;border:0px;}QGroupBox:disabled{background-color:rgb(194, 194, 194);}')
            self.tabWidget.setCurrentIndex(1)

    def showmokhass(self):
        self.tabWidget.setCurrentIndex(1)
        self.view.setHidden(True)
        self.hide.setHidden(False)

    def hidemokhass(self):
        self.tabWidget.setCurrentIndex(0)
        self.view.setHidden(False)
        self.hide.setHidden(True)

    def handleprocess(self):
        self.cancelbtn.clicked.connect(self.terminate)
        self.addbutton.clicked.connect(self.addrow)
        self.priceb.toggled.connect(self.hideWidget)
        self.view.clicked.connect(self.checkViewbtn)
        self.hide.clicked.connect(self.checkHidebtnn)



    def addrow(self):
        if self.sanf.text() == '':
            pass
        else:
            shadow = QGraphicsDropShadowEffect(blurRadius=8, xOffset=0, yOffset=0)
            self.remove = QPushButton('')
            self.remove.setIcon(QIcon(":/MainSources/delete.png"))
            self.remove.clicked.connect(self.removerow)
            self.rows = self.pricetable.rowCount()
            self.pricetable.insertRow(self.rows)
            self.pricetable.setItem(self.rows,0,QTableWidgetItem(str(self.sanf.text())))
            self.pricetable.setItem(self.rows, 1, QTableWidgetItem(str(self.sanfprice.value())))
            self.pricetable.setCellWidget(self.rows,2,self.remove)
            self.pricetable.setGraphicsEffect(shadow)
            self.sanf.setText('')
            self.sanfprice.setValue(0)
            self.sumdata()
            self.rowcountlabel.setText(str(self.pricetable.rowCount()))

    def removerow(self):
        self.pricetable.removeRow(self.pricetable.currentRow())
        self.pricetable.repaint()
        rows = self.pricetable.rowCount()
        self.rowcountlabel.setText(str(rows))
        self.sumdata()

    def sumdata(self):
        lis = []
        rows = self.pricetable.rowCount()
        for i in range(rows):
            x = float(self.pricetable.item(i,1).text())
            lis.append(x)
        self.sumall.setText(str(sum(map(float,lis))))
        self.allsum.setText(str(sum(map(float,lis))))

    def onrun(self):
        self.pricetable.horizontalHeader().setSectionResizeMode(0, QHeaderView.Stretch)
        self.pricetable.setColumnWidth(1,60)
        self.pricetable.setColumnWidth(2,30)
        self.pricetable.setColumnHidden(3,True)
        self.complet.setHidden(True)
        self.trago.setHidden(True)
        self.labelerror.setHidden(True)
        validator = QRegExpValidator(QRegExp(r'^[ا-يؤئء]*$'))
        vald = QRegExpValidator(QRegExp(r'^[ ا-يؤئء]*$'))
        self.previewname.setValidator(vald)
        self.lPatientName.setValidator(validator)
        self.flPatientName.setValidator(validator)
        self.sPatientName.setValidator(validator)
        self.fPatientName.setValidator(validator)

    def terminate(self):
        self.previewname.setText('')
        self.lPatientName.setText('')
        self.flPatientName.setText('')
        self.sPatientName.setText('')
        self.fPatientName.setText('')
        self.lPhone.setText('')
        self.lAddress.setText('')
        self.allsum.setText('0')
        self.rowcountlabel.setText('0')
        self.sumall.setText('0')
        self.sAge.setValue(1)
        self.cgender.setCurrentIndex(0)
        self.social.setCurrentIndex(0)
        self.pricetable.setRowCount(0)
        self.radiokashf.setChecked(True)
        self.priceb.setChecked(False)
        self.heightSpinBox.setValue(0)
        self.weightSpinBox.setValue(0)
        self.sugerSpinBox.setValue(0)
        self.highSpinBox.setValue(0)
        self.lowSpinBox.setValue(0)
        self.waycomboBox.setCurrentIndex(0)
        self.moadtime.setCurrentIndex(0)
        self.pricekashf.setCurrentIndex(0)
        self.priceest.setCurrentIndex(0)
        self.moaddateEdit.setDateTime(QDateTime.currentDateTime())
        self.repaint()
        self.accept()
