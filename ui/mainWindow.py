import sys
from PyQt5 import QtWidgets, QtGui, QtCore


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(652, 505)
        icon = QtGui.QIcon(".\\ui\\icons/window_icon.png")
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(
            "background-color: #121212;\n"
            "color: white;\n"
            "font-family: \"Lucida Console\", \"Courier New\", monospace;"
        )

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(40, 50, 381, 91))
        self.frame.setStyleSheet(
            "background-color: #1F2933;\n" "border-radius: 15px;"
        )
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")

        self.b_encrypt_btn = QtWidgets.QPushButton(self.centralwidget)
        self.b_encrypt_btn.setGeometry(QtCore.QRect(270, 60, 141, 31))
        self.b_decrypt_btn = QtWidgets.QPushButton(self.centralwidget)
        self.b_decrypt_btn.setGeometry(QtCore.QRect(270, 100, 141, 31))
        self.psw_encrypt_btn = QtWidgets.QPushButton(self.centralwidget)
        self.psw_encrypt_btn.setGeometry(QtCore.QRect(50, 60, 161, 31))
        self.psw_decrypt_btn = QtWidgets.QPushButton(self.centralwidget)
        self.psw_decrypt_btn.setGeometry(QtCore.QRect(50, 100, 161, 31))
        self.file_btn = QtWidgets.QPushButton(self.centralwidget)
        self.file_btn.setGeometry(QtCore.QRect(40, 370, 141, 71))
        self.filepath_label = QtWidgets.QLabel(self.centralwidget)
        self.filepath_label.setGeometry(QtCore.QRect(50, 450, 111, 21))
        self.psw_edit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.psw_edit.setGeometry(QtCore.QRect(200, 390, 211, 31))
        self.overwrite_check = QtWidgets.QCheckBox(self.centralwidget)
        self.overwrite_check.setGeometry(QtCore.QRect(510, 390, 91, 17))
        self.readonly_check = QtWidgets.QCheckBox(self.centralwidget)
        self.readonly_check.setGeometry(QtCore.QRect(510, 420, 81, 17))
        self.output_label = QtWidgets.QLabel(self.centralwidget)
        self.output_label.setGeometry(QtCore.QRect(50, 170, 361, 21))

        for button in (
            self.b_encrypt_btn,
            self.b_decrypt_btn,
            self.psw_encrypt_btn,
            self.psw_decrypt_btn,
            self.file_btn,
        ):
            button.setStyleSheet("background-color: #212121;\n" "text-decoration: underline;")

        self.file_btn.setStyleSheet("background-color: #102A43;\n" "font: 11pt \"Consolas\";")
        self.output_label.setStyleSheet("background-color: #222222")

        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "CipherShield"))
        self.b_encrypt_btn.setText(_translate("MainWindow", "Basic Encryption"))
        self.b_decrypt_btn.setText(_translate("MainWindow", "Basic Decrypt"))
        self.psw_encrypt_btn.setText(_translate("MainWindow", "Password Encryption"))
        self.psw_decrypt_btn.setText(_translate("MainWindow", "Password Decrypt"))
        self.file_btn.setText(_translate("MainWindow", "Select File"))
        self.filepath_label.setText(_translate("MainWindow", "[Selected File]"))
        self.psw_edit.setPlaceholderText(_translate("MainWindow", "Password"))
        self.overwrite_check.setText(_translate("MainWindow", "Overwrite"))
        self.readonly_check.setText(_translate("MainWindow", "ReadOnly"))
        self.output_label.setText(_translate("MainWindow", " >"))


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())
