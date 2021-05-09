from PyQt5.QtWidgets import (QMainWindow ,QDockWidget ,QGraphicsDropShadowEffect ,QPushButton ,QTableWidgetItem ,QCompleter ,QInputDialog ,QHBoxLayout ,QListWidgetItem,QMessageBox,QHeaderView,QLineEdit,QLabel,QFileDialog,QGraphicsPixmapItem,QGraphicsScene,QFrame,QSizePolicy,QGraphicsOpacityEffect,QApplication,QStyle,QVBoxLayout,QGroupBox,QToolButton)
from PyQt5.QtCore import (QPropertyAnimation,QMarginsF,Qt,QSettings,QDate,QDateTime,QPoint,QRegExp,QRect,QUrl,QProcess,pyqtSignal,QTimer,QPropertyAnimation,QEvent,QRectF,QSize,QThread)
from PyQt5.QtGui import (QRegExpValidator,QWindow,QBrush,QPageSize,QPageLayout,QIcon,QFont,QPixmap,QPainter,QColor,QMovie,QImage,QPainterPath,QTransform,QRegion,QCursor)
from man import Ui_MainWindow as mainn
from PyQt5.QtChart import QChart,QSplineSeries,QChartView,QValueAxis,QDateTimeAxis
from PyQt5.QtMultimedia import QSound
from jinja2 import FileSystemLoader, Environment
import os
import codecs
import mysql.connector
import newDialog
import editDialog
import priceEdit
import patientListWidget
import tableHagz
import patientCard
from os import path
from datetime import datetime, timedelta, date
import qrcode
import dockwidhistory
import dockwidvars
import socket
from threading import Thread
import win32con
import win32event
import win32process
from win32com.shell import shellcon
import win32com.shell.shell as shell
from PyQt5.QtWebEngineWidgets import QWebEngineView
import printPreview
import smulatorModule
import fitz
from bs4 import BeautifulSoup
import customMassage
import re
import sys


threadactive = True
dbbc = True
posit = []
locat = [0,1,2,3,4,5,6,7,8,9,10]
size = None
connn = None
mySQL80 = False
connect = None
dbconnect = None
dbcur = None
done = None

class Main(QMainWindow, mainn):
    def __init__(self,width,height,parent=None):
        super(Main, self).__init__(parent)
        QMainWindow.__init__(self)
        self.setupUi(self)
        global done
        self.widt = width
        self.heigh = height
        self.setWindowTitle("Doctor Clinic")
        self.setWindowIcon(QIcon('MainSources\DC.png'))
        self.tabWidget.tabBar().setVisible(False)
        self.settingstablewidget.tabBar().setVisible(False)
        self.tabWidgetvals.tabBar().setVisible(False)
        self.ttaskWidget.tabBar().setVisible(False)
        self.url.setHidden(True)
        self.enablebtn()
        self.set = QSettings('DoctorClinic', 'Main')
        self.addform = newDialog.Dialog()
        self.priceedit = priceEdit.Dialog()
        self.edit = editDialog.Dialog()
        self.dwid = dockwidhistory.Dialog()
        self.dvars = dockwidvars.Dialog()
        self.pPreview = printPreview.printpreviewme()
        self.smu = smulatorModule.Dialog()
        self.massage = customMassage.Dialog()
        self.roshPreviw = None
        self.tash = None
        self.handelbuttons()
        self.logofont = QFont('Crimson Text',15)
        self.font = QFont("Tajawal", 11)
        self.font1 = QFont("Tajawal", 9)
        self.font2 = QFont("Tajawal", 9)
        self.ont = QFont('Almarai', 10)
        self.onto = QFont('Almarai', 12)
        self.onto.setBold(True)
        self.fontsett = QFont("Samim", 9)
        self.fontlo = QFont("Samim", 12)
        self.ffont = QFont()
        self.fonts()
        self.historydock = QDockWidget("بيان", self, flags=Qt.Window)
        self.historydock.setWidget(self.dwid)
        self.historydock.setGeometry(150, 130, 300, 200)
        self.vardock = QDockWidget('إضافة قيم المعامل',self,flags=Qt.Window)
        self.vardock.setWidget(self.dvars)
        self.vardock.setGeometry(450, 330, 300, 200)
        self.taskid.setHidden(True)
        self.scrollAreapatient.setWidgetResizable(True)
        self.createChart()
        done = True

    def resolution(self):
        if self.widt == 1280:
            self.showMaximized()
        else:
            self.setMaximumHeight(self.heigh)
            self.setMaximumWidth(self.widt-40)

    def checkPatientExist(self):
        if self.patientlistWidget.count() != 0:
            self.patientlistWidget.setCurrentRow(self.patientlistWidget.count() - 1)
            self.exist = None
        else:
            self.exist = 'exist'

    def fonts(self):
        try:
            self.smokebox.setFont(self.ont)
            self.type1.setFont(self.ont)
            self.alcoholbox.setFont(self.ont)
            self.type2.setFont(self.ont)
            self.anemiabox.setFont(self.ont)
            self.otherbox.setFont(self.ont)
            self.label.setFont(self.font)
            self.label_2.setFont(self.font)
            self.label_3.setFont(self.font)
            self.label_4.setFont(self.font)
            self.label_5.setFont(self.font)
            self.logo1.setFont(self.font)
            self.lcdNumber.setFont(self.logofont)
            self.lcdNumberk.setFont(self.logofont)
            self.lcdNumbere.setFont(self.logofont)
            self.lcdNumberv.setFont(self.logofont)
            self.lcdNumberr.setFont(self.logofont)
            self.esttablewidget.horizontalHeader().setFont(self.font1)
            self.doctable.horizontalHeader().setFont(self.font1)
            self.addbtnvarss.setFont(self.font1)
            self.costbtn.setFont(self.font1)
            self.listWidget.setFont(self.font)
            self.newadd.setFont(self.font1)
            self.edittabbtn.setFont(self.font1)
            self.todoctorli.setFont(self.font1)
            self.pay.setFont(self.font1)
            self.delbtn.setFont(self.font1)
            self.towaiting.setFont(self.font1)
            self.exambtn.setFont(self.font1)
            self.continuetash.setFont(self.font1)
            self.db1connect.setFont(self.font2)
            self.db1disconnect.setFont(self.font2)
            self.db2connect.setFont(self.font2)
            self.db2disconnect.setFont(self.font2)
            self.pcconnect.setFont(self.font2)
            self.pcdisconnect.setFont(self.font2)
            self.settingslistwidget.setFont(self.font1)
            self.getimg.setFont(self.font)
            self.removeimg.setFont(self.font)
            self.setGroupbox.setFont(self.font)
            self.groupBoxtasmem.setFont(self.font)
            self.infoset.setFont(self.font2)
            self.nameclinic.setFont(self.font1)
            self.eyadamoad.setFont(self.font1)
            self.menn.setFont(self.font1)
            self.elaa.setFont(self.font1)
            self.galsa.setFont(self.font1)
            self.dekeka.setFont(self.font1)
            self.wda.setFont(self.font1)
            self.asha.setFont(self.font1)
            self.maipage.setFont(self.font1)
            self.typepp.setFont(self.font2)
            self.mainpageapp.setFont(self.font2)
            self.kapric.setFont(self.font1)
            self.espric.setFont(self.font1)
            self.editprice.setFont(self.font1)
            self.kashfprice.setFont(self.font1)
            self.estprice.setFont(self.font1)
            self.runonboot.setFont(self.font1)
            self.showerad.setFont(self.font1)
            self.selectloc.setFont(self.font1)
            self.creloc.setFont(self.font1)
            self.imploc.setFont(self.font1)
            self.saveloc.setFont(self.font1)
            self.createus.setFont(self.font1)
            self.autocreate.setFont(self.font1)
            self.imporsq.setFont(self.font1)
            self.mysql8ser.setFont(self.font1)
            self.my8check.setFont(self.font1)
            self.labelid.setFont(self.font1)
            self.labelname.setFont(self.font1)
            self.labeldate.setFont(self.font1)
            self.labelgender.setFont(self.font1)
            self.labelpaid.setFont(self.font1)
            self.labelage.setFont(self.font1)
            self.groupBox29.setFont(self.font)
            self.groupBox14.setFont(self.font)
            self.groupBox32.setFont(self.font)
            self.groupBox61.setFont(self.font)
            self.groupBox4.setFont(self.font)
            self.groupBox27.setFont(self.font)
            self.groupBox43.setFont(self.font)
            self.labelnc.setFont(self.font1)
            self.labeld2.setFont(self.font1)
            self.labelad.setFont(self.font1)
            self.labelcne.setFont(self.font1)
            self.labelde.setFont(self.font1)
            self.labelade.setFont(self.font1)
            self.labeladd.setFont(self.font1)
            self.labelpho.setFont(self.font1)
            self.labeltime.setFont(self.font1)
            self.labelsoical.setFont(self.font1)
            self.labelsavr.setFont(self.font1)
            self.labellocsa.setFont(self.font1)
            self.labelphr.setFont(self.font1)
            self.saveSettings.setFont(self.font1)
            self.saveroshset.setFont(self.font1)
            self.setlabel5.setFont(self.fontsett)
            self.setlabel6.setFont(self.fontsett)
            self.setlabel7.setFont(self.fontsett)
            self.setlabel8.setFont(self.fontsett)
            self.setlabel9.setFont(self.fontsett)
            self.setlabel10.setFont(self.fontsett)
            self.setlabel11.setFont(self.fontsett)
            self.setlabel12.setFont(self.fontsett)
            self.setlabel13.setFont(self.fontsett)
            self.setlabel14.setFont(self.fontsett)
            self.taskname.setFont(self.font)
            self.tahtitle.setFont(self.font)
            self.tashtag.setFont(self.font)
            self.ardtag.setFont(self.font)
            self.elag.setFont(self.font)
            self.taskshow.setFont(self.font)
            self.tahltag.setFont(self.font)
            self.notestag.setFont(self.font)
            self.dawa.setFont(self.font1)
            self.tkrar.setFont(self.font1)
            self.modah.setFont(self.font1)
            self.viewhagz.setFont(self.fontlo)
            self.addform.taglabel.setFont(self.font)
            self.label355.setFont(self.font1)
            self.label332.setFont(self.font1)
            self.label422.setFont(self.font1)
            self.label433.setFont(self.font1)
            self.label488.setFont(self.font1)
            self.label499.setFont(self.font1)
            self.label500.setFont(self.font1)
            self.label733.setFont(self.font1)
            self.label799.setFont(self.font1)
            self.assigned.setFont(self.font1)
            self.patienName.setFont(self.font)
            self.patienGender.setFont(self.ont)
            self.phopho.setFont(self.ont)
            self.addadd.setFont(self.ont)
            self.bpavg.setFont(self.font)
            self.tallweight.setFont(self.font)
            self.temprec.setFont(self.font)
            self.glucose.setFont(self.font)
            self.patienAge.setFont(self.ont)
            self.bpaverage.setFont(self.logofont)
            self.bmi.setFont(self.logofont)
            self.lastreco.setFont(self.logofont)
            self.bphigh.setFont(self.ont)
            self.tallheight.setFont(self.ont)
            self.wznweight.setFont(self.ont)
            self.bplow.setFont(self.ont)
            self.glustats.setFont(self.onto)
            self.lastrec.setFont(self.ont)
            self.recavg.setFont(self.ont)
            self.highrec.setFont(self.ont)
            self.lowrec.setFont(self.ont)
            self.groupBoxmaml.setFont(self.font1)
            self.groupBoxdwa.setFont(self.font1)
            self.groupBoxtashk.setFont(self.font1)
            self.groupBoxlogs.setFont(self.font1)
            self.labelvalue.setFont(self.font2)
            self.labellow.setFont(self.font2)
            self.labelhigh.setFont(self.font2)
            self.listWidgetvals.setFont(self.font1)
            self.label15.setFont(self.font)
            self.roshprev.setFont(self.font)
            self.saveandclose.setFont(self.font)
            self.closetash.setFont(self.font)
            self.activateserv.setFont(self.font1)
            self.loadstats.setFont(self.ont)
            self.namecolor.setFont(self.font1)
            self.nameinfocolor.setFont(self.font1)
            self.bordercolor.setFont(self.font1)
            self.topbgcolor.setFont(self.font1)
            self.iconcolor.setFont(self.font1)
            self.fontssize.setFont(self.font1)
            self.patinfofont.setFont(self.font2)
            self.medfont.setFont(self.font2)
            self.headfont.setFont(self.font2)
            self.timfont.setFont(self.font2)
            self.labelfonttype.setFont(self.font2)
            self.imagesandicons.setFont(self.font1)
            self.mainlines.setFont(self.font2)
            self.insiderosh.setFont(self.font2)
            self.bottomroshbg.setFont(self.font2)
            self.addressbg.setFont(self.font2)
            self.timebg.setFont(self.font2)
            self.docnamesize.setFont(self.font2)
            self.docinfosize.setFont(self.font2)
            self.mainlinessize.setFont(self.font2)
            self.mainlogo.setFont(self.font2)
            self.addressicon.setFont(self.font2)
            self.timeicon.setFont(self.font2)
            self.phoneicon.setFont(self.font2)
            self.attenicon.setFont(self.font2)
            self.tasmeme.setFont(self.font1)
            self.previewtestview.setFont(self.font1)
            self.soicalicon.setFont(self.font1)
            self.labelmedcounts.setFont(self.font1)
            self.labeltaskscounts.setFont(self.font1)
            self.throuhweek.setFont(self.ont)
            self.firsttime.setFont(self.ont)
            self.uniqueword.setFont(self.ont)
            self.defualtvalues.setFont(self.font1)
            self.previewtest.setFont(self.font1)
        except:
            self.saveErrors('Fonts Error')

    def showMassage(self,title,msg,order):
        self.massage.title.setText(title)
        self.massage.massage.setText(msg)
        self.massage.nobtn.clicked.connect(self.massage.close)
        self.massage.okbtn.clicked.connect(self.massage.accept)
        self.massage.okbtn.clicked.connect(order)
        self.massage.exec_()

    def saveErrors(self,err):
        with open("ErrorLogs.txt", "a", encoding='utf-8') as error:
            error.write(str(err)+'\n')
        self.checkMysql80()

    def chooseTab(self):
        if self.listWidget.currentRow() == 0:
            self.tabWidget.setCurrentIndex(0)
        elif self.listWidget.currentRow() == 1:
            self.tabWidget.setCurrentIndex(1)
        elif self.listWidget.currentRow() == 2:
            self.tabWidget.setCurrentIndex(2)
        elif self.listWidget.currentRow() == 3:
            self.tabWidget.setCurrentIndex(3)
        elif self.listWidget.currentRow() == 4:
            self.createPatientList()
        elif self.listWidget.currentRow() == 5:
            self.tabWidget.setCurrentIndex(5)

    def setShadow(self):
        lis = [self.groupBox_22,self.groupBox_24,self.ttaskWidget,self.groupBox_12,self.groupBox_16,self.groupBox_20,
               self.groupBox_31,self.doctable,self.chartView,self.previewtestview]
        for i in lis:
            shadow = QGraphicsDropShadowEffect(blurRadius=8, xOffset=0, yOffset=0)
            i.setGraphicsEffect(shadow)

    def setStyleformy8check(self):
        if self.my8check.text() == 'RUNNING':
            self.my8check.setStyleSheet('''QLineEdit{color:#21bf73;}''')
            self.databaseconnect()
        else:
            self.my8check.setStyleSheet('''QLineEdit{color:#ff4646;}''')
            self.hagzlistwid.clear()
            self.db1connect.setHidden(True)
            self.db1disconnect.setVisible(True)
            self.sqlstatus.setText('غير متصل')
            self.esttablewidget.setRowCount(0)
            self.esttablewidget.selectRow(-1)
            self.doctable.setRowCount(0)
            self.doctable.selectRow(-1)
            self.enablebtn()
            self.checkesttable()
            self.enbtntash()
            self.exist = 'exist'

    #دالة إضافة الاعراض
    def addarad(self):
        if self.arads.text() == '':
            self.showToaster('عفواً!', 'لا تترك الخانات فارغة.', ':/MainSources/close.gif', '#ec0101',
                             'MainSources/fail.wav', 1, 2000)
        else:
            shadow = QGraphicsDropShadowEffect(blurRadius=8, xOffset=0, yOffset=0)
            self.remove = QPushButton('')
            self.remove.setIcon(QIcon(":/MainSources/delete.png"))
            self.remove.clicked.connect(self.removerow)
            rows = self.tabarad.rowCount()
            self.tabarad.insertRow(rows)
            item = QTableWidgetItem(str(self.arads.text()))
            item.setTextAlignment(Qt.AlignCenter)
            self.tabarad.setItem(rows,0,item)
            self.tabarad.setCellWidget(rows,1,self.remove)
            self.tabarad.setGraphicsEffect(shadow)
            self.arads.setText('')

    def removerow(self):
        try:
            self.tabarad.removeRow(self.tabarad.currentRow())
            self.tabarad.repaint()
        except:
            self.saveErrors("Remove Arad Row Error")

    # دالة إضافة التحاليل
    def addtah(self):
        if self.tah1.text() == '':
            self.showToaster('عفواً!', 'لا تترك الخانات فارغة.', ':/MainSources/close.gif', '#ec0101',
                             'MainSources/fail.wav', 1, 2000)
        else:
            self.tahltag.setHidden(True)
            self.tabletah.setHidden(False)
            shadow = QGraphicsDropShadowEffect(blurRadius=8, xOffset=0, yOffset=0)
            rows = self.tabletah.rowCount()
            self.tabletah.insertRow(rows)
            self.remov = QPushButton('')
            self.remov.setIcon(QIcon(":/MainSources/delete.png"))
            self.remov.clicked.connect(self.removrow)
            item = QTableWidgetItem(str(self.tah1.text()))
            item.setTextAlignment(Qt.AlignCenter)
            self.tabletah.setItem(rows, 0, item)
            self.tabletah.setGraphicsEffect(shadow)
            self.tabletah.setCellWidget(rows, 1, self.remov)
            self.tah1.setText('')

    def removrow(self):
        self.tabletah.removeRow(self.tabletah.currentRow())
        self.tabletah.repaint()
        if self.tabletah.rowCount() == 0:
            self.tahltag.setHidden(False)
            self.tabletah.setHidden(True)


    #دالة البحث وعرض صفحة البروفايل للمريض
    def searchpatient(self):
        uuid = self.searchedit.text()
        if uuid.isdigit():
            x = self.patientlistWidget.findItems(uuid,Qt.MatchExactly)
            if len(x) == 0:
                self.showToaster('عفواً!', 'لا يوجد رقم تعريفى مطابق.', ':/MainSources/close.gif', '#ec0101',
                                 'MainSources/fail.wav', 1, 2000)
            else:
                for item in x:
                    row = self.patientlistWidget.row(item)
                    self.patientlistWidget.setCurrentRow(row)
                self.tabWidget.setCurrentIndex(4)
        else:
            self.showToaster('عفواً!', 'يتم البحث بالرقم التعريفى فقط.', ':/MainSources/close.gif', '#ec0101',
                             'MainSources/fail.wav', 1, 2000)

    #تعريف رابطة الازرار
    def handelbuttons(self):
        self.btn_newkashf.clicked.connect(self.newdialog)
        self.newadd.clicked.connect(self.newdialog)
        self.hagzlistwid.pressed.connect(self.selectit)
        self.edittabbtn.clicked.connect(self.checkcurrentrow)
        self.delbtn.clicked.connect(self.deletehagz)
        self.esttablewidget.pressed.connect(self.checkesttable)
        self.towaiting.clicked.connect(self.exporttohagz)
        self.todoctorli.clicked.connect(self.exporttodoc)
        self.exambtn.clicked.connect(self.tashkhes)
        self.addmedbtn.clicked.connect(self.addmedicine)
        self.doctable.pressed.connect(self.enbtntash)
        self.saveSettings.clicked.connect(self.store)
        self.roshprev.clicked.connect(self.viewrosh)
        self.editprice.clicked.connect(self.editallprice)
        self.priceedit.saveprices.clicked.connect(self.setpriceplans)
        self.searchbtn.clicked.connect(self.searchpatient)
        self.addaradd.clicked.connect(self.addarad)
        self.addtahl.clicked.connect(self.addtah)
        self.addvarr.clicked.connect(self.addvarsettings)
        self.addmtext.clicked.connect(self.addmedsettings)
        self.addtashset.clicked.connect(self.addtashsettings)
        self.addbtnvarss.clicked.connect(self.newvarss)
        self.dvars.addvarss.clicked.connect(self.addnewvarss)
        self.dvars.addvarss2.clicked.connect(self.addnewvars)
        self.costbtn.clicked.connect(self.getcost)
        self.pay.clicked.connect(self.checkcostinhagz)
        self.getimg.clicked.connect(self.chooseimage)
        self.radiono1.clicked.connect(self.color2box)
        self.radioyes1.clicked.connect(self.colorgbox)
        self.radionoboot.clicked.connect(self.colorgboxerd)
        self.radioyesboot.clicked.connect(self.colorgboxerad)
        self.radiono2.clicked.connect(self.colorgboxnotif)
        self.radioyes2.clicked.connect(self.colorgboxnotify)
        self.selectloc.clicked.connect(self.chooselocation)
        self.pushButton.clicked.connect(self.checkbutton1)
        self.pushButton_2.clicked.connect(self.checkbutton)
        self.saveno2.clicked.connect(self.checkroshbtn)
        self.saveyes2.clicked.connect(self.checkroshbtnn)
        self.addtask.clicked.connect(self.insertTodoList)
        self.showadtask.clicked.connect(self.showaddTask)
        self.closebtn.clicked.connect(self.closetask)
        self.editbttn.clicked.connect(self.updateTask)
        self.enternote.clicked.connect(self.addNotesToNotes)
        self.notesedit.textChanged.connect(self.countNotesLetters)
        self.edit.savebtn.clicked.connect(self.updatedata)
        self.addform.savebtn.clicked.connect(self.savedata)
        self.editkys.clicked.connect(self.enableEditKys)
        self.savekys.clicked.connect(self.disableEditKys)
        self.patientlistWidget.currentRowChanged.connect(self.getit)
        self.historyList.clicked.connect(self.selectHistoryCard)
        self.historyList.clicked.connect(self.viewDateLog)
        self.creloc.clicked.connect(self.exportBackup)
        self.activateserv.clicked.connect(self.activateMysql80)
        self.imploc.clicked.connect(self.chooseDbfile)
        self.db1disconnect.clicked.connect(self.databaseconnect)
        self.importdone.textChanged.connect(self.checkImportDone)
        self.saveroshset.clicked.connect(self.setRoshSettings)
        self.saveroshloc.clicked.connect(self.chooseRoshLocation)
        self.previewtest.clicked.connect(self.viewTestPreview)
        self.defualtvalues.clicked.connect(self.getRoshValues)
        self.zoomin.clicked.connect(self.zoomIn)
        self.zoomout.clicked.connect(self.zoomOut)
        self.listroshwidget.clicked.connect(self.viewRoshSettings)
        self.listroshwidget.currentRowChanged.connect(self.viewRoshSettings)
        self.saveandclose.clicked.connect(self.saveAndEnd)
        self.throuhweek.toggled.connect(self.saveUnique)
        self.firsttime.toggled.connect(self.saveUnique)
        self.uniqueword.toggled.connect(self.saveUnique)
        self.addform.complet.clicked.connect(self.completePatientInfo)
        self.addform.trago.clicked.connect(self.getback)
        self.listWidget.pressed.connect(self.chooseTab)
        self.closetash.clicked.connect(self.exitFromTash)
        self.continuetash.clicked.connect(self.continueTash)
        self.msgstatus.textChanged.connect(self.otherDevice)
        self.msgstatus.editingFinished.connect(self.otherDevice)
        self.pcconn.textChanged.connect(self.connOther)
        self.result.textChanged.connect(self.checkResult)
        self.my8check.textChanged.connect(self.setStyleformy8check)


    def connOther(self):
        if self.pcconn.text() == "connected":
            self.pcconnect.setHidden(False)
            self.pcdisconnect.setHidden(True)
        else:
            self.pcconnect.setHidden(True)
            self.pcdisconnect.setHidden(False)


    def otherDevice(self):
        try:
            self.db.commit()
            if self.msgstatus.text() == 'connected':
                self.secondDatabaseConnect()
            elif self.msgstatus.text() == 'new':
                self.loadkashftable()
                self.loadesttable()
            elif self.msgstatus.text() == 'edit':
                self.loadkashftable()
            elif self.msgstatus.text() == 'tohagz':
                self.loadkashftable()
                self.loadesttable()
            elif self.msgstatus.text() == 'save':
                self.loadkashftable()
            elif self.msgstatus.text() == 'cancel':
                self.loadkashftable()
                self.loadesttable()
                self.loaddoctable()
            elif self.msgstatus.text() == 'todoc':
                self.loadkashftable()
                self.loadesttable()
                self.loaddoctable()
            elif self.msgstatus.text() == 'reload':
                self.loadkashftable()
                self.loadesttable()
                self.loaddoctable()
            elif self.msgstatus.text() == 'pay':
                self.loadkashftable()
                self.loaddoctable()
            elif self.msgstatus.text() == 'kill':
                self.closeotherconn()
            elif self.msgstatus.text() == 'conect':
                self.databaseconnect()
        except:
            self.saveErrors('Command Error')



    def closeotherconn(self):
        global dbcur
        global dbconnect
        if dbconnect != None:
            dbcur.close()
            dbconnect.close()
            self.db2connect.setHidden(True)
            self.db2disconnect.setVisible(True)
            self.sqlstatus2.setText('غير متصل')
            dbcur = None
            dbconnect = None



    def checkroshbtn(self):
        if self.saveyes2.isChecked():
            self.saveno2.setChecked(True)
            self.saveyes2.setChecked(False)
            self.gBoxny2.setStyleSheet('background-color:#4683ff;border-radius:2px;')
        else:
            self.saveno2.setChecked(False)
            self.saveyes2.setChecked(True)
            self.gBoxny2.setStyleSheet('background-color:#c1c1c1;border-radius:2px;')

    def checkroshbtnn(self):
        if self.saveno2.isChecked():
            self.saveno2.setChecked(False)
            self.saveyes2.setChecked(True)
            self.gBoxny2.setStyleSheet('background-color:#c1c1c1;border-radius:2px;')
        else:
            self.saveno2.setChecked(True)
            self.saveyes2.setChecked(False)
            self.gBoxny2.setStyleSheet('background-color:#4683ff;border-radius:2px;')

    def checkbutton1(self):
        if self.pushButton_2.isChecked():
            self.pushButton.setChecked(True)
            self.pushButton_2.setChecked(False)
            self.gBoxny.setStyleSheet('background-color:#4683ff;border-radius:2px;')
        else:
            self.pushButton.setChecked(False)
            self.pushButton_2.setChecked(True)
            self.gBoxny.setStyleSheet('background-color:#c1c1c1;border-radius:2px;')

    def checkbutton(self):
        if self.pushButton.isChecked():
            self.pushButton.setChecked(False)
            self.pushButton_2.setChecked(True)
            self.gBoxny.setStyleSheet('background-color:#c1c1c1;border-radius:2px;')
        else:
            self.pushButton.setChecked(True)
            self.pushButton_2.setChecked(False)
            self.gBoxny.setStyleSheet('background-color:#4683ff;border-radius:2px;')

    def colorgbox(self):
        if self.radiono1.isChecked():
            self.radiono1.setChecked(False)
            self.radioyes1.setChecked(True)
            self.gBox1.setStyleSheet('background-color:#c1c1c1;border-radius:2px;')
        else:
            self.radiono1.setChecked(True)
            self.radioyes1.setChecked(False)
            self.gBox1.setStyleSheet('background-color:#4683ff;border-radius:2px;')

    def color2box(self):
        if self.radioyes1.isChecked():
            self.radiono1.setChecked(True)
            self.radioyes1.setChecked(False)
            self.gBox1.setStyleSheet('background-color:#4683ff;border-radius:2px;')
        else:
            self.radiono1.setChecked(False)
            self.radioyes1.setChecked(True)
            self.gBox1.setStyleSheet('background-color:#c1c1c1;border-radius:2px;')

    def colorgboxerad(self):
        if self.radionoboot.isChecked():
            self.radionoboot.setChecked(False)
            self.radioyesboot.setChecked(True)
            self.gBoxboot.setStyleSheet('background-color:#c1c1c1;border-radius:2px;')
        else:
            self.radionoboot.setChecked(True)
            self.radioyesboot.setChecked(False)
            self.gBoxboot.setStyleSheet('background-color:#4683ff;border-radius:2px;')


    def colorgboxerd(self):
        if self.radioyesboot.isChecked():
            self.radionoboot.setChecked(True)
            self.radioyesboot.setChecked(False)
            self.gBoxboot.setStyleSheet('background-color:#4683ff;border-radius:2px;')
        else:
            self.radionoboot.setChecked(False)
            self.radioyesboot.setChecked(True)
            self.gBoxboot.setStyleSheet('background-color:#c1c1c1;border-radius:2px;')

    def colorgboxnotify(self):
        if self.radiono2.isChecked():
            self.radiono2.setChecked(False)
            self.radioyes2.setChecked(True)
            self.gBox2.setStyleSheet('background-color:#c1c1c1;border-radius:2px;')
        else:
            self.radiono2.setChecked(True)
            self.radioyes2.setChecked(False)
            self.gBox2.setStyleSheet('background-color:#4683ff;border-radius:2px;')

    def colorgboxnotif(self):
        if self.radioyes2.isChecked():
            self.radiono2.setChecked(True)
            self.radioyes2.setChecked(False)
            self.gBox2.setStyleSheet('background-color:#4683ff;border-radius:2px;')
        else:
            self.radiono2.setChecked(False)
            self.radioyes2.setChecked(True)
            self.gBox2.setStyleSheet('background-color:#c1c1c1;border-radius:2px;')

    def closetask(self):
        self.ttaskWidget.setCurrentIndex(0)

    #دالة زرار عرض تعديل الاسعار
    def editallprice(self):
        self.priceedit.exec_()

    def setTimesForHagz(self):
        self.timelist = []
        start = self.starttime.value()
        startmin = self.starttimemin.value()
        end = self.endtime.value()
        endmin = self.endtimemin.value()
        fark = self.farktime.value()
        for h in range(start,end):
            if startmin !=  0 and h == start:
                for m in range(startmin,60,fark):
                    if m >= 60:
                        break
                    self.timelist.append(str(h)+':'+str(m))
            else:
                for m in range(0,60,fark):
                    if m >= 60:
                        break
                    self.timelist.append(str(h)+':'+str(m))

    #عرض مربع اضافة الحجز
    def newdialog(self):
        if mySQL80 == True:
            try:
                self.addform.moadtime.clear()
                self.setTimesForHagz()
                if self.hagzlistwid.count() != 0:
                    for i in range(self.hagzlistwid.count()):
                        val = self.hagzlistwid.itemWidget(self.hagzlistwid.item(i)).wakt.text()
                        if val in self.timelist:
                            self.timelist.remove(val)
                self.addform.moadtime.addItems(self.timelist)
                s = datetime.now()
                qrr = int(s.strftime("%Y%m%d%H%M%S%f"))
                self.addform.qrr.setText(str(qrr))
                self.clearhagzdialog()
                comSQL = '''SELECT hagz_patientname FROM hagz'''
                self.cur.execute(comSQL)
                liscom = self.cur.fetchall()
                self.liss = []
                for i in liscom:
                    for data in i:
                        self.liss.append(data)
                self.addform.rowcountlabel.setText(str(0))
                self.addform.sumall.setText(str(0))
                self.addform.allsum.setText(str(0))
                maincompleter = QCompleter(self.liss)
                maincompleter.setCaseSensitivity(Qt.CaseInsensitive)
                self.addform.previewname.setCompleter(maincompleter)
                self.addform.previewname.textChanged.connect(self.completedata)
                self.addform.exec_()
            except mysql.connector.Error as err:
                self.saveErrors('AddNewHagzError: '+str(err))
                self.showToaster('عفواً!', 'حدث خطأ ما.', ':/MainSources/close.gif', '#ec0101',
                                 'MainSources/fail.wav', 1, 2000)
        else:
            self.showToaster('عفواً!', 'خطأ الاتصال بقاعدة البيانات.', ':/MainSources/close.gif', '#ec0101',
                             'MainSources/fail.wav', 1, 2000)
            self.saveErrors('New Hagz Error')

    def completedata(self):
        text = self.addform.previewname.text()
        spli = list(text.split(" "))
        newlis = []
        for i in spli:
            if i != ' ' or i !='':
                newlis.append(i)
        for r,w in enumerate(newlis):
            if r == 0:
                self.addform.lPatientName.setText(w)
                self.addform.flPatientName.setText('')
                self.addform.sPatientName.setText('')
                self.addform.fPatientName.setText('')
            if r == 1:
                self.addform.flPatientName.setText(w)
                self.addform.sPatientName.setText('')
                self.addform.fPatientName.setText('')
            if r == 2:
                self.addform.sPatientName.setText(w)
                self.addform.fPatientName.setText('')
            if r == 3:
                self.addform.fPatientName.setText(w)
            if r > 3:
                self.addform.labelerror.setText('× يسمح فقط بالأسم الرباعى.')
                self.addform.labelerror.setHidden(False)
            else:
                self.addform.labelerror.setHidden(True)
        if len(self.addform.fPatientName.text()) >0 and len(self.addform.sPatientName.text())>0 and len(self.addform.flPatientName.text())>0:
            self.patienFullName = self.addform.lPatientName.text() + ' ' + self.addform.flPatientName.text() + ' ' + self.addform.sPatientName.text() + ' ' + self.addform.fPatientName.text()
        elif len(self.addform.fPatientName.text()) == 0 and len(self.addform.sPatientName.text())>0 and len(self.addform.flPatientName.text())>0:
            self.patienFullName = self.addform.lPatientName.text() + ' ' + self.addform.flPatientName.text() + ' ' + self.addform.sPatientName.text()
        elif len(self.addform.fPatientName.text())==0 and len(self.addform.sPatientName.text())==0 and len(self.addform.flPatientName.text())>0:
            self.patienFullName = self.addform.lPatientName.text() + ' ' + self.addform.flPatientName.text()
        else:
            self.patienFullName = self.addform.lPatientName.text()
        if self.patienFullName in self.liss:
            self.addform.complet.setEnabled(True)
            self.addform.trago.setEnabled(False)
        else:
            self.addform.trago.setEnabled(False)
            self.addform.complet.setEnabled(False)
            s = datetime.now()
            qrr = int(s.strftime("%Y%m%d%H%M%S%f"))
            self.addform.qrr.setText(str(qrr))
            self.addform.lPhone.setText('')
            self.addform.lAddress.setText('')
            self.addform.sAge.setValue(1)
            self.addform.cgender.setCurrentIndex(0)
            self.addform.social.setCurrentIndex(0)

    def getback(self):
        s = datetime.now()
        qrr = int(s.strftime("%Y%m%d%H%M%S%f"))
        self.addform.qrr.setText(str(qrr))
        self.addform.previewname.setText('')
        self.addform.lPhone.setText('')
        self.addform.lAddress.setText('')
        self.addform.sAge.setValue(1)
        self.addform.cgender.setCurrentIndex(0)
        self.addform.social.setCurrentIndex(0)

    def completePatientInfo(self):
        if mySQL80 == True:
            try:
                sql = '''SELECT hagz_age,hagz_gender,hagz_phone,hagz_address,hagz_soical,hagz_qrrandom FROM hagz WHERE hagz_patientname=%s'''
                self.cur.execute(sql, [(self.patienFullName)])
                fetch = self.cur.fetchall()
                for data in fetch:
                    self.addform.sAge.setValue(data[0])
                    self.addform.cgender.setCurrentIndex(data[1])
                    self.addform.social.setCurrentIndex(data[4])
                    self.addform.lPhone.setText(data[2])
                    self.addform.lAddress.setText(data[3])
                    self.addform.qrr.setText(data[5])
                self.addform.trago.setEnabled(True)
            except mysql.connector.Error as err:
                self.showToaster('عفواً!', 'حدث خطأ أثناء المحاولة.', ':/MainSources/close.gif', '#ec0101',
                                 'MainSources/fail.wav', 1, 2000)
                self.saveErrors('CompletePatientInfo: ' + str(err))
        else:
            self.saveErrors('Mysql Service')


    #دالة إضافة الاعراض وتعديلها
    def addaradsupdate(self):
        for i in range(self.tabarad.rowCount()):
            if mySQL80 == True:
                try:
                    sql = '''INSERT INTO arad(arad_name,arad_qrrandom,arad_history) VALUES(%s,%s,%s)'''
                    self.cur.execute(sql,(self.tabarad.item(i,0).text(),self.viewuid.text(),self.viewdate.text()))
                    if connect == None:
                        command = self.cur.statement
                        self.saveCommand(command)
                    else:
                        try:
                            dbcur.execute(sql,(self.tabarad.item(i,0).text(),self.viewuid.text(),self.viewdate.text()))
                            dbconnect.commit()
                        except:
                            command = self.cur.statement
                            self.saveCommand(command)
                except mysql.connector.Error as err :
                    self.saveErrors('AddArdError: '+ str(err))

    def saveCommand(self,command):
        with open("commands.txt", "a", encoding='utf-8') as sqlcommand:
            sqlcommand.write(command + ";")

    def allEarnToday(self):
        count = self.hagzlistwid.count()
        earn = []
        if count != 0:
            for i in range(count):
                var = self.hagzlistwid.itemWidget(self.hagzlistwid.item(i)).hala.text()
                if var == 'تم الإنتهاء':
                    money = self.hagzlistwid.itemWidget(self.hagzlistwid.item(i)).money.text()
                    earn.append(float(money[1:len(money)]))
            self.lcdNumberr.setText(str(sum(map(float,earn))))

    def allPeopleToday(self):
        count = self.hagzlistwid.count()
        people = []
        if count != 0:
            for i in range(count):
                var = self.hagzlistwid.itemWidget(self.hagzlistwid.item(i)).hala.text()
                if var == 'تم الإنتهاء':
                    people.append(i)
            self.lcdNumberv.setText(str(len(people)))

    #دالة تفعيل أزرار تابة الحجز
    def enablebtn(self):
        if self.hagzlistwid.currentRow() < 0:
            self.edittabbtn.setHidden(True)
            self.delbtn.setHidden(True)
            self.todoctorli.setHidden(True)
            self.pay.setHidden(True)
        else:
            var = self.hagzlistwid.itemWidget(self.hagzlistwid.item(self.hagzlistwid.currentRow())).cost.text()
            hala = self.hagzlistwid.itemWidget(self.hagzlistwid.item(self.hagzlistwid.currentRow())).hala.text()
            if var == '$0' and hala == 'مع الطبيب':
                self.edittabbtn.setHidden(True)
                self.delbtn.setHidden(True)
                self.todoctorli.setHidden(True)
                self.pay.setHidden(True)
            elif var == '$0' and hala == 'تم الإنتهاء':
                self.pay.setHidden(True)
                self.edittabbtn.setHidden(True)
                self.delbtn.setHidden(True)
                self.todoctorli.setHidden(True)
            elif var == '$0' and hala == 'فى الإنتظار':
                self.pay.setHidden(True)
                self.edittabbtn.setHidden(False)
                self.delbtn.setHidden(False)
                self.todoctorli.setHidden(False)
            elif var != '$0' and hala =='تم الإنتهاء':
                self.pay.setHidden(False)
                self.edittabbtn.setHidden(True)
                self.delbtn.setHidden(True)
                self.todoctorli.setHidden(True)
            elif var != '$0' and hala == 'فى الإنتظار':
                self.pay.setHidden(False)
                self.edittabbtn.setHidden(False)
                self.delbtn.setHidden(False)
                self.todoctorli.setHidden(False)
            elif var != '$0' and hala == 'مع الطبيب':
                self.pay.setHidden(False)
                self.edittabbtn.setHidden(True)
                self.delbtn.setHidden(True)
                self.todoctorli.setHidden(True)
            else:
                self.pay.setHidden(True)
                self.edittabbtn.setHidden(True)
                self.delbtn.setHidden(True)
                self.todoctorli.setHidden(True)

    def selectit(self):
        for i in range(0,self.hagzlistwid.count()):
            if i == self.hagzlistwid.currentRow():
                shadow = QGraphicsDropShadowEffect(blurRadius=30, xOffset=0, yOffset=0)
                self.hagzlistwid.itemWidget(self.hagzlistwid.item(self.hagzlistwid.currentRow())).setGraphicsEffect(shadow)
            else:
                shadow = QGraphicsDropShadowEffect(blurRadius=3, xOffset=0, yOffset=0)
                self.hagzlistwid.itemWidget(self.hagzlistwid.item(i)).setGraphicsEffect(shadow)
        self.enablebtn()

    #دالة معرفة موقع التحديد فى الجدول الحجز
    def checkcurrentrow(self):
        if self.hagzlistwid.currentRow() < 0  :
            self.showToaster('عفواً!', 'عفوا قم بتحديد الصف فى الجدول.', ':/MainSources/close.gif', '#ec0101',
                             'MainSources/fail.wav', 1, 2000)
        else:
            self.neweditdialog()

    #دالة حذف الحجز
    def deletehagz(self):
        uuid = self.hagzlistwid.itemWidget(self.hagzlistwid.item(self.hagzlistwid.currentRow())).tareef.text()
        dat = str(date.today())
        if mySQL80 == True:
            try:
                delSQL = '''UPDATE history SET his_moaked='ملغى',his_exam='3' WHERE his_qrrandom=%s AND his_moed=%s'''
                self.cur.execute(delSQL, (uuid,dat))
                if connect == None:
                    command = self.cur.statement
                    self.saveCommand(command)
                else:
                    try:
                        dbcur.execute(delSQL, (uuid,dat))
                        dbconnect.commit()
                    except:
                        command = self.cur.statement
                        self.saveCommand(command)
                    text = 'cancel'
                    connn.send(text.encode("utf-8"))
                self.db.commit()
            except mysql.connector.Error as err:
                self.showToaster('عفواً!', 'حدث خطأ أثناء المحاولة.', ':/MainSources/close.gif', '#ec0101',
                                 'MainSources/fail.wav', 1, 2000)
                self.saveErrors('CancelHagzError: ' + str(err))
        else:
            self.showToaster('عفواً!', 'خطأ الاتصال بقاعدة البيانات.', ':/MainSources/close.gif', '#ec0101',
                             'MainSources/fail.wav', 1, 2000)
        self.loadkashftable()

    def checkcostinhagz(self):
        cot = self.hagzlistwid.itemWidget(self.hagzlistwid.item(self.hagzlistwid.currentRow())).cost.text()
        cost = cot[1:len(cot)]
        if cost == '0':
            self.neweditdialog()
        else:
            self.paycosts(cost)

    def paycosts(self,cost):
        items = (cost,)
        item, okPressed = QInputDialog.getItem(self, "المطلوب", "المبلغ المطلوب :", items, 0, False)
        uuid = self.hagzlistwid.itemWidget(self.hagzlistwid.item(self.hagzlistwid.currentRow())).tareef.text()
        dat = str(date.today())
        if okPressed and item:
            if mySQL80 == True:
                try:
                    ss = '''SELECT his_payment FROM history WHERE his_qrrandom=%s AND his_moed=%s'''
                    self.cur.execute(ss,(uuid,dat))
                    if connect == None:
                        command = self.cur.statement
                        self.saveCommand(command)
                    else:
                        try:
                            dbcur.execute(ss,(uuid,dat))
                            dbconnect.commit()
                        except:
                            command = self.cur.statement
                            self.saveCommand(command)
                    fet = self.cur.fetchall()
                    msql = '''UPDATE history SET his_active=0,his_payment=%s,his_pricetype='مدفوع',his_cost='0' WHERE his_qrrandom=%s AND his_moed=%s'''
                    self.cur.execute(msql,((float(item)+float(fet[0][0])),uuid,dat))
                    if connect == None:
                        command = self.cur.statement
                        self.saveCommand(command)
                    else:
                        try:
                            dbcur.execute(msql,((float(item)+float(fet[0][0])),uuid,dat))
                            dbconnect.commit()
                        except:
                            command = self.cur.statement
                            self.saveCommand(command)
                        text = 'pay'
                        connn.send(text.encode("utf-8"))
                    self.db.commit()
                except mysql.connector.Error as err:
                    self.saveErrors('Costs: '+ str(err))
                    self.showToaster('عفواً!', 'حدث خطأ أثناء المحاولة.', ':/MainSources/close.gif', '#ec0101',
                                     'MainSources/fail.wav', 1, 2000)
                self.loadkashftable()
                self.loaddoctable()
            else:
                self.showToaster('عفواً!', 'خطأ الاتصال بقاعدة البيانات.', ':/MainSources/close.gif', '#ec0101',
                                 'MainSources/fail.wav', 1, 2000)


    # عرض مربع تعديل الحجز
    def neweditdialog(self):
        if mySQL80 == True:
            try:
                self.edit.moadtime.clear()
                self.setTimesForHagz()
                if self.hagzlistwid.count() != 0:
                    for i in range(self.hagzlistwid.count()):
                        val = self.hagzlistwid.itemWidget(self.hagzlistwid.item(i)).wakt.text()
                        if val in self.timelist:
                            self.timelist.remove(val)
                self.edit.moadtime.addItems(self.timelist)
                uid = self.hagzlistwid.itemWidget(self.hagzlistwid.item(self.hagzlistwid.currentRow())).tareef.text()
                today = str(date.today())
                sql = '''SELECT his_type,his_patientname,his_age,his_gender,his_phone,his_address,his_pricetype,
                 his_soical,his_suger, his_height, his_weight, his_blood, his_lblood,his_moed,his_timemoed,his_moaked,his_way,his_payname,his_payment,his_temp FROM history WHERE his_qrrandom=%s AND his_moed=%s'''
                self.cur.execute(sql,(uid,today))
                fetch = self.cur.fetchall()
                nameList = list(fetch[0][1].split())
                self.edit.previewname.setText(fetch[0][1])
                if len(nameList) == 4:
                    self.edit.lPatientName.setText(nameList[0])
                    self.edit.flPatientName.setText(nameList[1])
                    self.edit.sPatientName.setText(nameList[2])
                    self.edit.fPatientName.setText(nameList[3])
                elif len(nameList) == 3:
                    self.edit.lPatientName.setText(nameList[0])
                    self.edit.flPatientName.setText(nameList[1])
                    self.edit.sPatientName.setText(nameList[2])
                elif len(nameList) == 2:
                    self.edit.lPatientName.setText(nameList[0])
                    self.edit.flPatientName.setText(nameList[1])
                else:
                    self.edit.lPatientName.setText(nameList[0])
                self.edit.sAge.setValue(fetch[0][2])
                self.edit.cgender.setCurrentIndex(fetch[0][3])
                self.edit.lPhone.setText(fetch[0][4])
                self.edit.lAddress.setText(fetch[0][5])
                if fetch[0][6] == 'مدفوع':
                    self.edit.checkpaid.setChecked(True)
                else:
                    self.edit.checkpaid.setChecked(False)
                self.edit.social.setCurrentIndex(fetch[0][7])
                self.edit.sugerSpinBox.setValue(float(fetch[0][8]))
                self.edit.heightSpinBox.setValue(float(fetch[0][9]))
                self.edit.weightSpinBox.setValue(float(fetch[0][10]))
                self.edit.highSpinBox.setValue(float(fetch[0][11]))
                self.edit.lowSpinBox.setValue(float(fetch[0][12]))
                self.edit.tempSpinBox.setValue(float(fetch[0][19]))
                day = QDate(int(fetch[0][13][0:4]),int(fetch[0][13][5:7]),int(fetch[0][13][8:10]))
                self.edit.moaddateEdit.setDate(day)
                if fetch[0][15] == 'مؤكد':
                    self.edit.checkhagz.setChecked(True)
                else:
                    self.edit.checkhagz.setChecked(False)
                self.edit.waycomboBox.setCurrentIndex(fetch[0][16])
                self.edit.qrr.setText(str(uid))
                self.edit.datevie.setText(str(fetch[0][13]))
                lis = list(str(fetch[0][17]).split(','))
                if len(lis) == 1 and lis[0] == 'كشف':
                    self.edit.radiokashf.setChecked(True)
                    self.edit.pricekashf.setCurrentText(str(fetch[0][18]))
                elif len(lis) == 1 and lis[0] == 'إستشارة':
                    self.edit.radioest.setChecked(True)
                    self.edit.priceest.setCurrentText(str(fetch[0][18]))
                elif len(lis) == 1 and lis[0] =='':
                    self.edit.radiokashf.setChecked(True)
                else:
                    self.edit.priceb.setChecked(True)
                    x = []
                    for i in lis :
                        x.append(list(str(i).split('  ')))
                    total = 0.0
                    self.edit.pricetable.setRowCount(0)
                    for a,b in enumerate(x):
                        self.edit.pricetable.insertRow(a)
                        remove = QPushButton('')
                        remove.setIcon(QIcon(":/MainSources/delete.png"))
                        remove.clicked.connect(self.removePrice)
                        self.edit.pricetable.setItem(a, 0, QTableWidgetItem(str(b[0])))
                        self.edit.pricetable.setItem(a, 1, QTableWidgetItem(str(b[1])))
                        self.edit.pricetable.setCellWidget(a, 2, remove)
                        total += float(b[1])
                    self.edit.allsum.setText(str(total))
                    self.edit.sumall.setText(str(total))
                    self.edit.rowcountlabel.setText(str(self.edit.pricetable.rowCount()))
                self.edit.previewname.textChanged.connect(self.renterNames)
                self.edit.exec_()
            except mysql.connector.Error as err:
                self.saveErrors('NewDialog: '+str(err))
                self.showToaster('عفواً!', 'حدث خطأ أثناء المحاولة.', ':/MainSources/close.gif', '#ec0101',
                                 'MainSources/fail.wav', 1, 2000)
        else:
            self.showToaster('عفواً!', 'خطأ الاتصال بقاعدة البيانات.', ':/MainSources/close.gif', '#ec0101',
                             'MainSources/fail.wav', 1, 2000)

    def renterNames(self):
        text = self.edit.previewname.text()
        spli = list(text.split(" "))
        newlis = []
        for i in spli:
            if i != ' ' or i != '':
                newlis.append(i)
        for r, w in enumerate(newlis):
            if r == 0:
                self.edit.lPatientName.setText(w)
                self.edit.flPatientName.setText('')
                self.edit.sPatientName.setText('')
                self.edit.fPatientName.setText('')
            if r == 1:
                self.edit.flPatientName.setText(w)
                self.edit.sPatientName.setText('')
                self.edit.fPatientName.setText('')
            if r == 2:
                self.edit.sPatientName.setText(w)
                self.edit.fPatientName.setText('')
            if r == 3:
                self.edit.fPatientName.setText(w)
            if r > 3:
                self.edit.labelerror.setText('× يسمح فقط بالأسم الرباعى.')
                self.edit.labelerror.setHidden(False)
            else:
                self.edit.labelerror.setHidden(True)

    def handleQRCode(self, uid):
        qr_image = qrcode.make(uid, image_factory=Image).pixmap()
        self.qrPatientC.setPixmap(qr_image.scaled(90, 90, Qt.KeepAspectRatio, Qt.FastTransformation))
        self.qrPatientC.repaint()

    def retievePatientData(self,uid):
        if mySQL80 == True:
            try:
                sql = '''SELECT hag_date,hagz_patientname,hagz_gendername,hagz_age,hagz_phone,hagz_address FROM hagz WHERE hagz_qrrandom=%s'''
                self.cur.execute(sql,[(uid)])
                fetch = self.cur.fetchall()
                for r,data in enumerate(fetch):
                    self.patienName.setText(data[1])
                    self.patienGender.setText(data[2])
                    if data[3] == 1:
                        age = 'عام'
                    elif data[3] == 2:
                        age = 'عامين'
                    elif 3<=data[3]<=10:
                        age = str(data[3])+' أعوام'
                    else:
                        age = str(data[3]) + ' عام'
                    self.patienAge.setText(age)
                    self.assigned.setText('أحدث جلسة كانت فى يوم '+str(data[0]))
                    if data[4] == '':
                        self.phopho.setText('لا يوجد')
                    else:
                        self.phopho.setText(str(data[4]))
                    if data[5] == '':
                        self.addadd.setText('لا يوجد')
                    else:
                        self.addadd.setText(str(data[5]))
            except mysql.connector.Error as err:
                self.saveErrors('PatientData: '+str(err))
                self.showToaster('عفواً!', 'حدث خطأ أثناء المحاولة.', ':/MainSources/close.gif', '#ec0101',
                                 'MainSources/fail.wav', 1, 2000)
        else:
            self.showToaster('عفواً!', 'خطأ الاتصال بقاعدة البيانات.', ':/MainSources/close.gif', '#ec0101',
                             'MainSources/fail.wav', 1, 2000)


    def getit(self):
        if self.patientlistWidget.count() != 0:
            uid = self.patientlistWidget.itemWidget(self.patientlistWidget.item(self.patientlistWidget.currentRow())).objectName()
            self.handleQRCode(uid)
            self.retievePatientData(uid)
            self.bloodpressureChart()
            self.historyCards(uid)
            for i in range(0,self.patientlistWidget.count()):
                if i == self.patientlistWidget.currentRow():
                    shadow = QGraphicsDropShadowEffect(blurRadius=20, xOffset=0, yOffset=0)
                    self.patientlistWidget.itemWidget(self.patientlistWidget.item(self.patientlistWidget.currentRow())).setGraphicsEffect(shadow)
                else:
                    shadow = QGraphicsDropShadowEffect(blurRadius=2, xOffset=0, yOffset=0)
                    self.patientlistWidget.itemWidget(self.patientlistWidget.item(i)).setGraphicsEffect(shadow)
        else:
            pass

    def createPatientList(self):
        if mySQL80 == True:
            try:
                cou = self.patientlistWidget.count()
                if cou !=0:
                    for i in range(cou):
                        self.patientlistWidget.takeItem(i)
                sql = '''SELECT hag_date,hagz_patientname,hagz_phone,hagz_address,hagz_age,hagz_gender,hagz_qrrandom FROM hagz'''
                self.cur.execute(sql)
                fetch = self.cur.fetchall()
                if len(fetch) != 0:
                    self.tabWidget.setCurrentIndex(4)
                    for r,data in enumerate(fetch):
                        widget = patientListWidget.listwidget()
                        if data[5] == 0 and data[4] <= 15:
                            widget.sora.setPixmap(QPixmap(':/MainSources/ChildMale.png'))
                        elif data[5] == 0 and 30>=data[4] >= 16:
                            widget.sora.setPixmap(QPixmap(':/MainSources/youthMale.png'))
                        elif data[5] == 0 and 49>=data[4] >= 31:
                            widget.sora.setPixmap(QPixmap(':/MainSources/Male.png'))
                        elif data[5] == 0 and data[4] >= 50:
                            widget.sora.setPixmap(QPixmap(':/MainSources/oldMale.png'))
                        elif data[5] == 1 and data[4] <= 15:
                            widget.sora.setPixmap(QPixmap(':/MainSources/ChildFemale.png'))
                        elif data[5] == 1 and 30>=data[4] >= 16:
                            widget.sora.setPixmap(QPixmap(':/MainSources/youthFemale.png'))
                        elif data[5] == 1 and 49>=data[4] >= 31:
                            widget.sora.setPixmap(QPixmap(':/MainSources/Female.png'))
                        elif data[5] == 1 and data[4] >= 50:
                            widget.sora.setPixmap(QPixmap(':/MainSources/oldFemale.png'))
                        widget.tasjeel.setText(str(data[0]))
                        widget.patName.setText(str(data[1]))
                        widget.patInfo.setText(str(data[2]))
                        widget.setObjectName(str(data[6]))
                        listItem = QListWidgetItem(str(data[6]))
                        listItem.setHidden(True)
                        listItem.setTextAlignment(Qt.AlignCenter)
                        listItem.setSizeHint(widget.sizeHint())
                        shadow = QGraphicsDropShadowEffect(blurRadius=2, xOffset=0, yOffset=0)
                        widget.groupBox.setGraphicsEffect(shadow)
                        self.patientlistWidget.addItem(listItem)
                        self.patientlistWidget.setItemWidget(listItem,widget)
                else:
                    self.showToaster('عفواً!', 'لا يوجد سجل متاح.', ':/MainSources/close.gif', '#ec0101',
                                     'MainSources/fail.wav',
                                     1, 2000)
                self.patientlistWidget.setCurrentRow(self.patientlistWidget.count() - 1)
            except mysql.connector.Error as err:
                self.saveErrors('CreatePatient: '+str(err))


    def bloodpressureChart(self):
        x = []
        y = []
        y1 = []
        h = []
        w = []
        su = []
        tem = []
        uid = self.patientlistWidget.itemWidget(self.patientlistWidget.item(self.patientlistWidget.currentRow())).objectName()
        if mySQL80 == True:
            try:
                sql = '''SELECT his_blood,his_lblood,his_moed,his_height,his_weight,his_suger,his_temp FROM history WHERE his_qrrandom=%s AND his_exam='2' '''
                self.cur.execute(sql,[(uid)])
                fetch = self.cur.fetchall()
                for i,data in enumerate(fetch):
                    y.append(float(data[0]))
                    y1.append(float(data[1]))
                    x.append(data[2]+' 00:00:00')
                    h.append(float(data[3]))
                    w.append(float(data[4]))
                    su.append(float(data[5]))
                    tem.append(float(data[6]))
                while 0.0 in y:
                    y.remove(0.0)
                while 0.0 in y1:
                    y1.remove(0.0)
                while 0.0 in h:
                    h.remove(0.0)
                while 0.0 in w:
                    w.remove(0.0)
                while 0.0 in su:
                    su.remove(0.0)
                while 0.0 in tem:
                    tem.remove(0.0)
                if len(y) != 0:
                    self.bpaverage.setText(str("{:.2f}".format((sum(map(float,y))/len(y))))+'/'+str("{:.2f}".format((sum(map(float,y1))/len(y1)))))
                    self.bphigh.setText('أعلى قراءة انقباضية هى ' + str(max(y)))
                else:
                    self.bpaverage.setText('0.0/0.0')
                    self.bphigh.setText('أعلى قراءة انقباضية هى ' +'0.0')
                if len(y1)!=0:
                    self.bplow.setText('أدنى قراءة انبساطية هى '+str(min(y1)))
                else:
                    self.bplow.setText('أدنى قراءة انبساطية هى '+ '0.0')
                if len(h) !=0 and len(w) !=0:
                    havg = sum(map(float,h))/len(h)
                    wavg = sum(map(float,w))/len(w)
                    self.tallheight.setText('أخر طول مسجل هو '+str(h[len(h)-1]))
                    self.wznweight.setText('أخر وزن مسجل هو ' +str(w[len(w)-1]))
                    self.bmi.setText(str("{:.2f}".format((wavg/havg**2)*10000)))
                else:
                    self.tallheight.setText('أخر طول مسجل هو ' +'0.0')
                    self.wznweight.setText('أخر وزن مسجل هو ' +'0.0')
                    self.bmi.setText('0.0')
                if len(su)!=0:
                    val = su[len(su)-1]
                    if 80<= float(val) <=120:
                        suger = 'طبيعى'
                        self.glustats.setStyleSheet('''QLabel{color:#50d890;}''')
                    elif 80>su[len(su)-1]:
                        suger = 'منخفض'
                        self.glustats.setStyleSheet('''QLabel{color:#ffe227;}''')
                    else:
                        suger = 'مرتفع'
                        self.glustats.setStyleSheet('''QLabel{color:#e40017;}''')
                    self.glustats.setText(suger)
                    self.lastrec.setText('أخر قراءة مسجلة هى '+str(su[len(su)-1]))
                    self.recavg.setText('متوسط نسبة الجلوكوز '+str("{:.2f}".format((sum(map(float,su))/len(su)))))
                else:
                    self.glustats.setText('غير متاح')
                    self.glustats.setStyleSheet('''QLabel{color:#cdd0cb;}''')
                    self.lastrec.setText('أخر قراءة مسجلة هى ' + '0.0')
                    self.recavg.setText('متوسط نسبة الجلوكوز ' + '0.0')
                if len(tem)!=0:
                    self.lastreco.setText(str(tem[len(tem)-1])+' °C')
                    self.highrec.setText('أعلى درجة مسجلة هى '+str(max(tem)))
                    self.lowrec.setText('أدنى درجة مسجلة هى '+str(min(tem)))
                else:
                    self.lastreco.setText('0.0' + '°C')
                    self.highrec.setText('أعلى درجة مسجلة هى ' + '0.0')
                    self.lowrec.setText('أدنى درجة مسجلة هى ' + '0.0')
                if len(y)!=0 and len(y1) !=0:
                    self.updateAxis(x,y,y1)
                else:
                    try:
                        self.series.clear()
                        self.serie.clear()
                    except:
                        pass
            except mysql.connector.Error as err:
                self.saveErrors('Chart: '+str(err))

    def updateAxis(self,x,y,y1):
        self.series.clear()
        self.serie.clear()
        if len(x)<2:
            if len(y) ==0:
                val = 0.0
            else:
                val = y[0]
            if len(y1)==0:
                val1 = 0.0
            else:
                val1 = y1[0]
            self.axisX.setTickCount(2)
            wkt = QDateTime.currentDateTime()
            self.axisX.setMax(QDateTime.currentDateTime())
            if len(x) ==0:
                star = QDateTime.currentDateTime().addDays(-1)
                self.axisX.setMin(star)
                self.series.append(star.toMSecsSinceEpoch(),val)
                self.series.append(wkt.toMSecsSinceEpoch(), val)
                self.chart.addAxis(self.axisX, Qt.AlignBottom)
                self.chart.addSeries(self.series)
                self.chart.setAnimationOptions(QChart.SeriesAnimations)
                self.series.attachAxis(self.axisX)
                self.series.attachAxis(self.axisY)
                self.serie.append(star.toMSecsSinceEpoch(), val1)
                self.serie.append(wkt.toMSecsSinceEpoch(), val1)
                self.chart.addSeries(self.serie)
                self.serie.attachAxis(self.axisY)
                self.serie.attachAxis(self.axisX)
            elif len(x) ==1:
                sta = QDateTime.fromString(x[0], "yyyy-MM-dd hh:mm:ss").toMSecsSinceEpoch()
                self.axisX.setMin(QDateTime.fromString(x[0], "yyyy-MM-dd hh:mm:ss"))
                self.series.append(sta, val)
                self.series.append(wkt.toMSecsSinceEpoch(), val)
                self.chart.addAxis(self.axisX, Qt.AlignBottom)
                self.chart.addSeries(self.series)
                self.chart.setAnimationOptions(QChart.SeriesAnimations)
                self.series.attachAxis(self.axisX)
                self.series.attachAxis(self.axisY)
                self.serie.append(sta, val1)
                self.serie.append(wkt.toMSecsSinceEpoch(), val1)
                self.chart.addSeries(self.serie)
                self.serie.attachAxis(self.axisY)
                self.serie.attachAxis(self.axisX)
        else:
            self.axisX.setTickCount(len(x))
            for t, val in zip(x, y):
                self.series.append(QDateTime.fromString(t, "yyyy-MM-dd hh:mm:ss").toMSecsSinceEpoch(), val)
            self.chart.addAxis(self.axisX, Qt.AlignBottom)
            self.axisX.setMin(QDateTime.fromString(x[0], "yyyy-MM-dd hh:mm:ss"))
            self.axisX.setMax(QDateTime.fromString(x[len(x)-1], "yyyy-MM-dd hh:mm:ss"))
            self.chart.addSeries(self.series)
            self.chart.setAnimationOptions(QChart.SeriesAnimations)
            self.series.attachAxis(self.axisX)
            self.series.attachAxis(self.axisY)
            for b, va in zip(x, y1):
                self.serie.append(QDateTime.fromString(b, "yyyy-MM-dd hh:mm:ss").toMSecsSinceEpoch(), va)
            self.chart.addSeries(self.serie)
            self.serie.attachAxis(self.axisY)
            self.serie.attachAxis(self.axisX)

    def createChart(self):
        self.chart = QChart()
        self.series = QSplineSeries()
        self.axisY = QValueAxis()
        self.axisX = QDateTimeAxis()
        self.axisY.setLabelFormat("%.2f")
        self.axisY.setLinePenColor(self.series.pen().color())
        self.axisY.setMin(40)
        self.axisY.setMax(160)
        self.axisY.setTickCount(4)
        self.axisX.setFormat("dd-MM-yyyy")
        self.series.setName("Systolic")
        self.chart.legend().setVisible(True)
        self.chart.legend().setAlignment(Qt.AlignBottom)
        self.chart.setTitle("History-Blood Pressure")
        self.chart.addAxis(self.axisY, Qt.AlignLeft)
        self.serie = QSplineSeries()
        self.serie.setName("Diastolic")
        self.chartView = QChartView(self.chart)
        self.chartView.setRenderHint(QPainter.Antialiasing)
        hbox = QHBoxLayout()
        hbox.addWidget(self.chartView)
        self.bloodpchart.setLayout(hbox)

    def selectHistoryCard(self):
        for i in range(0,self.historyList.count()):
            if i == self.historyList.currentRow():
                shadow = QGraphicsDropShadowEffect(blurRadius=30, xOffset=0, yOffset=0)
                self.historyList.itemWidget(self.historyList.item(self.historyList.currentRow())).setGraphicsEffect(shadow)
            else:
                shadow = QGraphicsDropShadowEffect(blurRadius=3, xOffset=0, yOffset=0)
                self.historyList.itemWidget(self.historyList.item(i)).setGraphicsEffect(shadow)

    def historyCards(self,uid):
        if mySQL80 == True:
            try:
                sql = '''SELECT his_moed,his_typename,his_tashkhes,his_smoke,his_kohol,his_blood,his_lblood,his_height,his_weight,his_suger FROM history WHERE his_qrrandom=%s AND his_exam='2' '''
                self.cur.execute(sql,[(uid)])
                fetch = self.cur.fetchall()
                self.historyList.clear()
                for r,rdata in enumerate(fetch):
                    widget = patientCard.listwidget()
                    widget.tarekh.setText(rdata[0])
                    widget.hagz.setText(rdata[1])
                    widget.tash.setText(rdata[2])
                    if rdata[3] == 'Yes':
                        widget.smoke.setHidden(False)
                    else:
                        widget.smoke.setHidden(True)
                    if rdata[4] == 'Yes':
                        widget.drink.setHidden(False)
                    else:
                        widget.drink.setHidden(True)
                    widget.dakhd.setText(str(rdata[5])+'/'+str(rdata[6]))
                    widget.tall.setText(str(rdata[7]))
                    widget.wzn.setText(str(rdata[8]))
                    widget.suker.setText(str(rdata[9]))
                    widget.setObjectName(uid)
                    listItem = QListWidgetItem()
                    listItem.setSizeHint(widget.sizeHint())
                    self.historyList.addItem(listItem)
                    self.historyList.setItemWidget(listItem, widget)
                self.selectHistoryCard()
            except mysql.connector.Error as err:
                self.saveErrors('HistoryCards: '+ str(err))

    def viewDateLog(self):
        if mySQL80 == True:
            try:
                self.historydock.show()
                self.historydock.showNormal()
                self.dwid.listarad.clear()
                self.dwid.listdwaa.clear()
                uid = self.historyList.itemWidget(self.historyList.item(self.historyList.currentRow())).objectName()
                hist = self.historyList.itemWidget(self.historyList.item(self.historyList.currentRow())).tarekh.text()
                self.historydock.setWindowTitle(hist)
                sql = '''SELECT his_other,his_anemia,his_notes FROM history WHERE his_qrrandom=%s AND his_moed=%s'''
                self.cur.execute(sql,(uid,hist))
                fetch = self.cur.fetchall()
                if fetch[0][0] == 'No' or fetch[0][0] == '':
                    other = 'لا يوجد'
                else:
                    other = fetch[0][0]
                if fetch[0][1] == 'No' or fetch[0][1] == '':
                    anem = 'لا يوجد'
                else:
                    anem = fetch[0][1]
                if fetch[0][2] == 'No' or fetch[0][2] == '':
                    notes = 'لا يوجد'
                else:
                    notes = fetch[0][2]
                self.dwid.labeloth.setText(other)
                self.dwid.labelanemia.setText(anem)
                self.dwid.labelnotes.setPlainText(notes)
                ard = '''SELECT arad_name FROM arad WHERE arad_qrrandom=%s AND arad_history=%s '''
                self.cur.execute(ard,(uid,hist))
                arfetch = self.cur.fetchall()
                for r,rdata in enumerate(arfetch):
                    ritem = QListWidgetItem(rdata[0])
                    ritem.setTextAlignment(Qt.AlignCenter)
                    self.dwid.listarad.addItem(ritem)
                med = '''SELECT medicine_name FROM medicine WHERE medicine_qrrandom=%s AND medicine_date=%s'''
                self.cur.execute(med,(uid,hist))
                medfetch = self.cur.fetchall()
                for c,cdata in enumerate(medfetch):
                    citem = QListWidgetItem(cdata[0])
                    citem.setTextAlignment(Qt.AlignCenter)
                    self.dwid.listdwaa.addItem(citem)
            except mysql.connector.Error as err:
                self.saveErrors('ViewHistory'+str(err))

    def removePrice(self):
        self.edit.pricetable.removeRow(self.edit.pricetable.currentRow())
        lis = []
        rows = self.edit.pricetable.rowCount()
        for i in range(rows):
            x = float(self.edit.pricetable.item(i, 1).text())
            lis.append(x)
        self.edit.rowcountlabel.setText(str(len(lis)))
        self.edit.sumall.setText(str(sum(map(float, lis))))
        self.edit.allsum.setText(str(sum(map(float, lis))))

    #دالة تجديد معلومات المريض فى قائمة الانتظار
    def updatedata(self):
        if mySQL80 == True:
            try:
                uuid = self.edit.qrr.text()
                ddate = self.edit.datevie.text()
                if self.edit.radioest.isChecked():
                    ty = 1
                    tyname = 'إستشارة'
                else:
                    ty = 0
                    tyname = 'كشف'

                if self.edit.cgender.currentIndex() == 0:
                    gender = 0
                    gendername = 'ذكر'
                else:
                    gender = 1
                    gendername = 'أنثى'
                age = self.edit.sAge.value()
                phone = self.edit.lPhone.text()
                address = self.edit.lAddress.text()
                soical = self.edit.social.currentIndex()
                suger = self.edit.sugerSpinBox.value()
                height = self.edit.heightSpinBox.value()
                weight = self.edit.weightSpinBox.value()
                highBlood = self.edit.highSpinBox.value()
                lowBlood = self.edit.lowSpinBox.value()
                temp = self.edit.tempSpinBox.value()
                moad = self.edit.moaddateEdit.text()
                moadTime = self.edit.moadtime.currentText()
                if self.edit.checkhagz.isChecked():
                    moaked = 'مؤكد'
                else:
                    moaked = 'غير مؤكد'
                way = self.edit.waycomboBox.currentIndex()
                fullname = self.edit.fPatientName.text()+self.edit.sPatientName.text()+self.edit.flPatientName.text()+self.edit.lPatientName.text()
                if len(self.edit.fPatientName.text()) > 0 and len(self.edit.sPatientName.text()) > 0 and len(
                        self.edit.flPatientName.text()) > 0:
                    patienFullName = self.edit.lPatientName.text() + ' ' + self.edit.flPatientName.text() + ' ' + self.edit.sPatientName.text() + ' ' + self.edit.fPatientName.text()
                elif len(self.edit.fPatientName.text()) == 0 and len(self.edit.sPatientName.text()) > 0 and len(
                        self.edit.flPatientName.text()) > 0:
                    patienFullName = self.edit.lPatientName.text() + ' ' + self.edit.flPatientName.text() + ' ' + self.edit.sPatientName.text()
                elif len(self.edit.fPatientName.text()) == 0 and len(self.edit.sPatientName.text()) == 0 and len(
                        self.edit.flPatientName.text()) > 0:
                    patienFullName = self.edit.lPatientName.text() + ' ' + self.edit.flPatientName.text()
                else:
                    patienFullName = self.edit.lPatientName.text()
                self.getpaymentUpdate()
                exSQL = '''UPDATE history SET his_type=%s,his_typename=%s,his_patientname=%s,his_age=%s,his_gender=%s,his_gendername=%s,his_phone=%s,his_address=%s,his_pricetype=%s,his_payment=%s,his_soical=%s,his_suger=%s,his_height=%s,his_weight=%s,his_blood=%s,his_lblood=%s,his_moed=%s,his_timemoed=%s,his_moaked=%s,his_way=%s,his_payname=%s,his_temp=%s,his_cost=%s WHERE his_qrrandom=%s AND his_moed=%s'''
                value = (ty,tyname,patienFullName,age,gender,gendername,phone,address,self.pricetype,self.paymenthagz,soical,suger,height,weight,highBlood,lowBlood,moad,moadTime,moaked,way,self.payname,temp,self.cost,uuid,ddate)
                self.cur.execute(exSQL, value)
                if connect == None:
                    command = self.cur.statement
                    self.saveCommand(command)
                else:
                    try:
                        dbcur.execute(exSQL, value)
                        dbconnect.commit()
                    except:
                        command = self.cur.statement
                        self.saveCommand(command)
                    text = 'edit'
                    connn.send(text.encode("utf-8"))
                self.db.commit()
                self.edit.terminate()
                self.showToaster('تم!', 'تم الحفظ بنجاح.', ':/MainSources/check.gif', '#16c79a', 'MainSources/correct.wav',
                                     1,2000)
                self.loadkashftable()
            except mysql.connector.Error as err:
                self.showToaster('عفواً!', 'حدث خطأ أثناء المحاولة.', ':/MainSources/close.gif', '#ec0101',
                                 'MainSources/fail.wav', 1, 2000)
                self.saveErrors('EditError'+str(err))


    #دالة حفظ المبلغ المدفوع
    def getpayment(self):
        self.payname = ''
        if self.addform.checkpaid.isChecked():
            if self.addform.priceb.isChecked() == False:
                self.pricetype = 'مدفوع'
                if self.addform.radiokashf.isChecked():
                    self.payname = 'كشف'
                    self.paymenthagz = self.addform.pricekashf.currentText()
                    self.cost = '0'
                else:
                    self.payname = 'إستشارة'
                    self.paymenthagz = self.addform.priceest.currentText()
                    self.cost = '0'
            else:
                count = self.addform.pricetable.rowCount()
                self.pricetype = 'مدفوع'
                self.cost = '0'
                if count != 0:
                    for i in range(count):
                        itemname = self.addform.pricetable.item(i,0).text()
                        itemprice = self.addform.pricetable.item(i,1).text()
                        if i == (count-1):
                            self.payname += (itemname+'  '+itemprice)
                        else:
                            self.payname += (itemname + '  ' + itemprice + ',')
                    self.paymenthagz = self.addform.allsum.text()
                else:
                    self.pricetype = 'غير مدفوع'
                    self.paymenthagz = '0'
        else:
            if self.addform.priceb.isChecked() == False:
                if self.addform.radiokashf.isChecked():
                    self.cost = self.addform.pricekashf.currentText()
                else:
                    self.cost = self.addform.priceest.currentText()
            else:
                count = self.addform.pricetable.rowCount()
                if count != 0:
                    for i in range(count):
                        itemname = self.addform.pricetable.item(i,0).text()
                        itemprice = self.addform.pricetable.item(i,1).text()
                        if i == (count-1):
                            self.payname += (itemname+'  '+itemprice)
                        else:
                            self.payname += (itemname + '  ' + itemprice + ',')
                    self.cost = self.addform.allsum.text()
            self.pricetype = 'غير مدفوع'
            self.paymenthagz = '0'

    def getpaymentUpdate(self):
        self.payname = ''
        if self.edit.checkpaid.isChecked():
            if self.edit.priceb.isChecked() == False:
                self.pricetype = 'مدفوع'
                if self.edit.radiokashf.isChecked():
                    self.payname = 'كشف'
                    self.paymenthagz = self.edit.pricekashf.currentText()
                    self.cost = '0'
                elif self.edit.radioest.isChecked():
                    self.payname = 'إستشارة'
                    self.paymenthagz = self.edit.priceest.currentText()
                    self.cost = '0'
            else:
                count = self.edit.pricetable.rowCount()
                self.pricetype = 'مدفوع'
                self.cost = '0'
                if count != 0:
                    for i in range(count):
                        itemname = self.edit.pricetable.item(i, 0).text()
                        itemprice = self.edit.pricetable.item(i, 1).text()
                        if i == (count - 1):
                            self.payname += (itemname + '  ' + itemprice)
                        else:
                            self.payname += (itemname + '  ' + itemprice + ',')
                    self.paymenthagz = self.edit.allsum.text()
                else:
                    self.pricetype = 'غير مدفوع'
                    self.paymenthagz = '0'
        else:
            if self.edit.priceb.isChecked() == False:
                if self.edit.radiokashf.isChecked():
                    self.payname = 'كشف'
                    self.cost = self.edit.pricekashf.currentText()
                else:
                    self.payname = 'إستشارة'
                    self.cost = self.edit.priceest.currentText()
            else:
                count = self.edit.pricetable.rowCount()
                if count != 0:
                    for i in range(count):
                        itemname = self.edit.pricetable.item(i, 0).text()
                        itemprice = self.edit.pricetable.item(i, 1).text()
                        if i == (count - 1):
                            self.payname += (itemname + '  ' + itemprice)
                        else:
                            self.payname += (itemname + '  ' + itemprice + ',')
                    self.cost = self.edit.allsum.text()
            self.pricetype = 'غير مدفوع'
            self.paymenthagz = '0'

    #دالة حفظ وادخال الحجز الجديد
    def savedata(self):
        try:
            self.getpayment()
            if self.patienFullName in self.liss:
                self.stat = 'قديم'
            else:
                self.stat = 'جديد'
            if self.addform.radioest.isChecked():
                ty = 1
                tyname = 'إستشارة'
                est = 1
            else:
                ty = 0
                tyname = 'كشف'
                est = 0
            if self.addform.cgender.currentIndex() == 0:
                gender = 0
                gendername = 'ذكر'
            else:
                gender = 1
                gendername = 'أنثى'
            age = self.addform.sAge.value()
            phone = self.addform.lPhone.text()
            address = self.addform.lAddress.text()
            uid = self.addform.qrr.text()
            hagzTime = str(datetime.now().strftime("%H:%M:%S"))
            today = str(date.today())
            exam = 0
            done = 0
            active = 0
            soical = self.addform.social.currentIndex()
            suger = self.addform.sugerSpinBox.value()
            height = self.addform.heightSpinBox.value()
            weight = self.addform.weightSpinBox.value()
            highBlood = self.addform.highSpinBox.value()
            temp = self.addform.tempSpinBox.value()
            lowBlood = self.addform.lowSpinBox.value()
            moad = self.addform.moaddateEdit.text()
            moadTime = self.addform.moadtime.currentText()
            if self.addform.checkhagz.isChecked():
                moaked = 'مؤكد'
            else:
                moaked = 'غير مؤكد'
            way = self.addform.waycomboBox.currentIndex()
            if self.patienFullName in self.liss:
                if mySQL80 == True:
                    try:
                        sql = '''UPDATE hagz SET hagz_patientname=%s,hagz_age=%s,hagz_gender=%s,hagz_gendername=%s,hagz_phone=%s,hagz_address=%s,hagz_soical=%s,hag_date=%s,hagz_est=%s WHERE hagz_qrrandom = %s'''
                        vale = (self.patienFullName, age, gender, gendername, phone, address, soical, moad,est, uid)
                        self.cur.execute(sql,vale)
                        if connect == None:
                            command = self.cur.statement
                            self.saveCommand(command)
                        else:
                            try:
                                dbcur.execute(sql,vale)
                                dbconnect.commit()
                            except:
                                command = self.cur.statement
                                self.saveCommand(command)
                    except mysql.connector.Error as err:
                        self.showToaster('عفواً!', 'حدث خطأ أثناء المحاولة.', ':/MainSources/close.gif', '#ec0101',
                                         'MainSources/fail.wav', 1, 2000)
                        self.saveErrors('SaveData: ' + str(err))
                else:
                    self.showToaster('عفواً!', 'خطأ الاتصال بقاعدة البيانات.', ':/MainSources/close.gif', '#ec0101',
                                     'MainSources/fail.wav', 1, 2000)
            else:
                if mySQL80 == True:
                    try:
                        sql = '''INSERT INTO hagz(hagz_patientname,hagz_age,hagz_gender,hagz_gendername,hagz_phone,hagz_address,hagz_qrrandom,hagz_soical,hag_date,hagz_est) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'''
                        val = (self.patienFullName,age,gender,gendername,phone,address,uid,soical,moad,est)
                        self.cur.execute(sql,val)
                        if connect == None:
                            command = self.cur.statement
                            self.saveCommand(command)
                        else:
                            try:
                                dbcur.execute(sql,val)
                                dbconnect.commit()
                            except:
                                command = self.cur.statement
                                self.saveCommand(command)
                    except mysql.connector.Error as err:
                        self.showToaster('عفواً!', 'حدث خطأ أثناء المحاولة.', ':/MainSources/close.gif', '#ec0101',
                                         'MainSources/fail.wav', 1, 2000)
                        self.saveErrors('SaveData: ' + str(err))
                else:
                    self.showToaster('عفواً!', 'خطأ الاتصال بقاعدة البيانات.', ':/MainSources/close.gif', '#ec0101',
                                     'MainSources/fail.wav', 1, 2000)
            if mySQL80 == True:
                try:
                    exSQL = '''INSERT INTO history(his_date,his_type,his_typename,his_patientname,his_age,his_gender,his_gendername,his_phone,his_address,his_qrrandom,his_time,his_patientstat,his_exam,his_done,his_active,his_pricetype,his_payment,his_cost,his_soical,his_suger,his_height,his_weight,his_blood,his_lblood,his_moed,his_timemoed,his_moaked,his_way,his_payname,his_temp) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'''
                    value = (today,ty,tyname,self.patienFullName,age,gender,gendername,phone,address,uid,hagzTime,self.stat,exam,done,active,self.pricetype,self.paymenthagz,self.cost,soical,suger,height,weight,highBlood,lowBlood,moad,moadTime,moaked,way,str(self.payname),temp)
                    self.cur.execute(exSQL, value)
                    if connect == None:
                        command = self.cur.statement
                        self.saveCommand(command)
                    else:
                        try:
                            dbcur.execute(exSQL, value)
                            dbconnect.commit()
                        except:
                            command = self.cur.statement
                            self.saveCommand(command)
                        text = 'reload'
                        connn.send(text.encode("utf-8"))
                    self.db.commit()
                    self.addform.terminate()
                    self.showToaster('تم!', 'تم الحفظ بنجاح.', ':/MainSources/check.gif', '#16c79a', 'MainSources/correct.wav',
                                         1,2000)
                    self.loadkashftable()
                    self.loadesttable()
                    self.tabWidget.setCurrentIndex(0)
                    self.listWidget.setCurrentRow(0)
                except mysql.connector.Error as err:
                    self.saveErrors('SaveData: ' + str(err))
        except:
            self.saveErrors('Save Data Error')


    def addNotesToNotes(self):
        text = self.noterenter.text()
        self.notesedit.append('* '+text)
        self.noterenter.setText('')

    def countNotesLetters(self):
        text = self.notesedit.toPlainText()
        self.notescount.setText(str(len(text)))


    def secondDatabaseConnect(self):
        if dbconnect != None:
            self.sqlstatus2.setText("متصل")
            self.db2disconnect.setHidden(True)
            self.db2connect.setVisible(True)
        else:
            self.sqlstatus2.setText("غير متصل")
            self.db2connect.setHidden(True)
            self.db2disconnect.setVisible(True)

    #دالة الإتصال بقاعدة البيانات
    def databaseconnect(self):
        host = self.set.value("LocalIP")
        username = self.set.value("Admin")
        password = self.set.value("AdminPass")
        dbname = self.set.value("DBName")
        if mySQL80 == True:
            try:
                self.db = mysql.connector.connect(host=host,user=username,passwd=password,database=dbname,auth_plugin='mysql_native_password')
                self.cur = self.db.cursor()
                self.db1connect.setVisible(True)
                self.db1disconnect.setHidden(True)
                self.sqlstatus.setText('متصل')
                self.loadkashftable()
                self.loadesttable()
                self.loaddoctable()
                self.enablebtn()
                self.checkesttable()
                self.enbtntash()
                self.loadmedsettings()
                self.loadvarsettings()
                self.loadtashsettings()
            except mysql.connector.Error as err:
                self.saveErrors('dataconnect'+str(err))
                self.hagzlistwid.clear()
                self.db1connect.setHidden(True)
                self.db1disconnect.setVisible(True)
                self.sqlstatus.setText('غير متصل')
                self.esttablewidget.setRowCount(0)
                self.esttablewidget.selectRow(-1)
                self.doctable.setRowCount(0)
                self.doctable.selectRow(-1)
                self.enablebtn()
                self.checkesttable()
                self.enbtntash()
        else:
            self.hagzlistwid.clear()
            self.db1connect.setHidden(True)
            self.db1disconnect.setVisible(True)
            self.sqlstatus.setText('غير متصل')
            self.esttablewidget.setRowCount(0)
            self.esttablewidget.selectRow(-1)
            self.doctable.setRowCount(0)
            self.doctable.selectRow(-1)
            self.enablebtn()
            self.checkesttable()
            self.enbtntash()

    def closeDBConnection(self):
        self.cur.close()
        self.db.close()
        self.hagzlistwid.clear()
        self.db1connect.setHidden(True)
        self.db1disconnect.setVisible(True)
        self.sqlstatus.setText('غير متصل')
        self.esttablewidget.setRowCount(0)
        self.esttablewidget.selectRow(-1)
        self.doctable.setRowCount(0)
        self.doctable.selectRow(-1)
        self.enablebtn()
        self.checkesttable()
        self.enbtntash()


    #دالة تنظيم الجداول
    def designtables(self):
        self.medtable.horizontalHeader().setSectionResizeMode(0, QHeaderView.Stretch)
        self.medtable.setColumnWidth(1,100)
        self.medtable.setColumnWidth(2,100)
        self.medtable.setColumnWidth(3, 30)
        self.esttablewidget.setColumnWidth(0, 40)
        self.esttablewidget.setColumnWidth(1, 90)
        self.esttablewidget.setColumnWidth(2, 200)
        self.esttablewidget.setColumnWidth(3, 90)
        self.esttablewidget.horizontalHeader().setSectionResizeMode(4, QHeaderView.Stretch)
        self.esttablewidget.setColumnWidth(5, 150)
        self.doctable.setColumnWidth(0, 40)
        self.doctable.setColumnWidth(1,90)
        self.doctable.setColumnWidth(2,90)
        self.doctable.setColumnWidth(3,90)
        self.doctable.setColumnWidth(4,90)
        self.doctable.setColumnWidth(5,90)
        self.doctable.horizontalHeader().setSectionResizeMode(6, QHeaderView.Stretch)
        self.doctable.setColumnWidth(7,150)
        self.doctable.setColumnHidden(8, True)
        self.tabarad.horizontalHeader().setSectionResizeMode(0, QHeaderView.Stretch)
        self.tabarad.setColumnWidth(1, 40)
        self.tabletah.horizontalHeader().setSectionResizeMode(0, QHeaderView.Stretch)
        self.tabletah.setColumnWidth(1, 40)
        self.vartable.horizontalHeader().setSectionResizeMode(0, QHeaderView.Stretch)
        self.vartable.setColumnWidth(1,85)
        self.vartable.setColumnWidth(2,85)
        self.vartable.setColumnWidth(3,50)
        self.vartable.setColumnWidth(4,0)
        self.vartable.setColumnWidth(5,40)
        self.medlisst.horizontalHeader().setSectionResizeMode(0,QHeaderView.Stretch)
        self.medlisst.setColumnWidth(1,0)
        self.medlisst.setColumnWidth(2,40)
        self.tashtable.horizontalHeader().setSectionResizeMode(0,QHeaderView.Stretch)
        self.tashtable.setColumnWidth(1,0)
        self.tashtable.setColumnWidth(2,40)
        self.patienttable.horizontalHeader().setSectionResizeMode(0,QHeaderView.Stretch)
        self.patienttable.setColumnWidth(1,90)
        self.patienttable.horizontalHeader().setSectionResizeMode(2,QHeaderView.Stretch)
        self.patienttable.setColumnWidth(3,150)
        self.patienttable.setColumnWidth(4,150)
        self.tasktable.setColumnWidth(1,20)
        self.tasktable.setColumnWidth(2,20)
        self.tasktable.setColumnWidth(3,20)
        self.tasktable.setColumnHidden(4,True)
        self.tasktable.horizontalHeader().setSectionResizeMode(0,QHeaderView.Stretch)


    #دالة عرض قاعدة البيانات فى جدول الكشف
    def loadkashftable(self):
        today = str(date.today())
        if mySQL80 == True:
            try:
                sql = '''SELECT his_moed,his_timemoed,his_typename,his_moaked,his_patientname,his_phone,his_pricetype,his_payment,his_cost,his_qrrandom,his_payname,his_way,his_exam,his_gender,his_address,his_age,his_date,his_time,his_patientstat,his_blood,his_lblood,his_height,his_weight,his_suger,his_temp FROM history WHERE his_moed=%s OR his_active=1 AND his_moed=%s'''
                self.cur.execute(sql,(today,today))
                fetch = self.cur.fetchall()
                self.hagzlistwid.clear()
                for r,rdata in enumerate(fetch):
                    widget = tableHagz.tableOne()
                    widget.rakm.setText('#'+str(r+1))
                    s = rdata[0]
                    d = datetime.strptime(s, '%Y-%m-%d')
                    fd = d.strftime('%b %d, %Y')
                    widget.tareekh.setText(str(fd))
                    widget.wakt.setText(str(rdata[1]))
                    widget.hagz.setText(rdata[2])
                    widget.moak.setText(rdata[3])
                    if rdata[3] == 'مؤكد':
                        widget.moak.setStyleSheet('''QLabel{padding-left:5px;padding-right:5px;height:30px;border-radius:10px;color:#3cc13b;background-color:#ebf9eb;}''')
                    elif rdata[3] == 'غير مؤكد':
                        widget.moak.setStyleSheet('''QLabel{padding-left:5px;padding-right:5px;height:30px;border-radius:10px;color:#f3bb1c;background-color:#fef8e8;}''')
                    else:
                        widget.moak.setStyleSheet('''QLabel{padding-left:5px;padding-right:5px;height:30px;border-radius:10px;color:#f13e3f;background-color:#fdebeb;}''')
                    widget.esm.setText(rdata[4])
                    if len(rdata[5])==0:
                        widget.phone.setText('No Phone')
                    else:
                        widget.phone.setText('('+rdata[5][0:3]+')'+' '+rdata[5][3:6]+'-'+rdata[5][6:len(rdata[5])])
                    widget.paid.setText(rdata[6])
                    if rdata[6] == 'مدفوع':
                        widget.paid.setStyleSheet(
                            '''QLabel{color:#3cc13b;background-color:transparent;padding:0px;}QLabel:disabled{color:#dddddd;background-color:transparent;padding:0px;}''')
                    else:
                        widget.paid.setStyleSheet(
                            '''QLabel{color:#f13e3f;background-color:transparent;padding:0px;}QLabel:disabled{color:#dddddd;background-color:transparent;padding:0px;}''')
                    widget.money.setText('$'+rdata[7])
                    widget.cost.setText('$'+rdata[8])
                    if rdata[11] == 0:
                        wa = 'شخصيا'
                    else:
                        wa = 'هاتفيا'
                    widget.tyhagz.setText(wa)
                    #widget.setObjectName(rdata[9])
                    if rdata[12] == 0:
                        stat = 'فى الإنتظار'
                        widget.status.setPixmap(QPixmap(':/MainSources/wait.png'))
                        widget.groupBox.setTitle('انتظار')
                        widget.groupBox.setStyleSheet('''QGroupBox{color:#e27802;}''')
                        widget.hala.setStyleSheet('''QLabel{color:#ffffff;background-color:#ffc75f;border-radius:10px;}''')
                    elif rdata[12] == 1:
                        stat = 'مع الطبيب'
                        widget.status.setPixmap(QPixmap(':/MainSources/in.png'))
                        widget.groupBox.setTitle('فحص')
                        widget.groupBox.setStyleSheet('''QGroupBox{color:#00af91;}''')
                        widget.hala.setStyleSheet('''QLabel{color:#ffffff;background-color:#00af91;border-radius:10px;}''')
                    elif rdata[12] == 2:
                        stat = 'تم الإنتهاء'
                        widget.status.setPixmap(QPixmap(':/MainSources/out.png'))
                        widget.groupBox.setTitle('انتهى')
                        widget.groupBox.setStyleSheet('''QGroupBox{color:#91091e;}''')
                        widget.hala.setStyleSheet('''QLabel{color:#ffffff;background-color:#c70039;border-radius:10px;}''')
                    else:
                        stat = 'ملغى'
                        widget.status.setPixmap(QPixmap(':/MainSources/off.png'))
                        widget.groupBox.setTitle('ملغى')
                        widget.groupBox.setStyleSheet('''QGroupBox{color:#a6a9b6;}''')
                        widget.hala.setStyleSheet('''QLabel{color:#a6a9b6;background-color:#eeeded;border-radius:10px;}''')
                    widget.hala.setText(stat)
                    widget.gens.setCurrentIndex(rdata[13])
                    if rdata[14] == '':
                        addres = 'لا يوجد'
                    else:
                        addres = rdata[14]
                    widget.enwan.setText(addres)
                    widget.age.setText(str(rdata[15])+' عام/أعوام')
                    widget.date.setText(rdata[16])
                    widget.tim.setText(rdata[17])
                    widget.pastat.setText(rdata[18])
                    widget.bpressure.setText(rdata[19])
                    widget.lblood.setText(rdata[20])
                    widget.height.setText(rdata[21])
                    widget.weight.setText(rdata[22])
                    widget.diabetes.setText(rdata[23])
                    widget.temp.setText(rdata[24])
                    widget.tareef.setText(rdata[9])
                    widget.ezhar.clicked.connect(self.resizelist)
                    listItem = QListWidgetItem()
                    listItem.setSizeHint(widget.sizeHint())
                    global size
                    size = widget.sizeHint()
                    self.hagzlistwid.addItem(listItem)
                    self.hagzlistwid.setItemWidget(listItem, widget)
                self.selectit()
                rows = self.hagzlistwid.count()
                lis = []
                for row in range(0, rows):
                    if self.hagzlistwid.itemWidget(self.hagzlistwid.item(row)).hala.text() == 'فى الإنتظار':
                        item = self.hagzlistwid.itemWidget(self.hagzlistwid.item(row)).hagz.text()
                        lis.append(item)
                self.lcdNumber.setText(str(len(lis)))
                self.lcdNumberk.setText(str(lis.count('كشف')))
                self.lcdNumbere.setText(str(lis.count('إستشارة')))
                self.allEarnToday()
                self.allPeopleToday()
            except mysql.connector.Error as err:
                self.saveErrors('LoadKasf: ' + str(err))


    def resizelist(self):
        widget = self.sender()
        gp = widget.mapToGlobal(QPoint())
        lp = self.hagzlistwid.viewport().mapFromGlobal(gp)
        row = self.hagzlistwid.row(self.hagzlistwid.itemAt(lp))
        self.hagzlistwid.setCurrentRow(row)
        self.selectit()
        if self.hagzlistwid.itemWidget(self.hagzlistwid.item(row)).ezhar.text() == 'إخفاء':
            item  = self.hagzlistwid.item(row)
            item.setSizeHint(self.hagzlistwid.itemWidget(self.hagzlistwid.item(row)).sizeHint())
        else:
            item = self.hagzlistwid.item(row)
            item.setSizeHint(size)

    #دالة عرض بداية ونهاية تواريخ الاستشارة
    def daterange(self, start_date, end_date):
        for n in range(int((end_date - start_date).days)):
            yield start_date + timedelta(n)

    def insertTodoList(self):
        if self.radiono2.isChecked() == True:
            notify = 'Yes'
        else:
            notify = 'No'
        sql = '''INSERT INTO todolist(todolist_date,todolist_task,todolist_status,todolist_qr,todolist_name,todolist_notify,todolist_icon) VALUES(%s,%s,%s,%s,%s,%s,%s)'''
        value = (self.viewdate.text(),self.tasktextEdit.toPlainText(),'waiting',self.viewuid.text(),self.taskline.text(),notify,self.tasklevel.currentIndex())
        self.cur.execute(sql,value)
        if connect == None:
            command = self.cur.statement
            self.saveCommand(command)
        else:
            try:
                dbcur.execute(sql,value)
                dbconnect.commit()
            except:
                command = self.cur.statement
                self.saveCommand(command)
        self.db.commit()
        self.loadTodoList()
        self.taskline.setText('')
        self.ttaskWidget.setCurrentIndex(0)

    def loadTodoList(self):
        sql = '''SELECT todolist_name,todolist_status,idtodolist,todolist_notify,todolist_date FROM todolist WHERE todolist_qr = %s'''
        self.cur.execute(sql,[(self.viewuid.text())])
        fetch = self.cur.fetchall()
        if len(fetch) == 0:
            self.taskshow.setHidden(False)
            self.tasktable.setHidden(True)
        else:
            self.taskshow.setHidden(True)
            self.tasktable.setHidden(False)
            self.tasktable.setRowCount(0)
            num = 0
            notif = 0
            for r,rdata in enumerate(fetch):
                shadow = QGraphicsDropShadowEffect(blurRadius=5, xOffset=0, yOffset=0)
                self.tasktable.insertRow(r)
                if rdata[1] == 'waiting':
                    if rdata[3] == 'Yes' and self.viewdate.text() != str(rdata[4]):
                        notif += 1
                    num+=1
                else:
                    pass
                self.taskcount.setText(str(num))
                item = QTableWidgetItem(str(rdata[0]))
                font = QFont('Segoe UI',9)
                font.setStrikeOut(True)
                item.setToolTip(str(rdata[0]))
                if rdata[1] == 'waiting':
                    showbtn = QPushButton('')
                    showbtn.setIcon(QIcon(':/MainSources/details.png'))
                    showbtn.clicked.connect(self.showTaskDetails)
                    editbtn = QPushButton('')
                    editbtn.setIcon(QIcon(':/MainSources/edit.png'))
                    editbtn.clicked.connect(self.editTask)
                    waitbtn = QPushButton('')
                    waitbtn.setIcon(QIcon(':/MainSources/checkmark.png'))
                    waitbtn.clicked.connect(self.doTodoList)
                    self.tasktable.setCellWidget(r, 1, showbtn)
                    self.tasktable.setCellWidget(r, 2, editbtn)
                    self.tasktable.setCellWidget(r,3,waitbtn)
                else:
                    item.setFont(font)
                    donebtn = QPushButton('')
                    donebtn.setIcon(QIcon(':/MainSources/xred.png'))
                    donebtn.clicked.connect(self.deleteTodoList)
                    self.tasktable.setCellWidget(r, 3, donebtn)
                self.tasktable.setItem(r, 0, item)
                ite = QTableWidgetItem()
                ite.setData(Qt.EditRole,rdata[2])
                self.tasktable.setItem(r,4,ite)
                self.tasktable.setGraphicsEffect(shadow)
            self.tasktable.sortItems(4, Qt.DescendingOrder)


    def showTaskDetails(self):
        self.tasklogo.setPixmap(QPixmap(':/MainSources/listvi.png'))
        self.taskmode.setText('تفاصيل المهمة')
        self.taskmode.setFont(self.font)
        sql = '''SELECT todolist_name,todolist_task,todolist_icon,todolist_notify,todolist_date FROM todolist WHERE idtodolist=%s '''
        self.cur.execute(sql,[(int(self.tasktable.item(self.tasktable.currentRow(),4).text()))])
        fetch = self.cur.fetchall()
        self.taskline.setText(str(fetch[0][0]))
        self.tasktextEdit.setPlainText(str(fetch[0][1]))
        self.tasklevel.setCurrentIndex(fetch[0][2])
        self.dddate.setHidden(False)
        self.ddate.setHidden(False)
        self.dddate.setText(str(fetch[0][4]))
        if str(fetch[0][3]) == 'Yes':
            self.radioyes2.setChecked(True)
            self.radiono2.setChecked(False)
            self.colorgboxnotif()
        else:
            self.radiono2.setChecked(True)
            self.radioyes2.setChecked(False)
            self.colorgboxnotify()
        self.taskline.setReadOnly(True)
        self.tasktextEdit.setReadOnly(True)
        self.tasklevel.setEnabled(False)
        self.gBox2.setEnabled(False)
        self.editbttn.setHidden(True)
        self.addtask.setHidden(True)
        self.ttaskWidget.setCurrentIndex(1)


    def editTask(self):
        self.tasklogo.setPixmap(QPixmap(':/MainSources/listedit.png'))
        self.taskmode.setText('تعديل المهمة')
        self.taskmode.setFont(self.font)
        sql = '''SELECT todolist_name,todolist_task,todolist_icon,todolist_notify FROM todolist WHERE idtodolist=%s '''
        self.cur.execute(sql, [(int(self.tasktable.item(self.tasktable.currentRow(), 4).text()))])
        fetch = self.cur.fetchall()
        self.taskline.setText(str(fetch[0][0]))
        self.tasktextEdit.setPlainText(str(fetch[0][1]))
        self.tasklevel.setCurrentIndex(fetch[0][2])
        self.taskid.setText(str(self.tasktable.item(self.tasktable.currentRow(), 4).text()))
        self.dddate.setHidden(True)
        self.ddate.setHidden(True)
        if str(fetch[0][3]) == 'Yes':
            self.radioyes2.setChecked(True)
            self.radiono2.setChecked(False)
            self.colorgboxnotif()
        else:
            self.radiono2.setChecked(True)
            self.radioyes2.setChecked(False)
            self.colorgboxnotify()
        self.taskline.setReadOnly(False)
        self.tasktextEdit.setReadOnly(False)
        self.tasklevel.setEnabled(True)
        self.gBox2.setEnabled(True)
        self.addtask.setHidden(True)
        self.editbttn.setHidden(False)
        self.ttaskWidget.setCurrentIndex(1)


    def updateTask(self):
        if self.radiono2.isChecked() == True:
            notify = 'Yes'
        else:
            notify = 'No'
        sql = '''UPDATE todolist SET todolist_name=%s,todolist_task=%s,todolist_icon=%s,todolist_notify=%s,todolist_date=%s WHERE idtodolist = %s'''
        value = (self.taskline.text(),self.tasktextEdit.toPlainText(),self.tasklevel.currentIndex(),notify,self.viewdate.text(),int(self.taskid.text()))
        self.cur.execute(sql,value)
        self.db.commit()
        self.ttaskWidget.setCurrentIndex(0)
        self.loadTodoList()

    def showaddTask(self):
        self.addtask.setHidden(False)
        self.editbttn.setHidden(True)
        self.tasklogo.setPixmap(QPixmap(':/MainSources/listadd.png'))
        self.taskmode.setText('إضافة مهمة جديدة')
        self.taskmode.setFont(self.font)
        self.taskline.setText('')
        self.taskline.setReadOnly(False)
        self.tasktextEdit.setPlainText('')
        self.tasktextEdit.setReadOnly(False)
        self.tasklevel.setEnabled(True)
        self.gBox2.setEnabled(True)
        self.tasklevel.setCurrentIndex(0)
        self.radioyes2.setChecked(False)
        self.dddate.setHidden(True)
        self.ddate.setHidden(True)
        self.colorgboxnotif()
        self.ttaskWidget.setCurrentIndex(1)

    def doTodoList(self):
        sql = '''UPDATE todolist SET todolist_status='done' WHERE todolist_qr=%s AND idtodolist=%s'''
        self.cur.execute(sql,(self.viewuid.text(),int(self.tasktable.item(self.tasktable.currentRow(),4).text())))
        self.db.commit()
        self.loadTodoList()

    def deleteTodoList(self):
        sql = '''DELETE FROM todolist WHERE todolist_qr=%s AND idtodolist=%s'''
        self.cur.execute(sql,(self.viewuid.text(),int(self.tasktable.item(self.tasktable.currentRow(),4).text())))
        self.db.commit()
        self.loadTodoList()

    #دالة عرض جدول الاستشارة الاسبوع
    def loadesttable(self):
        if mySQL80 == True:
            try:
                days= int(self.set.value("EstTime"))
                start_date = date.today() - timedelta(days)
                end_date = date.today()
                daylist = []
                for single_date in self.daterange(start_date, end_date):
                    daylist.append(str(single_date))
                qrlist = '''SELECT his_qrrandom FROM history WHERE his_date IN ({}) AND his_type=0 and his_exam=2'''.format(
                ', '.join(['%s'] * len(daylist)))
                self.cur.execute(qrlist,daylist)
                fet = self.cur.fetchall()
                if len(fet) != 0:
                    qr = []
                    for ro,i in enumerate(fet):
                        qr.append(i[0])
                    qrl = list(dict.fromkeys(qr))
                    sqll = '''SELECT hag_date,hagz_patientname,hagz_phone,hagz_address,hagz_qrrandom FROM hagz WHERE hagz_qrrandom IN ({}) AND hagz_est = 0 '''.format(
                    ', '.join(['%s'] * len(qrl)))
                    self.cur.execute(sqll,qrl)
                    table1 = self.cur.fetchall()
                    if len(table1) == 0:
                        self.label15.setHidden(False)
                    else:
                        self.label15.setHidden(True)
                    self.esttablewidget.setRowCount(0)
                    for row_number , data in enumerate(table1):
                        self.esttablewidget.insertRow(row_number)
                        fo = QFont('Cairo', 10)
                        ite = QTableWidgetItem(str(row_number+1))
                        ite.setTextAlignment(Qt.AlignCenter)
                        self.esttablewidget.setItem(row_number, 0, ite)
                        itdate = QTableWidgetItem(str(data[0]))
                        itdate.setTextAlignment(Qt.AlignCenter)
                        nam = QTableWidgetItem(str(data[1]))
                        nam.setFont(fo)
                        nam.setTextAlignment(Qt.AlignCenter)
                        hiss = QTableWidgetItem(str(data[2]))
                        hiss.setTextAlignment(Qt.AlignCenter)
                        addr = QTableWidgetItem(str(data[3]))
                        addr.setTextAlignment(Qt.AlignCenter)
                        ui = QTableWidgetItem(str(data[4]))
                        ui.setTextAlignment(Qt.AlignCenter)
                        self.esttablewidget.setItem(row_number,1, itdate)
                        self.esttablewidget.setItem(row_number, 2, nam)
                        self.esttablewidget.setItem(row_number, 3, hiss)
                        self.esttablewidget.setItem(row_number, 4, addr)
                        self.esttablewidget.setItem(row_number, 5, ui)
                        shadow = QGraphicsDropShadowEffect(blurRadius=5, xOffset=0, yOffset=0)
                        self.esttablewidget.setGraphicsEffect(shadow)
                self.checkesttable()
            except mysql.connector.Error as err:
                #print('loadest'+str(err))
                pass

    #دالة عرض قائمة الطبيب
    def loaddoctable(self):
        try:
            today = str(date.today())
            docSQL = '''SELECT his_timemoed,his_typename,his_patientstat,his_pricetype,his_payment,his_patientname,his_qrrandom,his_moed FROM history WHERE his_moed = %s AND his_exam=1 AND his_done=0'''
            self.cur.execute(docSQL,[(today)])
            table = self.cur.fetchall()
            self.doctable.setRowCount(0)
            for row_number, data in enumerate(table):
                self.doctable.insertRow(row_number)
                fo = QFont('Cairo', 10)
                shadow = QGraphicsDropShadowEffect(blurRadius=5, xOffset=0, yOffset=0)
                ite = QTableWidgetItem(str(row_number + 1))
                ite.setTextAlignment(Qt.AlignCenter)
                self.doctable.setItem(row_number, 0, ite)
                itdate = QTableWidgetItem(str(data[0]))
                itdate.setTextAlignment(Qt.AlignCenter)
                hag = QTableWidgetItem(str(data[1]))
                hag.setTextAlignment(Qt.AlignCenter)
                hala = QTableWidgetItem(str(data[2]))
                hala.setTextAlignment(Qt.AlignCenter)
                pric = QTableWidgetItem(str(data[3]))
                pric.setTextAlignment(Qt.AlignCenter)
                daf = QTableWidgetItem(str(data[4]))
                daf.setTextAlignment(Qt.AlignCenter)
                nam = QTableWidgetItem(str(data[5]))
                nam.setFont(fo)
                nam.setTextAlignment(Qt.AlignCenter)
                ui = QTableWidgetItem(str(data[6]))
                ui.setTextAlignment(Qt.AlignCenter)
                self.doctable.setItem(row_number, 1, itdate)
                self.doctable.setItem(row_number, 2, hag)
                self.doctable.setItem(row_number, 3, hala)
                self.doctable.setItem(row_number, 4, pric)
                self.doctable.setItem(row_number, 5, daf)
                self.doctable.setItem(row_number, 6, nam)
                self.doctable.setItem(row_number, 7, ui)
                self.doctable.setItem(row_number, 8, QTableWidgetItem(str(data[7])))
                self.doctable.setGraphicsEffect(shadow)
            self.doctable.sortItems(1, Qt.AscendingOrder)
        except mysql.connector.Error as err:
            #print('loaddoc'+str(err))
            pass


    def exporttodoc(self):
        uuid = self.hagzlistwid.itemWidget(self.hagzlistwid.item(self.hagzlistwid.currentRow())).tareef.text()
        if mySQL80 == True:
            try:
                exSQL = '''UPDATE history SET his_exam=1,his_done=0,his_moaked='مؤكد' WHERE his_qrrandom = %s'''
                self.cur.execute(exSQL,[(uuid)])
                if connect == None:
                    command = self.cur.statement
                    self.saveCommand(command)
                else:
                    try:
                        dbcur.execute(exSQL,[(uuid)])
                        dbconnect.commit()
                    except:
                        command = self.cur.statement
                        self.saveCommand(command)
                    text = 'todoc'
                    connn.send(text.encode("utf-8"))
                self.db.commit()
                self.loadkashftable()
                self.loaddoctable()
            except mysql.connector.Error as err:
                self.showToaster('عفواً!', 'حدث خطأ أثناء المحاولة.', ':/MainSources/close.gif', '#ec0101',
                                 'MainSources/fail.wav', 1, 2000)
                self.saveErrors('ExportToDoc: ' + str(err))
        else:
            self.showToaster('عفواً!', 'خطأ الاتصال بقاعدة البيانات.', ':/MainSources/close.gif', '#ec0101',
                             'MainSources/fail.wav', 1, 2000)

    #دالة نقل الاستشارة لقائمة الحجز
    def exporttohagz(self):
        uuid = self.esttablewidget.item(self.esttablewidget.currentRow(), 5).text()
        stat = True
        self.updatetohagz(uuid,stat)

    #دالة الحجز من الاستشارة او البروفايل
    def updatetohagz(self,uuid,stat):
        if mySQL80 == True:
            try:
                comSQL = '''SELECT hagz_patientname FROM hagz'''
                self.cur.execute(comSQL)
                liscom = self.cur.fetchall()
                self.liss = []
                for i in liscom:
                    for data in i:
                        self.liss.append(data)
                self.addform.moadtime.clear()
                self.setTimesForHagz()
                if self.hagzlistwid.count() != 0:
                    for i in range(self.hagzlistwid.count()):
                        val = self.hagzlistwid.itemWidget(self.hagzlistwid.item(i)).wakt.text()
                        if val in self.timelist:
                            self.timelist.remove(val)
                self.addform.moadtime.addItems(self.timelist)
                self.addform.qrr.setText(str(uuid))
                sql = '''SELECT hagz_patientname,hagz_age,hagz_gender,hagz_phone,hagz_address,hagz_soical FROM hagz WHERE hagz_qrrandom=%s'''
                self.cur.execute(sql, [(uuid)])
                if connect == None:
                    command = self.cur.statement
                    self.saveCommand(command)
                else:
                    try:
                        dbcur.execute(sql, [(uuid)])
                        dbconnect.commit()
                    except:
                        command = self.cur.statement
                        self.saveCommand(command)
                    text = 'tohagz'
                    connn.send(text.encode("utf-8"))
                fetch = self.cur.fetchall()
                self.addform.radioest.setChecked(stat)
                nameList = list(fetch[0][0].split())
                self.addform.previewname.setText(fetch[0][0])
                if len(nameList) == 4:
                    self.addform.lPatientName.setText(nameList[0])
                    self.addform.flPatientName.setText(nameList[1])
                    self.addform.sPatientName.setText(nameList[2])
                    self.addform.fPatientName.setText(nameList[3])
                elif len(nameList) == 3:
                    self.addform.lPatientName.setText(nameList[0])
                    self.addform.flPatientName.setText(nameList[1])
                    self.addform.sPatientName.setText(nameList[2])
                elif len(nameList) == 2:
                    self.addform.lPatientName.setText(nameList[0])
                    self.addform.flPatientName.setText(nameList[1])
                else:
                    self.addform.lPatientName.setText(nameList[0])
                self.addform.sAge.setValue(fetch[0][1])
                self.addform.cgender.setCurrentIndex(fetch[0][2])
                self.addform.social.setCurrentIndex(fetch[0][5])
                self.addform.lPhone.setText(fetch[0][3])
                self.addform.lAddress.setText(fetch[0][4])
                self.addform.rowcountlabel.setText(str(0))
                self.addform.sumall.setText(str(0))
                self.addform.allsum.setText(str(0))
                self.completedata()
                self.addform.exec_()
            except mysql.connector.Error as err:
                self.saveErrors('ExportToHagz: ' + str(err))





    def clearhagzdialog(self):
        self.addform.previewname.setText('')
        self.addform.lPatientName.setText('')
        self.addform.flPatientName.setText('')
        self.addform.sPatientName.setText('')
        self.addform.fPatientName.setText('')
        self.addform.lPhone.setText('')
        self.addform.lAddress.setText('')
        self.addform.sAge.setValue(1)
        self.addform.cgender.setCurrentIndex(0)
        self.addform.social.setCurrentIndex(0)
        self.addform.pricetable.setRowCount(0)
        self.addform.radiokashf.setChecked(True)


    def checkesttable(self):
        if self.esttablewidget.currentRow() < 0:
            self.towaiting.setHidden(True)
        else:
            self.towaiting.setHidden(False)

    def enbtntash(self):
        if self.doctable.currentRow() < 0:
            self.exambtn.setHidden(True)
            self.continuetash.setHidden(True)
        else:
            if self.tash == None:
                self.exambtn.setHidden(False)
                self.continuetash.setHidden(True)
            else:
                self.exambtn.setHidden(True)
                self.continuetash.setHidden(False)

    def continueTash(self):
        self.tabWidget.setCurrentIndex(6)
        self.listWidget.setCurrentRow(-1)

    def enableEditKys(self):
        self.editkys.setHidden(True)
        self.savekys.setHidden(False)
        self.sugeer.setEnabled(True)
        self.heeight.setEnabled(True)
        self.weeight.setEnabled(True)
        self.lbloood.setEnabled(True)
        self.hbloood.setEnabled(True)
        self.temppa.setEnabled(True)

    def disableEditKys(self):
        self.editkys.setHidden(False)
        self.savekys.setHidden(True)
        self.sugeer.setEnabled(False)
        self.heeight.setEnabled(False)
        self.weeight.setEnabled(False)
        self.lbloood.setEnabled(False)
        self.hbloood.setEnabled(False)
        self.temppa.setEnabled(False)

    def tashkhes(self):
        if mySQL80 == True:
            try:
                self.empty()
                self.folder = os.getcwd()
                uuid = self.doctable.item(self.doctable.currentItem().row(), 7).text()
                dat = self.doctable.item(self.doctable.currentItem().row(), 8).text()
                getSQL ='''SELECT his_typename,his_moed,his_qrrandom,his_patientname,his_age,his_gendername,his_payment,his_suger,his_height,his_weight,his_blood,his_lblood,his_temp FROM history WHERE his_qrrandom= %s AND his_moed=%s'''
                self.cur.execute(getSQL,(uuid,dat))
                fetchdata = self.cur.fetchall()
                for row in fetchdata:
                    self.viewhagz.setText(row[0])
                    self.viewdate.setText(row[1])
                    self.viewuid.setText(row[2])
                    self.viewname.setText(row[3])
                    self.viewage.setText(str(row[4]))
                    self.viewgender.setText(row[5])
                    self.paidP.setText(row[6])
                    self.sugeer.setValue(float(row[7]))
                    self.heeight.setValue(float(row[8]))
                    self.weeight.setValue(float(row[9]))
                    self.lbloood.setValue(float(row[10]))
                    self.hbloood.setValue(float(row[11]))
                    self.temppa.setValue(float(row[12]))
                self.tabWidget.setCurrentIndex(6)
                self.listWidget.setCurrentRow(-1)
                link = "file:///"+self.folder.replace('\\', '/')+"/Prescription/roshview.html"
                self.url.setText(link)
                self.loadmedicine()
                if self.viewhagz.text()=='إستشارة':
                    self.logo1.setPixmap(QPixmap(':/MainSources/talk.png'))
                else:
                    self.logo1.setPixmap(QPixmap(':/MainSources/stethoscope.png'))
                self.loadTodoList()
                self.notesedit.setPlainText('')
                self.tahltag.setHidden(False)
                self.tabletah.setHidden(True)
                self.editkys.setHidden(False)
                self.savekys.setHidden(True)
                self.enbtntash()
                self.tash = 'work'
            except mysql.connector.Error as err:
                self.showToaster('عفواً!', 'حدث خطأ أثناء المحاولة.', ':/MainSources/close.gif', '#ec0101',
                                 'MainSources/fail.wav', 1, 2000)
                self.saveErrors('TashKhes: ' + str(err))
        else:
            self.showToaster('عفواً!', 'خطأ الاتصال بقاعدة البيانات.', ':/MainSources/close.gif', '#ec0101',
                             'MainSources/fail.wav', 1, 2000)


    def previewRoshImagestolist(self):
        self.listroshwidget.clear()
        for i in range(1,8):
            loc = os.getcwd()
            icon = QIcon(loc+'\RoshList\Test'+str(i)+'.png')
            item = QListWidgetItem(icon,str(i))
            self.listroshwidget.addItem(item)
        self.listroshwidget.setCurrentRow(self.set.value("CurrentRosh"))
        self.viewRoshSettings()
        
    def getcost(self):
        text, okPressed = QInputDialog.getText(self, "المطلوب", "إجمالى المبلغ المطلوب:", QLineEdit.Normal, "")
        if okPressed and text != '' and text.isdigit():
            if mySQL80 == True:
                try:
                    sql = '''UPDATE history SET his_cost=%s,his_active='1' WHERE his_qrrandom=%s AND  his_moed=%s'''
                    self.cur.execute(sql,(text,self.viewuid.text(),self.viewdate.text()))
                    if connect == None:
                        command = self.cur.statement
                        self.saveCommand(command)
                    else:
                        try:
                            dbcur.execute(sql,(text,self.viewuid.text(),self.viewdate.text()))
                            dbconnect.commit()
                        except:
                            command = self.cur.statement
                            self.saveCommand(command)
                        text = 'pay'
                        connn.send(text.encode("utf-8"))
                    self.db.commit()
                    self.loadkashftable()
                except mysql.connector.Error as err:
                    self.showToaster('عفواً!', 'حدث خطأ أثناء المحاولة.', ':/MainSources/close.gif', '#ec0101',
                                     'MainSources/fail.wav', 1, 2000)
                    self.saveErrors('GetCost: ' + str(err))
            else:
                self.showToaster('عفواً!', 'خطأ الاتصال بقاعدة البيانات.', ':/MainSources/close.gif', '#ec0101',
                                     'MainSources/fail.wav', 1, 2000)
        elif okPressed:
            self.showToaster('عفواً!', 'من فضلك أدخل رقم صحيح.', ':/MainSources/close.gif', '#ec0101',
                             'MainSources/fail.wav', 1, 2000)

    def viewEarnMoney(self):
        if self.set.value("HideMoney") == 'true':
            self.eradview.setHidden(True)
        else:
            self.eradview.setHidden(False)


    def countmed(self):
        self.medlist = []
        rows = self.medtable.rowCount()
        for row in range(0,rows):
            self.medlist.append('<ul>')
            for column in range(0,self.medtable.columnCount()-1):
                item = '<li>'+self.medtable.item(row, column).text()+'</li>'
                self.medlist.append(item)
            self.medlist.append('</ul>')
        self.neww = ' '.join(map(str, self.medlist))

    def counttah(self):
        self.tahhlist = []
        rows = self.tabletah.rowCount()
        self.tahhlist.append('<ol>')
        for row in range(0,rows):
            item = '<li>'+self.tabletah.item(row, 0).text()+'</li>'
            self.tahhlist.append(item)
        self.tahhlist.append('</ol>')
        self.tahlel = ' '.join(map(str, self.tahhlist))

    def viewrosh(self):
        try:
            self.countmed()
            self.counttah()
            setarlist = []
            setenlist = []
            for i in range(1,4):
                sett = 'ArAboutDoc' + str(i)
                setten = 'EnAboutDoc' + str(i)
                setarlist.append('<p class="info1">'+self.set.value(sett)+'</p>')
                setenlist.append('<p class="info1">'+self.set.value(setten)+'</p>')
            self.folder= os.getcwd()
            if self.cbaddressicon.currentIndex() == 0:
                addressicon = 'class="fas fa-map-marker-alt"'
            elif self.cbaddressicon.currentIndex() == 1:
                addressicon = 'class="fas fa-compass"'
            elif self.cbaddressicon.currentIndex() == 2:
                addressicon = 'class="fas fa-thumbtack"'
            elif self.cbaddressicon.currentIndex() == 3:
                addressicon = 'class="fas fa-map-marked-alt"'
            elif self.cbaddressicon.currentIndex() == 4:
                addressicon = 'class="fas fa-globe"'
            if self.cbtimeicon.currentIndex() == 0:
                timeicon = 'class="fas fa-clock"'
            elif self.cbtimeicon.currentIndex() == 1:
                timeicon = 'class="fas fa-stopwatch"'
            elif self.cbtimeicon.currentIndex() == 2:
                timeicon = 'class="fas fa-hourglass-half"'
            elif self.cbtimeicon.currentIndex() == 3:
                timeicon = 'class="far fa-calendar-alt"'
            if self.cbphoneicon.currentIndex() == 0:
                phoneicon = 'class="fas fa-phone"'
            elif self.cbphoneicon.currentIndex() == 1:
                phoneicon = 'class="fas fa-phone-square"'
            elif self.cbphoneicon.currentIndex() == 2:
                phoneicon = 'class="fas fa-mobile-alt"'
            if self.cbsoicalicon.currentIndex() == 0:
                socialicon = 'class="fab fa-whatsapp-square"'
            elif self.cbsoicalicon.currentIndex() == 1:
                socialicon = 'class="fab fa-whatsapp"'
            elif self.cbsoicalicon.currentIndex() == 2:
                socialicon = 'class="fab fa-facebook-square"'
            elif self.cbsoicalicon.currentIndex() == 3:
                socialicon = 'class="fab fa-facebook"'
            divshape = self.cblogo.currentText()
            if self.insertclinicname.isChecked():
                clitype = self.clinictype.currentText()
                cliname = self.clinicappName.text()
            else:
                clitype = ''
                cliname = ''
            if self.uniqueword.isChecked() == True:
                if self.cbalerticon.currentIndex() == 0 :
                    word = 'fas fa-exclamation-triangle'
                elif self.cbalerticon.currentIndex() == 1 :
                    word = 'fas fa-exclamation-circle'
                else:
                    word = 'fas fa-info-circle'
                unique = '<i class="{}" color="#bd2000"></i> <span>{}</span>'.format(word,
                    self.roshestisna.text())
            else:
                unique=''
            if self.throuhweek.isChecked() == True and self.firsttime.isChecked() == True:
                first = '<p>الإستشارة مره واحدة وخلال إسبوع من تاريخ الكشف.</p>'
            elif self.throuhweek.isChecked() == True and self.firsttime.isChecked() == False:
                first = '<p>الإستشارة خلال إسبوع من تاريخ الكشف.</p>'
            elif self.throuhweek.isChecked() == False and self.firsttime.isChecked() == True:
                first = '<p>الإستشارة مره واحدة فقط.</p>'
            else:
                first = ''
            name = self.listroshwidget.currentItem().text()
            hh = self.cBdocnamecolor.currentText()
            info = self.cBdocinfocolor.currentText()
            bordera = self.cBbordercolor.currentText()
            mainw = self.cBmaincolor.currentText()
            insidea = self.cBinsidecolor.currentText()
            heada = self.cBheadcolor.currentText()
            foota = self.cBfootcolor.currentText()
            addressa = self.cBaddresscolor.currentText()
            timea = self.cBtimecolor.currentText()
            iconc = self.cBiconcolor.currentText()
            namear = self.docname.text()
            about = ' '.join(map(str, setarlist))
            nameen = self.docename.text()
            abouten = ' '.join(map(str, setenlist))
            age = self.viewage.text()
            taskhes = self.tashline.text()
            paitent = self.viewname.text()
            date = self.viewdate.text()
            address = self.address1.text()
            if self.address2.text() != '':
                addressb = '<p><i {} style="color:{};"></i> <span class="mainw">العنوان:</span><span style="color:{};">{}</span></p>'.format(addressicon,iconc,addressa,self.address2.text())
            else:
                addressb=''
            if self.times.text() != '':
                timeb = ' <span style="color:{};">/ {}</span></p>'.format(timea,self.times.text())
            else:
                timeb = ''
            time = self.days.text()
            phone1 = self.phone1.text()
            phone2 = self.phone2.text()
            phone3 = self.phone3.text()
            new = self.neww
            tahlel = self.tahlel
            hsize = self.dsbdocnamesi.value()
            infosize = self.dspdocinfosi.value()
            patsize = self.dsbpatientinfo.value()
            insize = self.dsbinsidesi.value()
            outsize = self.dsbsidesi.value()
            addsize = self.dsbaddresssi.value()
            timsize = self.dsbtimesi.value()
            fonttyp = self.fonttype.currentText()
            heheight = (self.dshheeight.value() / 21.01) * 100
            foheight = (self.dsfheight.value() / 21.01) * 100
            file_loader = FileSystemLoader(searchpath="./")
            env = Environment(loader=file_loader)
            TEMPLATE_FILE = str(name) + ".html"
            template = env.get_template(TEMPLATE_FILE)
            output = template.render(heheight=heheight,foheight=foheight,unique=unique,addressb=addressb,timeb=timeb,first=first,fonttyp=fonttyp, addsize=addsize, timsize=timsize, hsize=hsize, infosize=infosize,
                                     patsize=patsize, insize=insize, outsize=outsize, clitype=clitype, cliname=cliname,
                                     divshape=divshape, addressicon=addressicon, timeicon=timeicon, phoneicon=phoneicon,
                                     socialicon=socialicon, hh=hh, info=info, bordera=bordera, mainw=mainw, insidea=insidea,
                                     heada=heada, foota=foota, addressa=addressa,
                                     timea=timea, iconc=iconc, namear=namear, about=about, nameen=nameen, abouten=abouten,
                                     age=age, taskhes=taskhes,
                                     paitent=paitent,
                                     date=date, address=address, time=time,
                                     phone1=phone1, phone2=phone2, phone3=phone3, new=new, tahlel=tahlel)
            with codecs.open("Prescription/roshview.html", "w", "utf-8") as fh:
                fh.write(u'\ufeff')
                fh.write(output)
            self.prpreview()
        except:
            self.saveErrors('View Rosh Error')
        #self.handleinfopatient('Name:'+self.viewname.text()+' Age:'+self.viewage.text()+' Date:'+self.viewdate.text()+' Diognosis:'+self.tashline.text())

    def handleinfopatient(self, text):
        qr_image = qrcode.make(text, image_factory=Image).pixmap()
        qlab = QLabel('')
        qlab.setPixmap(qr_image.scaled(100, 100, Qt.KeepAspectRatio, Qt.FastTransformation))
        qlab.pixmap().save('1111.png')


    def prpreview(self):
        self.pPreview.urllocation.setText('')
        self.pPreview.setWindowFlags(Qt.FramelessWindowHint)
        self.pPreview.getPrinterProcess()
        self.pPreview.label5.setText('جارى المعاينة...')
        if self.saveno2.isChecked() == True:
            if self.roshlinelocation.text() != '':
                self.pPreview.saveRoshbyName('do',self.roshlinelocation.text(),self.viewname.text(),self.viewdate.text())
            else:
                self.chooseRoshLocation()
        self.pPreview.urllocation.setText(self.url.text())
        self.pPreview.exec()


    def savepatient(self):
        try:
            if self.smokebox.isChecked():
                self.smoke = 'Yes'
            else:
                self.smoke = 'No'
            if self.alcoholbox.isChecked():
                self.cohol = 'Yes'
            else:
                self.cohol = 'No'
            if self.type1.isChecked():
                self.typeone = 'Yes'
            else:
                self.typeone = 'No'
            if self.type2.isChecked():
                self.typetwo = 'Yes'
            else:
                self.typetwo = 'No'
            if self.anemiabox.isChecked():
                self.anemia = self.anemialine.text()
            else:
                self.anemia = 'No'
            if self.otherbox.isChecked():
                self.other = self.otherline.text()
            else:
                self.other = 'No'
            self.tashkhesfinal = self.tashline.text()
            update = '''UPDATE history SET his_suger=%s,his_height=%s,his_weight=%s,his_blood=%s,his_lblood=%s,his_smoke=%s,his_kohol=%s,his_anemia=%s,
            his_typeone=%s,his_typetwo=%s,his_other=%s,his_tashkhes=%s,his_notes=%s,his_temp=%s WHERE his_qrrandom=%s AND  his_moed=%s'''
            valu = (self.sugeer.value(),self.heeight.value(),self.weeight.value(),self.lbloood.value(),self.hbloood.value(),self.smoke,self.cohol,self.anemia,self.typeone,self.typetwo,self.other,self.tashkhesfinal,self.notesedit.toPlainText(),self.temppa.value(),self.viewuid.text(),self.viewdate.text())
            self.cur.execute(update,valu)
            if connect == None:
                command = self.cur.statement
                self.saveCommand(command)
            else:
                try:
                    dbcur.execute(update,valu)
                    dbconnect.commit()
                except:
                    command = self.cur.statement
                    self.saveCommand(command)
            self.addaradsupdate()
            self.db.commit()
        except:
            self.saveErrors('Saving Patient data Error')

    def saveAndEnd(self):
        if mySQL80 == True:
            try:
                self.savepatient()
                sql = '''UPDATE history SET his_exam=2,his_done=1 WHERE his_qrrandom=%s AND  his_moed=%s'''
                self.cur.execute(sql,(self.viewuid.text(),self.viewdate.text()))
                if connect == None:
                    command = self.cur.statement
                    self.saveCommand(command)
                else:
                    try:
                        dbcur.execute(sql,(self.viewuid.text(),self.viewdate.text()))
                        dbconnect.commit()
                    except:
                        command = self.cur.statement
                        self.saveCommand(command)
                    text = 'save'
                    connn.send(text.encode("utf-8"))
                self.db.commit()
                self.loadkashftable()
                self.loaddoctable()
                self.tabWidget.setCurrentIndex(2)
                self.listWidget.setCurrentRow(2)
                self.enbtntash()
                self.tash = None
                self.enbtntash()
            except mysql.connector.Error as err:
                self.showToaster('عفواً!', 'حدث خطأ أثناء المحاولة.', ':/MainSources/close.gif', '#ec0101',
                                 'MainSources/fail.wav', 1, 2000)
                self.saveErrors('SaveAndEnd: ' + str(err))
        else:
            self.showToaster('عفواً!', 'خطأ الاتصال بقاعدة البيانات.', ':/MainSources/close.gif', '#ec0101',
                                 'MainSources/fail.wav', 1, 2000)

    def exitFromTash(self):
        self.showMassage('تنبية!','هل تود تأكيد إلغاء التشخيص ؟',self.closeTashkhes)

    def closeTashkhes(self):
        self.tash = None
        self.tabWidget.setCurrentIndex(2)
        self.enbtntash()


    def empty(self):
        self.smokebox.setChecked(False)
        self.alcoholbox.setChecked(False)
        self.type1.setChecked(False)
        self.type2.setChecked(False)
        self.anemiabox.setChecked(False)
        self.otherbox.setChecked(False)
        self.anemialine.setText('')
        self.otherline.setText('')
        self.tashline.setText('')
        self.arads.setText('')
        self.noterenter.setText('')
        self.tah1.setText('')
        self.tabarad.setRowCount(0)
        self.tabletah.setRowCount(0)
        self.notesedit.setPlainText('')
        self.sugeer.setValue(0)
        self.heeight.setValue(0)
        self.weeight.setValue(0)
        self.lbloood.setValue(0)
        self.hbloood.setValue(0)
        self.disableEditKys()


    def loadmedicine(self):
        uuid = self.viewuid.text()
        datee = self.viewdate.text()
        medsql = '''SELECT medicine_name,medicine_repeat,medicine_time FROM medicine WHERE medicine_qrrandom=%s AND medicine_date=%s'''
        self.cur.execute(medsql,(uuid,datee))
        table = self.cur.fetchall()
        self.medtable.setRowCount(0)
        for row_number, data in enumerate(table):
            self.medtable.insertRow(row_number)
            for column_number, column in enumerate(data):
                item = QTableWidgetItem(str(column))
                item.setTextAlignment(Qt.AlignCenter)
                self.medtable.setItem(row_number,column_number,item)
                self.removebtn = QPushButton('')
                self.removebtn.setIcon(QIcon(":/MainSources/delete.png"))
                self.removebtn.setMaximumSize(24,24)
                self.removebtn.clicked.connect(self.deletemedicine)
                self.medtable.setCellWidget(row_number,3,self.removebtn)
        self.medicinecount.setText(str(self.medtable.rowCount()))
        self.loadCompleter()

    def loadCompleter(self):
        if mySQL80 == True:
            try:
                sq = '''SELECT medlist_name,medlist_repeat,medlist_time FROM medlist'''
                self.cur.execute(sq)
                fet = self.cur.fetchall()
                self.medlisss = []
                self.replisss = []
                self.timlisss = []
                for r, data in enumerate(fet):
                    if data[0] != None:
                        self.medlisss.append(data[0])
                    if data[1] != None:
                        self.replisss.append(data[1])
                    if data[2] != None:
                        self.timlisss.append(data[2])
                if len(self.medlisss) != 0:
                    commed = QCompleter(self.medlisss)
                    commed.setCaseSensitivity(Qt.CaseInsensitive)
                    self.medname.setCompleter(commed)
                if len(self.replisss) != 0:
                    comrep = QCompleter(self.replisss)
                    comrep.setCaseSensitivity(Qt.CaseInsensitive)
                    self.medrepeat.setCompleter(comrep)
                if len(self.timlisss) != 0:
                    comtim = QCompleter(self.timlisss)
                    comtim.setCaseSensitivity(Qt.CaseInsensitive)
                    self.medtime.setCompleter(comtim)
            except mysql.connector.Error as err:
                self.saveErrors('LoadCompleter: ' + str(err))



    def deletemedicine(self):
        medname = self.medtable.item(self.medtable.currentRow(),0).text()
        medre = self.medtable.item(self.medtable.currentRow(),1).text()
        medti = self.medtable.item(self.medtable.currentRow(),2).text()
        if mySQL80 == True:
            try:
                delsql= '''DELETE FROM medicine WHERE medicine_name=%s AND medicine_repeat=%s AND medicine_time=%s'''
                self.cur.execute(delsql,(medname,medre,medti))
                if connect == None:
                    command = self.cur.statement
                    self.saveCommand(command)
                else:
                    try:
                        dbcur.execute(self.cur.statement)
                        dbconnect.commit()
                    except:
                        command = self.cur.statement
                        self.saveCommand(command)
                self.db.commit()
                self.loadmedicine()
            except mysql.connector.Error as err:
                self.showToaster('عفواً!', 'حدث خطأ أثناء المحاولة.', ':/MainSources/close.gif', '#ec0101',
                                 'MainSources/fail.wav', 1, 2000)
                self.saveErrors('DeleteMedicine: ' + str(err))
        else:
            self.showToaster('عفواً!', 'خطأ الاتصال بقاعدة البيانات.', ':/MainSources/close.gif', '#ec0101',
                     'MainSources/fail.wav', 1, 2000)

    def addmedicine(self):
        if self.medname.text() != '':
            s = datetime.now()
            obid = int(s.strftime("%m%d%H%M%S%f"))
            uuid = self.viewuid.text()
            medicinename = self.medname.text()
            medicinerepeat = self.medrepeat.text()
            medicinetime = self.medtime.text()
            if mySQL80 == True:
                try:
                    self.cur.execute('''INSERT INTO medicine(medicine_name,medicine_repeat,medicine_time,medicine_qrrandom,medicine_date) VALUES(%s,%s,%s,%s,%s)''',(medicinename,medicinerepeat,medicinetime,uuid,self.viewdate.text()))
                    if connect == None:
                        command = self.cur.statement
                        self.saveCommand(command)
                    else:
                        try:
                            dbcur.execute(self.cur.statement)
                            dbconnect.commit()
                        except:
                            command = self.cur.statement
                            self.saveCommand(command)
                    if self.medname.text() not in self.medlisss:
                        self.cur.execute('''INSERT INTO medlist(medlist_name,medlist_repeat,medlist_time,medlist_tim) VALUES(%s,%s,%s,%s)''',(medicinename,medicinerepeat,medicinetime,obid))
                        if connect == None:
                            command = self.cur.statement
                            self.saveCommand(command)
                        else:
                            try:
                                dbcur.execute(self.cur.statement)
                                dbconnect.commit()
                            except:
                                command = self.cur.statement
                                self.saveCommand(command)
                    self.db.commit()
                    self.loadmedicine()
                    self.loadmedsettings()
                    self.medname.setText('')
                    self.medrepeat.setText('')
                    self.medtime.setText('')
                except mysql.connector.Error as err:
                    self.showToaster('عفواً!', 'حدث خطأ أثناء المحاولة.', ':/MainSources/close.gif', '#ec0101',
                                     'MainSources/fail.wav', 1, 2000)
                    self.saveErrors('Addmedi: ' + str(err))
            else:
                self.showToaster('عفواً!', 'خطأ الاتصال بقاعدة البيانات.', ':/MainSources/close.gif', '#ec0101',
                                     'MainSources/fail.wav', 1, 2000)
        else:
            self.showToaster('خطأ!', 'من فضلك أدخل اسم الدواء.', ':/MainSources/close.gif', '#ec0101',
                             'MainSources/fail.wav',1, 2000)

    def newvarss(self):
        self.vardock.show()
        self.vardock.showNormal()
        self.loadvars()
        self.loadvarrs()

    def loadvarrs(self):
        if mySQL80 == True:
            try:
                sql = '''SELECT patientvar_name,patientvar_real,patientvar_low,patientvar_high,patientvar_time FROM patientvar WHERE patientvar_qrrandom=%s AND patientvar_date=%s'''
                self.cur.execute(sql,(self.viewuid.text(),self.viewdate.text()))
                fetch = self.cur.fetchall()
                self.dvars.varsstable.setRowCount(0)
                for i,idata in enumerate(fetch):
                    self.dvars.varsstable.insertRow(i)
                    item = QTableWidgetItem(str(idata[0]))
                    item.setTextAlignment(Qt.AlignCenter)
                    item1 = QTableWidgetItem(str(idata[1]))
                    item1.setTextAlignment(Qt.AlignCenter)
                    item2 = QTableWidgetItem(str(idata[2])+' - '+str(idata[3]))
                    item2.setTextAlignment(Qt.AlignCenter)
                    if float(idata[2]) > float(idata[1]):
                        item1.setBackground(QColor(255, 255, 127))
                    elif float(idata[3]) < float(idata[1]):
                        item1.setBackground(QColor(255, 0, 0))
                    else:
                        pass
                    remove = QPushButton('')
                    remove.setIcon(QIcon(":/MainSources/delete.png"))
                    remove.clicked.connect(self.deletepatientvar)
                    self.dvars.varsstable.setItem(i,0,item)
                    self.dvars.varsstable.setItem(i,1,item1)
                    self.dvars.varsstable.setItem(i,2,item2)
                    self.dvars.varsstable.setItem(i,3,QTableWidgetItem(str(idata[4])))
                    self.dvars.varsstable.setCellWidget(i, 4, remove)
            except mysql.connector.Error as err:
                self.saveErrors('loadvarrs: ' + str(err))



    def loadvars(self):
        self.dvars.varss.clear()
        if mySQL80 == True:
            try:
                sql = '''SELECT docvar_name FROM docvar'''
                self.cur.execute(sql)
                fetch = self.cur.fetchall()
                lis = []
                for i in fetch:
                    lis.append(i[0])
                self.dvars.varss.addItems(list(set(lis)))
            except mysql.connector.Error as err:
                self.saveErrors('LoadVars: ' + str(err))

    def addnewvarss(self):
        if mySQL80 == True:
            try:
                sql = '''SELECT docvar_name,docvar_low,docvar_high FROM docvar WHERE docvar_name=%s AND docvar_type=%s'''
                self.cur.execute(sql,(self.dvars.varss.currentText(),self.viewgender.text()))
                fetch = self.cur.fetchall()
                if len(fetch) == 0 :
                    self.showToaster('عفواً!', 'يرجى إنشاء معامل جديد لجنس المريض.', ':/MainSources/close.gif', '#ec0101',
                                     'MainSources/fail.wav', 1, 2000)
                else:
                    for i in fetch:
                        today = str(date.today())
                        s = datetime.now()
                        obid = int(s.strftime("%m%d%H%M%S%f"))
                        insql = '''INSERT INTO patientvar(patientvar_name,patientvar_real,patientvar_low,patientvar_high,patientvar_type,patientvar_date,patientvar_qrrandom,patientvar_time) VALUE(%s,%s,%s,%s,%s,%s,%s,%s)'''
                        values = (self.dvars.varss.currentText(),self.dvars.patientvarss.text(),i[1],i[2],self.viewgender.text(),today,self.viewuid.text(),obid)
                        self.cur.execute(insql,values)
                        if connect == None:
                            command = self.cur.statement
                            self.saveCommand(command)
                        else:
                            try:
                                dbcur.execute(insql,values)
                                dbconnect.commit()
                            except:
                                command = self.cur.statement
                                self.saveCommand(command)
                        self.db.commit()
            except mysql.connector.Error as err:
                self.showToaster('عفواً!', 'حدث خطأ أثناء المحاولة.', ':/MainSources/close.gif', '#ec0101',
                                 'MainSources/fail.wav', 1, 2000)
                self.saveErrors('Addnewvars: ' + str(err))
        else:
            self.showToaster('عفواً!', 'خطأ الاتصال بقاعدة البيانات.', ':/MainSources/close.gif', '#ec0101',
                             'MainSources/fail.wav', 1, 2000)
        self.loadvarrs()

    def addnewvars(self):
        if mySQL80 == True:
            try:
                sqll = '''SELECT docvar_name,docvar_low,docvar_high FROM docvar WHERE docvar_name=%s AND docvar_type=%s'''
                self.cur.execute(sqll, (self.dvars.varssname.text(), self.viewgender.text()))
                fetch = self.cur.fetchall()
                if len(fetch) == 0:
                    s = datetime.now()
                    obid = int(s.strftime("%m%d%H%M%S%f"))
                    sql = '''INSERT INTO docvar(docvar_name,docvar_low,docvar_high,docvar_type,docvar_time) VALUES(%s,%s,%s,%s,%s)'''
                    value = (self.dvars.varssname.text(), self.dvars.varsslow.text(), self.dvars.varsshigh.text(), self.viewgender.text(), obid)
                    self.cur.execute(sql, value)
                    if connect == None:
                        command = self.cur.statement
                        self.saveCommand(command)
                    else:
                        try:
                            dbcur.execute(sql, value)
                            dbconnect.commit()
                        except:
                            command = self.cur.statement
                            self.saveCommand(command)
                    today = str(date.today())
                    insql = '''INSERT INTO patientvar(patientvar_name,patientvar_real,patientvar_low,patientvar_high,patientvar_type,patientvar_date,patientvar_qrrandom,patientvar_time) VALUE(%s,%s,%s,%s,%s,%s,%s,%s)'''
                    values = (self.dvars.varssname.text(), self.dvars.patientvarss2.text(), self.dvars.varsslow.text(), self.dvars.varsshigh.text(), self.viewgender.text(), today,
                              self.viewuid.text(), obid)
                    self.cur.execute(insql, values)
                    if connect == None:
                        command = self.cur.statement
                        self.saveCommand(command)
                    else:
                        try:
                            dbcur.execute(insql, values)
                            dbconnect.commit()
                        except:
                            command = self.cur.statement
                            self.saveCommand(command)
                    self.db.commit()
                else:
                    self.showToaster('عفواً!', 'هذا المعامل مسجل مسبقا فى قاعدة البيانات.', ':/MainSources/close.gif', '#ec0101',
                                     'MainSources/fail.wav', 1, 2000)
            except mysql.connector.Error as err:
                self.showToaster('عفواً!', 'حدث خطأ أثناء المحاولة.', ':/MainSources/close.gif', '#ec0101',
                                 'MainSources/fail.wav', 1, 2000)
                self.saveErrors('Addnewvars: ' + str(err))
        else:
            self.showToaster('عفواً!', 'خطأ الاتصال بقاعدة البيانات.', ':/MainSources/close.gif', '#ec0101',
                             'MainSources/fail.wav', 1, 2000)
        self.loadvars()
        self.loadvarrs()
        self.loadvarsettings()

    def deletepatientvar(self):
        if mySQL80 == True:
            try:
                sql = '''DELETE FROM patientvar WHERE patientvar_qrrandom=%s AND patientvar_time=%s AND patientvar_date=%s'''
                self.cur.execute(sql,(self.viewuid.text(),self.dvars.varsstable.item(self.dvars.varsstable.currentRow(),3).text(),self.viewdate.text()))
                self.db.commit()
            except mysql.connector.Error as err:
                self.showToaster('عفواً!', 'حدث خطأ أثناء المحاولة.', ':/MainSources/close.gif', '#ec0101',
                                 'MainSources/fail.wav', 1, 2000)
                self.saveErrors('DeletePatientVar: ' + str(err))
        else:
            self.showToaster('عفواً!', 'خطأ الاتصال بقاعدة البيانات.', ':/MainSources/close.gif', '#ec0101',
                             'MainSources/fail.wav', 1, 2000)
        self.loadvarrs()

    #ما يحدث عند تشغيل التطبيق
    def onrun(self):
        #self.result.setHidden(True)
        self.listWidget.setCurrentRow(0)
        validator = QRegExpValidator(QRegExp('-?\d{0,20}(?:\.\d{0,20})?'))
        self.load.setHidden(True)
        self.loadstats.setHidden(True)
        self.importdone.setHidden(True)
        self.zoomin.setEnabled(False)
        self.zoomout.setEnabled(False)
        self.highvar.setValidator(validator)
        self.previewRoshImagestolist()
        validator = QRegExpValidator(QRegExp('-?\d{0,20}(?:\.\d{0,20})?'))
        self.lowvar.setValidator(validator)
        self.highvar.setValidator(validator)
        self.vartable.setColumnHidden(4, True)
        self.medlisst.setColumnHidden(1, True)
        self.tashtable.setColumnHidden(1, True)
        if self.set.value("MainPage",0) == 0 :
            self.listWidget.setCurrentRow(0)
            self.tabWidget.setCurrentIndex(0)
        else:
            self.listWidget.setCurrentRow(2)
            self.tabWidget.setCurrentIndex(2)
        self.connOther()
        self.secondDatabaseConnect()



    def chooselocation(self):
        try:
            dir = QFileDialog.getExistingDirectory(self,'Select Directory')
            if not os.path.exists(dir+'/BackUp') and dir[0]:
                os.makedirs(dir+'/BackUp')
                self.lineEditloc.setText(str(dir)+'/BackUp')
                self.set.setValue("BackUpDir",self.lineEditloc.text())
                self.exportBackup()
        except:
            pass

    def chooseRoshLocation(self):
        try:
            dir = QFileDialog.getExistingDirectory(self,'إختيار مكان حفظ الروشتات')
            if not os.path.exists(dir+'/Prescription_Copies') and dir[0]:
                os.makedirs(dir+'/Prescription_Copies')
            self.roshlinelocation.setText(str(dir)+'/Prescription_Copies')
            self.set.setValue("RoshLocation",self.roshlinelocation.text())
        except:
            pass

    def chooseDbfile(self):
        try:
            user = self.set.value("Admin")
            password = self.set.value("AdminPass")
            dbname = self.set.value("DBName")
            file = QFileDialog.getOpenFileName(self,'Choose DB File','','Database Files(*.sql)')
            if file[0] != '':
                command = r'cmd /c "C:\Program Files\MySQL\MySQL Server 8.0\bin\mysql.exe" -hlocalhost -u' + user + ' -p' + password + ' --default-character-set=utf8 ' + dbname + '< {}'.format(
                    file[0])
                she = importDatabase(self,command)
                self.closeDBConnection()
                if connn != None:
                    text = 'kill'
                    connn.send(text.encode("utf-8"))
                she.start()
        except:
            pass

    def chooseimage(self):
        dir = str(os.getcwd())
        try:
            imagename = QFileDialog.getOpenFileName(self,'Open File',dir,'Image files (*.png)')
            path = imagename[0]
            imgpath = path
            imgdata = open(imgpath, 'rb').read()
            pixmap = self.mask_image(imgdata)
            self.logochoose.setPixmap(pixmap)
        except:
            pass
            #print('error')

    def mask_image(self,imgdata, imgtype='png',size =100):
        image = QImage.fromData(imgdata, imgtype)
        image.convertToFormat(QImage.Format_ARGB32)
        imgsize = min(image.width(), image.height())
        rect = QRect(
            (image.width() - imgsize) / 2,
            (image.height() - imgsize) / 2,
            imgsize,
            imgsize,
        )
        image = image.copy(rect)
        out_img = QImage(imgsize, imgsize, QImage.Format_ARGB32)
        out_img.fill(Qt.transparent)
        brush = QBrush(image)
        painter = QPainter(out_img)
        painter.setBrush(brush)
        painter.setPen(Qt.NoPen)
        painter.drawEllipse(0, 0, imgsize, imgsize)
        painter.end()
        pr = QWindow().devicePixelRatio()
        pm = QPixmap.fromImage(out_img)
        pm.setDevicePixelRatio(pr)
        size *= pr
        pm = pm.scaled(size, size, Qt.KeepAspectRatio,
                       Qt.SmoothTransformation)
        return pm


    def handleTextEntered(self, text):
        qr_image = qrcode.make(text, image_factory=Image).pixmap()
        self.qrCode.setPixmap(qr_image.scaled(150, 150, Qt.KeepAspectRatio, Qt.FastTransformation))
        #self.qrCode.pixmap().save(text + '.png')

    #دالة إضافة معامل فى الاعدادات
    def addvarsettings(self):
        s = datetime.now()
        obid = int(s.strftime("%m%d%H%M%S%f"))
        if self.varname.text() == '' or self.lowvar.text() == '' or self.highvar.text()== '':
            self.showToaster('عفواً!', 'لا تترك الخانات فارغة.', ':/MainSources/close.gif', '#ec0101',
                             'MainSources/fail.wav',1, 2000)
        else:
            if mySQL80 == True:
                try:
                    sql = '''INSERT INTO docvar(docvar_name,docvar_low,docvar_high,docvar_type,docvar_time) VALUES(%s,%s,%s,%s,%s)'''
                    value = (self.varname.text(),self.lowvar.text(),self.highvar.text(),self.vartype.currentText(),obid)
                    self.cur.execute(sql,value)
                    if connect == None:
                        command = self.cur.statement
                        self.saveCommand(command)
                    else:
                        try:
                            dbcur.execute(sql,value)
                            dbconnect.commit()
                        except:
                            command = self.cur.statement
                            self.saveCommand(command)
                    self.db.commit()
                except mysql.connector.Error as err:
                    self.showToaster('عفواً!', 'حدث خطأ أثناء المحاولة.', ':/MainSources/close.gif', '#ec0101',
                                     'MainSources/fail.wav', 1, 2000)
                    self.saveErrors('AddVariableSett: ' + str(err))
            else:
                self.showToaster('عفواً!', 'خطأ الاتصال بقاعدة البيانات.', ':/MainSources/close.gif', '#ec0101',
                                 'MainSources/fail.wav', 1, 2000)
        self.loadvarsettings()

    def loadvarsettings(self):
        if mySQL80 == True:
            try:
                sql = '''SELECT docvar_name,docvar_low,docvar_high,docvar_type,docvar_time FROM docvar'''
                self.cur.execute(sql)
                fetch = self.cur.fetchall()
                self.vartable.setRowCount(0)
                for row,datarw in enumerate(fetch):
                    self.vartable.insertRow(row)
                    for col, data in enumerate(datarw):
                        remove = QPushButton('')
                        remove.setIcon(QIcon(":/MainSources/delete.png"))
                        remove.clicked.connect(self.deletevarsettings)
                        item = QTableWidgetItem(str(data))
                        item.setTextAlignment(Qt.AlignCenter)
                        self.vartable.setItem(row,col,item)
                        self.vartable.setCellWidget(row,5,remove)
            except mysql.connector.Error as err:
                self.saveErrors('LoadVariableSett: ' + str(err))

    def deletevarsettings(self):
        if mySQL80 == True:
            try:
                sql = '''DELETE FROM docvar WHERE docvar_name = %s AND docvar_low=%s AND docvar_high=%s AND docvar_type=%s AND docvar_time=%s'''
                value = (self.vartable.item(self.vartable.currentRow(),0).text(),self.vartable.item(self.vartable.currentRow(),1).text(),self.vartable.item(self.vartable.currentRow(),2).text(),self.vartable.item(self.vartable.currentRow(),3).text(),self.vartable.item(self.vartable.currentRow(),4).text())
                self.cur.execute(sql,value)
                self.db.commit()
            except mysql.connector.Error as err:
                self.showToaster('عفواً!', 'حدث خطأ أثناء المحاولة.', ':/MainSources/close.gif', '#ec0101',
                                 'MainSources/fail.wav', 1, 2000)
                self.saveErrors('DeleteVar: ' + str(err))
        else:
            self.showToaster('عفواً!', 'خطأ الاتصال بقاعدة البيانات.', ':/MainSources/close.gif', '#ec0101',
                             'MainSources/fail.wav', 1, 2000)
        self.loadvarsettings()

    #دالة إضافة دواء من الاعدادات
    def addmedsettings(self):
        s = datetime.now()
        obid = int(s.strftime("%m%d%H%M%S%f"))
        if self.medtext.text() != '':
            if mySQL80 == True:
                try:
                    sql = '''INSERT INTO medlist(medlist_name,medlist_tim) VALUE(%s,%s)'''
                    value = (self.medtext.text(),obid)
                    self.cur.execute(sql,value)
                    if connect == None:
                        command = self.cur.statement
                        self.saveCommand(command)
                    else:
                        try:
                            dbcur.execute(sql,value)
                            dbconnect.commit()
                        except:
                            command = self.cur.statement
                            self.saveCommand(command)
                    self.db.commit()
                    self.medtext.setText('')
                except mysql.connector.Error as err:
                    self.showToaster('عفواً!', 'حدث خطأ أثناء المحاولة.', ':/MainSources/close.gif', '#ec0101',
                                     'MainSources/fail.wav', 1, 2000)
                    self.saveErrors('AddMedicine: ' + str(err))
            else:
                self.showToaster('عفواً!', 'خطأ الاتصال بقاعدة البيانات.', ':/MainSources/close.gif', '#ec0101',
                                 'MainSources/fail.wav', 1, 2000)
        else:
            self.showToaster('عفواً!', 'لا تترك الخانات فارغة.', ':/MainSources/close.gif', '#ec0101',
                             'MainSources/fail.wav', 1, 2000)
        self.loadmedsettings()
        self.loadCompleter()

    def loadmedsettings(self):
        if mySQL80 == True:
            try:
                sql = '''SELECT medlist_name,medlist_tim FROM medlist'''
                self.cur.execute(sql)
                fetch = self.cur.fetchall()
                self.medlisst.setRowCount(0)
                for row , datarw in enumerate(fetch):
                    self.medlisst.insertRow(row)
                    for col, data in enumerate(datarw):
                        item = QTableWidgetItem(data)
                        item.setTextAlignment(Qt.AlignCenter)
                        remove = QPushButton('')
                        remove.setIcon(QIcon(":/MainSources/delete.png"))
                        remove.clicked.connect(self.deletemedsettings)
                        self.medlisst.setItem(row,col,item)
                        self.medlisst.setCellWidget(row,2,remove)
            except mysql.connector.Error as err:
                self.saveErrors('LoadMedicine: ' + str(err))

    def deletemedsettings(self):
        if mySQL80 == True:
            try:
                sql = '''DELETE FROM medlist WHERE medlist_name=%s AND medlist_tim=%s'''
                value = (self.medlisst.item(self.medlisst.currentRow(),0).text(),self.medlisst.item(self.medlisst.currentRow(),1).text())
                self.cur.execute(sql,value)
                self.db.commit()
            except mysql.connector.Error as err:
                self.showToaster('عفواً!', 'حدث خطأ أثناء المحاولة.', ':/MainSources/close.gif', '#ec0101',
                                 'MainSources/fail.wav', 1, 2000)
                self.saveErrors('DeleteMedSett: ' + str(err))
        else:
            self.showToaster('عفواً!', 'خطأ الاتصال بقاعدة البيانات.', ':/MainSources/close.gif', '#ec0101',
                             'MainSources/fail.wav', 1, 2000)
        self.loadmedsettings()

    #دالة إضافة تشخيص فى الاعدادات
    def addtashsettings(self):
        s = datetime.now()
        obid = int(s.strftime("%m%d%H%M%S%f"))
        if self.tashtext.text() != '':
            if mySQL80 == True:
                try:
                    sql = '''INSERT INTO tashlist(tashlist_name,tashlist_time) VALUE (%s,%s)'''
                    value = (self.tashtext.text(),obid)
                    self.cur.execute(sql,value)
                    if connect == None:
                        command = self.cur.statement
                        self.saveCommand(command)
                    else:
                        try:
                            dbcur.execute(sql,value)
                            dbconnect.commit()
                        except:
                            command = self.cur.statement
                            self.saveCommand(command)
                    self.db.commit()
                    self.tashtext.setText('')
                except mysql.connector.Error as err:
                    self.showToaster('عفواً!', 'حدث خطأ أثناء المحاولة.', ':/MainSources/close.gif', '#ec0101',
                                     'MainSources/fail.wav', 1, 2000)
                    self.saveErrors('Addtashsetting: ' + str(err))
            else:
                self.showToaster('عفواً!', 'خطأ الاتصال بقاعدة البيانات.', ':/MainSources/close.gif', '#ec0101',
                                 'MainSources/fail.wav', 1, 2000)
        else:
            self.showToaster('عفواً!', 'لا تترك الخانات فارغة.', ':/MainSources/close.gif', '#ec0101',
                             'MainSources/fail.wav', 1, 2000)
        self.loadtashsettings()

    def loadtashsettings(self):
        if mySQL80 == True:
            try:
                sql = '''SELECT tashlist_name,tashlist_time FROM tashlist'''
                self.cur.execute(sql)
                fetch = self.cur.fetchall()
                self.tashtable.setRowCount(0)
                for row,datarw in enumerate(fetch):
                    self.tashtable.insertRow(row)
                    for col,data in enumerate(datarw):
                        item = QTableWidgetItem(data)
                        item.setTextAlignment(Qt.AlignCenter)
                        remove = QPushButton('')
                        remove.setIcon(QIcon(":/MainSources/delete.png"))
                        remove.clicked.connect(self.deletetashsettings)
                        self.tashtable.setItem(row,col,item)
                        self.tashtable.setCellWidget(row,2,remove)
            except mysql.connector.Error as err:
                self.saveErrors('loadtashsettings: ' + str(err))

    def deletetashsettings(self):
        if mySQL80 == True:
            try:
                sql = '''DELETE FROM tashlist WHERE tashlist_name=%s AND tashlist_time=%s'''
                value = (self.tashtable.item(self.tashtable.currentRow(),0).text(),self.tashtable.item(self.tashtable.currentRow(),1).text())
                self.cur.execute(sql,value)
                self.db.commit()
            except mysql.connector.Error as err:
                self.showToaster('عفواً!', 'حدث خطأ أثناء المحاولة.', ':/MainSources/close.gif', '#ec0101',
                                 'MainSources/fail.wav', 1, 2000)
                self.saveErrors('Deletetashsettings: ' + str(err))
        else:
            self.showToaster('عفواً!', 'خطأ الاتصال بقاعدة البيانات.', ':/MainSources/close.gif', '#ec0101',
                             'MainSources/fail.wav', 1, 2000)
        self.loadtashsettings()

    def runOnBoot(self):
        try:
            RUN_PATH = "HKEY_CURRENT_USER\\Software\\Microsoft\\Windows\\CurrentVersion\\Run"
            s = QSettings(RUN_PATH, QSettings.NativeFormat)
            if self.radionoboot.isChecked() == True:
                s.setValue("DoctorClinic",sys.argv[0])
            else:
                s.remove("DoctorClinic")
        except:
            self.saveErrors('RunOnBoot Error')

    def storeRoshSettings(self):
        self.setrosh = QSettings('DoctorClinic', 'Rosh' + str(self.listroshwidget.currentRow() + 1))
        self.setrosh.setValue("DocNameColor",self.cBdocnamecolor.currentText())
        self.setrosh.setValue("DocInfoColor", self.cBdocinfocolor.currentText())
        self.setrosh.setValue("BorderColor", self.cBbordercolor.currentText())
        self.setrosh.setValue("MainFontColor", self.cBmaincolor.currentText())
        self.setrosh.setValue("InsideColor", self.cBinsidecolor.currentText())
        self.setrosh.setValue("HeaderColor", self.cBheadcolor.currentText())
        self.setrosh.setValue("FooterColor", self.cBfootcolor.currentText())
        self.setrosh.setValue("AddressColor", self.cBaddresscolor.currentText())
        self.setrosh.setValue("TimeColor", self.cBtimecolor.currentText())
        self.setrosh.setValue("IconColor", self.cBiconcolor.currentText())
        self.setrosh.setValue("Logo", self.cblogo.currentText())
        self.setrosh.setValue("AddressIcon", self.cbaddressicon.currentText())
        self.setrosh.setValue("TimeIcon", self.cbtimeicon.currentText())
        self.setrosh.setValue("PhoneIcon", self.cbphoneicon.currentText())
        self.setrosh.setValue("SocialIcon", self.cbsoicalicon.currentText())
        self.setrosh.setValue("AlertIcon", self.cbalerticon.currentText())
        self.setrosh.setValue("DocNameSize", self.dsbdocnamesi.value())
        self.setrosh.setValue("DocInfoSize", self.dspdocinfosi.value())
        self.setrosh.setValue("PatientSize", self.dsbpatientinfo.value())
        self.setrosh.setValue("InsideSize", self.dsbinsidesi.value())
        self.setrosh.setValue("SideSize", self.dsbsidesi.value())
        self.setrosh.setValue("AddressSize", self.dsbaddresssi.value())
        self.setrosh.setValue("TimeSize", self.dsbtimesi.value())
        self.setrosh.setValue("DisplayClinicName", self.insertclinicname.isChecked())
        self.setrosh.setValue("FontType",self.fonttype.currentText())
        self.set.setValue("HeaderHeight", self.dshheeight.value())
        self.set.setValue("FooterHeight", self.dsfheight.value())

    def checkIFDefalut(self):
        if self.listroshwidget.currentRow() == 0:
            self.cBdocnamecolor.setEnabled(False)
            self.cBdocinfocolor.setEnabled(False)
            self.cBmaincolor.setEnabled(False)
            self.cBheadcolor.setEnabled(False)
            self.cBfootcolor.setEnabled(False)
            self.cBaddresscolor.setEnabled(False)
            self.cBtimecolor.setEnabled(False)
            self.cBiconcolor.setEnabled(False)
            self.cblogo.setEnabled(False)
            self.insertclinicname.setEnabled(False)
            self.cbaddressicon.setEnabled(False)
            self.cbtimeicon.setEnabled(False)
            self.cbphoneicon.setEnabled(False)
            self.cbsoicalicon.setEnabled(False)
            self.cbalerticon.setEnabled(False)
            self.dsbdocnamesi.setEnabled(False)
            self.dspdocinfosi.setEnabled(False)
            self.dsbpatientinfo.setEnabled(False)
            self.dsbaddresssi.setEnabled(False)
            self.dsbtimesi.setEnabled(False)
            self.dshheeight.setEnabled(True)
            self.dsfheight.setEnabled(True)
        else:
            self.cBdocnamecolor.setEnabled(True)
            self.cBdocinfocolor.setEnabled(True)
            self.cBmaincolor.setEnabled(True)
            self.cBheadcolor.setEnabled(True)
            self.cBfootcolor.setEnabled(True)
            self.cBaddresscolor.setEnabled(True)
            self.cBtimecolor.setEnabled(True)
            self.cBiconcolor.setEnabled(True)
            self.cblogo.setEnabled(True)
            self.insertclinicname.setEnabled(True)
            self.cbaddressicon.setEnabled(True)
            self.cbtimeicon.setEnabled(True)
            self.cbphoneicon.setEnabled(True)
            self.cbsoicalicon.setEnabled(True)
            self.cbalerticon.setEnabled(True)
            self.dsbdocnamesi.setEnabled(True)
            self.dspdocinfosi.setEnabled(True)
            self.dsbpatientinfo.setEnabled(True)
            self.dsbaddresssi.setEnabled(True)
            self.dsbtimesi.setEnabled(True)
            self.dshheeight.setEnabled(False)
            self.dsfheight.setEnabled(False)




    def viewRoshSettings(self):
        self.checkIFDefalut()
        self.setrosh = QSettings('DoctorClinic', 'Rosh' + str(self.listroshwidget.currentRow() + 1))
        self.cBdocnamecolor.setCurrentText(self.setrosh.value("DocNameColor"))
        self.cBdocinfocolor.setCurrentText(self.setrosh.value("DocInfoColor"))
        self.cBbordercolor.setCurrentText(self.setrosh.value("BorderColor"))
        self.cBmaincolor.setCurrentText(self.setrosh.value("MainFontColor"))
        self.cBinsidecolor.setCurrentText(self.setrosh.value("InsideColor"))
        self.cBheadcolor.setCurrentText(self.setrosh.value("HeaderColor"))
        self.cBfootcolor.setCurrentText(self.setrosh.value("FooterColor"))
        self.cBaddresscolor.setCurrentText(self.setrosh.value("AddressColor"))
        self.cBtimecolor.setCurrentText(self.setrosh.value("TimeColor"))
        self.cBiconcolor.setCurrentText(self.setrosh.value("IconColor"))
        self.cblogo.setCurrentText(self.setrosh.value("Logo"))
        self.cbaddressicon.setCurrentText(self.setrosh.value("AddressIcon"))
        self.cbtimeicon.setCurrentText(self.setrosh.value("TimeIcon"))
        self.cbphoneicon.setCurrentText(self.setrosh.value("PhoneIcon"))
        self.cbsoicalicon.setCurrentText(self.setrosh.value("SocialIcon"))
        self.cbalerticon.setCurrentText(self.setrosh.value("AlertIcon"))
        self.dsbdocnamesi.setValue(float(self.setrosh.value("DocNameSize")))
        self.dspdocinfosi.setValue(float(self.setrosh.value("DocInfoSize")))
        self.dsbpatientinfo.setValue(float(self.setrosh.value("PatientSize")))
        self.dsbinsidesi.setValue(float(self.setrosh.value("InsideSize")))
        self.dsbsidesi.setValue(float(self.setrosh.value("SideSize")))
        self.dsbaddresssi.setValue(float(self.setrosh.value("AddressSize")))
        self.dsbtimesi.setValue(float(self.setrosh.value("TimeSize")))
        self.insertclinicname.setChecked(True) if self.setrosh.value("DisplayClinicName")=='true' else self.insertclinicname.setChecked(False)
        self.fonttype.setCurrentText(self.setrosh.value("FontType"))
        self.set.setValue("CurrentRosh", self.listroshwidget.currentRow())
        self.dshheeight.setValue(float(self.set.value("HeaderHeight")))
        self.dsfheight.setValue(float(self.set.value("FooterHeight")))
        self.loadRoshImage()
        self.viewEarnMoney()

    def saveUnique(self):
        self.set.setValue("UniqueWord", self.uniqueword.isChecked())
        self.set.setValue("OneTime", self.firsttime.isChecked())
        self.set.setValue("OneWeek", self.throuhweek.isChecked())

    def storeSqlData(self):
        self.set.setValue("LocalIP", self.sqlhost.text())
        self.set.setValue("DBName", self.sqlname.text())
        self.set.setValue("Admin", self.sqlusername.text())
        self.set.setValue("AdminPass", self.sqlpassword.text())
        self.set.setValue("Port", self.sqlport.text())
        self.set.setValue("RemoteIP", self.sqlhost2.text())
        self.set.setValue("RemoteDBName", self.sqlname2.text())
        self.set.setValue("RemoteUser", self.sqlusername2.text())
        self.set.setValue("RemotePass", self.sqlpassword2.text())
        self.set.setValue("RemotePort", self.sqlport2.text())

    def store(self):
        self.set.setValue("ClinicName", self.clinicappName.text())
        self.set.setValue("ClinicType", self.clinictype.currentIndex())
        self.set.setValue("StartHour", self.starttime.value())
        self.set.setValue("StartMinutes", self.starttimemin.value())
        self.set.setValue("EndHour", self.endtime.value())
        self.set.setValue("EndMinutes", self.endtimemin.value())
        self.set.setValue("AppMinus", self.farktime.value())
        self.set.setValue("EstTime", self.estdays.value())
        self.set.setValue("AppSt", self.typepp.currentIndex())
        self.set.setValue("MainPage", self.mainpageapp.currentIndex())
        if self.radionoboot.isChecked() == True:
            on = True
        else:
            on = False
        self.set.setValue("RunOnWindows", on)
        if self.radiono1.isChecked() == True:
            off = True
        else:
            off = False
        self.set.setValue("HideMoney", off)
        self.runOnBoot()
        self.viewEarnMoney()
        self.loadesttable()

    def viewTestPreview(self):
        self.roshPreviw = QWebEngineView()
        self.readConvertToTest()


    def getRoshValues(self):
        dir = os.getcwd()
        file = dir+"\\"+self.listroshwidget.currentItem().text()+'.html'
        with open(file) as fp:
            soup = BeautifulSoup(fp, 'html.parser')
        self.cBdocnamecolor.setCurrentText(soup.find('tag')['value'])
        self.cBdocinfocolor.setCurrentText(soup.find('tag1')['value'])
        self.cBbordercolor.setCurrentText(soup.find('tag2')['value'])
        self.cBmaincolor.setCurrentText(soup.find('tag3')['value'])
        self.cBinsidecolor.setCurrentText(soup.find('tag4')['value'])
        self.cBheadcolor.setCurrentText(soup.find('tag5')['value'])
        self.cBfootcolor.setCurrentText(soup.find('tag6')['value'])
        self.cBaddresscolor.setCurrentText(soup.find('tag7')['value'])
        self.cBtimecolor.setCurrentText(soup.find('tag8')['value'])
        self.cBiconcolor.setCurrentText(soup.find('tag9')['value'])
        self.dsbdocnamesi.setValue(float(soup.find('tag10')['value']))
        self.dspdocinfosi.setValue(float(soup.find('tag11')['value']))
        self.dsbpatientinfo.setValue(float(soup.find('tag12')['value']))
        self.dsbinsidesi.setValue(float(soup.find('tag14')['value']))
        self.dsbsidesi.setValue(float(soup.find('tag13')['value']))
        self.dsbaddresssi.setValue(float(soup.find('tag15')['value']))
        self.dsbtimesi.setValue(float(soup.find('tag16')['value']))
        self.cblogo.setCurrentText(soup.find('tag17')['value'])
        self.cbaddressicon.setCurrentText(soup.find('tag18')['value'])
        self.cbtimeicon.setCurrentText(soup.find('tag19')['value'])
        self.cbphoneicon.setCurrentText(soup.find('tag20')['value'])
        self.cbsoicalicon.setCurrentText(soup.find('tag21')['value'])
        self.cbalerticon.setCurrentText(soup.find('tag22')['value'])
        self.fonttype.setCurrentText(soup.find('tag23')['value'])


    def readConvertToTest(self):
        try:
            if self.cbaddressicon.currentIndex() == 0:
                addressicon = 'class="fas fa-map-marker-alt"'
            elif self.cbaddressicon.currentIndex() == 1:
                addressicon = 'class="fas fa-compass"'
            elif self.cbaddressicon.currentIndex() == 2:
                addressicon = 'class="fas fa-thumbtack"'
            elif self.cbaddressicon.currentIndex() == 3:
                addressicon = 'class="fas fa-map-marked-alt"'
            elif self.cbaddressicon.currentIndex() == 4:
                addressicon = 'class="fas fa-globe"'
            if self.cbtimeicon.currentIndex() == 0:
                timeicon = 'class="fas fa-clock"'
            elif self.cbtimeicon.currentIndex() == 1:
                timeicon = 'class="fas fa-stopwatch"'
            elif self.cbtimeicon.currentIndex() == 2:
                timeicon = 'class="fas fa-hourglass-half"'
            elif self.cbtimeicon.currentIndex() == 3:
                timeicon = 'class="far fa-calendar-alt"'
            if self.cbphoneicon.currentIndex() == 0:
                phoneicon = 'class="fas fa-phone"'
            elif self.cbphoneicon.currentIndex() == 1:
                phoneicon = 'class="fas fa-phone-square"'
            elif self.cbphoneicon.currentIndex() == 2:
                phoneicon = 'class="fas fa-mobile-alt"'
            if self.cbsoicalicon.currentIndex() == 0:
                socialicon = 'class="fab fa-whatsapp-square"'
            elif self.cbsoicalicon.currentIndex() == 1:
                socialicon = 'class="fab fa-whatsapp"'
            elif self.cbsoicalicon.currentIndex() == 2:
                socialicon = 'class="fab fa-facebook-square"'
            elif self.cbsoicalicon.currentIndex() == 3:
                socialicon = 'class="fab fa-facebook"'
            divshape= self.cblogo.currentText()
            if self.insertclinicname.isChecked():
                clitype = self.clinictype.currentText()
                cliname = self.clinicappName.text()
            else:
                clitype = ''
                cliname = ''
            name = self.listroshwidget.currentItem().text()
            hh = self.cBdocnamecolor.currentText()
            info = self.cBdocinfocolor.currentText()
            bordera = self.cBbordercolor.currentText()
            mainw = self.cBmaincolor.currentText()
            insidea = self.cBinsidecolor.currentText()
            heada = self.cBheadcolor.currentText()
            foota = self.cBfootcolor.currentText()
            addressa = self.cBaddresscolor.currentText()
            timea = self.cBtimecolor.currentText()
            iconc = self.cBiconcolor.currentText()
            heheight = (self.dshheeight.value()/21.01)*100
            foheight = (self.dsfheight.value()/21.01)*100
            namear = 'د/أحمد السيد'
            about = '<p class="info1">معاينة معاينة معاينة معاينة</p><p class="info1">معاينة معاينة معاينة معاينة</p><p class="info1">معاينة معاينة معاينة معاينة معاينة</p>'
            nameen = 'D/Ahmed Elsaid'
            abouten = '<p class="info1">معاينة معاينة معاينة معاينة</p><p class="info1">معاينة معاينة معاينة معاينة</p><p class="info1">معاينة معاينة معاينة معاينة معاينة</p>'
            age = '27'
            taskhes = 'معاينة'
            paitent = 'احمد السيد'
            date = '12/10/2021'
            address = ' معاينة'
            time = ' معاينة'
            phone1 = '01000000000'
            phone2 = '01000000000'
            phone3 = '01000000000'
            new = '<ul><li>معاينة</li><li>معاينة</li><li>معاينة</li></ul>'
            tahlel = '<ol><li>معاينة</li><li>معاينة</li><li>معاينة</li></ol>'
            hsize = self.dsbdocnamesi.value()
            infosize = self.dspdocinfosi.value()
            patsize = self.dsbpatientinfo.value()
            insize = self.dsbinsidesi.value()
            outsize = self.dsbsidesi.value()
            addsize = self.dsbaddresssi.value()
            timsize = self.dsbtimesi.value()
            fonttyp = self.fonttype.currentText()
            unique = '<i class="fas fa-exclamation-triangle" color="{}"></i> <span>معاينة</span>'.format(self.cBiconcolor.currentText())
            file_loader = FileSystemLoader(searchpath="./")
            env = Environment(loader=file_loader)
            TEMPLATE_FILE = str(name)+".html"
            template = env.get_template(TEMPLATE_FILE)
            output = template.render(heheight=heheight,foheight=foheight,unique=unique,fonttyp=fonttyp,addsize=addsize,timsize=timsize,hsize=hsize,infosize=infosize,patsize=patsize,insize=insize,outsize=outsize,clitype=clitype,cliname=cliname,divshape=divshape,addressicon=addressicon,timeicon=timeicon,phoneicon=phoneicon,socialicon=socialicon,hh=hh,info=info,bordera=bordera,mainw=mainw,insidea=insidea,heada=heada,foota=foota,addressa=addressa,
                                     timea=timea,iconc=iconc,namear=namear, about=about, nameen=nameen, abouten=abouten, age=age, taskhes=taskhes,
                                     paitent=paitent,
                                     date=date, address=address, time=time,
                                     phone1=phone1, phone2=phone2, phone3=phone3, new=new, tahlel=tahlel)
            with codecs.open("RoshList/Test" + name + ".html", "w", "utf-8") as fh:
                fh.write(u'\ufeff')
                fh.write(output)
            self.loadTestPreview()
            self.storeRoshSettings()
        except:
            self.saveErrors('Emulator Error')

    def loadTestPreview(self):
        name = self.listroshwidget.currentItem().text()
        dir = os.getcwd()
        loc = "file:///" + dir.replace('\\', '/') + "/RoshList/Test" + str(name) + ".html"
        q = QUrl(loc)
        if q.scheme() == "":
            q.setScheme("http")
        self.roshPreviw.load(q)
        self.roshPreviw.page().pdfPrintingFinished.connect(self.afterPDFPrint)
        self.roshPreviw.page().loadFinished.connect(self.showA5Test)

    def showA5Test(self):
        name = self.listroshwidget.currentItem().text()
        filename = 'RoshList/Test'+str(name)+'.pdf'
        siz = QPageSize.A5
        pap = QPageLayout.Portrait
        self.roshPreviw.page().printToPdf(filename,
                        pageLayout=QPageLayout(QPageSize(siz),pap , QMarginsF(4,4,4,4)))

    def afterPDFPrint(self):
        name = self.listroshwidget.currentItem().text()
        doc = None
        try:
            doc = fitz.open('RoshList/Test'+str(name)+'.pdf')
            first_page = doc[0]
            image_matrix = fitz.Matrix(fitz.Identity)
            image_matrix.preScale(3, 3)
            pix = first_page.getPixmap(alpha=False, matrix=image_matrix)
            pix.writePNG('RoshList/Test'+str(name)+'.png')
        except Exception as e:
            #print(e)
            if doc:
                doc.close()
                exit(0)
        self.ppixmap = QPixmap('RoshList/Test'+str(name)+'.png')
        item = QGraphicsPixmapItem(self.ppixmap.scaled(self.viewpngtest.width(), self.viewpngtest.height(),Qt.KeepAspectRatio,
                       Qt.SmoothTransformation))
        scene = QGraphicsScene()
        scene.addItem(item)
        self.viewpngtest.setScene(scene)
        self.zoomrate.setText('0X')
        self.zoomin.setEnabled(True)
        self.zoomout.setEnabled(False)

    def loadRoshImage(self):
        loc = os.getcwd()
        name = self.listroshwidget.currentItem().text()
        self.ppixmap = QPixmap(loc+'/RoshList/Test' + str(name) + '.png')
        ite = QGraphicsPixmapItem(
            self.ppixmap.scaled(self.viewpngtest.width(), self.viewpngtest.height(), Qt.KeepAspectRatio,
                                Qt.SmoothTransformation))
        scene = QGraphicsScene()
        scene.addItem(ite)
        self.viewpngtest.setScene(scene)
        self.zoomrate.setText('0X')
        self.zoomin.setEnabled(True)
        self.zoomout.setEnabled(False)

    def zoomIn(self):
        if self.zoomrate.text() == '0X':
            item = QGraphicsPixmapItem(
                self.ppixmap.scaled((self.viewpngtest.width()*0.25)+self.viewpngtest.width(), (self.viewpngtest.height()*0.25)+self.viewpngtest.height(), Qt.KeepAspectRatio,
                                    Qt.SmoothTransformation))
            self.zoomrate.setText('1X')
            self.zoomout.setEnabled(True)
        elif self.zoomrate.text() == '1X':
            item = QGraphicsPixmapItem(
                self.ppixmap.scaled((self.viewpngtest.width() * 0.50) + self.viewpngtest.width(),
                                    (self.viewpngtest.height() * 0.50) + self.viewpngtest.height(), Qt.KeepAspectRatio,
                                    Qt.SmoothTransformation))
            self.zoomrate.setText('2X')
        elif self.zoomrate.text() == '2X':
            item = QGraphicsPixmapItem(
                self.ppixmap.scaled((self.viewpngtest.width() * 1) + self.viewpngtest.width(),
                                    (self.viewpngtest.height() * 1) + self.viewpngtest.height(), Qt.KeepAspectRatio,
                                    Qt.SmoothTransformation))
            self.zoomrate.setText('3X')
        elif self.zoomrate.text() == '3X':
            item = QGraphicsPixmapItem(
                self.ppixmap.scaled((self.viewpngtest.width() * 1.25) + self.viewpngtest.width(),
                                    (self.viewpngtest.height() * 1.25) + self.viewpngtest.height(), Qt.KeepAspectRatio,
                                    Qt.SmoothTransformation))
            self.zoomrate.setText('Max')
            self.zoomin.setEnabled(False)
        scene = QGraphicsScene()
        scene.addItem(item)
        self.viewpngtest.setScene(scene)

    def zoomOut(self):
        if self.zoomrate.text() == 'Max':
            item = QGraphicsPixmapItem(
                self.ppixmap.scaled((self.viewpngtest.width()*1)+self.viewpngtest.width(), (self.viewpngtest.height()*1)+self.viewpngtest.height(), Qt.KeepAspectRatio,
                                    Qt.SmoothTransformation))
            self.zoomrate.setText('3X')
            self.zoomin.setEnabled(True)
        elif self.zoomrate.text() == '3X':
            item = QGraphicsPixmapItem(
                self.ppixmap.scaled((self.viewpngtest.width() * 0.50) + self.viewpngtest.width(),
                                    (self.viewpngtest.height() * 0.50) + self.viewpngtest.height(), Qt.KeepAspectRatio,
                                    Qt.SmoothTransformation))
            self.zoomrate.setText('2X')
        elif self.zoomrate.text() == '2X':
            item = QGraphicsPixmapItem(
                self.ppixmap.scaled((self.viewpngtest.width() * 0.25) + self.viewpngtest.width(),
                                    (self.viewpngtest.height() * 0.25) + self.viewpngtest.height(), Qt.KeepAspectRatio,
                                    Qt.SmoothTransformation))
            self.zoomrate.setText('1X')
        elif self.zoomrate.text() == '1X':
            item = QGraphicsPixmapItem(
                self.ppixmap.scaled(self.viewpngtest.width(),self.viewpngtest.height(), Qt.KeepAspectRatio,
                                    Qt.SmoothTransformation))
            self.zoomrate.setText('0X')
            self.zoomout.setEnabled(False)
        scene = QGraphicsScene()
        scene.addItem(item)
        self.viewpngtest.setScene(scene)

    def exportBackup(self):
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Question)
        msgBox.setText("Do You Accept To BackUp")
        msgBox.setWindowTitle("Create BackUp")
        msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        returnValue = msgBox.exec()
        padir = self.lineEditloc.text()
        user = self.set.value("Admin")
        password = self.set.value("AdminPass")
        dbname = self.set.value("DBName")
        if returnValue == QMessageBox.Ok:
            if self.set.value('BackUpDir') == '':
                self.chooselocation()
            else:
                if path.exists(padir) == False:
                    self.chooselocation()
                else:
                    command = r'cmd /c "C:\Program Files\MySQL\MySQL Server 8.0\bin\mysqldump.exe" --databases -hlocalhost -u'+user+' -p'+password+' '+dbname+'>'+padir+'/myBackUp_'+str(
                        date.today())+'.sql'
                    she = ShellThread(self,command)
                    she.start()

    def activateMysql80(self):
        thre = Mysql80Service(self)
        thre.start()

    def checkMysql80(self):
        self.process = QProcess()
        self.process.readyReadStandardError.connect(self.onReadyReadStandardError)
        self.process.readyReadStandardOutput.connect(self.onReadyReadStandardOutput)
        self.process.finished.connect(self.onFinished)
        self.process.start('SC query MySQL80')

    def onReadyReadStandardError(self):
        error = self.process.readAllStandardError().data().decode()
        self.saveErrors('Mysql80 Error: '+str(error))
        self.output = error

    def onReadyReadStandardOutput(self):
        result = self.process.readAllStandardOutput().data().decode()
        self.output = result


    def onFinished(self):
        stat = ""
        word = "SERVICE_NAME: MySQL80"
        if word in self.output:
            output = self.output.split('  +')
            k = []
            for i in output:
                j = re.sub('  +', "\r\n", i)
                j.split('\r\n')
                k.append(j)

            c = [o.split('\r\n') for o in k]

            last = [x for x in c if x != ['']]

            while ('' in last[0]):
                last[0].remove('')
            stat = last[0][6].strip()
        else:
            self.saveErrors('Mysql80 Error: '+ str(self.output))
        global mySQL80
        self.process.close()
        self.process.kill()
        if stat == 'RUNNING':
            self.my8check.setText('RUNNING')
            self.activateserv.setHidden(True)
            mySQL80 = True
        else:
            self.my8check.setText('STOPPED')
            self.activateserv.setHidden(False)
            mySQL80 = False
        self.setStyleformy8check()


    def checkResult(self):
        if self.result.text() == 'START':
            self.mov = QMovie(':/MainSources/tenor.gif')
            self.load.setMovie(self.mov)
            self.load.setHidden(False)
            self.loadstats.setHidden(False)
            self.mov.start()
        elif self.result.text() == 'VALID':
            self.showToaster('تم!', 'تم بنجاح.', ':/MainSources/check.gif', '#16c79a',
                             'MainSources/correct.wav',
                             1, 2000)
        elif self.result.text() == 'NOTVALID':
            self.showToaster('عفواً!', 'حدث خطأ أثناء العملية.', ':/MainSources/close.gif', '#ec0101',
                             'MainSources/fail.wav',
                             1, 2000)
        elif self.result.text() == 'UNKNOWN':
            self.showToaster('عفواً!', 'حدث خطأ أثناء العملية.', ':/MainSources/close.gif', '#ec0101',
                             'MainSources/fail.wav',
                             1, 2000)
        elif self.result.text() == 'FINISHED':
            self.load.setHidden(True)
            self.loadstats.setHidden(True)
            self.mov.stop()
        if self.result.text() == 'FINISHED' and self.sqlstatus.text() == 'غير متصل':
            self.databaseconnect()

    def checkImportDone(self):
        if self.importdone.text() == 'start':
            self.mov = QMovie(':/MainSources/tenor.gif')
            self.load.setMovie(self.mov)
            self.load.setHidden(False)
            self.loadstats.setHidden(False)
            self.mov.start()
        elif self.importdone.text() == '0':
            self.load.setHidden(True)
            self.loadstats.setHidden(True)
            self.mov.stop()
            self.showToaster('تم!', 'نجح إستيراد البيانات إلى القاعدة.', ':/MainSources/check.gif', '#16c79a', 'MainSources/correct.wav',
                             1, 2000)
            self.databaseconnect()
        else:
            self.showToaster('عفواً!', 'حدث خطأ أثناء العملية.', ':/MainSources/close.gif', '#ec0101',
                             'MainSources/fail.wav',
                             1, 2000)

    #دالة استدعاء الاعدادات وعرضها
    def settings(self):
        try:
            self.clinicappName.setText(self.set.value("ClinicName"))
            self.clinictype.setCurrentIndex(self.set.value("ClinicType"))
            self.starttime.setValue(self.set.value("StartHour"))
            self.starttimemin.setValue(self.set.value("StartMinutes"))
            self.endtime.setValue(self.set.value("EndHour"))
            self.endtimemin.setValue(self.set.value("EndMinutes"))
            self.farktime.setValue(self.set.value("AppMinus"))
            self.typepp.setCurrentIndex(self.set.value("AppSt"))
            self.estdays.setValue(self.set.value("EstTime"))
            self.mainpageapp.setCurrentIndex(self.set.value("MainPage"))
            if self.set.value("RunOnWindows") == 'true':
                self.radioyesboot.setChecked(True)
            else:
                self.radioyesboot.setChecked(False)
            self.colorgboxerd()
            if self.set.value("HideMoney") == 'true':
                self.radioyes1.setChecked(True)
            else:
                self.radioyes1.setChecked(False)
            self.color2box()
            self.lineEditloc.setText(self.set.value("BackUpDir"))

            self.sqlhost.setText(self.set.value("LocalIP"))
            self.sqlname.setText(self.set.value("DBName"))
            self.sqlusername.setText(self.set.value("Admin"))
            self.sqlpassword.setText(self.set.value("AdminPass"))
            self.sqlhost2.setText(self.set.value("RemoteIP"))
            self.sqlname2.setText(self.set.value("RemoteDBName"))
            self.sqlusername2.setText(self.set.value("RemoteUser"))
            self.sqlpassword2.setText(self.set.value("RemotePass"))
            self.sqlport2.setText(self.set.value("RemotePort"))

            self.clinicname.setText(self.set.value("ArClinicRoshName"))
            self.docname.setText(self.set.value("ArDocName"))
            self.aboutdoc1.setText(self.set.value("ArAboutDoc1"))
            self.aboutdoc2.setText(self.set.value("ArAboutDoc2"))
            self.aboutdoc3.setText(self.set.value("ArAboutDoc3"))
            self.clinicnamee.setText(self.set.value("EnClinicRoshName"))
            self.docename.setText(self.set.value("EnDocName"))
            self.aboutdoce.setText(self.set.value("EnAboutDoc1"))
            self.aboutdoce1.setText(self.set.value("EnAboutDoc2"))
            self.aboutdoce2.setText(self.set.value("EnAboutDoc3"))
            self.address1.setText(self.set.value("FirstAddress"))
            self.address2.setText(self.set.value("SecondAddress"))
            self.phone1.setText(self.set.value("PhoneOne"))
            self.phone2.setText(self.set.value("PhoneTwo"))
            self.phone3.setText(self.set.value("PhoneThird"))
            self.days.setText(self.set.value("ClinicRoshTime"))
            self.times.setText(self.set.value("ClinicRoshTimeTwo"))
            self.whatsup.setText(self.set.value("Social"))
            self.roshlinelocation.setText(self.set.value("RoshLocation"))
            self.roshestisna.setText(self.set.value("RoshWord"))
            self.listroshwidget.setCurrentRow(self.set.value("CurrentRosh"))
            if self.set.value("AutoSaveRosh") == 'Yes':
                self.saveno2.setChecked(False)
            else:
                self.saveno2.setChecked(True)
            self.checkroshbtnn()
            if self.set.value("UniqueWord") == 'true':
                self.uniqueword.setChecked(True)
            else:
                self.uniqueword.setChecked(False)
            if self.set.value("OneTime") == 'true':
                self.firsttime.setChecked(True)
            else:
                self.firsttime.setChecked(False)
            if self.set.value("OneWeek") == 'true':
                self.throuhweek.setChecked(True)
            else:
                self.throuhweek.setChecked(False)
            self.priceedit.plana.setText(self.set.value("Price1"))
            self.priceedit.planb.setText(self.set.value("Price2"))
            self.priceedit.planc.setText(self.set.value("Price3"))
            self.priceedit.pland.setText(self.set.value("Price4"))
            self.priceedit.planaa.setText(self.set.value("Price5"))
            self.priceedit.planbb.setText(self.set.value("Price6"))
            self.priceedit.plancc.setText(self.set.value("Price7"))
            self.priceedit.plandd.setText(self.set.value("Price8"))

            self.kashfprice.clear()
            self.estprice.clear()
            self.addform.pricekashf.clear()
            self.addform.priceest.clear()
            kashflis = [self.set.value("Price1"),self.set.value("Price2"),
                        self.set.value("Price3"),self.set.value("Price4")]
            estlis = [self.set.value("Price5"),self.set.value("Price6"),
                      self.set.value("Price7"),self.set.value("Price8")]
            while('' in kashflis):
                kashflis.remove('')
            while ('' in estlis):
                estlis.remove('')
            self.kashfprice.addItems(kashflis)
            self.estprice.addItems(estlis)
            self.addform.pricekashf.addItems(kashflis)
            self.addform.priceest.addItems(estlis)
            self.edit.pricekashf.addItems(kashflis)
            self.edit.priceest.addItems(estlis)
        except:
            self.saveErrors('Settings Errors')

    def setRoshSettings(self):
        try:
            self.set.setValue("ArClinicRoshName",self.clinicname.text())
            self.set.setValue("ArDocName", self.docname.text())
            self.set.setValue("ArAboutDoc1", self.aboutdoc1.text())
            self.set.setValue("ArAboutDoc2", self.aboutdoc2.text())
            self.set.setValue("ArAboutDoc3", self.aboutdoc3.text())
            self.set.setValue("EnClinicRoshName", self.clinicnamee.text())
            self.set.setValue("EnDocName", self.docename.text())
            self.set.setValue("EnAboutDoc1", self.aboutdoce.text())
            self.set.setValue("EnAboutDoc2", self.aboutdoce1.text())
            self.set.setValue("EnAboutDoc3", self.aboutdoce2.text())
            self.set.setValue("FirstAddress", self.address1.text())
            self.set.setValue("SecondAddress", self.address2.text())
            self.set.setValue("PhoneOne", self.phone1.text())
            self.set.setValue("PhoneTwo", self.phone2.text())
            self.set.setValue("PhoneThird", self.phone3.text())
            self.set.setValue("ClinicRoshTime", self.days.text())
            self.set.setValue("ClinicRoshTimeTwo", self.times.text())
            self.set.setValue("Social", self.whatsup.text())
            self.set.setValue("RoshWord",self.roshestisna.text())
            self.set.setValue("CurrentRosh",self.listroshwidget.currentRow())
            self.autoSaveRosh()
        except:
            self.saveErrors('Rosh Settings Error')

    def autoSaveRosh(self):
        if self.saveno2.isChecked() == True:
            auto = 'Yes'
        else:
            auto = 'No'
        self.set.setValue("AutoSaveRosh",auto)

    def setpriceplans(self):
        try:
            self.set.setValue("Price1", self.priceedit.plana.text())
            self.set.setValue("Price2", self.priceedit.planb.text())
            self.set.setValue("Price3", self.priceedit.planc.text())
            self.set.setValue("Price4", self.priceedit.pland.text())
            self.set.setValue("Price5", self.priceedit.planaa.text())
            self.set.setValue("Price6", self.priceedit.planbb.text())
            self.set.setValue("Price7", self.priceedit.plancc.text())
            self.set.setValue("Price8", self.priceedit.plandd.text())
            self.priceedit.close()
            self.settings()
        except:
            self.saveErrors('Price Settings Error')



    def showToaster(self,title,message,gif,fontcolor,wav,loop,time):
        try:
            parent = self
            desktop = False
            corner = Qt.BottomRightCorner
            QToaster.showMessage(parent, title,message,gif,'#ffffff',fontcolor,wav, corner=corner,loop=loop,timeout=time, desktop=desktop)
        except:
            self.saveErrors('Toaster Error')


class Image(qrcode.image.base.BaseImage):
    def __init__(self, border, width, box_size):
        self.border = border
        self.box_size = box_size
        self.width = width
        size = (width + border * 2) * box_size
        self._image = QImage(size, size, QImage.Format_RGB16)
        self._image.fill(Qt.white)

    def pixmap(self):
        return QPixmap.fromImage(self._image)

    def drawrect(self, row, col):
        # creating painter object
        painter = QPainter(self._image)

        # drawing rectangle
        painter.fillRect(
            (col + self.border) * self.box_size,
            (row + self.border) * self.box_size,
            self.box_size, self.box_size,Qt.black)


class QToaster(QFrame):
    closed = pyqtSignal()
    def __init__(self, *args, **kwargs):
        super(QToaster, self).__init__(*args, **kwargs)
        QHBoxLayout(self)
        self.setSizePolicy(QSizePolicy.Maximum,QSizePolicy.Maximum)
        self.font1 = QFont("Tajawal-Bold", 11)
        self.font2 = QFont("Tajawal-Bold", 9)
        # alternatively:
        #self.setAutoFillBackground(True)
        # self.setFrameShape(self.Box)

        self.timer = QTimer(singleShot=True, timeout=self.hide)
        self.position = 0
        self.setContentsMargins(9,1,9,1)
        if self.parent():
            self.opacityEffect = QGraphicsOpacityEffect(opacity=0)
            self.setGraphicsEffect(self.opacityEffect)
            self.opacityAni = QPropertyAnimation(self.opacityEffect, b'opacity')
            # we have a parent, install an eventFilter so that when it's resized
            # the notification will be correctly moved to the right corner
            self.parent().installEventFilter(self)
        else:
            # there's no parent, use the window opacity property, assuming that
            # the window manager supports it; if it doesn't, this won'd do
            # anything (besides making the hiding a bit longer by half a second)
            self.opacityAni = QPropertyAnimation(self, b'windowOpacity')
        self.opacityAni.setStartValue(0.)
        self.opacityAni.setEndValue(1.)
        self.opacityAni.setDuration(100)
        self.opacityAni.finished.connect(self.checkClosed)

        self.corner = Qt.BottomRightCorner
        self.margin = 10
        self.bgcolor = '#ffffff'

    def checkClosed(self):
        # if we have been fading out, we're closing the notification
        if self.opacityAni.direction() == self.opacityAni.Backward:
            self.close()

    def restore(self):
        # this is a "helper function", that can be called from mouseEnterEvent
        # and when the parent widget is resized. We will not close the
        # notification if the mouse is in or the parent is resized
        self.timer.stop()
        # also, stop the animation if it's fading out...
        self.opacityAni.stop()
        # ...and restore the opacity
        if self.parent():
            self.opacityEffect.setOpacity(1)
        else:
            self.setWindowOpacity(1)

    def hide(self):
        # start hiding
        self.opacityAni.setDirection(self.opacityAni.Backward)
        self.opacityAni.setDuration(500)
        self.opacityAni.start()


    def eventFilter(self, source, event):
        if source == self.parent() and event.type() == QEvent.Resize:
            self.opacityAni.stop()
            parentRect = self.parent().rect()
            geo = self.geometry()
            if self.corner == Qt.TopLeftCorner:
                geo.moveTopLeft(
                    parentRect.topLeft() + QPoint(self.margin, self.margin))
            elif self.corner == Qt.TopRightCorner:
                geo.moveTopRight(
                    parentRect.topRight() + QPoint(-self.margin, self.margin))
            elif self.corner == Qt.BottomRightCorner:
                geo.moveBottomRight(
                    parentRect.bottomRight() + QPoint(-10, -self.margin))
            else:
                geo.moveBottomLeft(
                    parentRect.bottomLeft() + QPoint(self.margin, -self.margin))
            self.setGeometry(geo)
            self.restore()
            self.timer.start()
        return super(QToaster, self).eventFilter(source, event)

    def enterEvent(self, event):
        self.restore()

    def leaveEvent(self, event):
        self.timer.start()

    def closeEvent(self, event):
        # we don't need the notification anymore, delete it!
        self.deleteLater()
        global posit
        posit.remove(self.position)
        #print(posit)

    def resizeEvent(self, event):
        super(QToaster, self).resizeEvent(event)
        # if you don't set a stylesheet, you don't need any of the following!
        if not self.parent():
            # there's no parent, so we need to update the mask
            path = QPainterPath()
            path.addRoundedRect(QRectF(self.rect()).translated(-.5, -.5), 4, 4)
            self.setMask(QRegion(path.toFillPolygon(QTransform()).toPolygon()))
        else:
            self.clearMask()


    def showMessage(parent, messagetitle,message,icon,bgcolor,lbgcolor,sound,corner=Qt.TopLeftCorner, closable=True,
                    timeout=5000,position=0,loop=1, desktop=False, parentWindow=True, ):

        if parent and parentWindow:
            parent = parent.window()

        if not parent or desktop:
            self = QToaster(None)
            self.setWindowFlags(self.windowFlags() | Qt.FramelessWindowHint | Qt.BypassWindowManagerHint)
            self.__self = self
            currentScreen = QApplication.primaryScreen()
            if parent and parent.window().geometry().size().isValid():
                reference = parent.window().geometry()
            else:
                reference = QRect(QCursor.pos() - QPoint(1, 1),QSize(3, 3))
            maxArea = 0
            for screen in QApplication.screens():
                intersected = screen.geometry().intersected(reference)
                area = intersected.width() * intersected.height()
                if area > maxArea:
                    maxArea = area
                    currentScreen = screen
            parentRect = currentScreen.availableGeometry()
        else:
            self = QToaster(parent)
            self.setStyleSheet('QToaster{border: 1px solid '+lbgcolor+';color:#ffffff;border-radius: 1px;background-color:'+bgcolor+';}')
            parentRect = parent.rect()
        self.timer.setInterval(timeout)

        move = QMovie(icon)
        labelIcon = QLabel()
        self.layout().setContentsMargins(9,2,9,2)
        self.layout().addWidget(labelIcon)
        #icon = self.style().standardIcon(icon)
        size = self.style().pixelMetric(QStyle.PM_SmallIconSize)
        move.setScaledSize(QSize(24, 24))
        labelIcon.setMovie(move)
        move.start()
        if loop == 1:
            loop = 1
        else:
            loop = QSound.Infinite

        self.sound = QSound(sound)
        self.sound.setLoops(loop)
        self.sound.play()

        self.group = QGroupBox()
        vbox = QVBoxLayout()
        self.label = QLabel(message)
        self.labeltitle = QLabel(messagetitle)
        self.labeltitle.setFont(self.font1)
        self.label.setFont(self.font2)
        vbox.addWidget(self.labeltitle)
        vbox.addWidget(self.label)
        vbox.setSpacing(1)
        self.group.setLayout(vbox)
        self.group.setContentsMargins(0,0,0,0)
        self.group.setStyleSheet('QGroupBox{background-color:transparent;border:0px;}QLabel{color:'+lbgcolor+';}')
        self.layout().addWidget(self.group)

        if closable:
            self.closeButton = QToolButton()
            self.closeButton.setStyleSheet('QToolButton{background-color: rgb(255, 255, 255);border:0px;}')
            self.layout().addWidget(self.closeButton)
            closeIcon = self.style().standardIcon(
                QStyle.SP_TitleBarCloseButton)
            self.closeButton.setIcon(closeIcon)
            self.closeButton.setIconSize(QSize(10,10))
            self.closeButton.setAutoRaise(True)
            self.closeButton.clicked.connect(self.close)
        global posit
        if not posit:
            position=0
        else:
            xx = list(set(locat) - set(posit))
            for b in xx:
                position=b
                break
        if 0 == position:
            margin = 10
        elif 1 == position:
            margin = 80
        elif 2 == position:
            margin = 150
        elif 3 == position:
            margin = 220
        elif 4 == position:
            margin = 290
        elif 5 == position:
            margin = 360
        elif 6 == position:
            margin = 430
        elif 7 == position:
            margin = 500
        elif 8 == position:
            margin = 570
        elif 9 == position:
            margin = 640
        elif 10 == position:
            margin = 710
        else:
            margin = 10

        self.timer.start()

        # raise the widget and adjust its size to the minimum
        self.raise_()
        self.adjustSize()

        self.corner = corner
        self.margin = margin

        geo = self.geometry()
        # now the widget should have the correct size hints, let's move it to the
        # right place
        if corner == Qt.TopLeftCorner:
            geo.moveTopLeft(
                parentRect.topLeft() + QPoint(margin, margin))
        elif corner == Qt.TopRightCorner:
            geo.moveTopRight(
                parentRect.topRight() + QPoint(-margin, margin))
        elif corner == Qt.BottomRightCorner:
            geo.moveBottomRight(
                parentRect.bottomRight() + QPoint(-10, -margin))
        else:
            geo.moveBottomLeft(
                parentRect.bottomLeft() + QPoint(margin, -margin))

        self.setGeometry(geo)
        self.show()

        if not posit:
            posit.append(0)
        else:
            xn = list(set(locat) - set(posit))
            for v in xn:
                for k in posit:
                    if v != k:
                        self.position = v
                        posit.append(v)
                        break
                break

        self.opacityAni.start()

class Mysql80Service(Thread):
    def __init__(self,window):
        Thread.__init__(self)
        self.window = window
        self.stop = None

    def run(self):
        commands = 'NET START "MySQL80"'
        w = shell.ShellExecuteEx(nShow=win32con.SW_HIDE,fMask=shellcon.SEE_MASK_NOCLOSEPROCESS,lpVerb='runas', lpFile='cmd.exe', lpParameters='/c ' + commands)
        procHandle = w['hProcess']
        obj = win32event.WaitForSingleObject(procHandle, win32event.INFINITE)
        rc = win32process.GetExitCodeProcess(procHandle)
        global mySQL80
        if rc == 0:
            self.window.my8check.setText('RUNNING')
            self.window.activateserv.setHidden(True)
            mySQL80 = True
            self.stop = True
        else:
            self.window.my8check.setText('STOPPED')
            self.window.activateserv.setHidden(False)
            mySQL80 = False
            self.stop = True

class importDatabase(Thread):
    def __init__(self,window,command):
        Thread.__init__(self)
        self.windo = window
        self.stop = None
        self.proc = QProcess()
        self.proc.readyReadStandardOutput.connect(self.readOutput)
        self.proc.readyReadStandardError.connect(self.readError)
        self.proc.readChannelFinished.connect(self.finish)
        self.proc.start(command)
        self.out = None

    def run(self):
        self.windo.result.setText('START')
        while True:
            if self.stop == None:
                self.proc.waitForReadyRead(1)
            else:
                break

    def readOutput(self):
        output = self.proc.readAllStandardOutput()
        result = bytes(output).decode("utf8")
        self.out = result

    def readError(self):
        output = self.proc.readAllStandardError()
        result = bytes(output).decode("utf8")
        self.out = result

    def finish(self):
        self.stop = True
        if 'not recognized' in self.out:
            self.windo.result.setText("NOTVALID")
        elif 'mysqldump: [Warning]' in self.out:
            self.windo.result.setText("VALID")
        elif 'mysql: [Warning]' in self.out:
            self.windo.result.setText("VALID")
        else:
            self.windo.result.setText("UNKNOWN")
        self.windo.result.setText("FINISHED")
        self.proc.kill()
        self.proc.close()
        if connn != None:
            text = 'conect'
            connn.send(text.encode("utf-8"))


class ShellThread(Thread):
    def __init__(self,ww,command):
        Thread.__init__(self)
        self.wind = ww
        self.stop = None
        self.out = None
        self.proc = QProcess()
        self.proc.readyReadStandardOutput.connect(self.readOutput)
        self.proc.readyReadStandardError.connect(self.readError)
        self.proc.readChannelFinished.connect(self.finish)
        self.proc.start(command)

    def run(self):
        self.wind.result.setText('START')
        while True:
            if self.stop == None:
                self.proc.waitForReadyRead(1)
            else:
                break

    def readOutput(self):
        output = self.proc.readAllStandardOutput()
        result = bytes(output).decode("utf8")
        self.out = result


    def readError(self):
        output = self.proc.readAllStandardError()
        result = bytes(output).decode("utf8")
        self.out = result

    def finish(self):
        self.stop = True
        if 'not recognized' in self.out:
            self.wind.result.setText("NOTVALID")
        elif 'mysqldump: [Warning]' in self.out:
            self.wind.result.setText("VALID")
        elif 'mysql: [Warning]' in self.out:
            self.wind.result.setText("VALID")
        else:
            self.wind.result.setText("UNKNOWN")
        self.wind.result.setText("FINISHED")
        self.proc.kill()
        self.proc.close()


class ServerThread(QThread):
    def __init__(self,window):
        QThread.__init__(self)
        self.window=window
        self.is_running = True

    def run(self):
        TCP_IP = '0.0.0.0'
        TCP_PORT = 25
        BUFFER_SIZE = 2000
        self.tcpServer = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.tcpServer.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.tcpServer.bind((TCP_IP, TCP_PORT))
        self.tcpServer.listen(4)
        global threadactive
        while threadactive:
            if(self.is_running):
                try:
                    global connect
                    connect = None
                    self.window.pcconn.setText('disconnected')
                    print("Multithreaded Python server : Waiting for connections from TCP clients...")
                    global connn
                    (connn, (ip,port)) = self.tcpServer.accept()
                    if self.is_running == False:
                        break
                    print("[+] New server socket thread started for " + ip + ":" + str(port))
                    connect = True
                    self.window.sqlhost2.setText(str(ip))
                    self.window.sqlport2.setText(str(port))
                    self.window.pcconn.setText('connected')
                    text = 'dbconnect'
                    connn.send(text.encode("utf-8"))
                    while (self.is_running):
                        if connn != None:
                            data = connn.recv(1024)
                            self.window.msgstatus.setText(str(data.decode("utf-8")))
                            #print(str(data.decode("utf-8")))
                            if str(data.decode("utf-8")) == 'dbconnect':
                                host = self.window.sqlhost2.text()
                                username = self.window.set.value("RemoteUser")
                                password = self.window.set.value("RemotePass")
                                dbname = self.window.set.value("RemoteDBName")
                                #print(str(data.decode("utf-8")))
                                try:
                                    global dbconnect
                                    global dbcur
                                    dbconnect = mysql.connector.connect(host=host, user=username, passwd=password, database=dbname,
                                                  auth_plugin='mysql_native_password')
                                    dbcur = dbconnect.cursor()
                                    self.window.msgstatus.setText('connected')
                                    self.send()
                                except mysql.connector.Error as err:
                                    pass
                                    #print(str(err))
                        else:
                            pass
                except socket.error as exc:
                    #print(str(exc))
                    connn=None
            else:
                break

    def send(self):
        if os.path.getsize('commands.txt') != 0:
            with open('commands.txt', 'r', encoding='utf-8') as file:
                data = file.read()
            for result in dbcur.execute(data, multi=True):
                if result.with_rows:
                    #print("Rows produced by statement '{}':".format(result.statement))
                    #print(result.fetchall())
                    pass
                else:
                    pass
                    #print("Number of rows affected by statement '{}': {}".format(result.statement, result.rowcount))
            dbconnect.commit()
            file = open('commands.txt', 'w')
            file.write('')
            file.close()
        else:
            pass

    def close(self):
        self.tcpServer.close()
        if connn != None:
            connn.close()



if __name__ == '__main__':
    from os import environ
    environ["QT_DEVICE_PIXEL_RATIO"] = "0"
    environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1"
    environ["QT_SCREEN_SCALE_FACTORS"] = "1"
    environ["QT_SCALE_FACTOR"] = "1"
    app = QApplication(sys.argv)
    window = Main()
    window.show()
    serverThread = ServerThread(window)
    serverThread.start()
    app.exec_()
    serverThread.is_running = False
    serverThread.close()


