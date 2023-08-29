import sys
from PyQt5 import QtWidgets, QtGui, QtCore


class Ui_DecryptedWindow(object):
    def setupUi(self, DecryptedWindow):
        DecryptedWindow.setObjectName("DecryptedWindow")
        DecryptedWindow.resize(407, 475)
        icon = QtGui.QIcon(".\\ui\\icons/decrypted_window_icon.png")
        DecryptedWindow.setWindowIcon(icon)
        DecryptedWindow.setStyleSheet("background-color: #1F2933;")

        self.textBrowser = QtWidgets.QTextBrowser(DecryptedWindow)
        self.textBrowser.setGeometry(QtCore.QRect(10, 10, 391, 451))
        self.textBrowser.setStyleSheet("background-color: #3E4C59;\n"
                                       "font: 12pt \"Calibri\";\n"
                                       "color: white;")
        self.textBrowser.setAcceptRichText(False)
        self.textBrowser.setObjectName("textBrowser")

        self.retranslateUi(DecryptedWindow)
        QtCore.QMetaObject.connectSlotsByName(DecryptedWindow)

    def retranslateUi(self, DecryptedWindow):
        _translate = QtCore.QCoreApplication.translate
        DecryptedWindow.setWindowTitle(_translate("DecryptedWindow", "Decrypted Text"))
        self.textBrowser.setHtml(_translate("DecryptedWindow", ""))


class DecryptedWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_DecryptedWindow()
        self.ui.setupUi(self)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    decrypted_window = DecryptedWindow()
    decrypted_window.show()
    sys.exit(app.exec_())
