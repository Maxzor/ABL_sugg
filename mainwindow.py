# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1285, 876)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralWidget)
        self.tabWidget.setGeometry(QtCore.QRect(10, 20, 1261, 771))
        self.tabWidget.setObjectName("tabWidget")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.textEdit = QtWidgets.QTextEdit(self.tab_3)
        self.textEdit.setGeometry(QtCore.QRect(30, 10, 1191, 711))
        self.textEdit.setObjectName("textEdit")
        self.tabWidget.addTab(self.tab_3, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.label_6 = QtWidgets.QLabel(self.tab)
        self.label_6.setGeometry(QtCore.QRect(10, 10, 211, 20))
        self.label_6.setObjectName("label_6")
        self.line_2 = QtWidgets.QFrame(self.tab)
        self.line_2.setGeometry(QtCore.QRect(50, 660, 291, 16))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.tableView = QtWidgets.QTableView(self.tab)
        self.tableView.setGeometry(QtCore.QRect(370, 20, 861, 691))
        self.tableView.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.tableView.setAutoScrollMargin(16)
        self.tableView.setObjectName("tableView")
        self.label_4 = QtWidgets.QLabel(self.tab)
        self.label_4.setGeometry(QtCore.QRect(40, 550, 80, 20))
        self.label_4.setObjectName("label_4")
        self.comboBox = QtWidgets.QComboBox(self.tab)
        self.comboBox.setGeometry(QtCore.QRect(120, 550, 231, 30))
        self.comboBox.setObjectName("comboBox")
        self.comboBox_2 = QtWidgets.QComboBox(self.tab)
        self.comboBox_2.setGeometry(QtCore.QRect(120, 610, 231, 30))
        self.comboBox_2.setObjectName("comboBox_2")
        self.label_5 = QtWidgets.QLabel(self.tab)
        self.label_5.setGeometry(QtCore.QRect(40, 610, 80, 20))
        self.label_5.setTextFormat(QtCore.Qt.PlainText)
        self.label_5.setObjectName("label_5")
        self.comboBox_3 = QtWidgets.QComboBox(self.tab)
        self.comboBox_3.setGeometry(QtCore.QRect(120, 450, 231, 30))
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_4 = QtWidgets.QComboBox(self.tab)
        self.comboBox_4.setGeometry(QtCore.QRect(120, 390, 231, 30))
        self.comboBox_4.setObjectName("comboBox_4")
        self.label_9 = QtWidgets.QLabel(self.tab)
        self.label_9.setGeometry(QtCore.QRect(40, 450, 80, 20))
        self.label_9.setObjectName("label_9")
        self.comboBox_5 = QtWidgets.QComboBox(self.tab)
        self.comboBox_5.setGeometry(QtCore.QRect(120, 330, 231, 30))
        self.comboBox_5.setObjectName("comboBox_5")
        self.label_10 = QtWidgets.QLabel(self.tab)
        self.label_10.setGeometry(QtCore.QRect(50, 390, 80, 20))
        self.label_10.setObjectName("label_10")
        self.comboBox_6 = QtWidgets.QComboBox(self.tab)
        self.comboBox_6.setGeometry(QtCore.QRect(120, 270, 231, 30))
        self.comboBox_6.setObjectName("comboBox_6")
        self.label_12 = QtWidgets.QLabel(self.tab)
        self.label_12.setGeometry(QtCore.QRect(50, 330, 80, 20))
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.tab)
        self.label_13.setGeometry(QtCore.QRect(40, 270, 80, 20))
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.tab)
        self.label_14.setGeometry(QtCore.QRect(50, 210, 80, 20))
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(self.tab)
        self.label_15.setGeometry(QtCore.QRect(130, 210, 231, 20))
        self.label_15.setObjectName("label_15")
        self.label_16 = QtWidgets.QLabel(self.tab)
        self.label_16.setGeometry(QtCore.QRect(130, 150, 231, 20))
        self.label_16.setObjectName("label_16")
        self.label_17 = QtWidgets.QLabel(self.tab)
        self.label_17.setGeometry(QtCore.QRect(30, 150, 80, 20))
        self.label_17.setObjectName("label_17")
        self.label_19 = QtWidgets.QLabel(self.tab)
        self.label_19.setGeometry(QtCore.QRect(140, 100, 231, 20))
        self.label_19.setObjectName("label_19")
        self.label_20 = QtWidgets.QLabel(self.tab)
        self.label_20.setGeometry(QtCore.QRect(210, 60, 31, 20))
        self.label_20.setObjectName("label_20")
        self.pushButton = QtWidgets.QPushButton(self.tab)
        self.pushButton.setGeometry(QtCore.QRect(20, 60, 106, 29))
        self.pushButton.setObjectName("pushButton")
        self.line = QtWidgets.QFrame(self.tab)
        self.line.setGeometry(QtCore.QRect(350, 70, 20, 621))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_3 = QtWidgets.QFrame(self.tab)
        self.line_3.setGeometry(QtCore.QRect(50, 510, 291, 16))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.tableView_2 = QtWidgets.QTableView(self.tab)
        self.tableView_2.setGeometry(QtCore.QRect(910, 30, 311, 671))
        self.tableView_2.setObjectName("tableView_2")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.scrollArea = QtWidgets.QScrollArea(self.tab_2)
        self.scrollArea.setGeometry(QtCore.QRect(740, 30, 491, 161))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 489, 159))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.label_29 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_29.setGeometry(QtCore.QRect(10, 0, 131, 20))
        self.label_29.setObjectName("label_29")
        self.label_30 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_30.setGeometry(QtCore.QRect(20, 40, 81, 20))
        self.label_30.setObjectName("label_30")
        self.comboBox_15 = QtWidgets.QComboBox(self.scrollAreaWidgetContents)
        self.comboBox_15.setGeometry(QtCore.QRect(20, 60, 131, 28))
        self.comboBox_15.setObjectName("comboBox_15")
        self.comboBox_16 = QtWidgets.QComboBox(self.scrollAreaWidgetContents)
        self.comboBox_16.setGeometry(QtCore.QRect(180, 60, 131, 28))
        self.comboBox_16.setObjectName("comboBox_16")
        self.label_31 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_31.setGeometry(QtCore.QRect(180, 40, 81, 20))
        self.label_31.setObjectName("label_31")
        self.comboBox_17 = QtWidgets.QComboBox(self.scrollAreaWidgetContents)
        self.comboBox_17.setGeometry(QtCore.QRect(340, 60, 131, 28))
        self.comboBox_17.setObjectName("comboBox_17")
        self.label_32 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_32.setGeometry(QtCore.QRect(340, 40, 81, 20))
        self.label_32.setObjectName("label_32")
        self.comboBox_23 = QtWidgets.QComboBox(self.scrollAreaWidgetContents)
        self.comboBox_23.setGeometry(QtCore.QRect(20, 110, 131, 28))
        self.comboBox_23.setObjectName("comboBox_23")
        self.comboBox_24 = QtWidgets.QComboBox(self.scrollAreaWidgetContents)
        self.comboBox_24.setGeometry(QtCore.QRect(180, 110, 131, 28))
        self.comboBox_24.setObjectName("comboBox_24")
        self.comboBox_25 = QtWidgets.QComboBox(self.scrollAreaWidgetContents)
        self.comboBox_25.setGeometry(QtCore.QRect(340, 110, 131, 28))
        self.comboBox_25.setObjectName("comboBox_25")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.scrollArea_2 = QtWidgets.QScrollArea(self.tab_2)
        self.scrollArea_2.setGeometry(QtCore.QRect(20, 10, 711, 201))
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName("scrollArea_2")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 709, 199))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.label_7 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.label_7.setGeometry(QtCore.QRect(50, 30, 81, 20))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.label_8.setGeometry(QtCore.QRect(260, 30, 71, 20))
        self.label_8.setObjectName("label_8")
        self.label_11 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.label_11.setGeometry(QtCore.QRect(470, 30, 91, 20))
        self.label_11.setObjectName("label_11")
        self.comboBox_7 = QtWidgets.QComboBox(self.scrollAreaWidgetContents_2)
        self.comboBox_7.setGeometry(QtCore.QRect(50, 50, 191, 28))
        self.comboBox_7.setObjectName("comboBox_7")
        self.comboBox_8 = QtWidgets.QComboBox(self.scrollAreaWidgetContents_2)
        self.comboBox_8.setGeometry(QtCore.QRect(260, 50, 191, 28))
        self.comboBox_8.setObjectName("comboBox_8")
        self.comboBox_9 = QtWidgets.QComboBox(self.scrollAreaWidgetContents_2)
        self.comboBox_9.setGeometry(QtCore.QRect(470, 50, 191, 28))
        self.comboBox_9.setObjectName("comboBox_9")
        self.label_23 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.label_23.setGeometry(QtCore.QRect(10, 0, 131, 20))
        self.label_23.setObjectName("label_23")
        self.label_24 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.label_24.setGeometry(QtCore.QRect(20, 140, 111, 20))
        self.label_24.setObjectName("label_24")
        self.comboBox_10 = QtWidgets.QComboBox(self.scrollAreaWidgetContents_2)
        self.comboBox_10.setGeometry(QtCore.QRect(20, 160, 191, 28))
        self.comboBox_10.setObjectName("comboBox_10")
        self.comboBox_11 = QtWidgets.QComboBox(self.scrollAreaWidgetContents_2)
        self.comboBox_11.setGeometry(QtCore.QRect(50, 110, 41, 28))
        self.comboBox_11.setObjectName("comboBox_11")
        self.label_25 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.label_25.setGeometry(QtCore.QRect(50, 90, 51, 20))
        self.label_25.setObjectName("label_25")
        self.comboBox_12 = QtWidgets.QComboBox(self.scrollAreaWidgetContents_2)
        self.comboBox_12.setGeometry(QtCore.QRect(90, 110, 81, 28))
        self.comboBox_12.setObjectName("comboBox_12")
        self.comboBox_13 = QtWidgets.QComboBox(self.scrollAreaWidgetContents_2)
        self.comboBox_13.setGeometry(QtCore.QRect(260, 110, 61, 28))
        self.comboBox_13.setObjectName("comboBox_13")
        self.label_26 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.label_26.setGeometry(QtCore.QRect(250, 110, 16, 20))
        self.label_26.setObjectName("label_26")
        self.comboBox_14 = QtWidgets.QComboBox(self.scrollAreaWidgetContents_2)
        self.comboBox_14.setGeometry(QtCore.QRect(490, 160, 191, 28))
        self.comboBox_14.setObjectName("comboBox_14")
        self.label_27 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.label_27.setGeometry(QtCore.QRect(490, 140, 91, 20))
        self.label_27.setObjectName("label_27")
        self.label_28 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.label_28.setGeometry(QtCore.QRect(250, 90, 51, 20))
        self.label_28.setObjectName("label_28")
        self.label_33 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.label_33.setGeometry(QtCore.QRect(280, 140, 91, 20))
        self.label_33.setObjectName("label_33")
        self.comboBox_19 = QtWidgets.QComboBox(self.scrollAreaWidgetContents_2)
        self.comboBox_19.setGeometry(QtCore.QRect(280, 160, 191, 28))
        self.comboBox_19.setObjectName("comboBox_19")
        self.comboBox_20 = QtWidgets.QComboBox(self.scrollAreaWidgetContents_2)
        self.comboBox_20.setGeometry(QtCore.QRect(590, 110, 71, 28))
        self.comboBox_20.setObjectName("comboBox_20")
        self.label_34 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.label_34.setGeometry(QtCore.QRect(590, 90, 91, 20))
        self.label_34.setObjectName("label_34")
        self.comboBox_22 = QtWidgets.QComboBox(self.scrollAreaWidgetContents_2)
        self.comboBox_22.setGeometry(QtCore.QRect(410, 110, 101, 28))
        self.comboBox_22.setObjectName("comboBox_22")
        self.label_35 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.label_35.setGeometry(QtCore.QRect(410, 90, 111, 20))
        self.label_35.setObjectName("label_35")
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)
        self.tableView_3 = QtWidgets.QTableView(self.tab_2)
        self.tableView_3.setGeometry(QtCore.QRect(20, 260, 1211, 401))
        self.tableView_3.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.tableView_3.setAutoScrollMargin(16)
        self.tableView_3.setObjectName("tableView_3")
        self.pushButton_2 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_2.setGeometry(QtCore.QRect(150, 230, 1081, 29))
        self.pushButton_2.setObjectName("pushButton_2")
        self.lineEdit = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit.setGeometry(QtCore.QRect(20, 690, 571, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.label_36 = QtWidgets.QLabel(self.tab_2)
        self.label_36.setGeometry(QtCore.QRect(20, 670, 191, 20))
        self.label_36.setObjectName("label_36")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_2.setGeometry(QtCore.QRect(620, 690, 611, 31))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_37 = QtWidgets.QLabel(self.tab_2)
        self.label_37.setGeometry(QtCore.QRect(620, 670, 191, 20))
        self.label_37.setObjectName("label_37")
        self.pushButton_3 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_3.setGeometry(QtCore.QRect(20, 230, 111, 29))
        self.pushButton_3.setObjectName("pushButton_3")
        self.tabWidget.addTab(self.tab_2, "")
        #MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 1285, 25))
        self.menuBar.setObjectName("menuBar")
        #MainWindow.setMenuBar(self.menuBar)
        self.mainToolBar = QtWidgets.QToolBar(MainWindow)
        self.mainToolBar.setObjectName("mainToolBar")
        #MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        #MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.textEdit.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\">Suggestions pour une évolution d\'ABL : fiche plante</span></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:14pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Les évolutions proposées dans cette démonstration portent sur deux axes :</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">- renforcer la valeur de la classification botanique interne , via une connexion avec une <span style=\" text-decoration: underline;\">classification botanique reconnue</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">- améliorer la <span style=\" text-decoration: underline;\">qualité des données</span> des fiches plantes.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Pour monter cette démonstration, j\'ai utilisé des logiciels libres, gratuit et open-source, (et qui peuvent supporter sans problème la charge de l\'entreprise) : PostgreSQL pour la base de données, QT et Python pour l\'interface graphique, sur un système d\'exploitation Linux.</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">L\'ensemble des outils et pistes explorées pendant cette recherche succinte (structure de la BDD pour éventuellement devis ABL) sont dans un même dossier, sur le serveur Appro.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">I - Interconnexion avec une base de données botanique - (onglet &quot;focus taxonomie botanique&quot;)</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Le projet <a href=\"https://tree.opentreeoflife.org\"><span style=\" text-decoration: underline; color:#0000ff;\">Open Tree of Life</span></a> est le plus adapté de ceux que j\'ai trouvés. La taxonomie est ouverte et gratuite, on peut facilement la relier à ABL. La taxonomie est exhaustive (elle couvre les mammifères, les bactéries...), part du niveau le plus général pour descendre jusqu\'aux espèces.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">C\'est elle qui m\'a servi pour cette démonstration, les outils que j\'ai utilisés pour relier les deux systèmes OTT et ABL sont en partie dans le dossier.</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">La taxonomie est ici tronquée au règne végétal et s\'enroule sur elle-même : chaque niveau est relié à son parent, et on parcours l\'arbre par récursion.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Les développeurs du projet m\'ont donné leur <a href=\"https://github.com/OpenTreeOfLife/reference-taxonomy/wiki/All-life-taxonomy-projects\"><span style=\" text-decoration: underline; color:#0000ff;\">point de vue</span></a> sur les taxonomies globales concurrentes.</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Pour obtenir des données de qualité <span style=\" font-style:italic;\">en dessous de l\'espèce : </span> variétés, formes, hybrides à parents connus, cultivars... les <a href=\"http://www.ishs.org/sci/icralist/icralist.htm\"><span style=\" text-decoration: underline; color:#0000ff;\">ICRAS</span></a> sont théoriquement en charge, mais le contenu est super fragmenté et <span style=\" font-style:italic;\">peu disponible</span>.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Avoir le système qui draîne la hiérarchie botanique depuis une source officielle permet d\'envisager de parcourir les étages de l\'arbre de façon intuitive voire ludique. J\'ai proposé une première façon d\'explorer l\'arborescence dans le premier onglet, mais, surtout pour des clients web, il peut-être fructueux de proposer une interface graphique bien plus riche et dynamique type <a href=\"http://www.onezoom.org/\"><span style=\" text-decoration: underline; color:#0000ff;\">Onezoom</span></a> ou <a href=\"http://circos.ca/\"><span style=\" text-decoration: underline; color:#0000ff;\">Circos</span></a>.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Mode d\'emploi de l\'onglet :</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">- Les enregistrements avec nombres entre parenthèses sont ceux pour lequels des articles existent dans ABL. Toutes les données des boîtes de sélection sont officielles, sauf les données des espèces et le contenu de la table d\'affichage, qui proviennent donc d\'ABL.</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">- RAZ - Remise à zéro</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">- Double cliquer sur une ligne de la table affiche un pop-up avec l\'arborescence complète, qui vient compléter la relative faiblesse des rangs taxonomiques de cette base.</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">- Echap pour fermer le pop-up.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">II- Structure des données de la fiche plante - (onglet &quot;focus structure fiche plante ABL&quot;)</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Un des principes majeurs en conception de base de données est d\'éviter les redondances.</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Ce n\'est pas le cas actuellement pour la taille de pot, la hauteur ou le conditionnement par exemple, qui sont tous renseignés deux fois, dans le libellé fourre-tout et dans leur champ spécifique.</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Les dérives entre les deux champs et les incohérences arrivent très vite et corrompent les données. C\'est un problème résolu avec la normalisation en première forme normale de Codd, et il y a 5 niveaux supérieurs.</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">On peut avoir des données beaucoup plus solides si ont les stockes à l\'échelle atomique.</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Mieux vaut ne pas stocker libellé &quot;Roland de Boissieu&quot;, mais prénom &quot;Roland&quot;, nom &quot;de Boissieu&quot; et on agrège les champs pour reconstituer le libellé.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Un autre point utile de mon point de vue est de limiter un peu la latitude dans la saisie : mieux vaut ne pas avoir à saisir les genres, espèces ou variétés à chaque création d\'article, mais sélectionner dans une liste déroulante par exemple.</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Le manque de rigueur des données qu\'on peut entrer dans le système se contemple avec les lagerstroemia : cf. le nombre de fautes d\'orthographes présentes aujourd\'hui dans ABL.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Un autre point intéressant dans cet onglet est le concept de métacaractérisation, déjà présent dans ABL avec la table des tables, mais étendu à l\'intérieur de la fiche plante.</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Permet d\'ajouter à la volée des caractéristiques de produits avec rigueur, <span style=\" font-style:italic;\">et en même temps</span>, facilité.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Mode d\'emploi de l\'onglet :</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">- Le jeu de données est ici tronqué au genre dracaena, mais j\'ai structuré les données pour tous les enregistrements.</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">- &quot;Actualiser&quot; pour lancer la requête à partir des options choisies.</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">-  La table montre les données stockées de façon peu lisibles, double cliquer sur une ligne affiche en dessous les libellés actuels reconstruits à partir des données atomiques.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Mi 2017 - Maxime Chambonnet</p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "A propos"))
        self.label_6.setText(_translate("MainWindow", "Classification botanique :"))
        self.label_4.setText(_translate("MainWindow", "GENRE  :"))
        self.label_5.setText(_translate("MainWindow", "espèce :"))
        self.label_9.setText(_translate("MainWindow", "Famille :"))
        self.label_10.setText(_translate("MainWindow", "Ordre :"))
        self.label_12.setText(_translate("MainWindow", "Classe :"))
        self.label_13.setText(_translate("MainWindow", "Phylum :"))
        self.label_14.setText(_translate("MainWindow", "Règne :"))
        self.label_15.setText(_translate("MainWindow", "Plantae (archaeplastida)"))
        self.label_16.setText(_translate("MainWindow", "Eukaryotes"))
        self.label_17.setText(_translate("MainWindow", "Domaine : "))
        self.label_19.setText(_translate("MainWindow", "Organismes cellulaires"))
        self.label_20.setText(_translate("MainWindow", "Vie"))
        self.pushButton.setText(_translate("MainWindow", "RAZ"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Focus taxonomie botanique"))
        self.tabWidget.setTabToolTip(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Données ABL peu structurées existantes"))
        self.label_29.setText(_translate("MainWindow", "Métacaractères"))
        self.label_30.setText(_translate("MainWindow", "Option 1"))
        self.label_31.setText(_translate("MainWindow", "Option 2"))
        self.label_32.setText(_translate("MainWindow", "Option 3"))
        self.label_7.setText(_translate("MainWindow", "GENRE"))
        self.label_8.setText(_translate("MainWindow", "espèce"))
        self.label_11.setText(_translate("MainWindow", "\'Variété\'"))
        self.label_23.setText(_translate("MainWindow", "Infos générales"))
        self.label_24.setText(_translate("MainWindow", "Fournisseur"))
        self.label_25.setText(_translate("MainWindow", "Pot"))
        self.label_26.setText(_translate("MainWindow", "x"))
        self.label_27.setText(_translate("MainWindow", "Forme"))
        self.label_28.setText(_translate("MainWindow", "Cdt"))
        self.label_33.setText(_translate("MainWindow", "Couleur"))
        self.label_34.setText(_translate("MainWindow", "Mix"))
        self.label_35.setText(_translate("MainWindow", "Hauteur (cm)"))
        self.pushButton_2.setText(_translate("MainWindow", "Actualiser"))
        self.label_36.setText(_translate("MainWindow", "Libellé 1 (reconstruit)"))
        self.label_37.setText(_translate("MainWindow", "Libellé 2 (reconstruit)"))
        self.pushButton_3.setText(_translate("MainWindow", "RAZ"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Focus structure fiche plante ABL"))
        self.tabWidget.setTabToolTip(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Structuration et métacaractérisation envisagées"))

