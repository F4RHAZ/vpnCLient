# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\vpnUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from pythonping import ping
import requests, json, sys, base64, tempfile, subprocess, time, signal

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(826, 573)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.IPLabel = QtWidgets.QLabel(self.centralwidget)
        self.IPLabel.setGeometry(QtCore.QRect(40, 40, 271, 51))
        font = QtGui.QFont()
        font.setPointSize(20)

        self.IPLabel.setFont(font)
        self.IPLabel.setTextFormat(QtCore.Qt.RichText)
        self.IPLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.IPLabel.setObjectName("IPLabel")

        self.IpInput = QtWidgets.QTextEdit(self.centralwidget)
        self.IpInput.setGeometry(QtCore.QRect(320, 40, 391, 61))
        self.IpInput.setObjectName("IpInput")

        self.pingBTN = QtWidgets.QPushButton(self.centralwidget)
        self.pingBTN.setGeometry(QtCore.QRect(80, 170, 161, 71))
        self.pingBTN.setObjectName("pingBTN")
        self.pingBTN.clicked.connect(self.pingIP)

        self.StatusLabel = QtWidgets.QLabel(self.centralwidget)
        self.StatusLabel.setGeometry(QtCore.QRect(80, 270, 101, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.StatusLabel.setFont(font)
        self.StatusLabel.setObjectName("StatusLabel")

        self.connectBTN = QtWidgets.QPushButton(self.centralwidget)
        self.connectBTN.setGeometry(QtCore.QRect(300, 170, 161, 71))
        self.connectBTN.setObjectName("connectBTN")
        self.connectBTN.clicked.connect(self.connectToVPN)


        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(520, 170, 161, 71))
        self.pushButton_2.setObjectName("pushButton_2")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(250, 280, 431, 221))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setText("")
        self.label.setObjectName("label")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 826, 26))
        self.menubar.setObjectName("menubar")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        self.menuAbout = QtWidgets.QMenu(self.menubar)
        self.menuAbout.setObjectName("menuAbout")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.IPLabel.setText(_translate("MainWindow", "Enter IP to server"))
        self.pingBTN.setText(_translate("MainWindow", "TEST CONNECTION"))
        self.StatusLabel.setText(_translate("MainWindow", "STATUS: "))
        self.connectBTN.setText(_translate("MainWindow", "CONNECT"))
        self.pushButton_2.setText(_translate("MainWindow", "DISCONNECT"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.menuAbout.setTitle(_translate("MainWindow", "About"))

    def pingIP(self):
        server = self.IpInput.toPlainText()
        reply = ping(str(server))
        reply = str(reply)
        self.label.setText("Server to ping is: " + server + "\nPinging.....  \n" + reply)



    def connectToVPN(self):
        ovpn_path = ""
        opevpn_process = subprocess.Popen(['sudo', OPENVPN_PATH, '--config', ovpn_path])

        try:
            while True:
                time.sleep(600)

        except:
            try:
                opevpn_process.kill()
            except:
                pass
            while opevpn_process.poll() != 0:
                time.sleep(1)
            print(" OPEN VPN DISCONNECTED ")


    def saveOvpn(self, server):
        _, ovpn_path = tempfile.mkstemp()
        ovpn = open(ovpn_path, 'w')
        ovpn.write(base64.b64decode(server["OpenVPN_ConfigData_Base64"]))
        ovpn.write('\nscript-security 2\nup /etc/openvpn/update-resolv-conf\ndown /etc/openvpn/update-resolv-conf'.encode())
        ovpn.close()
        return ovpn_path


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
