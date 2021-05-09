from PyQt5.QtWidgets import QDialog
from smulat import Ui_Form as smult

class Dialog(QDialog, smult):
    def __init__(self):
        super(Dialog, self).__init__()
        QDialog.__init__(self)
        self.setupUi(self)

