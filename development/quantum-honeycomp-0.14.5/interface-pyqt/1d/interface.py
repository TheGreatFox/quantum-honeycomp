# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'interface.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(878, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(328, 290, 471, 261))
        self.tabWidget.setDocumentMode(False)
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setMovable(False)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.gridLayoutWidget_4 = QtWidgets.QWidget(self.tab_2)
        self.gridLayoutWidget_4.setGeometry(QtCore.QRect(50, 30, 240, 100))
        self.gridLayoutWidget_4.setObjectName("gridLayoutWidget_4")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.gridLayoutWidget_4)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.label_8 = QtWidgets.QLabel(self.gridLayoutWidget_4)
        self.label_8.setObjectName("label_8")
        self.gridLayout_4.addWidget(self.label_8, 0, 0, 1, 1)
        self.lattice = QtWidgets.QComboBox(self.gridLayoutWidget_4)
        self.lattice.setObjectName("lattice")
        self.lattice.addItem("")
        self.lattice.addItem("")
        self.lattice.addItem("")
        self.lattice.addItem("")
        self.lattice.addItem("")
        self.lattice.addItem("")
        self.lattice.addItem("")
        self.gridLayout_4.addWidget(self.lattice, 0, 1, 1, 1)
        self.nsuper = QtWidgets.QLineEdit(self.gridLayoutWidget_4)
        self.nsuper.setObjectName("nsuper")
        self.gridLayout_4.addWidget(self.nsuper, 1, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.gridLayoutWidget_4)
        self.label_6.setObjectName("label_6")
        self.gridLayout_4.addWidget(self.label_6, 1, 0, 1, 1)
        self.width = QtWidgets.QLineEdit(self.gridLayoutWidget_4)
        self.width.setObjectName("width")
        self.gridLayout_4.addWidget(self.width, 2, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget_4)
        self.label_2.setObjectName("label_2")
        self.gridLayout_4.addWidget(self.label_2, 2, 0, 1, 1)
        self.tabWidget.addTab(self.tab_2, "")
        self.tabWidget_2 = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget_2.setGeometry(QtCore.QRect(20, 20, 261, 531))
        self.tabWidget_2.setObjectName("tabWidget_2")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.gridLayoutWidget = QtWidgets.QWidget(self.tab_3)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 0, 231, 464))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.Bx = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.Bx.setObjectName("Bx")
        self.gridLayout.addWidget(self.Bx, 2, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 4, 0, 1, 1)
        self.mAB = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.mAB.setObjectName("mAB")
        self.gridLayout.addWidget(self.mAB, 9, 1, 1, 1)
        self.By = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.By.setObjectName("By")
        self.gridLayout.addWidget(self.By, 3, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.peierls = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.peierls.setEnabled(True)
        self.peierls.setObjectName("peierls")
        self.gridLayout.addWidget(self.peierls, 1, 1, 1, 1)
        self.kanemele = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.kanemele.setObjectName("kanemele")
        self.gridLayout.addWidget(self.kanemele, 6, 1, 1, 1)
        self.label_24 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_24.setObjectName("label_24")
        self.gridLayout.addWidget(self.label_24, 7, 0, 1, 1)
        self.antihaldane = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.antihaldane.setObjectName("antihaldane")
        self.gridLayout.addWidget(self.antihaldane, 8, 1, 1, 1)
        self.label_26 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_26.setObjectName("label_26")
        self.gridLayout.addWidget(self.label_26, 11, 0, 1, 1)
        self.fermi = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.fermi.setEnabled(True)
        self.fermi.setObjectName("fermi")
        self.gridLayout.addWidget(self.fermi, 0, 1, 1, 1)
        self.rashba = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.rashba.setObjectName("rashba")
        self.gridLayout.addWidget(self.rashba, 5, 1, 1, 1)
        self.haldane = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.haldane.setObjectName("haldane")
        self.gridLayout.addWidget(self.haldane, 7, 1, 1, 1)
        self.mAF = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.mAF.setObjectName("mAF")
        self.gridLayout.addWidget(self.mAF, 10, 1, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_10.setObjectName("label_10")
        self.gridLayout.addWidget(self.label_10, 5, 0, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_11.setObjectName("label_11")
        self.gridLayout.addWidget(self.label_11, 6, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_12.setObjectName("label_12")
        self.gridLayout.addWidget(self.label_12, 9, 0, 1, 1)
        self.label_14 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_14.setObjectName("label_14")
        self.gridLayout.addWidget(self.label_14, 1, 0, 1, 1)
        self.swave = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.swave.setObjectName("swave")
        self.gridLayout.addWidget(self.swave, 11, 1, 1, 1)
        self.Bz = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.Bz.setObjectName("Bz")
        self.gridLayout.addWidget(self.Bz, 4, 1, 1, 1)
        self.label_13 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_13.setObjectName("label_13")
        self.gridLayout.addWidget(self.label_13, 10, 0, 1, 1)
        self.label_25 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_25.setObjectName("label_25")
        self.gridLayout.addWidget(self.label_25, 8, 0, 1, 1)
        self.tabWidget_2.addTab(self.tab_3, "")
        self.tabWidget_3 = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget_3.setGeometry(QtCore.QRect(330, 30, 521, 231))
        self.tabWidget_3.setObjectName("tabWidget_3")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.show_structure = QtWidgets.QPushButton(self.tab_4)
        self.show_structure.setGeometry(QtCore.QRect(80, 150, 188, 28))
        self.show_structure.setObjectName("show_structure")
        self.gridLayoutWidget_3 = QtWidgets.QWidget(self.tab_4)
        self.gridLayoutWidget_3.setGeometry(QtCore.QRect(80, 30, 160, 80))
        self.gridLayoutWidget_3.setObjectName("gridLayoutWidget_3")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.gridLayoutWidget_3)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.nsuper_struct = QtWidgets.QLineEdit(self.gridLayoutWidget_3)
        self.nsuper_struct.setObjectName("nsuper_struct")
        self.gridLayout_3.addWidget(self.nsuper_struct, 0, 1, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.label_7.setObjectName("label_7")
        self.gridLayout_3.addWidget(self.label_7, 0, 0, 1, 1)
        self.tabWidget_3.addTab(self.tab_4, "")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.show_bands = QtWidgets.QPushButton(self.tab_5)
        self.show_bands.setGeometry(QtCore.QRect(20, 30, 188, 28))
        self.show_bands.setObjectName("show_bands")
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.tab_5)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(30, 70, 168, 64))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_15 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_15.setObjectName("label_15")
        self.gridLayout_2.addWidget(self.label_15, 0, 0, 1, 1)
        self.bands_color = QtWidgets.QComboBox(self.gridLayoutWidget_2)
        self.bands_color.setObjectName("bands_color")
        self.bands_color.addItem("")
        self.bands_color.addItem("")
        self.bands_color.addItem("")
        self.bands_color.addItem("")
        self.bands_color.addItem("")
        self.bands_color.addItem("")
        self.gridLayout_2.addWidget(self.bands_color, 0, 1, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_9.setObjectName("label_9")
        self.gridLayout_2.addWidget(self.label_9, 1, 0, 1, 1)
        self.nk_bands = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.nk_bands.setObjectName("nk_bands")
        self.gridLayout_2.addWidget(self.nk_bands, 1, 1, 1, 1)
        self.tabWidget_3.addTab(self.tab_5, "")
        self.tab_9 = QtWidgets.QWidget()
        self.tab_9.setObjectName("tab_9")
        self.show_dosbands = QtWidgets.QPushButton(self.tab_9)
        self.show_dosbands.setGeometry(QtCore.QRect(260, 150, 171, 28))
        self.show_dosbands.setObjectName("show_dosbands")
        self.gridLayoutWidget_11 = QtWidgets.QWidget(self.tab_9)
        self.gridLayoutWidget_11.setGeometry(QtCore.QRect(30, 20, 201, 176))
        self.gridLayoutWidget_11.setObjectName("gridLayoutWidget_11")
        self.gridLayout_11 = QtWidgets.QGridLayout(self.gridLayoutWidget_11)
        self.gridLayout_11.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_11.setObjectName("gridLayout_11")
        self.delta_kbands = QtWidgets.QLineEdit(self.gridLayoutWidget_11)
        self.delta_kbands.setObjectName("delta_kbands")
        self.gridLayout_11.addWidget(self.delta_kbands, 0, 1, 1, 1)
        self.label_27 = QtWidgets.QLabel(self.gridLayoutWidget_11)
        self.label_27.setObjectName("label_27")
        self.gridLayout_11.addWidget(self.label_27, 0, 0, 1, 1)
        self.ne_kbands = QtWidgets.QLineEdit(self.gridLayoutWidget_11)
        self.ne_kbands.setObjectName("ne_kbands")
        self.gridLayout_11.addWidget(self.ne_kbands, 1, 1, 1, 1)
        self.label_28 = QtWidgets.QLabel(self.gridLayoutWidget_11)
        self.label_28.setObjectName("label_28")
        self.gridLayout_11.addWidget(self.label_28, 1, 0, 1, 1)
        self.label_29 = QtWidgets.QLabel(self.gridLayoutWidget_11)
        self.label_29.setObjectName("label_29")
        self.gridLayout_11.addWidget(self.label_29, 2, 0, 1, 1)
        self.window_kbands = QtWidgets.QLineEdit(self.gridLayoutWidget_11)
        self.window_kbands.setObjectName("window_kbands")
        self.gridLayout_11.addWidget(self.window_kbands, 2, 1, 1, 1)
        self.label_30 = QtWidgets.QLabel(self.gridLayoutWidget_11)
        self.label_30.setObjectName("label_30")
        self.gridLayout_11.addWidget(self.label_30, 3, 0, 1, 1)
        self.scale_kbands = QtWidgets.QLineEdit(self.gridLayoutWidget_11)
        self.scale_kbands.setObjectName("scale_kbands")
        self.gridLayout_11.addWidget(self.scale_kbands, 3, 1, 1, 1)
        self.label_31 = QtWidgets.QLabel(self.gridLayoutWidget_11)
        self.label_31.setObjectName("label_31")
        self.gridLayout_11.addWidget(self.label_31, 4, 0, 1, 1)
        self.nv_kbands = QtWidgets.QLineEdit(self.gridLayoutWidget_11)
        self.nv_kbands.setObjectName("nv_kbands")
        self.gridLayout_11.addWidget(self.nv_kbands, 4, 1, 1, 1)
        self.tabWidget_3.addTab(self.tab_9, "")
        self.tab_6 = QtWidgets.QWidget()
        self.tab_6.setObjectName("tab_6")
        self.show_dos = QtWidgets.QPushButton(self.tab_6)
        self.show_dos.setGeometry(QtCore.QRect(50, 40, 188, 28))
        self.show_dos.setObjectName("show_dos")
        self.gridLayoutWidget_5 = QtWidgets.QWidget(self.tab_6)
        self.gridLayoutWidget_5.setGeometry(QtCore.QRect(60, 87, 211, 81))
        self.gridLayoutWidget_5.setObjectName("gridLayoutWidget_5")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.gridLayoutWidget_5)
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.label_16 = QtWidgets.QLabel(self.gridLayoutWidget_5)
        self.label_16.setObjectName("label_16")
        self.gridLayout_5.addWidget(self.label_16, 0, 0, 1, 1)
        self.DOS_smearing = QtWidgets.QLineEdit(self.gridLayoutWidget_5)
        self.DOS_smearing.setObjectName("DOS_smearing")
        self.gridLayout_5.addWidget(self.DOS_smearing, 0, 1, 1, 1)
        self.tabWidget_3.addTab(self.tab_6, "")
        self.tab_7 = QtWidgets.QWidget()
        self.tab_7.setObjectName("tab_7")
        self.show_interactive_ldos = QtWidgets.QPushButton(self.tab_7)
        self.show_interactive_ldos.setGeometry(QtCore.QRect(310, 150, 188, 28))
        self.show_interactive_ldos.setObjectName("show_interactive_ldos")
        self.gridLayoutWidget_6 = QtWidgets.QWidget(self.tab_7)
        self.gridLayoutWidget_6.setGeometry(QtCore.QRect(20, 10, 251, 176))
        self.gridLayoutWidget_6.setObjectName("gridLayoutWidget_6")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.gridLayoutWidget_6)
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.ne_ldos = QtWidgets.QLineEdit(self.gridLayoutWidget_6)
        self.ne_ldos.setObjectName("ne_ldos")
        self.gridLayout_6.addWidget(self.ne_ldos, 0, 1, 1, 1)
        self.delta_ldos = QtWidgets.QLineEdit(self.gridLayoutWidget_6)
        self.delta_ldos.setObjectName("delta_ldos")
        self.gridLayout_6.addWidget(self.delta_ldos, 3, 1, 1, 1)
        self.label_20 = QtWidgets.QLabel(self.gridLayoutWidget_6)
        self.label_20.setObjectName("label_20")
        self.gridLayout_6.addWidget(self.label_20, 3, 0, 1, 1)
        self.nk_ldos = QtWidgets.QLineEdit(self.gridLayoutWidget_6)
        self.nk_ldos.setObjectName("nk_ldos")
        self.gridLayout_6.addWidget(self.nk_ldos, 1, 1, 1, 1)
        self.label_17 = QtWidgets.QLabel(self.gridLayoutWidget_6)
        self.label_17.setObjectName("label_17")
        self.gridLayout_6.addWidget(self.label_17, 0, 0, 1, 1)
        self.label_18 = QtWidgets.QLabel(self.gridLayoutWidget_6)
        self.label_18.setObjectName("label_18")
        self.gridLayout_6.addWidget(self.label_18, 1, 0, 1, 1)
        self.label_19 = QtWidgets.QLabel(self.gridLayoutWidget_6)
        self.label_19.setObjectName("label_19")
        self.gridLayout_6.addWidget(self.label_19, 2, 0, 1, 1)
        self.window_ldos = QtWidgets.QLineEdit(self.gridLayoutWidget_6)
        self.window_ldos.setObjectName("window_ldos")
        self.gridLayout_6.addWidget(self.window_ldos, 2, 1, 1, 1)
        self.nsuper_ldos = QtWidgets.QLineEdit(self.gridLayoutWidget_6)
        self.nsuper_ldos.setObjectName("nsuper_ldos")
        self.gridLayout_6.addWidget(self.nsuper_ldos, 4, 1, 1, 1)
        self.label_21 = QtWidgets.QLabel(self.gridLayoutWidget_6)
        self.label_21.setObjectName("label_21")
        self.gridLayout_6.addWidget(self.label_21, 4, 0, 1, 1)
        self.tabWidget_3.addTab(self.tab_7, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 878, 24))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        self.tabWidget_2.setCurrentIndex(0)
        self.tabWidget_3.setCurrentIndex(1)
        self.bands_color.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "1D systems"))
        self.label_8.setText(_translate("MainWindow", "Type of lattice"))
        self.lattice.setItemText(0, _translate("MainWindow", "Chain"))
        self.lattice.setItemText(1, _translate("MainWindow", "Square"))
        self.lattice.setItemText(2, _translate("MainWindow", "Honeycomb zigzag"))
        self.lattice.setItemText(3, _translate("MainWindow", "Honeycomb armchair"))
        self.lattice.setItemText(4, _translate("MainWindow", "Triangular"))
        self.lattice.setItemText(5, _translate("MainWindow", "Kagome"))
        self.lattice.setItemText(6, _translate("MainWindow", "Lieb"))
        self.nsuper.setText(_translate("MainWindow", "1"))
        self.label_6.setText(_translate("MainWindow", "Supercell"))
        self.width.setText(_translate("MainWindow", "1"))
        self.label_2.setText(_translate("MainWindow", "Width"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Geometry"))
        self.Bx.setText(_translate("MainWindow", "0.0"))
        self.label_5.setText(_translate("MainWindow", "Zeeman Jz"))
        self.mAB.setText(_translate("MainWindow", "0.0"))
        self.By.setText(_translate("MainWindow", "0.0"))
        self.label.setText(_translate("MainWindow", "Fermi energy"))
        self.peierls.setText(_translate("MainWindow", "0.0"))
        self.kanemele.setText(_translate("MainWindow", "0.0"))
        self.label_24.setText(_translate("MainWindow", "Haldane"))
        self.antihaldane.setText(_translate("MainWindow", "0.0"))
        self.label_26.setText(_translate("MainWindow", "swave pairing"))
        self.fermi.setText(_translate("MainWindow", "0.0"))
        self.rashba.setText(_translate("MainWindow", "0.0"))
        self.haldane.setText(_translate("MainWindow", "0.0"))
        self.mAF.setText(_translate("MainWindow", "0.0"))
        self.label_10.setText(_translate("MainWindow", "Rashba"))
        self.label_11.setText(_translate("MainWindow", "Kane-Mele"))
        self.label_3.setText(_translate("MainWindow", "Zeeman Jx"))
        self.label_4.setText(_translate("MainWindow", "Zeeman Jy"))
        self.label_12.setText(_translate("MainWindow", "Sublattice imbalance"))
        self.label_14.setText(_translate("MainWindow", "Magnetic field"))
        self.swave.setText(_translate("MainWindow", "0.0"))
        self.Bz.setText(_translate("MainWindow", "0.0"))
        self.label_13.setText(_translate("MainWindow", "Antiferromagnetism"))
        self.label_25.setText(_translate("MainWindow", "Anti-Haldane"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_3), _translate("MainWindow", "Terms in the Hamiltonian"))
        self.show_structure.setText(_translate("MainWindow", "Show structure"))
        self.nsuper_struct.setText(_translate("MainWindow", "5"))
        self.label_7.setText(_translate("MainWindow", "Supercell"))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_4), _translate("MainWindow", "Structure"))
        self.show_bands.setText(_translate("MainWindow", "Band structure"))
        self.label_15.setText(_translate("MainWindow", "Operator"))
        self.bands_color.setItemText(0, _translate("MainWindow", "None"))
        self.bands_color.setItemText(1, _translate("MainWindow", "y-position"))
        self.bands_color.setItemText(2, _translate("MainWindow", "Sx"))
        self.bands_color.setItemText(3, _translate("MainWindow", "Sy"))
        self.bands_color.setItemText(4, _translate("MainWindow", "Sz"))
        self.bands_color.setItemText(5, _translate("MainWindow", "Valley"))
        self.label_9.setText(_translate("MainWindow", "# kpoints"))
        self.nk_bands.setText(_translate("MainWindow", "100"))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_5), _translate("MainWindow", "Bands"))
        self.show_dosbands.setToolTip(_translate("MainWindow", "This is equivalent to band structure calculation, but it can be applied for very large systems"))
        self.show_dosbands.setText(_translate("MainWindow", "Show DOS Bands"))
        self.delta_kbands.setText(_translate("MainWindow", "0.02"))
        self.label_27.setText(_translate("MainWindow", "Smearing"))
        self.ne_kbands.setText(_translate("MainWindow", "400"))
        self.label_28.setText(_translate("MainWindow", "# of energies"))
        self.label_29.setText(_translate("MainWindow", "Energy window"))
        self.window_kbands.setText(_translate("MainWindow", "3.0"))
        self.label_30.setText(_translate("MainWindow", "KPM scale"))
        self.scale_kbands.setText(_translate("MainWindow", "10.0"))
        self.label_31.setText(_translate("MainWindow", "# vectors"))
        self.nv_kbands.setText(_translate("MainWindow", "3"))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_9), _translate("MainWindow", "DOS Bands"))
        self.show_dos.setText(_translate("MainWindow", "Density of states"))
        self.label_16.setText(_translate("MainWindow", "Smearing"))
        self.DOS_smearing.setText(_translate("MainWindow", "0.01"))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_6), _translate("MainWindow", "DOS"))
        self.show_interactive_ldos.setText(_translate("MainWindow", "Show LDOS"))
        self.ne_ldos.setText(_translate("MainWindow", "300"))
        self.delta_ldos.setText(_translate("MainWindow", "0.03"))
        self.label_20.setText(_translate("MainWindow", "Smearing"))
        self.nk_ldos.setText(_translate("MainWindow", "20"))
        self.label_17.setText(_translate("MainWindow", "# of energies"))
        self.label_18.setText(_translate("MainWindow", "# of kpoints"))
        self.label_19.setText(_translate("MainWindow", "Energy window"))
        self.window_ldos.setText(_translate("MainWindow", "0.5"))
        self.nsuper_ldos.setText(_translate("MainWindow", "1"))
        self.label_21.setText(_translate("MainWindow", "SUpercell"))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_7), _translate("MainWindow", "LDOS"))

