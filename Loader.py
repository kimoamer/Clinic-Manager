from PyQt5.QtWidgets import QApplication , QMainWindow , QGraphicsDropShadowEffect,QMessageBox
from PyQt5.QtCore import Qt , QTimer
from PyQt5.QtGui import QFont,QMovie,QIcon
from load import Ui_MainWindow as load
import sys

count = 0
class Load(QMainWindow,load):
    import doctorclinic as other
    def __init__(self,parent=None):
        super(Load, self).__init__(parent)
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.setWindowIcon(QIcon('MainSources\DC.png'))
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.font2 = QFont("Helvetica", 50)
        self.font2.setBold(True)
        self.ont = QFont('Almarai', 15)
        self.onto = QFont('Almarai', 10)
        self.msg.setFont(self.onto)
        self.mov = QMovie(':/MainSources/tenor.gif')
        self.mov.start()
        self.looop.setMovie(self.mov)
        self.loadshadow()
        self.timer = QTimer()
        self.timer.timeout.connect(self.showMain)
        self.timer.start(35)


    def loadshadow(self):
        self.label.setFont(self.font2)
        self.label3.setFont(self.ont)
        lis = [self.groupBox_3,self.groupBox_4,self.groupBox_5,self.groupBox_6]
        for i in lis:
            shadow = QGraphicsDropShadowEffect(blurRadius=8, xOffset=0, yOffset=0)
            i.setGraphicsEffect(shadow)

    def massege(self, text):
        self.msBox = QMessageBox()
        self.msBox.setIcon(QMessageBox.Information)
        self.msBox.setText(text)
        self.msBox.setWindowTitle("Screen Resolution Error")
        self.msBox.setStandardButtons(QMessageBox.Cancel)
        self.msBox.exec()

    def showMain(self):
        global count
        if count==5:
            if rect.width() < 1240:
                self.massege("App Can't perform on screen width lower than 1240px.")
                self.timer.stop()
                self.close()
            self.main = self.other.Main(rect.width(),rect.height())
            self.msg.setText('جارى تجهيز التطبيق..')
        elif count == 12:
            self.main.settings()
            self.msg.setText('تجهيز الإعدادات...')
        elif count == 15:
            self.main.checkMysql80()
            self.msg.setText('فحص خدمة قاعدة البيانات..')
        elif count == 20:
            self.main.onrun()
            self.msg.setText('تعريف المكونات...')
        elif count == 25:
            self.main.designtables()
        elif count == 30:
            self.msg.setText('إنشاء الرسم البيانى...')
            self.main.setShadow()
            self.main.runOnBoot()
            self.main.resolution()
            self.msg.setText('وضع الظلال...')
            self.msg.setText('جارى فتح التطبيق..')
            self.thre = self.other.ServerThread(self.main)
        elif count >35:
            if self.other.done == True:
                self.timer.stop()
                self.main.show()
                self.main.checkPatientExist()
                self.thre.start()
                self.close()
        count+=1


def main():
    global rect
    app = QApplication(sys.argv)
    screen = app.primaryScreen()
    rect = screen.availableGeometry()
    window= Load()
    window.show()
    app.exec_()

if __name__ == '__main__':
    from os import environ
    environ["QT_DEVICE_PIXEL_RATIO"] = "0"
    environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1"
    environ["QT_SCREEN_SCALE_FACTORS"] = "1"
    environ["QT_SCALE_FACTOR"] = "1"
    main()
