import os
import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QFileDialog
from cryptography.fernet import InvalidToken
from ui.mainWindow import Ui_MainWindow
from ui.decryptedTextWindow import Ui_DecryptedWindow
from crypto import basic_encryption, basic_decryption, \
    encryption_with_psw, decryption_with_psw
class UIFunctionality(Ui_MainWindow, QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setupInteraction()
        self.readonly_check.setChecked(True)
    def setupInteraction(self):
        self.psw_encrypt_btn.clicked.connect(self.psw_encrypt_clicker)
        self.psw_decrypt_btn.clicked.connect(self.psw_decrypt_clicker)
        self.b_encrypt_btn.clicked.connect(self.b_encrypt_clicker)
        self.b_decrypt_btn.clicked.connect(self.b_decrypt_clicker)
        self.file_btn.clicked.connect(self.file_dialog)
    def psw_encrypt_clicker(self):
        try:
            encryption_with_psw(
                self.fname,
                self.psw_edit.toPlainText(),
                self.overwrite_check.isChecked()
            )
            self.output_text("Succeed Encryption")
            self.reset_state()
        except AttributeError:
            self.output_text("ERROR: File or password not selected")
    def psw_decrypt_clicker(self):
        try:
            readonly = self.readonly_check.isChecked()
            decrypted_content = decryption_with_psw(
                self.fname,
                self.psw_edit.toPlainText(),
                readonly
            )
            if readonly:
                decrypted_text_window.showText(decrypted_content.decode('utf-8'))
            self.output_text("Succeed Decryption")
            self.reset_state()
        except AttributeError:
            self.output_text("ERROR: File or password not selected")
        except InvalidToken:
            self.output_text("ERROR: Invalid or Wrong password")
    def b_encrypt_clicker(self):
        try:
            basic_encryption(
                self.fname,
                self.overwrite_check.isChecked()
            )
            self.output_text("Succeed Basic Encryption")
            self.reset_state()
        except AttributeError:
            self.output_text("ERROR: File not selected")
    def b_decrypt_clicker(self):
        try:
            readonly = self.readonly_check.isChecked()
            decrypted_content = basic_decryption(
                self.fname,
                readonly
            )
            if readonly:
                decrypted_text_window.showText(decrypted_content.decode('utf-8'))
            self.output_text("Succeed Basic Decryption")
            self.reset_state()
        except AttributeError:
            self.output_text("ERROR: File not selected")
    def file_dialog(self):
        fname, _ = QFileDialog.getOpenFileName(
            self, "Select File", "", "All Files (*)"
        )
        if os.path.isfile(fname):
            self.fname = fname
            self.filepath_label.setText(fname)
            self.filepath_label.adjustSize()
    def output_text(self, text: str):
        """Outputs the text into the output label"""
        self.output_label.setText(' > ' + text)
    def reset_state(self):
        """Resets the general state of the program"""
        del self.fname
        self.filepath_label.setText("[Selected File]")
        self.filepath_label.adjustSize()
        self.overwrite_check.setChecked(False)
        self.readonly_check.setChecked(False)
class OutputWindow(Ui_DecryptedWindow, QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
    def showText(self, text: str):
        """Shows a text"""
        self.textBrowser.setPlainText(text)
        self.show()
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = UIFunctionality()
    decrypted_text_window = OutputWindow()
    MainWindow.show()
    sys.exit(app.exec_())
