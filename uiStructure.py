
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QStringListModel, Qt
from PyQt5.QtWidgets import QMainWindow, QAction, QMenuBar, QMessageBox, QProgressBar,QMenu
from PyQt5.QtGui import QFont , QMovie
from DirectoryModel import DirProxyModel
from PyQt5.QtWebEngineWidgets import QWebEngineView 
from PySide2extn.RoundProgressBar import roundProgressBar
import os,sys, pandas as pd, seaborn as sns, matplotlib.pyplot as plt
from PIL import Image
import numpy as np
from torch.utils.data import Dataset, DataLoader
# from matplotlib.axes import Subplot as plt

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT
from matplotlib.figure import Figure



class Ui_mainWindow(object):
    def setupUi(self, mainWindow):

#========= setting up some GLOBAL variable values=============
        self.pathfiles =  'C:/Users/a_ade/Desktop/Files/Capstone/Breast_Cancer/testoutput1.csv'
        self.df = pd.read_csv(self.pathfiles)
        # self.base_path = "breast-histopathology-images/IDC_regular_ps50_idx5/"

#======================================================================================

        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(1830, 980)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(mainWindow.sizePolicy().hasHeightForWidth())
        mainWindow.setSizePolicy(sizePolicy)
        mainWindow.setMinimumSize(QtCore.QSize(200, 200))
        # mainWindow.setMaximumSize(QtCore.QSize(1840, 980))
        mainWindow.setSizeIncrement(QtCore.QSize(40, 40))
        mainWindow.setAcceptDrops(True)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("imagesicons/gene.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        mainWindow.setWindowIcon(icon)
        mainWindow.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(254, 255, 244, 255), stop:1 rgba(255, 255, 255, 255)\n"
"\n"
");")
        self.behindFrame = QtWidgets.QFrame(mainWindow)
        self.behindFrame.setGeometry(QtCore.QRect(0, -10, 1841, 991))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(200)
        sizePolicy.setVerticalStretch(200)
        sizePolicy.setHeightForWidth(self.behindFrame.sizePolicy().hasHeightForWidth())
        self.behindFrame.setSizePolicy(sizePolicy)
        self.behindFrame.setMinimumSize(QtCore.QSize(1500, 350))
        self.behindFrame.setMaximumSize(QtCore.QSize(5000, 5000))
        self.behindFrame.setStyleSheet("QFrame#behindFrame\n"
"{     \n"
"background-color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"QFrame:hover#behindFrame\n"
"{\n"
"\n"
"}\n"
"")
        self.behindFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.behindFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.behindFrame.setObjectName("behindFrame")
        self.frontFrame = QtWidgets.QFrame(self.behindFrame)
        self.frontFrame.setGeometry(QtCore.QRect(-30, 10, 1861, 981))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frontFrame.sizePolicy().hasHeightForWidth())
        self.frontFrame.setSizePolicy(sizePolicy)
        self.frontFrame.setMinimumSize(QtCore.QSize(147, 350))
        self.frontFrame.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.frontFrame.setStyleSheet("QFrame#frontFrame\n"
"{ \n"
"    background-color: rgb(43, 86, 129);\n"
"\n"
"}\n"
"\n"
"QFrame:hover#frontFrame\n"
"{\n"
"\n"
"}\n"
"\n"
"")
        self.frontFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frontFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frontFrame.setObjectName("frontFrame")
        self.tabWidget = QtWidgets.QTabWidget(self.frontFrame)
        self.tabWidget.setGeometry(QtCore.QRect(60, 7, 1781, 951))
        self.tabWidget.setMaximumSize(QtCore.QSize(5000, 5000))
        self.tabWidget.setSizeIncrement(QtCore.QSize(5000, 5000))
        self.tabWidget.setStyleSheet("background-color: rgb(237, 254, 255);\n"
"font: 10pt \"Segoe UI\";\n"
"font: 10pt \"Segoe UI\";\n"
"font: 10pt \"Segoe UI\";")
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.tab1Behindwidget = QtWidgets.QWidget(self.tab)
        self.tab1Behindwidget.setGeometry(QtCore.QRect(370, 30, 1406, 871))
        self.tab1Behindwidget.setMaximumSize(QtCore.QSize(5000, 5000))
        self.tab1Behindwidget.setStyleSheet("\n"
"QWidget#tab1Behindwidget{\n"
"    background-color: rgb(41, 137, 182);\n"
"border-radius:12px;\n"
"border-style:outset;\n"
"border-width:2px;\n"
"border-color:rgb(16, 79, 127);\n"
"\n"
"font: 350 8pt \"Segoe UI\";}\n"
"\n"
"QWidget:hover#tab1Behindwidget\n"
"{\n"
"border-width:2px;\n"
"    border-color: rgb(84, 204, 255);\n"
"}\n"
"\n"
"")
        self.tab1Behindwidget.setObjectName("tab1Behindwidget")
        self.labelMainTitle = QtWidgets.QLabel(self.tab1Behindwidget)
        self.labelMainTitle.setGeometry(QtCore.QRect(546, 8, 411, 31))
        self.labelMainTitle.setStyleSheet("font: 600 9pt \"Segoe UI\";\n"
"border-color: rgb(0, 170, 255);")
        self.labelMainTitle.setObjectName("labelMainTitle")
        self.tableView = QtWidgets.QTableView(self.tab1Behindwidget)
        self.tableView.setGeometry(QtCore.QRect(8, 60, 1389, 801))
        self.tableView.setObjectName("tableView")
        self.BigScreenWidget = QtWidgets.QWidget(self.tab1Behindwidget)
        self.BigScreenWidget.setGeometry(QtCore.QRect(12, 60, 1382, 797))
        self.BigScreenWidget.setStyleSheet("background-color: rgb(233, 255, 250);")
        self.BigScreenWidget.setObjectName("BigScreenWidget")

        # self.scrollArea =QtWidgets.QScrollArea(self.tab1Behindwidget)
        # self.scrollArea.setObjectName("scrollArea")
        # self.scrollArea.setGeometry(QtCore.QRect(0, 0, 1381, 801))
        # self.scrollArea.setWidgetResizable(True)
        # self.scrollAreaWidgetContents = QtWidgets.QWidget()
        # self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        # self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 1379, 799))
        # self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        # self.scrollArea.setVisible(False)
        # self.scrollAreaWidgetContents.setVisible(False)
#========================================================================

        self.plottingLeftWidget = QtWidgets.QWidget(self.tab1Behindwidget)
        self.plottingLeftWidget.setGeometry(QtCore.QRect(0, 60, 760, 801))
        self.plottingLeftWidget.setObjectName("plottingLeftWidget")
        self.plottingRightWidget = QtWidgets.QWidget(self.tab1Behindwidget)
        self.plottingRightWidget.setGeometry(QtCore.QRect(686, 60, 689, 801))
        self.plottingRightWidget.setObjectName("plottingRightWidget")
        self.TitleFrameBehind = QtWidgets.QFrame(self.tab1Behindwidget)
        self.TitleFrameBehind.setGeometry(QtCore.QRect(530, 10, 441, 51))
        self.TitleFrameBehind.setStyleSheet("background-color: rgb(149, 200, 255);")
        self.TitleFrameBehind.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.TitleFrameBehind.setFrameShadow(QtWidgets.QFrame.Raised)
        self.TitleFrameBehind.setObjectName("TitleFrameBehind")
        self.TitleFrameBehind_2 = QtWidgets.QFrame(self.TitleFrameBehind)
        self.TitleFrameBehind_2.setGeometry(QtCore.QRect(10, -13, 421, 66))
        self.TitleFrameBehind_2.setStyleSheet("    background-color: rgb(43, 86, 129);")
        self.TitleFrameBehind_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.TitleFrameBehind_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.TitleFrameBehind_2.setObjectName("TitleFrameBehind_2")
        self.labelTitleCNN = QtWidgets.QLabel(self.TitleFrameBehind_2)
        self.labelTitleCNN.setGeometry(QtCore.QRect(110, 40, 271, 20))
        self.labelTitleCNN.setStyleSheet("font: 9pt \"MS Shell Dlg 2\";\n"
"color: rgb(245, 245, 245);")
        self.labelTitleCNN.setObjectName("labelTitleCNN")
#================================================================
        self.labelWithPhoto = QtWidgets.QLabel(self.tab1Behindwidget)
        self.labelWithPhoto.setGeometry(QtCore.QRect(0, 0, 1406, 871))
        self.labelWithPhoto.setStyleSheet("\n"
"QLabel#labelWithPhoto{\n"
"    background-color: rgb(41, 137, 182);\n"
"border-radius:12px;\n"
"border-style:outset;\n"
"border-width:2px;\n"
"border-color:rgb(16, 79, 127);\n"
"\n"
"font: 350 8pt \"Segoe UI\";}\n"
"\n"
"QLabel:hover#labelWithPhoto\n"
"{\n"
"border-width:2px;\n"
"    border-color: rgb(84, 204, 255);\n"
"}\n"
"\n"
"")

        self.rowsCount_01 = QtWidgets.QLineEdit(self.tab1Behindwidget)
        self.rowsCount_01.setGeometry(QtCore.QRect(10, 20, 251, 31))
        self.rowsCount_01.setAutoFillBackground(False)
        self.rowsCount_01.setReadOnly(True)
        self.rowsCount_01.setVisible(False)



        self.middleLabel = QtWidgets.QLabel(mainWindow)
        self.middleLabel.setGeometry(QtCore.QRect(432, 165, 371, 171))
        self.middleLabel.setStyleSheet("\n"
"QLabel#middleLabel{\n"
"    background-color: rgb(231, 255, 247);\n"
"border-radius:12px;\n"
"border-style:outset;\n"
"border-width:2px;\n"
"border-color:rgb(0, 170, 255);\n"
"\n"
"font: 600 9pt  \"Segoe UI\";}\n"
"\n"
"QLabel:hover#middleLabel\n"
"{\n"
"border-width:2px;\n"
"    border-color: rgb(84, 204, 255);\n"
"}\n"
"\n"
"")
        self.middleLabel.setObjectName("middleLabel")
        self.middleLabel.setVisible(False)


        self.labelWithPhoto.setText("")
        self.labelWithPhoto.setObjectName("labelWithPhoto")
   
        self.tableView.raise_()
        self.BigScreenWidget.raise_()
        self.plottingLeftWidget.raise_()
        self.plottingRightWidget.raise_()
        self.labelWithPhoto.raise_()
        self.TitleFrameBehind.raise_()
        self.labelMainTitle.raise_()


        self.EDAFrame = QtWidgets.QFrame(self.tab)
        self.EDAFrame.setGeometry(QtCore.QRect(0, 60, 361, 111))
        self.EDAFrame.setStyleSheet("    background-color: rgb(43, 86, 129);")
        self.EDAFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.EDAFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.EDAFrame.setObjectName("EDAFrame")

        self.uploadFilesbutton = QtWidgets.QPushButton(self.EDAFrame)
        self.uploadFilesbutton.setGeometry(QtCore.QRect(10, 9, 151, 31))
        self.uploadFilesbutton.setStyleSheet("\n"
"QPushButton#uploadFilesbutton{\n"
"    font: 500 9pt \"Segoe UI\";\n"
"    \n"
"border-color:rgb(16, 79, 127);\n"
"background-color: rgb(149, 200, 255);\n"
"border-radius:12px;\n"
"border-style:outset;\n"
"border-width:2px;\n"
"\n"
"border-color:rgb(16, 79, 127);\n"
"\n"
";}\n"
"\n"
"QPushButton:hover#uploadFilesbutton\n"
"{\n"
"border-width:2px;\n"
"border-color: rgb(84, 204, 255);\n"
"}\n"
"\n"
"")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("imagesicons/addIcon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.uploadFilesbutton.setIcon(icon1)
        self.uploadFilesbutton.setObjectName("uploadFilesbutton")
        self.uploadfilesLabel = QtWidgets.QLabel(self.EDAFrame)
        self.uploadfilesLabel.setGeometry(QtCore.QRect(7, 34, 211, 21))
        self.uploadfilesLabel.setStyleSheet("font: 8pt \"Segoe UI\";\n"
"\n"
"    background-color: rgb(43, 86, 129);\n"
"border-color: rgb(0, 170, 255);\n"
"color: rgb(225, 225, 225);")
        self.uploadfilesLabel.setObjectName("uploadfilesLabel")


        self.EDALabel = QtWidgets.QLabel(self.tab)
        self.EDALabel.setGeometry(QtCore.QRect(59, 30, 271, 21))
        self.EDALabel.setStyleSheet("font: 600 9pt \"Segoe UI\";\n"
"border-color: rgb(0, 170, 255);\n"
"text-decoration: underline;")
        self.EDALabel.setObjectName("EDALabel")

        self.showUploadedFilesButton = QtWidgets.QPushButton(self.EDAFrame)
        self.showUploadedFilesButton.setGeometry(QtCore.QRect(174, 9, 181, 31))
        self.showUploadedFilesButton.setStyleSheet("\n"
"QPushButton#showUploadedFilesButton{\n"
"    font: 500 9pt \"Segoe UI\";\n"
"    \n"
"border-color:rgb(16, 79, 127);\n"
"background-color: rgb(149, 200, 255);\n"
"border-radius:12px;\n"
"border-style:outset;\n"
"border-width:2px;\n"
"\n"
"border-color:rgb(16, 79, 127);\n"
"\n"
";}\n"
"\n"
"QPushButton:hover#showUploadedFilesButton\n"
"{\n"
"border-width:2px;\n"
"    border-color: rgb(5, 209, 255);\n"
"}\n"
"\n"
"")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("imagesicons/list-icon-1441.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.showUploadedFilesButton.setIcon(icon2)
        self.showUploadedFilesButton.setIconSize(QtCore.QSize(24, 24))
        self.showUploadedFilesButton.setObjectName("showUploadedFilesButton")

        self.dataCounts = QtWidgets.QPushButton(self.EDAFrame)
        self.dataCounts.setGeometry(QtCore.QRect(10, 60, 151, 31))
        self.dataCounts.setStyleSheet("\n"
"QPushButton#dataCounts{\n"
"    font: 500 9pt \"Segoe UI\";\n"
"    \n"
"border-color:rgb(16, 79, 127);\n"
"background-color: rgb(149, 200, 255);\n"
"border-radius:12px;\n"
"border-style:outset;\n"
"border-width:2px;\n"
"\n"
"border-color:rgb(16, 79, 127);\n"
"\n"
";}\n"
"\n"
"QPushButton:hover#dataCounts\n"
"{\n"
"border-width:2px;\n"
"border-color: rgb(84, 204, 255);\n"
"}\n"
"\n"
"")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("imagesicons/search.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.dataCounts.setIcon(icon3)
        self.dataCounts.setObjectName("dataCounts")

        self.reviewPatches = QtWidgets.QPushButton(self.EDAFrame)
        self.reviewPatches.setGeometry(QtCore.QRect(170, 60, 181, 31))
        self.reviewPatches.setStyleSheet("\n"
"QPushButton#reviewPatches{\n"
"    font: 500 9pt \"Segoe UI\";\n"
"    \n"
"border-color:rgb(16, 79, 127);\n"
"background-color: rgb(149, 200, 255);\n"
"border-radius:12px;\n"
"border-style:outset;\n"
"border-width:2px;\n"
"\n"
"border-color:rgb(16, 79, 127);\n"
"\n"
";}\n"
"\n"
"QPushButton:hover#reviewPatches\n"
"{\n"
"border-width:2px;\n"
"border-color: rgb(84, 204, 255);\n"
"}\n"
"\n"
"")
        self.reviewPatches.setIcon(icon3)
        self.reviewPatches.setObjectName("reviewPatches")
#=====================================================================
        self.frame = QtWidgets.QFrame(self.tab)
        self.frame.setGeometry(QtCore.QRect(0, 190, 361, 160))
        self.frame.setStyleSheet("    background-color: rgb(43, 86, 129);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.visualizeBinary = QtWidgets.QPushButton(self.frame)
        self.visualizeBinary.setGeometry(QtCore.QRect(0, 73, 356, 37))
        self.visualizeBinary.setStyleSheet("\n"
"QPushButton#visualizeBinary{\n"
"        font: 500 9pt \"Segoe UI\";\n"
"    \n"
"border-color:rgb(16, 79, 127);\n"
"    background-color: rgb(138, 218, 255);\n"
"border-radius:12px;\n"
"border-style:outset;\n"
"border-width:2px;\n"
"\n"
"border-color:rgb(16, 79, 127);\n"
"\n"
";}\n"
"\n"
"QPushButton:hover#visualizeBinary\n"
"{\n"
"border-width:2px;\n"
"border-color: rgb(84, 204, 255);\n"
"}\n"
"\n"
"")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("imagesicons/exit.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.visualizeBinary.setIcon(icon4)
        self.visualizeBinary.setIconSize(QtCore.QSize(30, 30))
        self.visualizeBinary.setObjectName("visualizeBinary")
        self.visualizeBreastTissue = QtWidgets.QPushButton(self.frame)
        self.visualizeBreastTissue.setGeometry(QtCore.QRect(0, 115, 356, 36))
        self.visualizeBreastTissue.setStyleSheet("\n"
"QPushButton#visualizeBreastTissue{\n"
"    font: 500 9pt \"Segoe UI\";\n"
"    \n"
"border-color:rgb(16, 79, 127);\n"
"    background-color: rgb(138, 218, 255);\n"
"border-radius:12px;\n"
"border-style:outset;\n"
"border-width:2px;\n"
"\n"
"border-color:rgb(16, 79, 127);\n"
"\n"
";}\n"
"\n"
"QPushButton:hover#visualizeBreastTissue\n"
"{\n"
"border-width:2px;\n"
"border-color: rgb(84, 204, 255);\n"
"}\n"
"\n"
"")
        self.visualizeBreastTissue.setIcon(icon4)
        self.visualizeBreastTissue.setIconSize(QtCore.QSize(30, 30))
        self.visualizeBreastTissue.setObjectName("visualizeBreastTissue")
        self.viewBreastTissueLabel = QtWidgets.QLabel(self.frame)
        self.viewBreastTissueLabel.setGeometry(QtCore.QRect(75, 4, 201, 21))
        self.viewBreastTissueLabel.setStyleSheet("font: 600 9pt \"Segoe UI\";\n"
"border-color: rgb(0, 170, 255);\n"
"text-decoration: underline;\n"
"background-color: rgb(231, 255, 247);")
        self.viewBreastTissueLabel.setObjectName("viewBreastTissueLabel")
        self.breastTissuePatches = QtWidgets.QPushButton(self.frame)
        self.breastTissuePatches.setGeometry(QtCore.QRect(0, 31, 356, 37))
        self.breastTissuePatches.setStyleSheet("\n"
"QPushButton#breastTissuePatches{\n"
"    font: 500 9pt \"Segoe UI\";\n"
"border-color:rgb(16, 79, 127);\n"
"    background-color: rgb(180, 226, 255);\n"
"border-radius:12px;\n"
"border-style:outset;\n"
"border-width:2px;\n"
"\n"
"border-color:rgb(16, 79, 127);\n"
"\n"
";}\n"
"\n"
"QPushButton:hover#breastTissuePatches\n"
"{\n"
"border-width:2px;\n"
"border-color: rgb(84, 204, 255);\n"
"}\n"
"\n"
"")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("imagesicons/summary-png-icon-6071.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.breastTissuePatches.setIcon(icon5)
        self.breastTissuePatches.setIconSize(QtCore.QSize(28, 28))
        self.breastTissuePatches.setObjectName("breastTissuePatches")
        self.machineLearningModelLabel = QtWidgets.QLabel(self.tab)
        self.machineLearningModelLabel.setGeometry(QtCore.QRect(53, 370, 241, 21))
        self.machineLearningModelLabel.setStyleSheet("font: 600 9pt \"Segoe UI\";\n"
"border-color: rgb(0, 170, 255);\n"
"text-decoration: underline;")
        self.machineLearningModelLabel.setObjectName("machineLearningModelLabel")
        self.machineLearningCnnFrame = QtWidgets.QFrame(self.tab)
        self.machineLearningCnnFrame.setGeometry(QtCore.QRect(0, 366, 361, 521))
        self.machineLearningCnnFrame.setStyleSheet("    background-color: rgb(43, 86, 129);")
        self.machineLearningCnnFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.machineLearningCnnFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.machineLearningCnnFrame.setObjectName("machineLearningCnnFrame")
        self.ViewDatasets = QtWidgets.QPushButton(self.machineLearningCnnFrame)
        self.ViewDatasets.setGeometry(QtCore.QRect(5, 36, 351, 41))
        self.ViewDatasets.setStyleSheet("\n"
"QPushButton#ViewDatasets{\n"
"    font: 500 9pt \"Segoe UI\";\n"
"    \n"
"border-color:rgb(16, 79, 127);\n"
"    background-color: rgb(180, 226, 255);\n"
"border-radius:12px;\n"
"border-style:outset;\n"
"border-width:2px;\n"
"\n"
"border-color:rgb(16, 79, 127);\n"
"\n"
";}\n"
"\n"
"QPushButton:hover#ViewDatasets\n"
"{\n"
"border-width:2px;\n"
"border-color: rgb(84, 204, 255);\n"
"}\n"
"\n"
"")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("imagesicons/fax-icon-png-4933.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.ViewDatasets.setIcon(icon6)
        self.ViewDatasets.setIconSize(QtCore.QSize(22, 22))
        self.ViewDatasets.setObjectName("ViewDatasets")

        self.train = QtWidgets.QLineEdit(self.machineLearningCnnFrame)
        self.train.setObjectName(u"train")
        self.train.setGeometry(QtCore.QRect(5, 80, 39, 31))
        self.train.setStyleSheet(u"\n"
"\n"
"QLineEdit#train{border-radius: 6px;\n"
"	background-color: rgb(247, 255, 251);\n"
"border-style:outset;\n"
"border-width:2px;\n"
"border-color:rgb(16, 79, 127);\n"
"	font: 400 7pt \"Segoe UI\";\n"
";}\n"
"\n"
"\n"
"QLineEdit:hover#train\n"
"{\n"
"border-width:2px;\n"
"	border-color: rgb(84, 204, 255);\n"
"}\n"
"")
        self.train.setFrame(False)
        self.train.setAlignment(Qt.AlignCenter)
        self.train.setReadOnly(False)
        self.train.setClearButtonEnabled(False)
        self.validationdata_ = QtWidgets.QLineEdit(self.machineLearningCnnFrame)
        self.validationdata_.setObjectName(u"validationdata_")
        self.validationdata_.setGeometry(QtCore.QRect(46, 80, 39, 31))
        self.validationdata_.setStyleSheet(u"\n"
"\n"
"QLineEdit#validationdata_{border-radius: 6px;\n"
"	background-color: rgb(247, 255, 251);\n"
"border-style:outset;\n"
"border-width:2px;\n"
"border-color:rgb(16, 79, 127);\n"
"	font: 400 7pt \"Segoe UI\";\n"
";}\n"
"\n"
"\n"
"QLineEdit:hover#validationdata_\n"
"{\n"
"border-width:2px;\n"
"	border-color: rgb(84, 204, 255);\n"
"}\n"
"")
        self.validationdata_.setFrame(False)
        self.validationdata_.setAlignment(Qt.AlignCenter)
        self.validationdata_.setReadOnly(False)
        self.validationdata_.setClearButtonEnabled(False)
        self.testdata_ = QtWidgets.QLineEdit(self.machineLearningCnnFrame)
        self.testdata_.setObjectName("testdata_")
        self.testdata_.setGeometry(QtCore.QRect(87, 80, 39, 31))
        self.testdata_.setStyleSheet("\n"
"\n"
"QLineEdit#testdata_{border-radius: 6px;\n"
"	background-color: rgb(247, 255, 251);\n"
"border-style:outset;\n"
"border-width:2px;\n"
"border-color:rgb(16, 79, 127);\n"
"	font: 400 7pt \"Segoe UI\";\n"
";}\n"
"\n"
"\n"
"QLineEdit:hover#testdata_\n"
"{\n"
"border-width:2px;\n"
"	border-color: rgb(84, 204, 255);\n"
"}\n"
"")
        self.testdata_.setFrame(False)
        self.testdata_.setAlignment(Qt.AlignCenter)
        self.testdata_.setReadOnly(False)
        self.testdata_.setClearButtonEnabled(False)
        self.datadistributionLabel = QtWidgets.QLabel(self.machineLearningCnnFrame)
        self.datadistributionLabel.setObjectName(u"datadistributionLabel")
        self.datadistributionLabel.setGeometry(QtCore.QRect(10, 111, 281, 21))
        self.datadistributionLabel.setStyleSheet(u"font: 7pt \"Segoe UI\";\n"
"\n"
"	background-color: rgb(43, 86, 129);\n"
"border-color: rgb(0, 170, 255);\n"
"color: rgb(225, 225, 225);")



        self.createDatasetButton = QtWidgets.QPushButton(self.machineLearningCnnFrame)
        self.createDatasetButton.setGeometry(QtCore.QRect(129, 82, 221, 31))
        self.createDatasetButton.setStyleSheet("\n"
"QPushButton#createDatasetButton{\n"
"    font: 500 9pt \"Segoe UI\";\n"
"    \n"
"border-color:rgb(16, 79, 127);\n"
"background-color: rgb(149, 200, 255);\n"
"border-radius:12px;\n"
"border-style:outset;\n"
"border-width:2px;\n"
"\n"
"border-color:rgb(16, 79, 127);\n"
"\n"
";}\n"
"\n"
"QPushButton:hover#createDatasetButton\n"
"{\n"
"border-width:2px;\n"
"border-color: rgb(84, 204, 255);\n"
"}\n"
"\n"
"")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("imagesicons/server-icons-3716.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.createDatasetButton.setIcon(icon7)
        self.createDatasetButton.setIconSize(QtCore.QSize(23, 23))
        self.createDatasetButton.setObjectName("createDatasetButton")

        self.applyCNNfilter_Button = QtWidgets.QPushButton(self.machineLearningCnnFrame)
        self.applyCNNfilter_Button.setGeometry(QtCore.QRect(8, 134, 341, 39))
        self.applyCNNfilter_Button.setStyleSheet("\n"
"QPushButton#applyCNNfilter_Button{\n"
"    font: 500 9pt \"Segoe UI\";\n"
"    \n"
"border-color:rgb(16, 79, 127);\n"
"background-color: rgb(149, 200, 255);\n"
"border-radius:12px;\n"
"border-style:outset;\n"
"border-width:2px;\n"
"\n"
"border-color:rgb(16, 79, 127);\n"
"\n"
";}\n"
"\n"
"QPushButton:hover#applyCNNfilter_Button\n"
"{\n"
"border-width:2px;\n"
"border-color: rgb(84, 204, 255);\n"
"}\n"
"\n"
"")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("imagesicons/logo3.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.applyCNNfilter_Button.setIcon(icon8)
        self.applyCNNfilter_Button.setIconSize(QtCore.QSize(39, 55))
        self.applyCNNfilter_Button.setObjectName("applyCNNfilter_Button")

        self.Search_OptimalCyclicalButton = QtWidgets.QPushButton(self.machineLearningCnnFrame)
        self.Search_OptimalCyclicalButton.setGeometry(QtCore.QRect(8, 176, 341, 41))
        self.Search_OptimalCyclicalButton.setStyleSheet("\n"
"QPushButton#Search_OptimalCyclicalButton{\n"
"    font: 500 9pt \"Segoe UI\";\n"
"    \n"
"border-color:rgb(16, 79, 127);\n"
"    background-color: rgb(180, 226, 255);\n"
"border-radius:12px;\n"
"border-style:outset;\n"
"border-width:2px;\n"
"\n"
"border-color:rgb(16, 79, 127);\n"
"\n"
";}\n"
"\n"
"QPushButton:hover#Search_OptimalCyclicalButton\n"
"{\n"
"border-width:2px;\n"
"border-color: rgb(84, 204, 255);\n"
"}\n"
"\n"
"")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("imagesicons/logo1.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.Search_OptimalCyclicalButton.setIcon(icon8)
        self.Search_OptimalCyclicalButton.setIconSize(QtCore.QSize(30, 30))
        self.Search_OptimalCyclicalButton.setObjectName("Search_OptimalCyclicalButton")

        self.idcprobabilityMap_button = QtWidgets.QPushButton(self.machineLearningCnnFrame)
        self.idcprobabilityMap_button.setGeometry(QtCore.QRect(8, 220, 341, 41))
        self.idcprobabilityMap_button.setStyleSheet("\n"
"QPushButton#idcprobabilityMap_button{\n"
"    font: 500 9pt \"Segoe UI\";\n"
"    \n"
"border-color:rgb(16, 79, 127);\n"
"    background-color: rgb(180, 226, 255);\n"
"border-radius:12px;\n"
"border-style:outset;\n"
"border-width:2px;\n"
"\n"
"border-color:rgb(16, 79, 127);\n"
"\n"
";}\n"
"\n"
"QPushButton:hover#idcprobabilityMap_button\n"
"{\n"
"border-width:2px;\n"
"border-color: rgb(84, 204, 255);\n"
"}\n"
"\n"
"")
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap("imagesicons/logo2.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.idcprobabilityMap_button.setIcon(icon10)
        self.idcprobabilityMap_button.setIconSize(QtCore.QSize(30, 30))
        self.idcprobabilityMap_button.setObjectName("idcprobabilityMap_button")
        self.validationDataSet_Button = QtWidgets.QPushButton(self.machineLearningCnnFrame)
        self.validationDataSet_Button.setGeometry(QtCore.QRect(8, 264, 341, 35))
        self.validationDataSet_Button.setStyleSheet("\n"
"QPushButton#validationDataSet_Button{\n"
"    font: 500 9pt \"Segoe UI\";\n"
"    \n"
"border-color:rgb(16, 79, 127);\n"
"    background-color: rgb(180, 226, 255);\n"
"border-radius:12px;\n"
"border-style:outset;\n"
"border-width:2px;\n"
"\n"
"border-color:rgb(16, 79, 127);\n"
"\n"
";}\n"
"\n"
"QPushButton:hover#validationDataSet_Button\n"
"{\n"
"border-width:2px;\n"
"border-color: rgb(84, 204, 255);\n"
"}\n"
"\n"
"")
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap("imagesicons/logo5.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.validationDataSet_Button.setIcon(icon11)
        self.validationDataSet_Button.setIconSize(QtCore.QSize(30, 30))
        self.validationDataSet_Button.setObjectName("validationDataSet_Button")
        self.validationConfusionMatrix_Button = QtWidgets.QPushButton(self.machineLearningCnnFrame)
        self.validationConfusionMatrix_Button.setGeometry(QtCore.QRect(8, 302, 341, 35))
        self.validationConfusionMatrix_Button.setStyleSheet("\n"
"QPushButton#validationConfusionMatrix_Button{\n"
"    font: 500 9pt \"Segoe UI\";\n"
"    \n"
"border-color:rgb(16, 79, 127);\n"
"    background-color: rgb(180, 226, 255);\n"
"border-radius:12px;\n"
"border-style:outset;\n"
"border-width:2px;\n"
"\n"
"border-color:rgb(16, 79, 127);\n"
"\n"
";}\n"
"\n"
"QPushButton:hover#validationConfusionMatrix_Button\n"
"{\n"
"border-width:2px;\n"
"border-color: rgb(84, 204, 255);\n"
"}\n"
"\n"
"")
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap("imagesicons/logo6.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.validationConfusionMatrix_Button.setIcon(icon12)
        self.validationConfusionMatrix_Button.setIconSize(QtCore.QSize(30, 30))
        self.validationConfusionMatrix_Button.setObjectName("validationConfusionMatrix_Button")
        self.viewAllpatients_probabilityButton = QtWidgets.QPushButton(self.machineLearningCnnFrame)
        self.viewAllpatients_probabilityButton.setGeometry(QtCore.QRect(8,342, 341, 34))
        self.viewAllpatients_probabilityButton.setStyleSheet("\n"
"QPushButton#viewAllpatients_probabilityButton{\n"
"    font: 500 9pt \"Segoe UI\";\n"
"    \n"
"border-color:rgb(16, 79, 127);\n"
"background-color: rgb(149, 200, 255);\n"
"border-radius:12px;\n"
"border-style:outset;\n"
"border-width:2px;\n"
"\n"
"border-color:rgb(16, 79, 127);\n"
"\n"
";}\n"
"\n"
"QPushButton:hover#viewAllpatients_probabilityButton\n"
"{\n"
"border-width:2px;\n"
"border-color: rgb(84, 204, 255);\n"
"}\n"
"\n"
"")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("imagesicons/filesicon2.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.viewAllpatients_probabilityButton.setIcon(icon7)
        self.viewAllpatients_probabilityButton.setIconSize(QtCore.QSize(23, 23))
        self.viewAllpatients_probabilityButton.setObjectName("viewAllpatients_probabilityButton")
        
        
        
        self.predictionResult = QtWidgets.QPushButton(self.machineLearningCnnFrame)
        self.predictionResult.setGeometry(QtCore.QRect(50, 470, 251, 41))
        self.predictionResult.setStyleSheet("\n"
"QPushButton#predictionResult{\n"
"    font: 700 9pt \"Segoe UI\";\n"
"    \n"
"border-color:rgb(16, 79, 127);\n"
"background-color: rgb(149, 200, 255);\n"
"border-radius:12px;\n"
"border-style:outset;\n"
"border-width:2px;\n"
"\n"
"border-color:rgb(16, 79, 127);\n"
"\n"
";}\n"
"\n"
"QPushButton:hover#predictionResult\n"
"{\n"
"border-width:2px;\n"
"border-color: rgb(84, 204, 255);\n"
"}\n"
"\n"
"")
        icon13 = QtGui.QIcon()
        icon13.addPixmap(QtGui.QPixmap("imagesicons/save.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.predictionResult.setIcon(icon13)
        self.predictionResult.setIconSize(QtCore.QSize(30, 30))
        self.predictionResult.setObjectName("predictionResult")


        self.dividerFrameEnterPatient = QtWidgets.QFrame(self.machineLearningCnnFrame)
        self.dividerFrameEnterPatient.setGeometry(QtCore.QRect(8, 390, 341, 72))
        self.dividerFrameEnterPatient.setStyleSheet("background-color: rgb(85, 170, 255);")
        self.dividerFrameEnterPatient.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.dividerFrameEnterPatient.setFrameShadow(QtWidgets.QFrame.Raised)
        self.dividerFrameEnterPatient.setObjectName("dividerFrameEnterPatient")

        self.searchPatientID = QtWidgets.QLineEdit(self.dividerFrameEnterPatient)
        self.searchPatientID.setGeometry(QtCore.QRect(43, 8, 251, 34))
        self.searchPatientID.setStyleSheet("\n"
"\n"
"QLineEdit#searchPatientID{border-radius: 6px;\n"
"    background-color: rgb(247, 255, 251);\n"
"border-style:outset;\n"
"border-width:2px;\n"
"border-color:rgb(16, 79, 127);\n"
"    font: 400 9pt \"Segoe UI\";\n"
";}\n"
"\n"
"\n"
"QLineEdit:hover#searchPatientID\n"
"{\n"
"border-width:2px;\n"
"    border-color: rgb(84, 204, 255);\n"
"}\n"
"")
        self.searchPatientID.setText("")
        self.searchPatientID.setFrame(False)
        self.searchPatientID.setReadOnly(False)
        self.searchPatientID.setClearButtonEnabled(True)
        self.searchPatientID.setObjectName("searchPatientID")
        self.negative_Checkbox = QtWidgets.QCheckBox(self.dividerFrameEnterPatient)
        self.negative_Checkbox.setGeometry(QtCore.QRect(60, 45, 91, 24))
        self.negative_Checkbox.setObjectName("negative_Checkbox")
        self.positive_Checkbox = QtWidgets.QCheckBox(self.dividerFrameEnterPatient)
        self.positive_Checkbox.setGeometry(QtCore.QRect(170, 45, 101, 24))
        self.positive_Checkbox.setObjectName("positive_Checkbox")




        self.dividerFrameEnterPatient.raise_()
        self.ViewDatasets.raise_()
        self.createDatasetButton.raise_()
        self.applyCNNfilter_Button.raise_()
        self.searchPatientID.raise_()
       
        self.EDAFrame.raise_()
        self.machineLearningCnnFrame.raise_()
        self.frame.raise_()
        self.tab1Behindwidget.raise_()
        self.uploadfilesLabel.raise_()
        self.EDALabel.raise_()
        self.showUploadedFilesButton.raise_()
        self.dataCounts.raise_()
        self.uploadFilesbutton.raise_()
        self.machineLearningModelLabel.raise_()
        self.predictionResult.raise_()


#======================================================================
#======================================================================
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap("imagesicons/filesicon.jfif"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.tabWidget.addTab(self.tab, icon10, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tab2Behindwidget = QtWidgets.QWidget(self.tab_2)
        self.tab2Behindwidget.setGeometry(QtCore.QRect(190, 60, 1581, 781))
        self.tab2Behindwidget.setStyleSheet("\n"
"QWidget#tab2Behindwidget{\n"
"    background-color: rgb(41, 137, 182);\n"
"border-radius:12px;\n"
"border-style:outset;\n"
"border-width:2px;\n"
"border-color:rgb(16, 79, 127);\n"
"\n"
"font: 350 8pt \"Segoe UI\";}\n"
"\n"
"QWidget:hover#tab2Behindwidget\n"
"{\n"
"border-width:2px;\n"
"    border-color: rgb(84, 204, 255);\n"
"}\n"
"\n"
"")
        self.tab2Behindwidget.setObjectName("tab2Behindwidget")
        self.widget = QtWidgets.QWidget(self.tab2Behindwidget)
        self.widget.setGeometry(QtCore.QRect(10, 10, 1561, 761))
        self.widget.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.widget.setObjectName("widget")
        self.horizontalSlider = QtWidgets.QSlider(self.tab_2)
        self.horizontalSlider.setGeometry(QtCore.QRect(670, 880, 211, 18))
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.uploadCSV = QtWidgets.QPushButton(self.tab_2)
        self.uploadCSV.setGeometry(QtCore.QRect(470, 870, 111, 31))
        self.uploadCSV.setStyleSheet("\n"
"QPushButton#resetButton{\n"
"    font: 700 9pt \"Segoe UI\";\n"
"    \n"
"border-color:rgb(16, 79, 127);\n"
"background-color: rgb(149, 200, 255);\n"
"border-radius:12px;\n"
"border-style:outset;\n"
"border-width:2px;\n"
"\n"
"border-color:rgb(16, 79, 127);\n"
"\n"
";}\n"
"\n"
"QPushButton:hover#resetButton\n"
"{\n"
"border-width:2px;\n"
"border-color: rgb(84, 204, 255);\n"
"}\n"
"\n"
"")
        self.uploadCSV.setObjectName("uploadCSV")
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap("imagesicons/vsqvicon2.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.tabWidget.addTab(self.tab_2, icon11, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.label_2 = QtWidgets.QLabel(self.tab_3)
        self.label_2.setGeometry(QtCore.QRect(470, 190, 491, 271))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("imagesicons/symbols.png"))
        self.label_2.setObjectName("label_2")
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap("imagesicons/new.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.tabWidget.addTab(self.tab_3, icon12, "")

        self.retranslateUi(mainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

        # self.canvas_scrollarea =  QtWidgets.QScrollArea(self.tab1Behindwidget, widgetResizable=True)
        # self.canvas_scrollarea.setWidget(self.BigScreenWidget)
        self.mpl_RightCanvasToPlot = MplWidget(parent=self.plottingRightWidget,f1=10, f2=6, sp1=5, sp2=10)
        self.mpl_LeftCanvasToPlot = MplWidget(parent=self.plottingLeftWidget, f1=10, f2=6, sp1=5, sp2=10)
        self.mpl_CanvasToPlot = MplWidget(parent=self.BigScreenWidget, f1=10, f2=6, sp1=5, sp2=10)
        self.mpl_CanvasToPlot3 = MplWidget(parent=self.BigScreenWidget, f1=13, f2=7, sp1=1, sp2=2)
        self.mpl_CanvasToPlot4 = MplWidget(parent=self.BigScreenWidget, f1=15, f2=8, sp1=1, sp2=2)
        self.mpl_CanvasToPlot5 = MplWidget(parent=self.BigScreenWidget, f1=15, f2=7, sp1=1, sp2=3)
        self.mpl_CanvasToPlot6 = MplWidget(parent=self.BigScreenWidget, f1=20, f2=11, sp1=3, sp2=6)
        self.mpl_CanvasToPlot7 = MplWidget(parent=self.BigScreenWidget, f1=20, f2=5, sp1=1, sp2=2)
       
        self.mpl_CanvasToPlot3.setVisible(False)
        self.mpl_CanvasToPlot4.setVisible(False)

        self.mpl_CanvasToPlot2 = QWebEngineView(self.BigScreenWidget)


#=====================================================================
     #progress bar after button clicked
        # self.round_ProgressBar = QtWidgets.roundProgressBar(mainWindow)
        # self.round_ProgressBar.rpb_setMaximum(720) 
        # self.round_ProgressBar.rpb_setValue(456)
        # self.round_ProgressBar.setVisible(True)
        # self.round_ProgressBar.setGeometry(800,467,411,61)
        # self.round_ProgressBar.rpb_setBarStyle("Hybrid1")

        self.progressBar2 = QProgressBar(mainWindow)
        self.progressBar2.setGeometry(800,467,411,61)
        self.progressBar2.setFormat('Downloading. . .'+ '%p%' + ' Please..wait')
        self.progressBar2.setVisible(False)
        self.progressBar2.setFont(QFont('Times', 9))
        self.progressBar2.setRange(0, 25)
        self.progressBar2.setAlignment(QtCore.Qt.AlignCenter)
        self.progressBar2.setStyleSheet("progressBar2::chunk "
                          "{"
                          "background-color: #96d6fc;"
                          "border-width:2px;"
                           "border-color:   #085DAD;"
                          "}")

#=============================================================================
#*****************************************************************************
       #progress bar after button clicked
        self.progressBar = QProgressBar(mainWindow)
        self.progressBar.setGeometry(800,467,411,61)
        self.progressBar.setFormat('Loading. . .'+ '%p%' + ' Please..wait')
        self.progressBar.setVisible(False)
        self.progressBar.setFont(QFont('Times', 9))
        self.progressBar.setRange(0, 25)
        self.progressBar.setAlignment(QtCore.Qt.AlignCenter)
        self.progressBar.setStyleSheet("QProgressBar::chunk "
                          "{"
                          "background-color: #96d6fc;"
                          "border-width:2px;"
                           "border-color:   #085DAD;"
                          "}")
        
        

#====================================================
#=================Functions=========================    
        self.setBackgroundImage()

#========================================================
    def setBackgroundImage(self):
        # self.movie = QMovie("imagesicons/cells.gif")
        # self.labelWithPhoto.setMovie(self.movie)
        # self.movie.start()
        # self.movie.scaledSize()

        background=  QtGui.QPixmap('imagesicons/blue_bg.jpg')    
        self.labelWithPhoto.setPixmap(background)
        self.labelWithPhoto.resize(background.width(),background.height())


#=============================================================================

class MplWidget(QtWidgets.QWidget):
    send_fig = QtCore.pyqtSignal(str)
  
    def __init__(self, parent=None, f1=15, f2=8, sp1=1, sp2=2):
        
        super().__init__(parent)
        
        # figsize=(10,5)
        self.figure = Figure(figsize=(f1,f2))
        self.canvas = FigureCanvasQTAgg(self.figure)
        self.toolbar = NavigationToolbar2QT(self.canvas, self)
        layout = QtWidgets.QVBoxLayout(self)
        layout.addWidget(self.toolbar)
        layout.addWidget(self.canvas)
        # subplots = (1,2)
        self.ax = self.canvas.figure.subplots(sp1,sp2)

#============================================
