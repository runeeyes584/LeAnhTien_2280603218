# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './ui/caesar.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_CaesarCipher(object):
    def setupUi(self, CaesarCipher):
        CaesarCipher.setObjectName("CaesarCipher")
        CaesarCipher.resize(941, 704)
        self.label_2 = QtWidgets.QLabel(CaesarCipher)
        self.label_2.setGeometry(QtCore.QRect(20, 130, 171, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(CaesarCipher)
        self.label_3.setGeometry(QtCore.QRect(20, 340, 171, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(CaesarCipher)
        self.label_4.setGeometry(QtCore.QRect(20, 430, 191, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(CaesarCipher)
        self.label_5.setGeometry(QtCore.QRect(250, 30, 691, 81))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.btn_decrypt = QtWidgets.QPushButton(CaesarCipher)
        self.btn_decrypt.setGeometry(QtCore.QRect(690, 630, 191, 61))
        self.btn_decrypt.setObjectName("btn_decrypt")
        self.btn_encrypt = QtWidgets.QPushButton(CaesarCipher)
        self.btn_encrypt.setGeometry(QtCore.QRect(490, 630, 171, 61))
        self.btn_encrypt.setObjectName("btn_encrypt")
        self.plaintext = QtWidgets.QTextEdit(CaesarCipher)
        self.plaintext.setGeometry(QtCore.QRect(250, 130, 651, 201))
        self.plaintext.setObjectName("plaintext")
        self.ciphertext = QtWidgets.QTextEdit(CaesarCipher)
        self.ciphertext.setGeometry(QtCore.QRect(250, 430, 651, 171))
        self.ciphertext.setObjectName("ciphertext")
        self.key = QtWidgets.QTextEdit(CaesarCipher)
        self.key.setGeometry(QtCore.QRect(250, 340, 651, 81))
        self.key.setObjectName("key")

        self.retranslateUi(CaesarCipher)
        QtCore.QMetaObject.connectSlotsByName(CaesarCipher)

    def retranslateUi(self, CaesarCipher):
        _translate = QtCore.QCoreApplication.translate
        CaesarCipher.setWindowTitle(_translate("CaesarCipher", "Caesar Cipher"))
        self.label_2.setText(_translate("CaesarCipher", "PLAIN TEXT:"))
        self.label_3.setText(_translate("CaesarCipher", "KEY:"))
        self.label_4.setText(_translate("CaesarCipher", "CIPHER TEXT:"))
        self.label_5.setText(_translate("CaesarCipher", "CAESAR CIPHER"))
        self.btn_decrypt.setText(_translate("CaesarCipher", "Decrypt"))
        self.btn_encrypt.setText(_translate("CaesarCipher", "Encrypt"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    CaesarCipher = QtWidgets.QDialog()
    ui = Ui_CaesarCipher()
    ui.setupUi(CaesarCipher)
    CaesarCipher.show()
    sys.exit(app.exec_())
