from PyQt5.QtCore import QUrl,Qt,QProcess,QEventLoop,QMarginsF
from PyQt5.QtGui import QFont,QPixmap,QPageSize,QPageLayout,QIcon,QMovie
from PyQt5.QtWidgets import QVBoxLayout,QDialog,QApplication,QLabel,QWidget
import re
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtPrintSupport import QPrintDialog, QPrinter
import fitz
from printpre import Ui_Dialog as printpre


class printpreviewme(QDialog,printpre):
    def __init__(self):
        super(printpreviewme, self).__init__()
        QDialog.__init__(self)
        self.setupUi(self)
        self.did = False
        self.pP = None
        self.do = None
        self.win = QWebEngineView()
        self.font = QFont('Google Sans,arial,sans-serif',11)
        self.printpsize.setFont(self.font)
        self.layoutP.setFont(self.font)
        self.pusprint.clicked.connect(self.print)
        self.printdes.currentIndexChanged.connect(self.seticon)
        self.printpsize.currentIndexChanged.connect(self.handle_loadFinished)
        self.layoutP.currentIndexChanged.connect(self.handle_loadFinished)
        self.printdialog.clicked.connect(self.printDialog)
        self.urllocation.textChanged.connect(self.openurl)
        self.win.page().pdfPrintingFinished.connect(self.handle_pdfPrintingFinished)
        self.win.page().loadFinished.connect(self.handle_loadFinished)

    def saveRoshbyName(self,do,loc,name,dat):
        self.do = do
        self.location = loc
        self.name = name
        self.date = dat

    def openurl(self):
        url = self.urllocation.text()
        q = QUrl(url)
        if q.scheme() == "":
            q.setScheme("http")
        self.win.load(q)


    def handle_pdfPrintingFinished(self):
        doc = None
        try:
            doc = fitz.open('out.pdf')
            first_page = doc[0]
            image_matrix = fitz.Matrix(fitz.Identity)
            image_matrix.preScale(3, 3)
            pix = first_page.getPixmap(alpha=False, matrix=image_matrix)
            pix.writePNG('out.png')
        except Exception as e:
            print(e)
            self.label5.setText('حدث خطأ!')
            if doc:
                doc.close()
                exit(0)
        self.did = True
        pixmap = QPixmap('out.png')
        self.label5.setPixmap(pixmap.scaled(self.label5.width(), self.label5.height(),Qt.KeepAspectRatio,
                       Qt.SmoothTransformation))



    def handle_loadFinished(self):
        self.label5.setText('جارى المعاينة...')
        if self.printpsize.currentIndex() == 0:
            siz = QPageSize.A5
        elif self.printpsize.currentIndex() ==1:
            siz = QPageSize.Letter
        elif self.printpsize.currentIndex() ==2:
            siz = QPageSize.Legal
        elif self.printpsize.currentIndex() ==3:
            siz = QPageSize.A4
        elif self.printpsize.currentIndex() ==4:
            siz = QPageSize.B5
        else:
            siz = QPageSize.A6
        if self.layoutP.currentIndex() == 0:
            pap = QPageLayout.Portrait
        else:
            pap = QPageLayout.Landscape
        self.win.page().printToPdf('out.pdf',
                        pageLayout=QPageLayout(QPageSize(siz),pap , QMarginsF(4,4,4,4)))



    def saveinPDF(self,loc):
        printer = QPrinter(QPrinter.HighResolution)
        printer.setOutputFormat(QPrinter.PdfFormat)
        printer.setPageSize(QPrinter.A5)
        printer.setOutputFileName(loc)
        self.printDocument(printer)

    def getPrinterProcess(self):
        self.printdes.clear()
        if self.pP is None:
            self.pP = QProcess()  # Keep a reference to the QProcess (e.g. on self) while it's running.
            self.pP.readyReadStandardOutput.connect(self.handle_stdout)
            self.pP.readyReadStandardError.connect(self.handle_stderr)
            #self.pP.stateChanged.connect(self.handle_state)
            self.pP.finished.connect(self.process_finished)  # Clean up once complete.
            self.pP.start("wmic printer get name,default")


    def handle_stderr(self):
        data = self.pP.readAllStandardError()
        stderr = bytes(data).decode("utf8")
        # Extract progress if it is in the data.

    def handle_stdout(self):
        data = self.pP.readAllStandardOutput()
        stdout = bytes(data).decode("utf8")
        output = stdout.split('\r\r\n')
        k = []
        for i in output:
            j = re.sub('  +', "\r\r\n", i)
            j.split('\r\r\n')
            k.append(j)
        c = [o.split('\r\r\n') for o in k]
        last = [x for x in c if x != ['']]
        while ('' in last):
            last.remove('')
        m = []
        for x in range(1, len(last)):
            value = last[x][0:2]
            m.append(value)
        for n, nn in enumerate(m):
            try:
                if nn.index('TRUE') == 0:
                    ss = nn
                    self.printdes.addItem(ss[1])
                else:
                    pass
            except:
                pass
        liss = [x for x in m if x != ss]
        for i in liss:
            self.printdes.addItem(i[1])
        self.seticon(0)
        self.printdes.setFont(self.font)
        self.printdes.view().setMinimumWidth(300)


    def seticon(self,index):
        icon = QIcon(':/MainSources/printerblue.png')
        iconw = QIcon(':/MainSources/printerwhite.png')
        self.printdes.setItemIcon(index,icon)
        for i in range(0,self.printdes.count()):
            if i == index:
                continue
            self.printdes.setItemIcon(i, iconw)

    def process_finished(self):
        self.pP = None

    def printDialog(self):
        printer = QPrinter(QPrinter.HighResolution)
        printer.setPageMargins(0, 0, 0, 0, QPrinter.Millimeter)
        printer.setPageSize(QPrinter.A5)
        printer.setOrientation(QPrinter.Portrait)
        dialog = QPrintDialog(printer, self)
        if dialog.exec_() != QDialog.Accepted:
            return
        self.printDocument(printer)

    def print(self):
        printer = QPrinter(QPrinter.HighResolution)
        printer.setPrinterName(self.printdes.currentText())
        printer.setPageMargins(0, 0, 0, 0, QPrinter.Millimeter)
        if self.printpsize.currentIndex() == 0:
            printer.setPageSize(QPrinter.A5)
        elif self.printpsize.currentIndex() == 1:
            printer.setPageSize(QPrinter.Letter)
        elif self.printpsize.currentIndex() == 2:
            printer.setPageSize(QPrinter.Legal)
        elif self.printpsize.currentIndex() == 3:
            printer.setPageSize(QPrinter.A4)
        elif self.printpsize.currentIndex() == 4:
            printer.setPageSize(QPrinter.B5)
        else:
            printer.setPageSize(QPrinter.A5)
        if self.layoutP.currentIndex() == 0:
            printer.setOrientation(QPrinter.Portrait)
        else:
            printer.setOrientation(QPrinter.Landscape)
        printer.setCopyCount(self.spinBox.value())
        self.printDocument(printer)
        if self.do != None:
            loc=self.location+'/'+self.name+self.date+'.pdf'
            self.saveinPDF(loc)
        self.do = None
        #print(printer.printerName())

    def printDocument(self, printer):
        loop = QEventLoop()
        result = False

        def printPreview(success):
            nonlocal result
            result = success
            loop.quit()
        self.win.page().print(printer,printPreview)
        loop.exec_()
        '''
        if not result:
            setText('تم رفض الأمر')
            return
        else:
            self.accept()
        '''
