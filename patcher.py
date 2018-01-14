# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'patcher.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import urllib.request
import random
import tarfile
import os
import subprocess

url = "http://fallback.hextcg.com/static/live/linux/hex.tar.gz"
archivepath = "hex.tar.gz"

defaultInstallDir="{}/hex/".format(os.getcwd())
defaultDownloadDir="/tmp/"

class Ui_hexpatcherwindow(object):
    def setupUi(self, hexpatcherwindow):
        hexpatcherwindow.setObjectName("hexpatcherwindow")
        hexpatcherwindow.resize(800, 570)
        hexpatcherwindow.setMinimumSize(QtCore.QSize(800, 570))
        hexpatcherwindow.setMaximumSize(QtCore.QSize(800, 570))
        self.centralwidget = QtWidgets.QWidget(hexpatcherwindow)
        self.centralwidget.setStyleSheet("#centralwidget { \n"
                                         "background-image: url(:/bg/hex-bg.jpg); \n"
                                         "background-position: center;\n"
                                         "}")
        self.centralwidget.setObjectName("centralwidget")
        settings = QtCore.QSettings('fosspill', 'hex-linux-patcher')
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(180, 440, 441, 23))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setTextVisible(False)
        self.progressBar.setInvertedAppearance(False)
        self.progressBar.setObjectName("progressBar")
        self.playButton = QtWidgets.QPushButton(self.centralwidget)
        self.playButton.setEnabled(True)
        self.playButton.setGeometry(QtCore.QRect(200, 470, 401, 81))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.playButton.setFont(font)
        self.playButton.setAutoFillBackground(False)
        self.playButton.setCheckable(False)
        self.playButton.setAutoExclusive(False)
        self.playButton.setAutoDefault(True)
        self.playButton.setDefault(True)
        self.playButton.setFlat(False)
        self.playButton.setObjectName("playButton")
        self.newsframe = QtWidgets.QFrame(self.centralwidget)
        self.newsframe.setEnabled(True)
        self.newsframe.setGeometry(QtCore.QRect(189, 159, 421, 251))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(4, 23, 44))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(6, 34, 66))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(5, 28, 55))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(2, 11, 22))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(2, 15, 29))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(4, 23, 44))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(2, 11, 22))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(4, 23, 44))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(6, 34, 66))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(5, 28, 55))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(2, 11, 22))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(2, 15, 29))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(4, 23, 44))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(2, 11, 22))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(2, 11, 22))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(4, 23, 44))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(6, 34, 66))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(5, 28, 55))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(2, 11, 22))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(2, 15, 29))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(2, 11, 22))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(2, 11, 22))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(4, 23, 44))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(4, 23, 44))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(4, 23, 44))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipText, brush)
        self.newsframe.setPalette(palette)
        self.newsframe.setAutoFillBackground(True)
        self.newsframe.setFrameShape(QtWidgets.QFrame.Box)
        self.newsframe.setFrameShadow(QtWidgets.QFrame.Raised)
        self.newsframe.setObjectName("newsframe")
        self.label = QtWidgets.QLabel(self.newsframe)
        self.label.setGeometry(QtCore.QRect(10, 10, 351, 20))
        font = QtGui.QFont()
        font.setFamily("Nimbus Sans")
        font.setKerning(False)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.line = QtWidgets.QFrame(self.newsframe)
        self.line.setGeometry(QtCore.QRect(10, 20, 401, 16))
        self.line.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line.setMidLineWidth(0)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setObjectName("line")
        self.patchnotes = QtWidgets.QWidget(self.newsframe)
        self.patchnotes.setGeometry(QtCore.QRect(9, 39, 401, 201))
        self.patchnotes.setObjectName("patchnotes")
        self.patchtext = QtWidgets.QTextBrowser(self.patchnotes)
        self.patchtext.setGeometry(QtCore.QRect(10, 0, 381, 201))
        self.patchtext.setStyleSheet("background-color:rgba(0,0,0,0)")
        self.patchtext.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.patchtext.setObjectName("patchtext")
        self.patchtext.setOpenExternalLinks(True)
        self.uptodate = QtWidgets.QCheckBox(self.centralwidget)
        self.uptodate.setToolTip("Workaround until update detection is possible.")
        self.uptodate.setGeometry(QtCore.QRect(10, 540, 151, 22))
        self.uptodate.setObjectName("uptodate")
        self.uptodate.setChecked(settings.value('forceuptodate', type=bool))
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(180, 551, 441, 15))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_6.setFont(font)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.optionsButton = QtWidgets.QPushButton(self.centralwidget)
        self.optionsButton.setGeometry(QtCore.QRect(670, 540, 119, 18))
        self.optionsButton.setAutoFillBackground(False)
        self.optionsButton.setStyleSheet(":hover{ \n"
                                         "color: gray;\n"
                                         "}\n"
                                         "#optionsButton{\n"
                                         "border:0;\n"
                                         "text-align: right;\n"
                                         "}")
        self.optionsButton.setFlat(True)
        self.optionsButton.setObjectName("optionsButton")
        self.optionsWidget = QtWidgets.QWidget(self.centralwidget)
        self.optionsWidget.setGeometry(QtCore.QRect(670, 452, 121, 81))
        self.optionsWidget.setObjectName("optionsWidget")
        self.optionsWidget.setVisible(False)
        self.verticalLayoutWidget = QtWidgets.QWidget(self.optionsWidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 10, 121, 71))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.optionsLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.optionsLayout.setContentsMargins(0, 0, 0, 0)
        self.optionsLayout.setObjectName("optionsLayout")
        self.forceInstallButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.forceInstallButton.setEnabled(False)
        self.forceInstallButton.setAutoFillBackground(False)
        self.forceInstallButton.setStyleSheet(":hover{ \n"
                                              "color: gray;\n"
                                              "}\n"
                                              "#forceInstallButton{\n"
                                              "border:0;\n"
                                              "text-align: right;\n"
                                              "}")
        self.forceInstallButton.setFlat(True)
        self.forceInstallButton.setObjectName("forceInstallButton")
        self.optionsLayout.addWidget(self.forceInstallButton)
        self.installDirButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.installDirButton.setAutoFillBackground(False)
        self.installDirButton.setStyleSheet(":hover{ \n"
                                            "color: gray;\n"
                                            "}\n"
                                            "#installDirButton{\n"
                                            "border:0;\n"
                                            "text-align: right;\n"
                                            "}")
        self.installDirButton.setFlat(True)
        self.installDirButton.setObjectName("installDirButton")
        self.installDirButton.setToolTip(settings.value("installDir", defaultInstallDir, type=str))
        self.optionsLayout.addWidget(self.installDirButton)
        self.downloadDirButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.downloadDirButton.setAutoFillBackground(False)
        self.downloadDirButton.setStyleSheet(":hover{ \n"
                                             "color: gray;\n"
                                             "}\n"
                                             "#downloadDirButton{\n"
                                             "border:0;\n"
                                             "text-align: right;\n"
                                             "}")
        self.downloadDirButton.setFlat(True)
        self.downloadDirButton.setObjectName("downloadDirButton")
        self.downloadDirButton.setToolTip(settings.value("downloadDir", defaultDownloadDir, type=str))
        self.optionsLayout.addWidget(self.downloadDirButton)
        hexpatcherwindow.setCentralWidget(self.centralwidget)
        self.actionChange_download_directory = QtWidgets.QAction(hexpatcherwindow)
        self.actionChange_download_directory.setEnabled(True)
        self.actionChange_download_directory.setObjectName("actionChange_download_directory")
        self.actionForce_redownload = QtWidgets.QAction(hexpatcherwindow)
        self.actionForce_redownload.setObjectName("actionForce_redownload")

        self.retranslateUi(hexpatcherwindow)

        self.playButton.clicked.connect(self.playButtonClick)
        self.uptodate.toggled.connect(self.uptodateToggle)
        self.optionsButton.clicked.connect(self.toggleOptions)
        self.installDirButton.clicked.connect(self.selectInstallDir)
        self.downloadDirButton.clicked.connect(self.selectDownloadDir)


        QtCore.QMetaObject.connectSlotsByName(hexpatcherwindow)

    def retranslateUi(self, hexpatcherwindow):
        _translate = QtCore.QCoreApplication.translate
        hexpatcherwindow.setWindowTitle(_translate("hexpatcherwindow", "Unofficial Hex: Shards of Fate Patcher"))
        self.playButton.setText(_translate("hexpatcherwindow", "Check for updates"))
        self.label.setText(_translate("hexpatcherwindow", "Maintenance and Updates - HEX: Shards of Fate"))
        self.patchtext.setHtml(_translate("hexpatcherwindow",
                                          "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                          "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                          "p, li { white-space: pre-wrap; }\n"
                                          "</style></head><body style=\" font-family:\'Noto Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
                                          "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a href=\"https://forums.hextcg.com/index.php?thread/3001-dead-of-winter-update-patch-notes-1-0-8-049/\"><span style=\" font-weight:600; text-decoration: underline; color:#2980b9;\">Dead of Winter Update - Patch Notes 1.0.8.049</span></a><br />Patch Notes for our 1.0.8.049 update are now up: <a href=\"https://www.hextcg.com/dead-winter-update-patch-notes-1-0-8-049/\"><span style=\" text-decoration: underline; color:#2980b9;\">hextcg.com/dead-winter-update-patch-notes-1-0-8-049/</span></a></p>\n"
                                          "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#999999;\">Fri, 12 Jan 2018, 9:15 am</span></p></body></html>"))
        self.patchtext.setPlaceholderText(_translate("hexpatcherwindow", "Loading news."))
        self.uptodate.setText(_translate("hexpatcherwindow", "Game is up-to-date"))
        self.label_6.setText(_translate("hexpatcherwindow", "Made by fans. All assets are the property of their respective owners."))
        self.forceInstallButton.setText(_translate("hexpatcherwindow", "Force Install"))
        self.installDirButton.setText(_translate("hexpatcherwindow", "Install Location"))
        self.downloadDirButton.setText(_translate("hexpatcherwindow", "Download Location"))
        self.optionsButton.setText(_translate("hexpatcherwindow", "Options"))

    def uptodateToggle(self):
        settings = QtCore.QSettings('fosspill', 'hex-linux-patcher')
        settings.setValue('forceuptodate', bool(self.uptodate.isChecked()))
        settings.sync()
        del settings

    def playButtonClick(self):
        if self.gameuptodate():
            self.playButton.setEnabled(True)
            self.playButton.setText("PLAY")
            self.playButton.clicked.disconnect(self.playButtonClick)
            self.playButton.clicked.connect(self.playGame)
            self.uptodate.setEnabled(False)
        else:
            self.playButton.setEnabled(False)
            self.playButton.setText("Warm-up in progress")
            self.download()

    def playGame(self):
        self.playButton.setText("Starting game.")
        self.playButton.setEnabled(False)
        settings = QtCore.QSettings('fosspill', 'hex-linux-patcher')
        chosenpath = settings.value("installDir", defaultInstallDir, type=str)
        p = subprocess.Popen(["./Hex.x86"], cwd=chosenpath, shell=True)
        hexpatcherwindow.hide()
        p.wait()
        hexpatcherwindow.close()


    def toggleOptions(self):
        self.optionsWidget.setVisible(not self.optionsWidget.isVisible())

    def selectInstallDir(self):
        selectedPath=QtWidgets.QFileDialog.getExistingDirectory()
        settings = QtCore.QSettings('fosspill', 'hex-linux-patcher')
        settings.setValue('installDir', selectedPath)
        settings.sync()
        del settings
        self.installDirButton.setToolTip(selectedPath)
        self.label_6.setText(selectedPath)

    def selectDownloadDir(self):
        selectedPath=QtWidgets.QFileDialog.getExistingDirectory()
        settings = QtCore.QSettings('fosspill', 'hex-linux-patcher')
        settings.setValue('downloadDir', selectedPath)
        settings.sync()
        del settings
        self.downloadDirButton.setToolTip(selectedPath)
        self.label_6.setText(selectedPath)

    def getDownloadDir(self):
        settings = QtCore.QSettings('fosspill', 'hex-linux-patcher')
        chosenpath = settings.value("downloadDir", defaultDownloadDir, type=str)
        fullpath = "{}/hex.tar.gz".format(chosenpath)
        return fullpath

    def download(self):
        settings = QtCore.QSettings('fosspill', 'hex-linux-patcher')
        def reporthook(blocknum, blocksize, totalsize):
            readsofar = blocknum * blocksize
            if totalsize > 0:
                percent = readsofar * 1e2 / totalsize
                self.progressBar.setValue(round(percent))
                self.playButton.setText("{}% downloaded".format(round(percent)))
                QtWidgets.QApplication.processEvents()
            else:  # total size is unknown
                self.progressBar.setValue(random.randint(1, 101))
                self.playButton.setText("{}% downloaded".format(random.randint(1, 101)))
                QtWidgets.QApplication.processEvents()

        self.playButton.setEnabled(False)
        self.playButton.setText("Downloading")
        if self.url_is_alive(url):
            urllib.request.urlretrieve(url, self.getDownloadDir(), reporthook)
            self.progressBar.setValue(100)
            self.playButton.setEnabled(True)
            self.playButton.setText("Download Complete")
        else:
            self.progressBar.setValue(0)
            self.playButton.setEnabled(True)
            self.playButton.setText("Error. Try again later.")
        self.playButton.setText("Extracting")
        self.progressBar.setValue(0)

        def extraction(archivepath):

            def tarpercent(cur, max):
                x = max / 100
                percentage = cur / x
                return round(percentage)

            tar = tarfile.open(archivepath)

            for member_info in tar.getmembers():
                self.progressBar.setValue(tarpercent(tar.getmembers().index(member_info), len(tar.getmembers())))
                self.playButton.setText(
                    "{}% extracted".format(tarpercent(tar.getmembers().index(member_info), len(tar.getmembers()))))
                QtWidgets.QApplication.processEvents()
                tar.extract(member_info, settings.value("installDir", defaultDownloadDir, type=str))

            tar.close()

        extraction(self.getDownloadDir())
        self.playButton.setText("Extraction complete")

    def gameuptodate(self):
        if self.uptodate.isChecked():
            return True
        else:
            return False

    def url_is_alive(self, url):
        request = urllib.request.Request(url)
        request.get_method = lambda: 'HEAD'

        try:
            urllib.request.urlopen(request)
            return True
        except urllib.request.HTTPError:
            return False


import bg_rc

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    hexpatcherwindow = QtWidgets.QMainWindow()
    ui = Ui_hexpatcherwindow()
    ui.setupUi(hexpatcherwindow)
    hexpatcherwindow.show()
    sys.exit(app.exec_())
