
#
#
# Build.Your.Game
# by Jonas and Robert
# version: 1.2.3 Beta
#
#

from PyQt5 import QtCore, QtGui, QtWidgets
import time
import shutil
#from PyQt5.QtWidgets import QSizePolicy, QGridLayout


class Ui_Form(object):

    def open_side_menue(self):

        #hide_main_menue
        self.toolButton.hide()
        self.pushButton.hide()
        self.pushButton_2.hide()
        self.textBrowser.hide()
        self.textBrowser_2.hide()
        #hide_side_menue
        self.toolButton_2.hide()
        self.textBrowser_3.hide()
        self.pushButton_3.hide()
        self.pushButton_4.hide()
        #hide_custom_menue
        self.toolButton_3.hide()
        self.toolButton_4.hide()
        self.listWidget.hide()
        #hide_build_menue
        self.progressBar.hide()
        self.pushButton_5.hide()
        self.textBrowser_4.hide()
        self.pushButton_6.hide()
        #self.pushButton_11.hide()
        self.pushButton_7.hide()

        #show_side_menue
        self.toolButton_2.show()
        self.textBrowser_3.show()
        self.pushButton_3.show()
        self.pushButton_4.show()

        # modify_window
        Form.setStyleSheet("background-color:white")

    def open_custom_menue(self):

        # hide_main_menue
        self.toolButton.hide()
        self.pushButton.hide()
        self.pushButton_2.hide()
        self.textBrowser.hide()
        self.textBrowser_2.hide()
        # hide_side_menue
        self.toolButton_2.hide()
        self.textBrowser_3.hide()
        self.pushButton_3.hide()
        self.pushButton_4.hide()
        # hide_custom_menue
        self.toolButton_3.hide()
        self.toolButton_4.hide()
        self.listWidget.hide()
        # hide_build_menue
        self.progressBar.hide()
        self.pushButton_5.hide()
        self.textBrowser_4.hide()
        self.pushButton_6.hide()
        # self.pushButton_11.hide()
        self.pushButton_7.hide()

        # show_custom_menue
        self.toolButton_3.show()
        self.toolButton_4.show()
        self.listWidget.show()

        #modify_window
        Form.setStyleSheet("background-color:gray")

    def open_build_menue(self):

        # hide_main_menue
        self.toolButton.hide()
        self.pushButton.hide()
        self.pushButton_2.hide()
        self.textBrowser.hide()
        self.textBrowser_2.hide()
        # hide_side_menue
        self.toolButton_2.hide()
        self.textBrowser_3.hide()
        self.pushButton_3.hide()
        self.pushButton_4.hide()
        # hide_custom_menue
        self.toolButton_3.hide()
        self.toolButton_4.hide()
        self.listWidget.hide()
        # hide_build_menue
        self.progressBar.hide()
        self.pushButton_5.hide()
        self.textBrowser_4.hide()
        self.pushButton_6.hide()
        # self.pushButton_11.hide()
        self.pushButton_7.hide()

        # show_build_menue
        self.pushButton_5.show()
        self.textBrowser_4.show()
        self.pushButton_6.show()
        # self.pushButton_11.show()
        self.pushButton_7.show()

        if self.build_process == "in_work":
            self.substract_step = "true"
            self.pushButton_6.setText("Von neu beginnen")
            self.pushButton_7.setText("Fortfahren")
            self.textBrowser_4.setText("Fortfahren oder von neu beginnen?")

        #modify_window
        Form.setStyleSheet("background-color:gray")

    def open_main_menue(self):

        # hide_main_menue
        self.toolButton.hide()
        self.pushButton.hide()
        self.pushButton_2.hide()
        self.textBrowser.hide()
        self.textBrowser_2.hide()
        # hide_side_menue
        self.toolButton_2.hide()
        self.textBrowser_3.hide()
        self.pushButton_3.hide()
        self.pushButton_4.hide()
        # hide_custom_menue
        self.toolButton_3.hide()
        self.toolButton_4.hide()
        self.listWidget.hide()
        # hide_build_menue
        self.progressBar.hide()
        self.pushButton_5.hide()
        self.textBrowser_4.hide()
        self.pushButton_6.hide()
        # self.pushButton_11.hide()
        self.pushButton_7.hide()

        # show_main_menue
        self.toolButton.show()
        self.pushButton.show()
        self.pushButton_2.show()
        self.textBrowser.show()
        self.textBrowser_2.show()

        # modify_window
        Form.setStyleSheet("background-color:white")

    def setupUi(self, Form):

        #variabals_build_menue:

        self.step = 0
        self.build_process = "bypass"
        self.substract_step = "false"

        #variabals_custom_menue

        self.position_of_list_items = 0
        self.current_line = 0

        #main_menue

        Form.setObjectName("Form")
        Form.resize(1414, 738)
        Form.setBaseSize(QtCore.QSize(1920, 1080))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("assets/textures/icons/main_icon.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        Form.setToolTip("")
        Form.setStyleSheet("background-color:white")
        Form.setWindowFilePath("")
        self.toolButton = QtWidgets.QToolButton(Form)
        self.toolButton.setGeometry(QtCore.QRect(1330, 10, 71, 51))
        self.toolButton.clicked.connect(self.open_side_menue)
        self.toolButton.setStyleSheet("background-color:gray;\n"
"color:white;\n"
"border-style:outset;\n"
"border-width:2px;\n"
"border-radius:10px;\n"
"border-color:white;\n"
"font:bold 30px;\n"
"padding:6px\n"
"")
        self.toolButton.setObjectName("toolButton")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(470, 190, 471, 111))
        self.pushButton.clicked.connect(self.open_custom_menue)
        #self.pushButton.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.pushButton.setStyleSheet("background-color:gray;\n"
"color:white;\n"
"border-style:outset;\n"
"border-width:2px;\n"
"border-radius:20px;\n"
"border-color:white;\n"
"font:bold 30px;\n"
"padding:6px")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(470, 330, 471, 111))
        self.pushButton_2.clicked.connect(self.open_build_menue)
        self.pushButton_2.setStyleSheet("background-color:gray;\n"
"color:white;\n"
"border-style:outset;\n"
"border-width:2px;\n"
"border-radius:20px;\n"
"border-color:white;\n"
"font:bold 30px;\n"
"padding:6px")
        self.pushButton_2.setObjectName("pushButton_2")
        self.textBrowser = QtWidgets.QTextBrowser(Form)
        self.textBrowser.setGeometry(QtCore.QRect(220, 20, 961, 151))
        self.textBrowser.setStyleSheet("background-color:white;\n"
"border-style:outset;\n"
"border-width:0px;\n"
"border-radius:0px;\n"
"border-color:white;\n"
"")
        self.textBrowser.setObjectName("textBrowser")
        self.textBrowser_2 = QtWidgets.QTextBrowser(Form)
        self.textBrowser_2.setGeometry(QtCore.QRect(10, 710, 241, 21))
        self.textBrowser_2.setStyleSheet("background-color:white;\n"
"border-style:outset;\n"
"border-width:0px;\n"
"border-radius:0px;\n"
"border-color:white;")
        self.textBrowser_2.setOpenExternalLinks(True)
        self.textBrowser_2.setObjectName("textBrowser_2")

        #side_menue

        self.toolButton_2 = QtWidgets.QToolButton(Form)
        self.toolButton_2.setGeometry(QtCore.QRect(0, 0, 431, 51))
        self.toolButton_2.clicked.connect(self.open_main_menue)
        self.toolButton_2.setStyleSheet("background-color:gray;\n"
                                      "color:white;\n"
                                      "border-style:outset;\n"
                                      "border-width:2px;\n"
                                      "border-radius:10px;\n"
                                      "border-color:white;\n"
                                      "font:bold 30px;\n"
                                      "padding:6px\n"
                                      "")
        self.toolButton_2.setObjectName("toolButton_2")
        self.toolButton_2.hide()
        self.textBrowser_3 = QtWidgets.QTextBrowser(Form)
        self.textBrowser_3.setGeometry(QtCore.QRect(10, 60, 1231, 401))
        self.textBrowser_3.setStyleSheet("background-color:white;\n"
                                       "border-style:outset;\n"
                                       "border-width:0px;\n"
                                       "border-radius:0px;\n"
                                       "border-color:white;")
        self.textBrowser_3.setOpenExternalLinks(True)
        self.textBrowser_3.setObjectName("textBrowser_3")
        self.textBrowser_3.hide()
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.move(10, 140)
        self.lineEdit.hide()
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(1250, 660, 151, 61))
        self.pushButton_3.clicked.connect(self.quit_fuction)
        self.pushButton_3.setStyleSheet("background-color:gray;\n"
                                      "color:white;\n"
                                      "border-style:outset;\n"
                                      "border-width:2px;\n"
                                      "border-radius:10px;\n"
                                      "border-color:white;\n"
                                      "font:bold 30px;\n"
                                      "padding:6px\n"
                                      "")
        self.pushButton_3.setObjectName("pushButton_2")
        self.pushButton_3.hide()
        self.pushButton_03 = QtWidgets.QPushButton(Form)
        self.pushButton_03.setGeometry(QtCore.QRect(1250, 660, 151, 61))
        self.pushButton_03.setText("Sichern")
        self.pushButton_03.clicked.connect(self.change_installtion_byg_path_write)
        self.pushButton_03.setStyleSheet("background-color:gray;\n"
                                        "color:white;\n"
                                        "border-style:outset;\n"
                                        "border-width:2px;\n"
                                        "border-radius:10px;\n"
                                        "border-color:white;\n"
                                        "font:bold 30px;\n"
                                        "padding:6px\n"
                                        "")
        self.pushButton_03.setObjectName("pushButton_03")
        self.pushButton_03.hide()
        self.pushButton_4 = QtWidgets.QPushButton(Form)
        self.pushButton_4.setGeometry(QtCore.QRect(1090, 660, 151, 61))
        self.pushButton_4.clicked.connect(self.change_installtion_byg_path)
        self.pushButton_4.setStyleSheet("background-color:gray;\n"
                                        "color:white;\n"
                                        "border-style:outset;\n"
                                        "border-width:2px;\n"
                                        "border-radius:10px;\n"
                                        "border-color:white;\n"
                                        "font:bold 30px;\n"
                                        "padding:6px\n"
                                        "")
        self.pushButton_4.setObjectName("pushButton_3")
        self.pushButton_4.hide()

        #custom_menue

        self.toolButton_3 = QtWidgets.QToolButton(Form)
        self.toolButton_3.setGeometry(QtCore.QRect(20, 10, 431, 51))
        self.toolButton_3.clicked.connect(self.open_main_menue)
        self.toolButton_3.setStyleSheet("background-color:gray;\n"
                                      "color:white;\n"
                                      "border-style:outset;\n"
                                      "border-width:2px;\n"
                                      "border-radius:10px;\n"
                                      "border-color:white;\n"
                                      "font:bold 30px;\n"
                                      "padding:6px\n"
                                      "")
        self.toolButton_3.setObjectName("toolButton_3")
        self.toolButton_3.hide()
        self.toolButton_4 = QtWidgets.QToolButton(Form)
        self.toolButton_4.setGeometry(QtCore.QRect(1330, 10, 71, 51))
        self.toolButton_4.clicked.connect(self.open_side_menue)
        self.toolButton_4.setStyleSheet("background-color:gray;\n"
                                        "color:white;\n"
                                        "border-style:outset;\n"
                                        "border-width:2px;\n"
                                        "border-radius:10px;\n"
                                        "border-color:white;\n"
                                        "font:bold 30px;\n"
                                        "padding:6px\n"
                                        "")
        self.toolButton_4.setObjectName("toolButton_4")
        self.toolButton_4.hide()



        self.listWidget = QtWidgets.QListWidget(Form)
        self.listWidget.setGeometry(QtCore.QRect(15, 71, 1071, 651))
        self.listWidget.setStyleSheet("background-color:transparent;\n"
                                      "color:white;\n"
                                      "border-style:outset;\n"
                                      "border-width:2px;\n"
                                      "border-radius:10px;\n"
                                      "border-color:white;\n"
                                      "font:bold 30px;\n"
                                      "padding:6px\n"
                                      "")
        self.listWidget.setObjectName("listWidget")
        item = QtWidgets.QListWidgetItem()
        #icon1 = QtGui.QIcon()
        #icon1.addPixmap(QtGui.QPixmap("assets/textures/icons/project_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        #item.setIcon(icon1)
        self.listWidget.addItem(item)
        self.listWidget.hide()

        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        #item = self.listWidget.item(0)
        #item.setText(("Testname,  erstellt am 00.00.0000"))
        self.listWidget.setSortingEnabled(__sortingEnabled)
        self.listWidget.clicked.connect(self.open_list_item)

        F_project_number = open("projects/project_BYG_number", "r")
        project_number = (F_project_number.read())
        print("Projekte: " + project_number)
        project_number = int(project_number)

        #F_project_names = open("projects/project_BYG_names", "r")
        #project_names = (F_project_names.readline())
        ##print("Projekte: " + project_names)
        #project_names = int(project_names)

        while project_number > 0:
            #print(project_number)

            F_current_project_name = open("projects/project_BYG_names", "r")
            current_project_name_lines = (F_current_project_name.readlines())
            current_project_name = current_project_name_lines[self.current_line]
            #print(current_project_name)
            self.listWidget.insertItem(self.position_of_list_items, current_project_name)
            self.position_of_list_items = self.position_of_list_items + 1
            self.current_line = self.current_line + 1

            project_number = project_number - 1

        #custom1_menue

        self.pushButton_008 = QtWidgets.QPushButton(Form)
        self.pushButton_008.setGeometry(QtCore.QRect(530, 600, 341, 61))
        self.pushButton_008.setStyleSheet("color:white;\n"
                                        "border-style:outset;\n"
                                        "border-width:2px;\n"
                                        "border-radius:10px;\n"
                                        "border-color:white;\n"
                                        "font:bold 30px;\n"
                                        "padding:6px")
        self.pushButton_008.setObjectName("pushButton008")
        self.pushButton_008.clicked.connect(self.custom1_save)
        self.pushButton_008.hide()
        self.pushButton_009 = QtWidgets.QPushButton(Form)
        self.pushButton_009.setGeometry(QtCore.QRect(530, 530, 341, 61))
        self.pushButton_009.setStyleSheet("color:white;\n"
                                        "border-style:outset;\n"
                                        "border-width:2px;\n"
                                        "border-radius:10px;\n"
                                        "border-color:white;\n"
                                        "font:bold 20px;\n"
                                        "padding:6px")
        self.pushButton_009.setObjectName("pushButton_2")
        self.pushButton_009.clicked.connect(self.custom1_code_show)
        self.pushButton_009.hide()
        self.pushButton_008_ = QtWidgets.QPushButton(Form)
        self.pushButton_008_.setGeometry(QtCore.QRect(530, 670, 341, 61))
        self.pushButton_008_.setStyleSheet("color:white;\n"
                                           "border-style:outset;\n"
                                           "border-width:2px;\n"
                                           "border-radius:10px;\n"
                                           "border-color:white;\n"
                                           "font:bold 30px;\n"
                                           "padding:6px")
        self.pushButton_008_.setObjectName("pushButton008_")
        self.pushButton_008_.clicked.connect(self.change_to_p_BYG_y)
        self.pushButton_008_.hide()
        self.toolButton_002 = QtWidgets.QToolButton(Form)
        self.toolButton_002.setGeometry(QtCore.QRect(5, 5, 400, 51))
        self.toolButton_002.clicked.connect(self.custom1_menue_close)
        self.toolButton_002.setStyleSheet("background-color:gray;\n"
                                        "color:white;\n"
                                        "border-style:outset;\n"
                                        "border-width:2px;\n"
                                        "border-radius:10px;\n"
                                        "border-color:white;\n"
                                        "font:bold 30px;\n"
                                        "padding:6px\n"
                                        "")
        self.toolButton_002.setObjectName("toolButton_002")
        self.toolButton_002.hide()
        self.textBrowser_005 = QtWidgets.QTextBrowser(Form)
        self.textBrowser_005.setGeometry(QtCore.QRect(410, 20, 551, 91))
        self.textBrowser_005.setStyleSheet("color:white;\n"
                                         "border-style:outset;\n"
                                         "border-width:2px;\n"
                                         "border-radius:10px;\n"
                                         "border-color:white;\n"
                                         "padding:6px")
        self.textBrowser_005.setObjectName("textBrowser005")
        self.textBrowser_005.hide()


        self.horizontalSlider_000 = QtWidgets.QSlider(Form)
        self.horizontalSlider_000.setGeometry(QtCore.QRect(60, 170, 221, 31))
        self.horizontalSlider_000.sliderReleased.connect(self.custom1_hs_value)
        self.horizontalSlider_000.valueChanged.connect(self.custom1_hs_value_changed)
        self.horizontalSlider_000.setStyleSheet("")
        self.horizontalSlider_000.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_000.setObjectName("horizontalSlider")
        self.horizontalSlider_000.hide()
        self.label_000 = QtWidgets.QLabel(Form)
        self.label_000.setGeometry(QtCore.QRect(60, 140, 370, 21))
        self.label_000.setObjectName("label")
        self.label_000.hide()

        self.comboBox_000 = QtWidgets.QComboBox(Form)
        self.comboBox_000.move(60, 240)
        self.comboBox_000.addItems(["Baustein 1", "Baustein2", "Baustein 3", "Baustein 4", "Baustein 5", "Baustein 6" , "Baustein 7", "Baustein 8"])
        self.comboBox_000.currentIndexChanged.connect(self.custom1_cb_barrier_changed)
        self.comboBox_000.hide()

        self.label_001 = QtWidgets.QLabel(Form)
        self.label_001.setGeometry(QtCore.QRect(60, 210, 370, 21))
        self.label_001.setObjectName("label001")
        self.label_001.setText("Level ändern")
        self.label_001.hide()

        self.label_002 = QtWidgets.QLabel(Form)
        self.label_002.setGeometry(QtCore.QRect(60, 270, 370, 21))
        self.label_002.setObjectName("label002")
        self.label_002.setText("Höhe über dem Boden")
        self.label_002.hide()

        self.label_003 = QtWidgets.QLabel(Form)
        self.label_003.setGeometry(QtCore.QRect(60, 330, 370, 21))
        self.label_003.setObjectName("label003")
        self.label_003.setText("Länge")
        self.label_003.hide()

        self.label_004 = QtWidgets.QLabel(Form)
        self.label_004.setGeometry(QtCore.QRect(60, 390, 370, 21))
        self.label_004.setObjectName("label004")
        self.label_004.setText("Breite")
        self.label_004.hide()

        self.horizontalSlider_001 = QtWidgets.QSlider(Form)
        self.horizontalSlider_001.setGeometry(QtCore.QRect(60, 295, 221, 31))
        self.horizontalSlider_001.setMinimum(1)
        self.horizontalSlider_001.setMaximum(1079)
        self.horizontalSlider_001.setValue(50)
        self.horizontalSlider_001.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_001.setObjectName("horizontalSlider_001")
        self.horizontalSlider_001.valueChanged.connect(self.custom1_hs001_value_changed)
        self.horizontalSlider_001.valueChanged.connect(self.custom1_hs_dfe)
        self.horizontalSlider_001.sliderReleased.connect(self.custom1_hs001_003_value)
        self.horizontalSlider_001.hide()

        self.horizontalSlider_002 = QtWidgets.QSlider(Form)
        self.horizontalSlider_002.setGeometry(QtCore.QRect(60, 355, 221, 31))
        self.horizontalSlider_002.setMinimum(5)
        self.horizontalSlider_002.setMaximum(150)
        self.horizontalSlider_002.setValue(100)
        self.horizontalSlider_002.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_002.setObjectName("horizontalSlider_002")
        self.horizontalSlider_002.valueChanged.connect(self.custom1_hs002_value_changed)
        self.horizontalSlider_002.valueChanged.connect(self.custom1_hs_dfe)
        self.horizontalSlider_002.sliderReleased.connect(self.custom1_hs001_003_value)
        self.horizontalSlider_002.hide()

        self.horizontalSlider_003 = QtWidgets.QSlider(Form)
        self.horizontalSlider_003.setGeometry(QtCore.QRect(60, 415, 221, 31))
        self.horizontalSlider_003.setMinimum(5)
        self.horizontalSlider_003.setMaximum(150)
        self.horizontalSlider_003.setValue(30)
        self.horizontalSlider_003.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_003.setObjectName("horizontalSlider_003")
        self.horizontalSlider_003.valueChanged.connect(self.custom1_hs003_value_changed)
        self.horizontalSlider_003.valueChanged.connect(self.custom1_hs_dfe)
        self.horizontalSlider_003.sliderReleased.connect(self.custom1_hs001_003_value)
        self.horizontalSlider_003.hide()

        self.label_005 = QtWidgets.QLabel(Form)
        self.label_005.setGeometry(QtCore.QRect(60, 440, 370, 21))
        self.label_005.setObjectName("label005")
        self.label_005.setText("Vorschau:")
        self.label_005.hide()

        #self.textBrowser_007 = QtWidgets.QTextEdit(Form)
        self.textBrowser_007_bg = QtWidgets.QTextBrowser(Form)
        self.textBrowser_007_bg.setGeometry(QtCore.QRect(60, 470, 384, 216))
        #1920 / 5 = 384, 1080 / 5 = 216
        self.textBrowser_007_bg.setStyleSheet("background-color:black")
        self.textBrowser_007_bg.setObjectName("textBrowser007")
        self.textBrowser_007_bg.hide()

        self.textBrowser_007_fg1 = QtWidgets.QTextBrowser(Form)
        self.textBrowser_007_fg1.setGeometry(QtCore.QRect(70, 676, 20, 6))
        #686 = 470 + 216, untere Kante des "Fensterns", 100 / 5 = 20, 30 / 5 = 6, 50 / 5 = 10, also 686 - 10 <- Höhe überm Boden
        self.textBrowser_007_fg1.setStyleSheet("background-color:black")
        self.textBrowser_007_fg1.hide()

        self.textBrowser_007_fg2 = QtWidgets.QTextBrowser(Form)
        self.textBrowser_007_fg2.setGeometry(QtCore.QRect(90, 666, 14, 8))
        self.textBrowser_007_fg2.setStyleSheet("background-color:black")
        self.textBrowser_007_fg2.hide()

        self.textBrowser_007_fg3 = QtWidgets.QTextBrowser(Form)
        self.textBrowser_007_fg3.setGeometry(QtCore.QRect(104, 656, 24, 8))
        self.textBrowser_007_fg3.setStyleSheet("background-color:black")
        self.textBrowser_007_fg3.hide()

        self.textBrowser_007_fg4 = QtWidgets.QTextBrowser(Form)
        self.textBrowser_007_fg4.setGeometry(QtCore.QRect(128, 646, 8, 4))
        self.textBrowser_007_fg4.setStyleSheet("background-color:black")
        self.textBrowser_007_fg4.hide()

        self.textBrowser_007_fg5 = QtWidgets.QTextBrowser(Form)
        self.textBrowser_007_fg5.setGeometry(QtCore.QRect(136, 636, 4, 4))
        self.textBrowser_007_fg5.setStyleSheet("background-color:black")
        self.textBrowser_007_fg5.hide()

        self.textBrowser_007_fg5 = QtWidgets.QTextBrowser(Form)
        self.textBrowser_007_fg5.setGeometry(QtCore.QRect(136, 636, 4, 4))
        self.textBrowser_007_fg5.setStyleSheet("background-color:black")
        self.textBrowser_007_fg5.hide()

        self.textBrowser_007_fg6 = QtWidgets.QTextBrowser(Form)
        self.textBrowser_007_fg6.setGeometry(QtCore.QRect(140, 656, 16, 16))
        self.textBrowser_007_fg6.setStyleSheet("background-color:black")
        self.textBrowser_007_fg6.hide()

        self.textBrowser_007_fg7 = QtWidgets.QTextBrowser(Form)
        self.textBrowser_007_fg7.setGeometry(QtCore.QRect(156, 666, 6, 8))
        self.textBrowser_007_fg7.setStyleSheet("background-color:black")
        self.textBrowser_007_fg7.hide()

        self.textBrowser_007_fg8 = QtWidgets.QTextBrowser(Form)
        self.textBrowser_007_fg8.setGeometry(QtCore.QRect(162, 656, 24, 8))
        self.textBrowser_007_fg8.setStyleSheet("background-color:black")
        self.textBrowser_007_fg8.hide()

        self.textBrowser_006 = QtWidgets.QTextEdit(Form)
        self.textBrowser_006.setGeometry(QtCore.QRect(0, 0, 1421, 741))
        self.textBrowser_006.setStyleSheet("background-color:black;\n"
                                         "color:white")
        self.textBrowser_006.setObjectName("textBrowser")
        self.textBrowser_006.hide()
        self.pushButton_010 = QtWidgets.QPushButton(Form)
        self.pushButton_010.setGeometry(QtCore.QRect(950, 10, 421, 51))
        self.pushButton_010.clicked.connect(self.close_show_code_001)
        self.pushButton_010.setText("Exit")
        self.pushButton_010.setStyleSheet("background-color:gray;\n"
                                         "color:white;\n"
                                         "border-style:outset;\n"
                                         "border-width:2px;\n"
                                         "border-radius:10px;\n"
                                         "border-color:white;\n"
                                         "font:bold 30px;\n"
                                         "padding:6px")
        self.pushButton_010.setObjectName("pushButton_10")
        self.pushButton_010.hide()

        #build_menue

        self.progressBar = QtWidgets.QProgressBar(Form)
        self.progressBar.setGeometry(QtCore.QRect(564, 420, 301, 101))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.progressBar.hide()

        self.pushButton_5 = QtWidgets.QPushButton(Form)
        self.pushButton_5.setGeometry(QtCore.QRect(10, 10, 421, 51))
        self.pushButton_5.clicked.connect(self.open_main_menue)
        self.pushButton_5.setStyleSheet("background-color:gray;\n"
                                      "color:white;\n"
                                      "border-style:outset;\n"
                                      "border-width:2px;\n"
                                      "border-radius:10px;\n"
                                      "border-color:white;\n"
                                      "font:bold 30px;\n"
                                      "padding:6px")
        self.pushButton_5.setObjectName("pushButton_4")
        self.pushButton_5.hide()
        self.textBrowser_4 = QtWidgets.QTextBrowser(Form)
        self.textBrowser_4.setGeometry(QtCore.QRect(344, 120, 740, 91))
        self.textBrowser_4.setStyleSheet("color:white;\n"
                                       "border-style:outset;\n"
                                       "border-width:2px;\n"
                                       "border-radius:10px;\n"
                                       "border-color:white;\n"
                                       "padding:6px")
        self.textBrowser_4.setObjectName("textBrowser_4")
        self.textBrowser_4.hide()
        self.pushButton_6 = QtWidgets.QPushButton(Form)
        self.pushButton_6.setGeometry(QtCore.QRect(200, 420, 301, 101))
        self.pushButton_6.clicked.connect(self.step_selction_pb6)
        self.pushButton_6.setStyleSheet("background-color:gray;\n"
                                        "color:white;\n"
                                        "border-style:outset;\n"
                                        "border-width:2px;\n"
                                        "border-radius:10px;\n"
                                        "border-color:white;\n"
                                        "font:bold 30px;\n"
                                        "padding:6px")
        self.pushButton_6.setObjectName("pushButton_5")
        self.pushButton_6.hide()
        # self.pushButton_11 = QtWidgets.QPushButton(Form)
        # self.pushButton_11.setGeometry(QtCore.QRect(470, 420, 301, 101))
        # self.pushButton_11.setStyleSheet("background-color:gray;\n"
        # "color:white;\n"
        # "border-style:outset;\n"
        # "border-width:2px;\n"
        # "border-radius:10px;\n"
        # "border-color:white;\n"
        # "font:bold 30px;\n"
        # "padding:6px")
        # self.pushButton_11.setObjectName("pushButton_11")
        self.pushButton_7 = QtWidgets.QPushButton(Form)
        self.pushButton_7.setGeometry(QtCore.QRect(901, 420, 301, 101))
        self.pushButton_7.clicked.connect(self.step_selction_pb7)
        self.pushButton_7.setStyleSheet("background-color:gray;\n"
                                        "color:white;\n"
                                        "border-style:outset;\n"
                                        "border-width:2px;\n"
                                        "border-radius:10px;\n"
                                        "border-color:white;\n"
                                        "font:bold 30px;\n"
                                        "padding:6px")
        self.pushButton_7.setObjectName("pushButton_6")
        self.pushButton_7.hide()

        # build1_menue

        self.pushButton_8 = QtWidgets.QPushButton(Form)
        self.pushButton_8.setGeometry(QtCore.QRect(530, 600, 341, 61))
        self.pushButton_8.setStyleSheet("color:white;\n"
                                        "border-style:outset;\n"
                                        "border-width:2px;\n"
                                        "border-radius:10px;\n"
                                        "border-color:white;\n"
                                        "font:bold 30px;\n"
                                        "padding:6px")
        self.pushButton_8.setObjectName("pushButton")
        self.pushButton_8.clicked.connect(self.build1_save)
        self.pushButton_8.hide()
        self.pushButton_9 = QtWidgets.QPushButton(Form)
        self.pushButton_9.setGeometry(QtCore.QRect(530, 670, 341, 61))
        self.pushButton_9.setStyleSheet("color:white;\n"
                                        "border-style:outset;\n"
                                        "border-width:2px;\n"
                                        "border-radius:10px;\n"
                                        "border-color:white;\n"
                                        "font:bold 30px;\n"
                                        "padding:6px")
        self.pushButton_9.setObjectName("pushButton_2")
        self.pushButton_9.hide()
        self.textBrowser_5 = QtWidgets.QTextBrowser(Form)
        self.textBrowser_5.setGeometry(QtCore.QRect(410, 20, 551, 91))
        self.textBrowser_5.setStyleSheet("color:white;\n"
                                         "border-style:outset;\n"
                                         "border-width:2px;\n"
                                         "border-radius:10px;\n"
                                         "border-color:white;\n"
                                         "padding:6px")
        self.textBrowser_5.setObjectName("textBrowser")
        self.textBrowser_5.hide()
        self.horizontalSlider = QtWidgets.QSlider(Form)
        self.horizontalSlider.setGeometry(QtCore.QRect(60, 170, 221, 31))
        self.horizontalSlider.setStyleSheet("")
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.horizontalSlider.hide()
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(60, 140, 370, 21))
        self.label.setObjectName("label")
        self.label.hide()
        self.textBrowser_6 = QtWidgets.QTextBrowser(Form)
        self.textBrowser_6.setGeometry(QtCore.QRect(0, 0, 1421, 741))
        self.textBrowser_6.setStyleSheet("background-color:black;\n"
                                       "color:white")
        self.textBrowser_6.setObjectName("textBrowser")
        self.textBrowser_6.hide()
        self.pushButton_10 = QtWidgets.QPushButton(Form)
        self.pushButton_10.setGeometry(QtCore.QRect(950, 10, 421, 51))
        self.pushButton_10.clicked.connect(self.close_show_code)
        self.pushButton_10.setText("Exit")
        self.pushButton_10.setStyleSheet("background-color:gray;\n"
                                        "color:white;\n"
                                        "border-style:outset;\n"
                                        "border-width:2px;\n"
                                        "border-radius:10px;\n"
                                        "border-color:white;\n"
                                        "font:bold 30px;\n"
                                        "padding:6px")
        self.pushButton_10.setObjectName("pushButton_10")
        self.pushButton_10.hide()

        self.lineEdit_build1 = QtWidgets.QLineEdit(Form)
        self.lineEdit_build1.setGeometry(567, 140, 200, 20)
        self.lineEdit_build1.hide()

        self.label_build1_6 = QtWidgets.QLabel(Form)
        self.label_build1_6.setGeometry(567, 120, 200, 20)
        self.label_build1_6.setText("Name des Projektes")
        self.label_build1_6.hide()

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        F_00 = open("byg_insta_BYG_lation_path_byg", "r")
        self.instalation_path_byg = F_00.read()
        print ("Instalationspfad: " + self.instalation_path_byg)
        if self.instalation_path_byg == "no_setting":
            print("Bitte lege einen Instalationspfad fest!")

            self.toolButton.hide()
            self.pushButton.hide()
            self.pushButton_2.hide()
            self.textBrowser.hide()
            self.textBrowser_2.hide()

            self.toolButton_2.show()
            self.textBrowser_3.show()
            self.pushButton_3.show()
            self.pushButton_4.show()

            # modify_window
            Form.setStyleSheet("background-color:white")

            self.lineEdit.show()
            self.pushButton_03.show()
            self.pushButton_4.hide()
            self.pushButton_3.hide()
            self.toolButton_2.hide()
            self.textBrowser_3.setHtml(
                ("<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                 "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                 "p, li { white-space: pre-wrap; }\n"
                 "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
                 "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:48pt;\">Installationspfad ändern</span></p>\n"))

    #main_menue_functions

    #side_menue_functions
    def quit_fuction(self):
        sys.exit(app.exec_())

    #custom_menue_functions


    def open_list_item(self):
        item = self.listWidget.currentItem()
        item_number = self.listWidget.currentRow()
        #print("ROW", item_number)
        self.current_item = str(item.text())
        #print(str(item.text()))
        #print(self.current_item)
        s = self.current_item
        s = " ".join(s.split())
        #s = s.replace(" ", "")
        self.current_item = s
        #print("self.current item ohne leerzeichen" + self.current_item)
        #print("TEST")
        self.pushButton_008.show()
        self.pushButton_009.show()
        self.textBrowser_005.show()
        self.horizontalSlider_000.show()
        self.label_000.show()
        self.toolButton_002.show()
        #self.textBrowser_006.show()
        #self.pushButton_010.show()
        self.pushButton_008_.show()
        self.comboBox_000.show()
        self.label_001.show()
        self.label_002.show()
        self.label_003.show()
        self.label_004.show()
        self.horizontalSlider_001.show()
        self.horizontalSlider_002.show()
        self.horizontalSlider_003.show()
        self.label_005.show()
        self.textBrowser_007_bg.show()
        self.textBrowser_007_fg1.show()
        self.textBrowser_007_fg2.show()
        self.textBrowser_007_fg3.show()
        self.textBrowser_007_fg4.show()
        self.textBrowser_007_fg5.show()
        self.textBrowser_007_fg6.show()
        self.textBrowser_007_fg7.show()
        self.textBrowser_007_fg8.show()
        self.toolButton_3.hide()
        self.toolButton_4.hide()
        self.listWidget.hide()

        custom1_game_project = open("projects/" + self.current_item, "r")
        self.current_project_code = custom1_game_project.read()
        #print(self.current_project_code)

        #with open("projects/" + self.current_item, "r") as file:
            #list = []
            #for line in file:
                #list += [line.strip()]
        ##print(list[0])
        #self.custom1_project_code_1mod = list[1]

        F_current_project_kind = open("projects/project_BYG_kinds", "r")
        current_project_kind_lines = (F_current_project_kind.readlines())
        self.current_project_kind = current_project_kind_lines[item_number]
        #print(self.current_project_kind)
        s1 = self.current_project_kind
        s1 = " ".join(s1.split())
        self.current_project_kind = s1
        #print("self.kind item ohne leerzeichen" + self.current_project_kind)
        #print("TEST")

        self.current_project_kind = s1
        #print("self.kind item ohne leerzeichen" + self.current_project_kind)
        #print("TEST")

        self.write_hob1, self.write_le1, self.write_wi1 = 50, 100, 30
        self.write_hob2, self.write_le2, self.write_wi2 = 100, 70, 40
        self.write_hob3, self.write_le3, self.write_wi3 = 150, 120, 40
        self.write_hob4, self.write_le4, self.write_wi4 = 200, 40, 20
        self.write_hob5, self.write_le5, self.write_wi5 = 250, 20, 20
        self.write_hob6, self.write_le6, self.write_wi6 = 150, 80, 80
        self.write_hob7, self.write_le7, self.write_wi7 = 100, 30, 40
        self.write_hob8, self.write_le8, self.write_wi8 = 150, 120, 40

        self.preview_hob1, self.preview_le1, self.preview_wi1 = 676, 20, 6
        self.preview_hob2, self.preview_le2, self.preview_wi2 = 666, 14, 8
        self.preview_hob3, self.preview_le3, self.preview_wi3 = 656, 24, 8
        self.preview_hob4, self.preview_le4, self.preview_wi4 = 646, 8, 4
        self.preview_hob5, self.preview_le5, self.preview_wi5 = 636, 4, 4
        self.preview_hob6, self.preview_le6, self.preview_wi6 = 656, 16, 16
        self.preview_hob7, self.preview_le7, self.preview_wi7 = 666, 6, 8
        self.preview_hob8, self.preview_le8, self.preview_wi8 = 656, 24, 8

        self.preview_dfe2 = 70 + self.preview_le1
        self.preview_dfe3 = 70 + self.preview_le1 + self.preview_le2
        self.preview_dfe4 = 70 + self.preview_le1 + self.preview_le2 + self.preview_le3
        self.preview_dfe5 = 70 + self.preview_le1 + self.preview_le2 + self.preview_le3 + self.preview_le4
        self.preview_dfe6 = 70 + self.preview_le1 + self.preview_le2 + self.preview_le3 + self.preview_le4 + self.preview_le5
        self.preview_dfe7 = 70 + self.preview_le1 + self.preview_le2 + self.preview_le3 + self.preview_le4 + self.preview_le5 + self.preview_le6
        self.preview_dfe8 = 70 + self.preview_le1 + self.preview_le2 + self.preview_le3 + self.preview_le4 + self.preview_le5 + self.preview_le6 + self.preview_le7

        self.current_barrier = 1
        self.comboBox_000.setCurrentIndex(0)

        self.textBrowser_007_fg1.setGeometry(QtCore.QRect(70, 676, 20, 6))
        self.textBrowser_007_fg2.setGeometry(QtCore.QRect(90, 666, 14, 8))
        self.textBrowser_007_fg3.setGeometry(QtCore.QRect(104, 656, 24, 8))
        self.textBrowser_007_fg4.setGeometry(QtCore.QRect(128, 646, 8, 4))
        self.textBrowser_007_fg5.setGeometry(QtCore.QRect(136, 636, 4, 4))
        self.textBrowser_007_fg5.setGeometry(QtCore.QRect(136, 636, 4, 4))
        self.textBrowser_007_fg6.setGeometry(QtCore.QRect(140, 656, 16, 16))
        self.textBrowser_007_fg7.setGeometry(QtCore.QRect(156, 666, 6, 8))
        self.textBrowser_007_fg8.setGeometry(QtCore.QRect(162, 656, 24, 8))

        self.horizontalSlider_001.setValue(50)
        self.horizontalSlider_002.setValue(100)
        self.horizontalSlider_003.setValue(30)

        if self.current_project_kind == "jumpnrunmodern":
            #print("Jump'n Run: " + self.current_project_kind)
            self.horizontalSlider_000.setMinimum(0)
            self.horizontalSlider_000.setMaximum(99)
            self.horizontalSlider_000.setValue(10)
            self.label_000.setText("Tempo des Spielcharachters")
            self.textBrowser_007_bg.setStyleSheet("background-color:rgb(255, 255, 102)")
            self.textBrowser_007_fg1.setStyleSheet("background-color:rgb(186, 218, 85)")
            self.textBrowser_007_fg2.setStyleSheet("background-color:rgb(186, 218, 85)")
            self.textBrowser_007_fg3.setStyleSheet("background-color:rgb(186, 218, 85)")
            self.textBrowser_007_fg4.setStyleSheet("background-color:rgb(186, 218, 85)")
            self.textBrowser_007_fg5.setStyleSheet("background-color:rgb(186, 218, 85)")
            self.textBrowser_007_fg6.setStyleSheet("background-color:rgb(186, 218, 85)")
            self.textBrowser_007_fg7.setStyleSheet("background-color:rgb(186, 218, 85)")
            self.textBrowser_007_fg8.setStyleSheet("background-color:rgb(186, 218, 85)")

        if self.current_project_kind == "jumpnrunpixelart":
            #print("Jump'n Run: " + self.current_project_kind)
            self.horizontalSlider_000.setMinimum(0)
            self.horizontalSlider_000.setMaximum(99)
            self.horizontalSlider_000.setValue(10)
            self.label_000.setText("Tempo des Spielcharachters")
            self.textBrowser_007_bg.setStyleSheet("background-color:rgb(255, 255, 0)")
            self.textBrowser_007_fg1.setStyleSheet("background-color:rgb(80, 240, 30)")
            self.textBrowser_007_fg2.setStyleSheet("background-color:rgb(80, 240, 30)")
            self.textBrowser_007_fg3.setStyleSheet("background-color:rgb(80, 240, 30)")
            self.textBrowser_007_fg4.setStyleSheet("background-color:rgb(80, 240, 30)")
            self.textBrowser_007_fg5.setStyleSheet("background-color:rgb(80, 240, 30)")
            self.textBrowser_007_fg6.setStyleSheet("background-color:rgb(80, 240, 30)")
            self.textBrowser_007_fg7.setStyleSheet("background-color:rgb(80, 240, 30)")
            self.textBrowser_007_fg8.setStyleSheet("background-color:rgb(80, 240, 30)")

        if self.current_project_kind == "tetrismodern":
            #print("Tetris: " + self.current_project_kind)
            self.horizontalSlider_000.setMinimum(1000)
            self.horizontalSlider_000.setMaximum(100000)
            self.horizontalSlider_000.setValue(30000)
            self.label_000.setText("Rythmuslänge der Geschwindigkeitswechsel")
            self.comboBox_000.hide()
            self.label_001.hide()
            self.label_002.hide()
            self.label_003.hide()
            self.label_004.hide()
            self.horizontalSlider_001.hide()
            self.horizontalSlider_002.hide()
            self.horizontalSlider_003.hide()
            self.label_005.hide()
            self.textBrowser_007_bg.hide()
            self.textBrowser_007_fg1.hide()
            self.textBrowser_007_fg2.hide()
            self.textBrowser_007_fg3.hide()
            self.textBrowser_007_fg4.hide()
            self.textBrowser_007_fg5.hide()
            self.textBrowser_007_fg6.hide()
            self.textBrowser_007_fg7.hide()
            self.textBrowser_007_fg8.hide()

        if self.current_project_kind == "tetrispixelart":
            #print("Tetris: " + self.current_project_kind)
            self.horizontalSlider_000.setMinimum(1000)
            self.horizontalSlider_000.setMaximum(100000)
            self.horizontalSlider_000.setValue(30000)
            self.label_000.setText("Rythmuslänge der Geschwindigkeitswechsel")
            self.comboBox_000.hide()
            self.label_001.hide()
            self.label_002.hide()
            self.label_003.hide()
            self.label_004.hide()
            self.horizontalSlider_001.hide()
            self.horizontalSlider_002.hide()
            self.horizontalSlider_003.hide()
            self.label_005.hide()
            self.textBrowser_007_bg.hide()
            self.textBrowser_007_fg1.hide()
            self.textBrowser_007_fg2.hide()
            self.textBrowser_007_fg3.hide()
            self.textBrowser_007_fg4.hide()
            self.textBrowser_007_fg5.hide()
            self.textBrowser_007_fg6.hide()
            self.textBrowser_007_fg7.hide()
            self.textBrowser_007_fg8.hide()

    def custom1_hs_value(self):

        if self.current_project_kind == "jumpnrunmodern":
            game_project = open("('jumpnrun', 'modern')", "r")
            game_project_code = game_project.read()
            self.custom1_velocity = self.horizontalSlider_000.value()
            ##print(self.custom1_velocity)
            #self.current_project_code = "velocity = " + str(self.custom1_velocity) + game_project_code
            if self.custom1_velocity < 11:
                assessment = "langsam"
            if self.custom1_velocity > 10 and self.custom1_velocity < 50:
                assessment = "schnell"
            if self.custom1_velocity > 49:
                assessment = "extrem schnell"
            self.label_000.setText("Tempo des Spielcharachters " + "(" + str(self.custom1_velocity) + "), " + assessment)
        if self.current_project_kind == "jumpnrunpixelart":
            game_project = open("('jumpnrun', 'pixelart')", "r")
            game_project_code = game_project.read()
            self.custom1_velocity = self.horizontalSlider_000.value()
            ##print(self.custom1_velocity)
            #self.current_project_code = "velocity = " + str(self.custom1_velocity) + game_project_code
            if self.custom1_velocity < 11:
                assessment = "langsam"
            if self.custom1_velocity > 10 and self.custom1_velocity < 50:
                assessment = "schnell"
            if self.custom1_velocity > 49:
                assessment = "extrem schnell"
            self.label_000.setText("Tempo des Spielcharachters " + "(" + str(self.custom1_velocity) + "), " + assessment)

        if self.current_project_kind == "jumpnrunpixelart" or self.current_project_kind == "jumpnrunmodern":
            w_line0 = "velocity = " + str(self.custom1_velocity)
            w_line1 = "hob1, le1, wi1 = " + str(self.write_hob1) + ", " + str(self.write_le1) + ", " + str(
                self.write_wi1)
            w_line2 = "hob2, le2, wi2 = " + str(self.write_hob2) + ", " + str(self.write_le2) + ", " + str(
                self.write_wi2)
            w_line3 = "hob3, le3, wi3 = " + str(self.write_hob3) + ", " + str(self.write_le3) + ", " + str(
                self.write_wi3)
            w_line4 = "hob4, le4, wi4 = " + str(self.write_hob4) + ", " + str(self.write_le4) + ", " + str(
                self.write_wi4)
            w_line5 = "hob5, le5, wi5 = " + str(self.write_hob5) + ", " + str(self.write_le5) + ", " + str(
                self.write_wi5)
            w_line6 = "hob6, le6, wi6 = " + str(self.write_hob6) + ", " + str(self.write_le6) + ", " + str(
                self.write_wi6)
            w_line7 = "hob7, le7, wi7 = " + str(self.write_hob7) + ", " + str(self.write_le7) + ", " + str(
                self.write_wi7)
            w_line8 = "hob8, le8, wi8 = " + str(self.write_hob8) + ", " + str(self.write_le8) + ", " + str(
                self.write_wi8)

            w_line9 = "hob9, le9, wi9 = " + str(self.write_hob1) + ", " + str(self.write_le1) + ", " + str(
                self.write_wi1)
            w_line10 = "hob10, le10, wi10 = " + str(self.write_hob2) + ", " + str(self.write_le2) + ", " + str(
                self.write_wi2)
            w_line11 = "hob11, le11, wi11 = " + str(self.write_hob3) + ", " + str(self.write_le3) + ", " + str(
                self.write_wi3)
            w_line12 = "hob12, le12, wi12 = " + str(self.write_hob4) + ", " + str(self.write_le4) + ", " + str(
                self.write_wi4)
            w_line13 = "hob13, le13, wi13 = " + str(self.write_hob5) + ", " + str(self.write_le5) + ", " + str(
                self.write_wi5)
            w_line14 = "hob14, le14, wi14 = " + str(self.write_hob6) + ", " + str(self.write_le6) + ", " + str(
                self.write_wi6)
            w_line15 = "hob15, le15, wi15 = " + str(self.write_hob7) + ", " + str(self.write_le7) + ", " + str(
                self.write_wi7)
            w_line16 = "hob16, le16, wi16 = " + str(self.write_hob8) + ", " + str(self.write_le8) + ", " + str(
                self.write_wi8)

            w_line17 = "hob17, le17, wi17 = " + str(self.write_hob1) + ", " + str(self.write_le1) + ", " + str(
                self.write_wi1)
            w_line18 = "hob18, le18, wi18 = " + str(self.write_hob2) + ", " + str(self.write_le2) + ", " + str(
                self.write_wi2)
            w_line19 = "hob19, le19, wi19 = " + str(self.write_hob3) + ", " + str(self.write_le3) + ", " + str(
                self.write_wi3)
            w_line20 = "hob20, le20, wi20 = " + str(self.write_hob4) + ", " + str(self.write_le4) + ", " + str(
                self.write_wi4)
            w_line21 = "hob21, le21, wi21 = " + str(self.write_hob5) + ", " + str(self.write_le5) + ", " + str(
                self.write_wi5)
            w_line22 = "hob22, le22, wi22 = " + str(self.write_hob6) + ", " + str(self.write_le6) + ", " + str(
                self.write_wi6)
            w_line23 = "hob23, le23, wi23 = " + str(self.write_hob7) + ", " + str(self.write_le7) + ", " + str(
                self.write_wi7)
            w_line24 = "hob24, le24, wi24 = " + str(self.write_hob8) + ", " + str(self.write_le8) + ", " + str(
                self.write_wi8)

            w_line25 = "hob25, le25, wi25 = " + str(self.write_hob1) + ", " + str(self.write_le1) + ", " + str(
                self.write_wi1)
            w_line26 = "hob26, le26, wi26 = " + str(self.write_hob2) + ", " + str(self.write_le2) + ", " + str(
                self.write_wi2)
            w_line27 = "hob27, le27, wi27 = " + str(self.write_hob3) + ", " + str(self.write_le3) + ", " + str(
                self.write_wi3)
            w_line28 = "hob28, le28, wi28 = " + str(self.write_hob4) + ", " + str(self.write_le4) + ", " + str(
                self.write_wi4)
            w_line29 = "hob29, le29, wi29 = " + str(self.write_hob5) + ", " + str(self.write_le5) + ", " + str(
                self.write_wi5)
            w_line30 = "hob30, le30, wi30 = " + str(self.write_hob6) + ", " + str(self.write_le6) + ", " + str(
                self.write_wi6)
            w_line31 = "hob31, le31, wi31 = " + str(self.write_hob7) + ", " + str(self.write_le7) + ", " + str(
                self.write_wi7)
            w_line32 = "hob32, le32, wi32 = " + str(self.write_hob8) + ", " + str(self.write_le8) + ", " + str(
                self.write_wi8)

            w_lines_0_8_package1 = w_line0 + "\n" + w_line1 + "\n" + w_line2 + "\n" + w_line3 + "\n" + w_line4 + "\n" + w_line5 + "\n" + w_line6 + "\n" + w_line7 + "\n" + w_line8

            w_lines_9_16_package2 = w_line9 + "\n" + w_line10 + "\n" + w_line11 + "\n" + w_line12 + "\n" + w_line13 + "\n" + w_line14 + "\n" + w_line15 + "\n" + w_line16

            w_lines_17_24_package3 = w_line17 + "\n" + w_line18 + "\n" + w_line19 + "\n" + w_line20 + "\n" + w_line21 + "\n" + w_line22 + "\n" + w_line23 + "\n" + w_line24

            w_lines_25_32_package4 = w_line25 + "\n" + w_line26 + "\n" + w_line27 + "\n" + w_line28 + "\n" + w_line29 + "\n" + w_line30 + "\n" + w_line31 + "\n" + w_line32

            # #print(w_lines_0_8_package1 + "\n" + w_lines_9_16_package2 + "\n" + w_lines_17_24_package3 + "\n" + w_lines_25_32_package4)

            self.current_project_code = w_lines_0_8_package1 + "\n" + w_lines_9_16_package2 + "\n" + w_lines_17_24_package3 + "\n" + w_lines_25_32_package4 + "\n" + game_project_code

        if self.current_project_kind == "tetrismodern":
            game_project = open("('tetris', 'modern')", "r")
            game_project_code = game_project.read()
            self.custom1_velocity = self.horizontalSlider_000.value()
            #print(self.custom1_velocity)
            self.current_project_code = "velocity = " + str(self.custom1_velocity) + game_project_code
            if self.custom1_velocity < 11000:
                assessment = "schneller Wechsel"
            if self.custom1_velocity > 10000 and self.custom1_velocity < 50000:
                assessment = "mäßig schneller Wechsel"
            if self.custom1_velocity > 49000:
                assessment = "langsamer Wechsel"
            self.label_000.setText("Rythmuslänge der Geschwindigkeitswechsel " + "(" + str(self.custom1_velocity) + "ms), " + assessment)
        if self.current_project_kind == "tetrispixelart":
            game_project = open("('tetris', 'pixelart')", "r")
            game_project_code = game_project.read()
            self.custom1_velocity = self.horizontalSlider_000.value()
            #print(self.custom1_velocity)
            self.current_project_code = "velocity = " + str(self.custom1_velocity) + game_project_code
            if self.custom1_velocity < 11000:
                assessment = "schneller Wechsel"
            if self.custom1_velocity > 10000 and self.custom1_velocity < 50000:
                assessment = "mäßig schneller Wechsel"
            if self.custom1_velocity > 49000:
                assessment = "langsamer Wechsel"
            self.label_000.setText("Rythmuslänge der Geschwindigkeitswechsel " + "(" + str(self.custom1_velocity) + "ms), " + assessment)

    def custom1_hs_value_changed(self):
        ##print(self.horizontalSlider_000.value())
        if self.current_project_kind == "jumpnrunmodern":
            self.custom1_velocity = self.horizontalSlider_000.value()
            ##print(self.custom1_velocity)
            if self.custom1_velocity < 11:
                assessment = "langsam"
            if self.custom1_velocity > 10 and self.custom1_velocity < 50:
                assessment = "schnell"
            if self.custom1_velocity > 49:
                assessment = "extrem schnell"
            self.label_000.setText("Tempo des Spielcharachters " + "(" + str(self.custom1_velocity) + "), " + assessment)
        if self.current_project_kind == "jumpnrunpixelart":
            self.custom1_velocity = self.horizontalSlider_000.value()
            ##print(self.custom1_velocity)
            if self.custom1_velocity < 11:
                assessment = "langsam"
            if self.custom1_velocity > 10 and self.custom1_velocity < 50:
                assessment = "schnell"
            if self.custom1_velocity > 49:
                assessment = "extrem schnell"
            self.label_000.setText("Tempo des Spielcharachters " + "(" + str(self.custom1_velocity) + "), " + assessment)
        if self.current_project_kind == "tetrismodern":
            self.custom1_velocity = self.horizontalSlider_000.value()
            ##print(self.custom1_velocity)
            if self.custom1_velocity < 11000:
                assessment = "schneller Wechsel"
            if self.custom1_velocity > 10000 and self.custom1_velocity < 50000:
                assessment = "mäßig schneller Wechsel"
            if self.custom1_velocity > 49000:
                assessment = "langsamer Wechsel"
            self.label_000.setText("Rythmuslänge der Geschwindigkeitswechsel " + "(" + str(self.custom1_velocity) + "ms), " + assessment)
        if self.current_project_kind == "tetrispixelart":
            self.custom1_velocity = self.horizontalSlider_000.value()
            ##print(self.custom1_velocity)
            if self.custom1_velocity < 11000:
                assessment = "schneller Wechsel"
            if self.custom1_velocity > 10000 and self.custom1_velocity < 50000:
                assessment = "mäßig schneller Wechsel"
            if self.custom1_velocity > 49000:
                assessment = "langsamer Wechsel"
            self.label_000.setText("Rythmuslänge der Geschwindigkeitswechsel " + "(" + str(self.custom1_velocity) + "ms), " + assessment)

    def custom1_cb_barrier_changed(self):
        #print(self.comboBox_000.currentIndex())
        self.current_barrier = self.comboBox_000.currentIndex() + 1
        #print(self.current_barrier)
        #self.write_hob1, self.write_le1, self.write_wi1 = 50, 100, 30

        if self.current_barrier == 1:
            self.horizontalSlider_001.setValue(self.write_hob1)
            self.horizontalSlider_002.setValue(self.write_le1)
            self.horizontalSlider_003.setValue(self.write_wi1)

        if self.current_barrier == 2:
            self.horizontalSlider_001.setValue(self.write_hob2)
            self.horizontalSlider_002.setValue(self.write_le2)
            self.horizontalSlider_003.setValue(self.write_wi2)

        if self.current_barrier == 3:
            self.horizontalSlider_001.setValue(self.write_hob3)
            self.horizontalSlider_002.setValue(self.write_le3)
            self.horizontalSlider_003.setValue(self.write_wi3)

        if self.current_barrier == 4:
            self.horizontalSlider_001.setValue(self.write_hob4)
            self.horizontalSlider_002.setValue(self.write_le4)
            self.horizontalSlider_003.setValue(self.write_wi4)

        if self.current_barrier == 5:
            self.horizontalSlider_001.setValue(self.write_hob5)
            self.horizontalSlider_002.setValue(self.write_le5)
            self.horizontalSlider_003.setValue(self.write_wi5)

        if self.current_barrier == 6:
            self.horizontalSlider_001.setValue(self.write_hob6)
            self.horizontalSlider_002.setValue(self.write_le6)
            self.horizontalSlider_003.setValue(self.write_wi6)

        if self.current_barrier == 7:
            self.horizontalSlider_001.setValue(self.write_hob7)
            self.horizontalSlider_002.setValue(self.write_le7)
            self.horizontalSlider_003.setValue(self.write_wi7)

        if self.current_barrier == 8:
            self.horizontalSlider_001.setValue(self.write_hob8)
            self.horizontalSlider_002.setValue(self.write_le8)
            self.horizontalSlider_003.setValue(self.write_wi8)

    def custom1_hs001_value_changed(self):
        ##print(self.horizontalSlider_001.value())

        if self.current_barrier == 1:
            self.preview_hob1 = 686 - self.horizontalSlider_001.value() // 5
            self.write_hob1 = self.horizontalSlider_001.value()
            ##print(self.preview_hob1)
            self.textBrowser_007_fg1.setGeometry(70, self.preview_hob1, self.preview_le1, self.preview_wi1)
            # 686 = 470 + 216, untere Kante des "Fensterns", 100 / 5 = 20, 30 / 5 = 6, 50 / 5 = 10, also 686 - 10 <- Höhe überm Boden

        if self.current_barrier == 2:
            self.preview_hob2 = 686 - self.horizontalSlider_001.value() // 5
            self.write_hob2 = self.horizontalSlider_001.value()
            self.textBrowser_007_fg2.setGeometry(self.preview_dfe2, self.preview_hob2, self.preview_le2, self.preview_wi2)

        if self.current_barrier == 3:
            self.preview_hob3 = 686 - self.horizontalSlider_001.value() // 5
            self.write_hob3 = self.horizontalSlider_001.value()
            self.textBrowser_007_fg3.setGeometry(self.preview_dfe3, self.preview_hob3, self.preview_le3, self.preview_wi3)

        if self.current_barrier == 4:
            self.preview_hob4 = 686 - self.horizontalSlider_001.value() // 5
            self.write_hob4 = self.horizontalSlider_001.value()
            self.textBrowser_007_fg4.setGeometry(self.preview_dfe4, self.preview_hob4, self.preview_le4, self.preview_wi4)

        if self.current_barrier == 5:
            self.preview_hob5 = 686 - self.horizontalSlider_001.value() // 5
            self.write_hob5 = self.horizontalSlider_001.value()
            self.textBrowser_007_fg5.setGeometry(self.preview_dfe5, self.preview_hob5, self.preview_le5, self.preview_wi5)

        if self.current_barrier == 6:
            self.preview_hob6 = 686 - self.horizontalSlider_001.value() // 5
            self.write_hob6 = self.horizontalSlider_001.value()
            self.textBrowser_007_fg6.setGeometry(self.preview_dfe6, self.preview_hob6, self.preview_le6, self.preview_wi6)

        if self.current_barrier == 7:
            self.preview_hob7 = 686 - self.horizontalSlider_001.value() // 5
            self.write_hob7 = self.horizontalSlider_001.value()
            self.textBrowser_007_fg7.setGeometry(self.preview_dfe7, self.preview_hob7, self.preview_le7, self.preview_wi7)

        if self.current_barrier == 8:
            self.preview_hob8 = 686 - self.horizontalSlider_001.value() // 5
            self.write_hob8 = self.horizontalSlider_001.value()
            self.textBrowser_007_fg8.setGeometry(self.preview_dfe8, self.preview_hob8, self.preview_le8, self.preview_wi8)

    def custom1_hs001_003_value(self):
        #print(self.horizontalSlider_001.value())

        if self.current_project_kind == "jumpnrunmodern":
            game_project = open("('jumpnrun', 'modern')", "r")
            game_project_code = game_project.read()
        if self.current_project_kind == "jumpnrunpixelart":
            game_project = open("('jumpnrun', 'pixelart')", "r")
            game_project_code = game_project.read()

        w_line0 = "velocity = " + str(self.horizontalSlider_000.value())
        w_line1 = "hob1, le1, wi1 = " + str(self.write_hob1) + ", " + str(self.write_le1) + ", " + str(self.write_wi1)
        w_line2 = "hob2, le2, wi2 = " + str(self.write_hob2) + ", " + str(self.write_le2) + ", " + str(self.write_wi2)
        w_line3 = "hob3, le3, wi3 = " + str(self.write_hob3) + ", " + str(self.write_le3) + ", " + str(self.write_wi3)
        w_line4 = "hob4, le4, wi4 = " + str(self.write_hob4) + ", " + str(self.write_le4) + ", " + str(self.write_wi4)
        w_line5 = "hob5, le5, wi5 = " + str(self.write_hob5) + ", " + str(self.write_le5) + ", " + str(self.write_wi5)
        w_line6 = "hob6, le6, wi6 = " + str(self.write_hob6) + ", " + str(self.write_le6) + ", " + str(self.write_wi6)
        w_line7 = "hob7, le7, wi7 = " + str(self.write_hob7) + ", " + str(self.write_le7) + ", " + str(self.write_wi7)
        w_line8 = "hob8, le8, wi8 = " + str(self.write_hob8) + ", " + str(self.write_le8) + ", " + str(self.write_wi8)

        w_line9 = "hob9, le9, wi9 = " + str(self.write_hob1) + ", " + str(self.write_le1) + ", " + str(self.write_wi1)
        w_line10 = "hob10, le10, wi10 = " + str(self.write_hob2) + ", " + str(self.write_le2) + ", " + str(self.write_wi2)
        w_line11 = "hob11, le11, wi11 = " + str(self.write_hob3) + ", " + str(self.write_le3) + ", " + str(self.write_wi3)
        w_line12 = "hob12, le12, wi12 = " + str(self.write_hob4) + ", " + str(self.write_le4) + ", " + str(self.write_wi4)
        w_line13 = "hob13, le13, wi13 = " + str(self.write_hob5) + ", " + str(self.write_le5) + ", " + str(self.write_wi5)
        w_line14 = "hob14, le14, wi14 = " + str(self.write_hob6) + ", " + str(self.write_le6) + ", " + str(self.write_wi6)
        w_line15 = "hob15, le15, wi15 = " + str(self.write_hob7) + ", " + str(self.write_le7) + ", " + str(self.write_wi7)
        w_line16 = "hob16, le16, wi16 = " + str(self.write_hob8) + ", " + str(self.write_le8) + ", " + str(self.write_wi8)

        w_line17 = "hob17, le17, wi17 = " + str(self.write_hob1) + ", " + str(self.write_le1) + ", " + str(self.write_wi1)
        w_line18 = "hob18, le18, wi18 = " + str(self.write_hob2) + ", " + str(self.write_le2) + ", " + str(self.write_wi2)
        w_line19 = "hob19, le19, wi19 = " + str(self.write_hob3) + ", " + str(self.write_le3) + ", " + str(self.write_wi3)
        w_line20 = "hob20, le20, wi20 = " + str(self.write_hob4) + ", " + str(self.write_le4) + ", " + str(self.write_wi4)
        w_line21 = "hob21, le21, wi21 = " + str(self.write_hob5) + ", " + str(self.write_le5) + ", " + str(self.write_wi5)
        w_line22 = "hob22, le22, wi22 = " + str(self.write_hob6) + ", " + str(self.write_le6) + ", " + str(self.write_wi6)
        w_line23 = "hob23, le23, wi23 = " + str(self.write_hob7) + ", " + str(self.write_le7) + ", " + str(self.write_wi7)
        w_line24 = "hob24, le24, wi24 = " + str(self.write_hob8) + ", " + str(self.write_le8) + ", " + str(self.write_wi8)

        w_line25 = "hob25, le25, wi25 = " + str(self.write_hob1) + ", " + str(self.write_le1) + ", " + str(self.write_wi1)
        w_line26 = "hob26, le26, wi26 = " + str(self.write_hob2) + ", " + str(self.write_le2) + ", " + str(self.write_wi2)
        w_line27 = "hob27, le27, wi27 = " + str(self.write_hob3) + ", " + str(self.write_le3) + ", " + str(self.write_wi3)
        w_line28 = "hob28, le28, wi28 = " + str(self.write_hob4) + ", " + str(self.write_le4) + ", " + str(self.write_wi4)
        w_line29 = "hob29, le29, wi29 = " + str(self.write_hob5) + ", " + str(self.write_le5) + ", " + str(self.write_wi5)
        w_line30 = "hob30, le30, wi30 = " + str(self.write_hob6) + ", " + str(self.write_le6) + ", " + str(self.write_wi6)
        w_line31 = "hob31, le31, wi31 = " + str(self.write_hob7) + ", " + str(self.write_le7) + ", " + str(self.write_wi7)
        w_line32 = "hob32, le32, wi32 = " + str(self.write_hob8) + ", " + str(self.write_le8) + ", " + str(self.write_wi8)

        w_lines_0_8_package1 = w_line0  + "\n" + w_line1  + "\n" + w_line2  + "\n" +  w_line3  + "\n" +  w_line4  + "\n" +  w_line5  + "\n" + w_line6  + "\n" +  w_line7  + "\n" +  w_line8

        w_lines_9_16_package2 = w_line9 + "\n" + w_line10 + "\n" + w_line11 + "\n" + w_line12 + "\n" + w_line13 + "\n" + w_line14 + "\n" + w_line15 + "\n" + w_line16

        w_lines_17_24_package3 = w_line17 + "\n" + w_line18 + "\n" + w_line19 + "\n" + w_line20 + "\n" + w_line21 + "\n" + w_line22 + "\n" + w_line23 + "\n" + w_line24

        w_lines_25_32_package4 = w_line25 + "\n" + w_line26 + "\n" + w_line27 + "\n" + w_line28 + "\n" + w_line29 + "\n" + w_line30 + "\n" + w_line31 + "\n" + w_line32

        ##print(w_lines_0_8_package1 + "\n" + w_lines_9_16_package2 + "\n" + w_lines_17_24_package3 + "\n" + w_lines_25_32_package4)

        self.current_project_code = w_lines_0_8_package1 + "\n" + w_lines_9_16_package2 + "\n" + w_lines_17_24_package3 + "\n" + w_lines_25_32_package4 + "\n" + game_project_code

    def custom1_hs002_value_changed(self):
        ##print(self.horizontalSlider_002.value())

        if self.current_barrier == 1:
            self.preview_le1 = self.horizontalSlider_002.value() // 5
            self.write_le1 = self.horizontalSlider_002.value()
            ##print(self.preview_le1)
            self.textBrowser_007_fg1.setGeometry(70, self.preview_hob1, self.preview_le1, self.preview_wi1)
            # 686 = 470 + 216, untere Kante des "Fensterns", 100 / 5 = 20, 30 / 5 = 6, 50 / 5 = 10, also 10 <- Höhe überm Boden

        if self.current_barrier == 2:
            self.preview_le2 = self.horizontalSlider_002.value() // 5
            self.write_le2 = self.horizontalSlider_002.value()
            self.textBrowser_007_fg2.setGeometry(self.preview_dfe2, self.preview_hob2, self.preview_le2, self.preview_wi2)

        if self.current_barrier == 3:
            self.preview_le3 = self.horizontalSlider_002.value() // 5
            self.write_le3 = self.horizontalSlider_002.value()
            self.textBrowser_007_fg3.setGeometry(self.preview_dfe3, self.preview_hob3, self.preview_le3, self.preview_wi3)

        if self.current_barrier == 4:
            self.preview_le4 = self.horizontalSlider_002.value() // 5
            self.write_le4 = self.horizontalSlider_002.value()
            self.textBrowser_007_fg4.setGeometry(self.preview_dfe4, self.preview_hob4, self.preview_le4, self.preview_wi4)

        if self.current_barrier == 5:
            self.preview_le5 = self.horizontalSlider_002.value() // 5
            self.write_le5 = self.horizontalSlider_002.value()
            self.textBrowser_007_fg5.setGeometry(self.preview_dfe5, self.preview_hob5, self.preview_le5, self.preview_wi5)

        if self.current_barrier == 6:
            self.preview_le6 = self.horizontalSlider_002.value() // 5
            self.write_le6 = self.horizontalSlider_002.value()
            self.textBrowser_007_fg6.setGeometry(self.preview_dfe6, self.preview_hob6, self.preview_le6, self.preview_wi6)

        if self.current_barrier == 7:
            self.preview_le7 = self.horizontalSlider_002.value() // 5
            self.write_le7 = self.horizontalSlider_002.value()
            self.textBrowser_007_fg7.setGeometry(self.preview_dfe7, self.preview_hob7, self.preview_le7, self.preview_wi7)

        if self.current_barrier == 8:
            self.preview_le8 = self.horizontalSlider_002.value() // 5
            self.write_le8 = self.horizontalSlider_002.value()
            self.textBrowser_007_fg8.setGeometry(self.preview_dfe8, self.preview_hob8, self.preview_le8, self.preview_wi8)

    #def custom1_hs002_value(self):
        ##print(self.horizontalSlider_002.value())

    def custom1_hs003_value_changed(self):
        ##print(self.horizontalSlider_003.value())

        if self.current_barrier == 1:
            self.preview_wi1 = self.horizontalSlider_003.value() // 5
            self.write_wi1 = self.horizontalSlider_003.value()
            ##print(self.preview_wi1)
            self.textBrowser_007_fg1.setGeometry(70, self.preview_hob1, self.preview_le1, self.preview_wi1)
            # 686 = 470 + 216, untere Kante des "Fensterns", 100 / 5 = 20, 30 / 5 = 6, 50 / 5 = 10, also 10 <- Höhe überm Boden

        if self.current_barrier == 2:
            self.preview_wi2 = self.horizontalSlider_003.value() // 5
            self.write_wi2 = self.horizontalSlider_003.value()
            self.textBrowser_007_fg2.setGeometry(self.preview_dfe2, self.preview_hob2, self.preview_le2, self.preview_wi2)

        if self.current_barrier == 3:
            self.preview_wi3 = self.horizontalSlider_003.value() // 5
            self.write_wi3 = self.horizontalSlider_003.value()
            self.textBrowser_007_fg3.setGeometry(self.preview_dfe3, self.preview_hob3, self.preview_le3, self.preview_wi3)

        if self.current_barrier == 4:
            self.preview_wi4 = self.horizontalSlider_003.value() // 5
            self.write_wi4 = self.horizontalSlider_003.value()
            self.textBrowser_007_fg4.setGeometry(self.preview_dfe4, self.preview_hob4, self.preview_le4, self.preview_wi4)

        if self.current_barrier == 5:
            self.preview_wi5 = self.horizontalSlider_003.value() // 5
            self.write_wi5 = self.horizontalSlider_003.value()
            self.textBrowser_007_fg5.setGeometry(self.preview_dfe5, self.preview_hob5, self.preview_le5, self.preview_wi5)

        if self.current_barrier == 6:
            self.preview_wi6 = self.horizontalSlider_003.value() // 5
            self.write_wi6 = self.horizontalSlider_003.value()
            self.textBrowser_007_fg6.setGeometry(self.preview_dfe6, self.preview_hob6, self.preview_le6, self.preview_wi6)

        if self.current_barrier == 7:
            self.preview_wi7 = self.horizontalSlider_003.value() // 5
            self.write_wi7 = self.horizontalSlider_003.value()
            self.textBrowser_007_fg7.setGeometry(self.preview_dfe7, self.preview_hob7, self.preview_le7, self.preview_wi7)

        if self.current_barrier == 8:
            self.preview_wi8 = self.horizontalSlider_003.value() // 5
            self.write_wi8 = self.horizontalSlider_003.value()
            self.textBrowser_007_fg8.setGeometry(self.preview_dfe8, self.preview_hob8, self.preview_le8, self.preview_wi8)

    #def custom1_hs003_value(self):
        ##print(self.horizontalSlider_003.value())

    def custom1_hs_dfe(self):
        self.preview_dfe2 = 70 + self.preview_le1
        self.preview_dfe3 = 70 + self.preview_le1 + self.preview_le2
        self.preview_dfe4 = 70 + self.preview_le1 + self.preview_le2 + self.preview_le3
        self.preview_dfe5 = 70 + self.preview_le1 + self.preview_le2 + self.preview_le3 + self.preview_le4
        self.preview_dfe6 = 70 + self.preview_le1 + self.preview_le2 + self.preview_le3 + self.preview_le4 + self.preview_le5
        self.preview_dfe7 = 70 + self.preview_le1 + self.preview_le2 + self.preview_le3 + self.preview_le4 + self.preview_le5 + self.preview_le6
        self.preview_dfe8 = 70 + self.preview_le1 + self.preview_le2 + self.preview_le3 + self.preview_le4 + self.preview_le5 + self.preview_le6 + self.preview_le7

        self.textBrowser_007_fg2.setGeometry(self.preview_dfe2, self.preview_hob2, self.preview_le2, self.preview_wi2)
        self.textBrowser_007_fg3.setGeometry(self.preview_dfe3, self.preview_hob3, self.preview_le3, self.preview_wi3)
        self.textBrowser_007_fg4.setGeometry(self.preview_dfe4, self.preview_hob4, self.preview_le4, self.preview_wi4)
        self.textBrowser_007_fg5.setGeometry(self.preview_dfe5, self.preview_hob5, self.preview_le5, self.preview_wi5)
        self.textBrowser_007_fg6.setGeometry(self.preview_dfe6, self.preview_hob6, self.preview_le6, self.preview_wi6)
        self.textBrowser_007_fg7.setGeometry(self.preview_dfe7, self.preview_hob7, self.preview_le7, self.preview_wi7)
        self.textBrowser_007_fg8.setGeometry(self.preview_dfe8, self.preview_hob8, self.preview_le8, self.preview_wi8)

    def custom1_save(self):
        #print("CS")
        F_000 = open("projects/" + self.current_item, "w")
        F_000.write(self.current_project_code)


    def custom1_code_show(self):
        #print("C1CS")
        self.textBrowser_006.show()
        self.pushButton_010.show()
        self.textBrowser_006.setText(self.current_project_code)

    def custom1_menue_close(self):
        self.pushButton_008.hide()
        self.pushButton_009.hide()
        self.textBrowser_005.hide()
        self.horizontalSlider_000.hide()
        self.label_000.hide()
        self.toolButton_002.hide()
        self.pushButton_008_.hide()
        self.comboBox_000.hide()
        self.label_001.hide()
        self.label_002.hide()
        self.label_003.hide()
        self.label_004.hide()
        self.horizontalSlider_001.hide()
        self.horizontalSlider_002.hide()
        self.horizontalSlider_003.hide()
        self.label_005.hide()
        self.textBrowser_007_bg.hide()
        self.textBrowser_007_bg.hide()
        self.textBrowser_007_fg1.hide()
        self.textBrowser_007_fg2.hide()
        self.textBrowser_007_fg3.hide()
        self.textBrowser_007_fg4.hide()
        self.textBrowser_007_fg5.hide()
        self.textBrowser_007_fg6.hide()
        self.textBrowser_007_fg7.hide()
        self.textBrowser_007_fg8.hide()
        self.toolButton_3.show()
        self.toolButton_4.show()
        self.listWidget.show()

    def close_show_code_001(self):
        self.textBrowser_006.hide()
        self.pushButton_010.hide()
        self.current_project_code = self.textBrowser_006.toPlainText()
        #print(self.current_project_code)

    def change_to_p_BYG_y(self):
        #print("CTPY")
        custom1_game_project_saved = open("projects/" + self.current_item, "r")
        current_saved_project_code = custom1_game_project_saved.read()
        #print(current_saved_project_code)
        F_001 = open("projects/" + self.current_item + ".py", "w")
        F_001.write(current_saved_project_code)

    def change_installtion_byg_path(self):
        #C:/Users/Jonas/Documents/pythonscripts/Build.Your.Game/
        self.lineEdit.show()
        self.pushButton_03.show()
        self.pushButton_4.hide()
        self.pushButton_3.hide()
        self.toolButton_2.hide()
        self.textBrowser_3.setHtml(("<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                            "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                            "p, li { white-space: pre-wrap; }\n"
                                            "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
                                            "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:48pt;\">Installationspfad ändern</span></p>\n"))

    def change_installtion_byg_path_write(self):
        F_4 = open("byg_insta_BYG_lation_path_byg", "w")
        F_4.write(self.lineEdit.text())
        self.pushButton_4.show()
        self.pushButton_3.show()
        self.toolButton_2.show()
        self.lineEdit.hide()
        self.pushButton_03.hide()
        self.textBrowser_3.setHtml((
                                    "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                    "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                    "p, li { white-space: pre-wrap; }\n"
                                    "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
                                    "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:48pt;\">Build.Your.Game ist eine Open Source GameEngine für Jedermann.</span></p>\n"
                                    "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:48pt;\">Entwickelt wurde sie von </span><a href=\"https://www.youtube.com/channel/UCANAe4mkm2vCSdA22uqZ4qA\"><span style=\" font-size:48pt; text-decoration: underline; color:#0000ff;\">RoJoSciences</span></a><span style=\" font-size:48pt;\">.</span></p>\n"
                                    "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:48pt;\">Version 1.2.3 Beta</span></p>\n"
                                    "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:48pt;\">Release: 22.11.2020</span></p></body></html>"))
        self.instalation_path_byg = self.lineEdit.text()

    # build_menue_functions

    def path(self, Form):
        #print(self.step)

        if self.step == 1:
            self.textBrowser_4.setHtml((
                "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                "p, li { white-space: pre-wrap; }\n"
                "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
                "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:36pt; font-weight:600;\">Grafik: Pixel-Art oder modern?</span></p></body></html>"))

            self.pushButton_6.setText("Pixel-Art")
            self.pushButton_7.setText("Modern")

        if self.step == 2:
            self.textBrowser_4.setHtml((
                "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                "p, li { white-space: pre-wrap; }\n"
                "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
                "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:36pt; font-weight:600;\">Dein Spiel wird ertstellt, dies kann eineige Minuten in Ansrpuch nehmen!</span></p></body></html>"))

            self.pushButton_6.setText("")
            self.pushButton_6.hide()
            self.pushButton_7.setText("")
            self.pushButton_7.hide()
            self.progressBar.show()

            self.comboBox_build1_0 = QtWidgets.QComboBox(Form)
            self.comboBox_build1_0.move(60, 240)
            self.comboBox_build1_0.addItems(
                ["Baustein 1", "Baustein2", "Baustein 3", "Baustein 4", "Baustein 5", "Baustein 6", "Baustein 7",
                 "Baustein 8"])
            self.comboBox_build1_0.currentIndexChanged.connect(self.build1_cb_barrier_changed)

            self.label_build1_1 = QtWidgets.QLabel(Form)
            self.label_build1_1.setGeometry(QtCore.QRect(60, 210, 370, 21))
            self.label_build1_1.setObjectName("labelbuild1_1")
            self.label_build1_1.setText("Level ändern")

            self.label_build1_2 = QtWidgets.QLabel(Form)
            self.label_build1_2.setGeometry(QtCore.QRect(60, 270, 370, 21))
            self.label_build1_2.setObjectName("labelbuild1_2")
            self.label_build1_2.setText("Höhe über dem Boden")

            self.label_build1_3 = QtWidgets.QLabel(Form)
            self.label_build1_3.setGeometry(QtCore.QRect(60, 330, 370, 21))
            self.label_build1_3.setObjectName("labelbuild1_3")
            self.label_build1_3.setText("Länge")

            self.label_build1_4 = QtWidgets.QLabel(Form)
            self.label_build1_4.setGeometry(QtCore.QRect(60, 390, 370, 21))
            self.label_build1_4.setObjectName("labelbuild1_4")
            self.label_build1_4.setText("Breite")

            self.horizontalSlider_build1_1 = QtWidgets.QSlider(Form)
            self.horizontalSlider_build1_1.setGeometry(QtCore.QRect(60, 295, 221, 31))
            self.horizontalSlider_build1_1.setMinimum(1)
            self.horizontalSlider_build1_1.setMaximum(1079)
            self.horizontalSlider_build1_1.setValue(50)
            self.horizontalSlider_build1_1.setOrientation(QtCore.Qt.Horizontal)
            self.horizontalSlider_build1_1.setObjectName("horizontalSlider_build1_1")
            self.horizontalSlider_build1_1.valueChanged.connect(self.build1_hsbuild1_1_value_changed)
            self.horizontalSlider_build1_1.valueChanged.connect(self.build1_hs_dfe)
            self.horizontalSlider_build1_1.sliderReleased.connect(self.build1_hsbuild1_1_build1_3_value)
            #self.horizontalSlider_build1_1.hide()

            self.horizontalSlider_build1_2 = QtWidgets.QSlider(Form)
            self.horizontalSlider_build1_2.setGeometry(QtCore.QRect(60, 355, 221, 31))
            self.horizontalSlider_build1_2.setMinimum(5)
            self.horizontalSlider_build1_2.setMaximum(150)
            self.horizontalSlider_build1_2.setValue(100)
            self.horizontalSlider_build1_2.setOrientation(QtCore.Qt.Horizontal)
            self.horizontalSlider_build1_2.setObjectName("horizontalSlider_build1_2")
            self.horizontalSlider_build1_2.valueChanged.connect(self.build1_hsbuild1_2_value_changed)
            self.horizontalSlider_build1_2.valueChanged.connect(self.build1_hs_dfe)
            self.horizontalSlider_build1_2.sliderReleased.connect(self.build1_hsbuild1_1_build1_3_value)
            #self.horizontalSlider_build1_2.hide()

            self.horizontalSlider_build1_3 = QtWidgets.QSlider(Form)
            self.horizontalSlider_build1_3.setGeometry(QtCore.QRect(60, 415, 221, 31))
            self.horizontalSlider_build1_3.setMinimum(5)
            self.horizontalSlider_build1_3.setMaximum(150)
            self.horizontalSlider_build1_3.setValue(30)
            self.horizontalSlider_build1_3.setOrientation(QtCore.Qt.Horizontal)
            self.horizontalSlider_build1_3.setObjectName("horizontalSlider_build1_3")
            self.horizontalSlider_build1_3.valueChanged.connect(self.build1_hsbuild1_3_value_changed)
            self.horizontalSlider_build1_3.valueChanged.connect(self.build1_hs_dfe)
            self.horizontalSlider_build1_3.sliderReleased.connect(self.build1_hsbuild1_1_build1_3_value)
            #self.horizontalSlider_build1_3.hide()

            self.label_build1_5 = QtWidgets.QLabel(Form)
            self.label_build1_5.setGeometry(QtCore.QRect(60, 440, 370, 21))
            self.label_build1_5.setObjectName("labelbuild1_5")
            self.label_build1_5.setText("Vorschau:")
           # self.label_build1_5.hide()

            # self.textBrowser_build1_7 = QtWidgets.QTextEdit(Form)
            self.textBrowser_build1_7_bg = QtWidgets.QTextBrowser(Form)
            self.textBrowser_build1_7_bg.setGeometry(QtCore.QRect(60, 470, 384, 216))
            # 1920 / 5 = 384, 1080 / 5 = 216
            self.textBrowser_build1_7_bg.setStyleSheet("background-color:black")
            self.textBrowser_build1_7_bg.setObjectName("textBrowserbuild1_7")
            #self.textBrowser_build1_7_bg.hide()

            self.textBrowser_build1_7_fg1 = QtWidgets.QTextBrowser(Form)
            self.textBrowser_build1_7_fg1.setGeometry(QtCore.QRect(70, 676, 20, 6))
            # 686 = 470 + 216, untere Kante des "Fensterns", 1build1_ / 5 = 20, 30 / 5 = 6, 50 / 5 = 10, also 686 - 10 <- Höhe überm Boden
            self.textBrowser_build1_7_fg1.setStyleSheet("background-color:black")
            #self.textBrowser_build1_7_fg1.hide()

            self.textBrowser_build1_7_fg2 = QtWidgets.QTextBrowser(Form)
            self.textBrowser_build1_7_fg2.setGeometry(QtCore.QRect(90, 666, 14, 8))
            self.textBrowser_build1_7_fg2.setStyleSheet("background-color:black")
            #self.textBrowser_build1_7_fg2.hide()

            self.textBrowser_build1_7_fg3 = QtWidgets.QTextBrowser(Form)
            self.textBrowser_build1_7_fg3.setGeometry(QtCore.QRect(104, 656, 24, 8))
            self.textBrowser_build1_7_fg3.setStyleSheet("background-color:black")
            #self.textBrowser_build1_7_fg3.hide()

            self.textBrowser_build1_7_fg4 = QtWidgets.QTextBrowser(Form)
            self.textBrowser_build1_7_fg4.setGeometry(QtCore.QRect(128, 646, 8, 4))
            self.textBrowser_build1_7_fg4.setStyleSheet("background-color:black")
            #self.textBrowser_build1_7_fg4.hide()

            self.textBrowser_build1_7_fg5 = QtWidgets.QTextBrowser(Form)
            self.textBrowser_build1_7_fg5.setGeometry(QtCore.QRect(136, 636, 4, 4))
            self.textBrowser_build1_7_fg5.setStyleSheet("background-color:black")
            #self.textBrowser_build1_7_fg5.hide()

            self.textBrowser_build1_7_fg5 = QtWidgets.QTextBrowser(Form)
            self.textBrowser_build1_7_fg5.setGeometry(QtCore.QRect(136, 636, 4, 4))
            self.textBrowser_build1_7_fg5.setStyleSheet("background-color:black")
            #self.textBrowser_build1_7_fg5.hide()

            self.textBrowser_build1_7_fg6 = QtWidgets.QTextBrowser(Form)
            self.textBrowser_build1_7_fg6.setGeometry(QtCore.QRect(140, 656, 16, 16))
            self.textBrowser_build1_7_fg6.setStyleSheet("background-color:black")
            #self.textBrowser_build1_7_fg6.hide()

            self.textBrowser_build1_7_fg7 = QtWidgets.QTextBrowser(Form)
            self.textBrowser_build1_7_fg7.setGeometry(QtCore.QRect(156, 666, 6, 8))
            self.textBrowser_build1_7_fg7.setStyleSheet("background-color:black")
            #self.textBrowser_build1_7_fg7.hide()

            self.textBrowser_build1_7_fg8 = QtWidgets.QTextBrowser(Form)
            self.textBrowser_build1_7_fg8.setGeometry(QtCore.QRect(162, 656, 24, 8))
            self.textBrowser_build1_7_fg8.setStyleSheet("background-color:black")
            #self.textBrowser_build1_7_fg8.hide()#

            self.comboBox_build1_0.show()
            self.label_build1_2.show()
            self.label_build1_3.show()
            self.label_build1_4.show()
            self.horizontalSlider_build1_1.show()
            self.horizontalSlider_build1_2.show()
            self.horizontalSlider_build1_3.show()
            self.label_build1_5.show()
            self.textBrowser_build1_7_bg.show()
            self.textBrowser_build1_7_fg1.show()
            self.textBrowser_build1_7_fg2.show()
            self.textBrowser_build1_7_fg3.show()
            self.textBrowser_build1_7_fg4.show()
            self.textBrowser_build1_7_fg5.show()
            self.textBrowser_build1_7_fg6.show()
            self.textBrowser_build1_7_fg7.show()
            self.textBrowser_build1_7_fg8.show()
            self.label_build1_6.show()
            self.lineEdit_build1.show()

            self.build1_write_hob1, self.build1_write_le1, self.build1_write_wi1 = 50, 100, 30
            self.build1_write_hob2, self.build1_write_le2, self.build1_write_wi2 = 100, 70, 40
            self.build1_write_hob3, self.build1_write_le3, self.build1_write_wi3 = 150, 120, 40
            self.build1_write_hob4, self.build1_write_le4, self.build1_write_wi4 = 200, 40, 20
            self.build1_write_hob5, self.build1_write_le5, self.build1_write_wi5 = 250, 20, 20
            self.build1_write_hob6, self.build1_write_le6, self.build1_write_wi6 = 150, 80, 80
            self.build1_write_hob7, self.build1_write_le7, self.build1_write_wi7 = 100, 30, 40
            self.build1_write_hob8, self.build1_write_le8, self.build1_write_wi8 = 150, 120, 40

            self.build1_preview_hob1, self.build1_preview_le1, self.build1_preview_wi1 = 676, 20, 6
            self.build1_preview_hob2, self.build1_preview_le2, self.build1_preview_wi2 = 666, 14, 8
            self.build1_preview_hob3, self.build1_preview_le3, self.build1_preview_wi3 = 656, 24, 8
            self.build1_preview_hob4, self.build1_preview_le4, self.build1_preview_wi4 = 646, 8, 4
            self.build1_preview_hob5, self.build1_preview_le5, self.build1_preview_wi5 = 636, 4, 4
            self.build1_preview_hob6, self.build1_preview_le6, self.build1_preview_wi6 = 656, 16, 16
            self.build1_preview_hob7, self.build1_preview_le7, self.build1_preview_wi7 = 666, 6, 8
            self.build1_preview_hob8, self.build1_preview_le8, self.build1_preview_wi8 = 656, 24, 8

            self.build1_preview_dfe2 = 70 + self.build1_preview_le1
            self.build1_preview_dfe3 = 70 + self.build1_preview_le1 + self.build1_preview_le2
            self.build1_preview_dfe4 = 70 + self.build1_preview_le1 + self.build1_preview_le2 + self.build1_preview_le3
            self.build1_preview_dfe5 = 70 + self.build1_preview_le1 + self.build1_preview_le2 + self.build1_preview_le3 + self.build1_preview_le4
            self.build1_preview_dfe6 = 70 + self.build1_preview_le1 + self.build1_preview_le2 + self.build1_preview_le3 + self.build1_preview_le4 + self.build1_preview_le5
            self.build1_preview_dfe7 = 70 + self.build1_preview_le1 + self.build1_preview_le2 + self.build1_preview_le3 + self.build1_preview_le4 + self.build1_preview_le5 + self.build1_preview_le6
            self.build1_preview_dfe8 = 70 + self.build1_preview_le1 + self.build1_preview_le2 + self.build1_preview_le3 + self.build1_preview_le4 + self.build1_preview_le5 + self.build1_preview_le6 + self.build1_preview_le7

            self.build1_current_barrier = 1
            self.comboBox_build1_0.setCurrentIndex(0)

            build1_default_values = open("jumpnrun_default_values", "r")
            self.jumpnrun_values = build1_default_values.read()

            #print(self.step1_selection, self.step2_selection)
            self.selection = self.step1_selection + self.step2_selection
            #print(self.selection)
            if self.selection == "jumpnrunmodern":
                self.pushButton_9.clicked.connect(self.build1_code_show_jumpnrun_modern)

                self.textBrowser_build1_7_bg.setStyleSheet("background-color:rgb(255, 255, 102)")
                self.textBrowser_build1_7_fg1.setStyleSheet("background-color:rgb(186, 218, 85)")
                self.textBrowser_build1_7_fg2.setStyleSheet("background-color:rgb(186, 218, 85)")
                self.textBrowser_build1_7_fg3.setStyleSheet("background-color:rgb(186, 218, 85)")
                self.textBrowser_build1_7_fg4.setStyleSheet("background-color:rgb(186, 218, 85)")
                self.textBrowser_build1_7_fg5.setStyleSheet("background-color:rgb(186, 218, 85)")
                self.textBrowser_build1_7_fg6.setStyleSheet("background-color:rgb(186, 218, 85)")
                self.textBrowser_build1_7_fg7.setStyleSheet("background-color:rgb(186, 218, 85)")
                self.textBrowser_build1_7_fg8.setStyleSheet("background-color:rgb(186, 218, 85)")

                date = time.gmtime()
                date1 = date[0], date[1], date[2]
                self.date1 = str(date1)

                F_2 = open("nofp_j_m", "r")
                n = F_2.read()
                self.ni = "0"
                if n != "0":
                    self.ni = n

                self.ni = int(n) + 1
                self.ni = str(self.ni)
                F_3 = open("nofp_j_m", "w")
                F_3.write(self.ni)

                self.lineEdit_build1.setText("Jump'n Run, Modern, " + self.date1)

            if self.selection == "jumpnrunpixelart":
                self.pushButton_9.clicked.connect(self.build1_code_show_jumpnrun_pixel_art)

                self.textBrowser_build1_7_bg.setStyleSheet("background-color:rgb(255, 255, 0)")
                self.textBrowser_build1_7_fg1.setStyleSheet("background-color:rgb(80, 240, 30)")
                self.textBrowser_build1_7_fg2.setStyleSheet("background-color:rgb(80, 240, 30)")
                self.textBrowser_build1_7_fg3.setStyleSheet("background-color:rgb(80, 240, 30)")
                self.textBrowser_build1_7_fg4.setStyleSheet("background-color:rgb(80, 240, 30)")
                self.textBrowser_build1_7_fg5.setStyleSheet("background-color:rgb(80, 240, 30)")
                self.textBrowser_build1_7_fg6.setStyleSheet("background-color:rgb(80, 240, 30)")
                self.textBrowser_build1_7_fg7.setStyleSheet("background-color:rgb(80, 240, 30)")
                self.textBrowser_build1_7_fg8.setStyleSheet("background-color:rgb(80, 240, 30)")

                date = time.gmtime()
                date1 = date[0], date[1], date[2]
                self.date1 = str(date1)

                F_2 = open("nofp_j_p", "r")
                n = F_2.read()
                self.ni = "0"
                if n != "0":
                    self.ni = n

                self.ni = int(n) + 1
                self.ni = str(self.ni)
                F_3 = open("nofp_j_p", "w")
                F_3.write(self.ni)

                self.lineEdit_build1.setText("Jump'n Run, Pixel Art, " + self.date1)

            if self.selection == "tetrismodern":
                self.pushButton_9.clicked.connect(self.build1_code_show_tetris_modern)

                date = time.gmtime()
                date1 = date[0], date[1], date[2]
                self.date1 = str(date1)

                F_2 = open("nofp_t_m", "r")
                n = F_2.read()
                self.ni = "0"
                if n != "0":
                    self.ni = n

                self.ni = int(n) + 1
                self.ni = str(self.ni)
                F_3 = open("nofp_t_m", "w")
                F_3.write(self.ni)

                self.lineEdit_build1.setText("Tetris, Modern, " + self.date1)

            if self.selection == "tetrispixelart":
                self.pushButton_9.clicked.connect(self.build1_code_show_tetris_pixel_art)

                date = time.gmtime()
                date1 = date[0], date[1], date[2]
                self.date1 = str(date1)

                F_2 = open("nofp_t_p", "r")
                n = F_2.read()
                self.ni = "0"
                if n != "0":
                    self.ni = n

                self.ni = int(n) + 1
                self.ni = str(self.ni)
                F_3 = open("nofp_t_p", "w")
                F_3.write(self.ni)

                self.lineEdit_build1.setText("Tetris, Pixel Art, " + self.date1)

            if self.selection == "tetrismodern" or self.selection == "tetrispixelart":
                #print("euzdfdfh")
                self.comboBox_build1_0.hide()
                self.label_build1_1.hide()
                self.label_build1_2.hide()
                self.label_build1_3.hide()
                self.label_build1_4.hide()
                self.horizontalSlider_build1_1.hide()
                self.horizontalSlider_build1_2.hide()
                self.horizontalSlider_build1_3.hide()
                self.label_build1_5.hide()
                self.textBrowser_build1_7_bg.hide()
                self.textBrowser_build1_7_fg1.hide()
                self.textBrowser_build1_7_fg2.hide()
                self.textBrowser_build1_7_fg3.hide()
                self.textBrowser_build1_7_fg4.hide()
                self.textBrowser_build1_7_fg5.hide()
                self.textBrowser_build1_7_fg6.hide()
                self.textBrowser_build1_7_fg7.hide()
                self.textBrowser_build1_7_fg8.hide()

            self.pushButton_5.hide()
            self.textBrowser_4.hide()
            self.pushButton_6.hide()
            self.pushButton_8.show()
            self.pushButton_9.show()
            self.label.show()
            self.horizontalSlider.show()
            self.textBrowser_5.show()
            self.progressBar.setProperty("value", 100)
            self.progressBar.hide()
            self.horizontalSlider.sliderReleased.connect(self.hs_value)
            self.horizontalSlider.valueChanged.connect(self.hs_value_changed)
            #print("DONE!")


    def build(self, Form):

            if self.step == 2:
                print("DONE!")
                #print(self.step1_selection, self.step2_selection)

            else:
                self.step = self.step + 1

            self.path(Form)


    def step_selction_pb6(self):

        self.build_process = "in_work"

        if self.substract_step == "true":
                if self.step == 1:
                    self.pushButton_6.setText("Jump'n Run")

                if self.step == 1:
                    self.pushButton_7.setText("Tetris")
                self.substract_step = "false"
                self.textBrowser_4.setText("Jump'n Run oder Tetris")
                self.step = 0


        else:

            if self.step == 0:
                self.step1_selection = "jumpnrun"
            if self.step == 1:
                self.step2_selection = "pixelart"
            self.build(Form)

    def step_selction_pb7(self):

        self.build_process = "in_work"

        if self.substract_step == "true":
                if self.step == 1:
                    self.pushButton_6.setText("Pixel Art")

                if self.step == 1:
                    self.pushButton_7.setText("Modern")
                self.substract_step = "false"
                self.textBrowser_4.setText("Grafik: Modern oder Pixel Art")

        else:

            if self.step == 0:
                self.step1_selection = "tetris"
                self.horizontalSlider.setMinimum(1000)
                self.horizontalSlider.setMaximum(100000)
                self.horizontalSlider.setValue(30000)
                self.label.setText("Rythmuslänge der Geschwindigkeitswechsel")
            if self.step == 1:
                self.step2_selection = "modern"
            self.build(Form)

    def build1_save(self):

        if self.selection == "tetrispixelart":
            # src = self.instalation_path_byg
            # dst = self.instalation_path_byg + "/projects"
            #date = time.gmtime()
            #date1 = date[0], date[1], date[2]
            #date1 = str(date1)
            # shutil.copyfile(src=src + "/('tetris', 'pixelart')", dst=dst + "/Tetris, Pixel Art, " + date1)

            #F_2 = open("nofp_t_p", "r")
            #n = F_2.read()
            #ni = "0"
            #if n != "0":
                #ni = n

            #ni = int(n) + 1
            #ni = str(ni)
            #F_3 = open("nofp_t_p", "w")
            #F_3.write(ni)

            #self.file_name = "projects/" + "Tetris, Pixel Art, " + date1 + ni

            user_file_name = self.lineEdit_build1.text()

            self.file_name = "projects/" + user_file_name + self.ni

            game_project = open("('tetris', 'pixelart')", "r")
            game_project_code = game_project.read()
            #self.velocity = 1
            self.velocity = self.horizontalSlider.value()
            #print(self.velocity)
            self.x = "velocity = " + str(self.velocity) + game_project_code

            F_project_names_write = open("projects/project_BYG_number", "r")
            project_names_write_number_of_projects = (F_project_names_write.read())
            project_names_write_number_of_projects = int(project_names_write_number_of_projects) + 1
            project_names_write_number_of_projects = str(project_names_write_number_of_projects)
            project_names_write_ = open("projects/project_BYG_number", "w")
            project_names_write_.write(project_names_write_number_of_projects)

            project_names_write_read = open("projects/project_BYG_names", "r")
            project_names_write_read_ = (project_names_write_read.read())

            if project_names_write_read_ == "":
                #print("no new line")
                project_names_write__ = open("projects/project_BYG_names", "a")
                project_names_write__.write(user_file_name + self.ni)
                project_names_write___ = open("projects/project_BYG_kinds", "a")
                project_names_write___.write(self.selection)
            else:
                #print("new line")
                project_names_write__ = open("projects/project_BYG_names", "a")
                project_names_write__.write("\n" + user_file_name + self.ni)
                project_names_write___ = open("projects/project_BYG_kinds", "a")
                project_names_write___.write("\n" + self.selection)

        if self.selection == "tetrismodern":
            #src = self.instalation_path_byg
            #dst = self.instalation_path_byg + "/projects"
            #date = time.gmtime()
            #date1 = date[0], date[1], date[2]
            #date1 = str(date1)
            #shutil.copyfile(src=src + "/('tetris', 'modern')", dst=dst + "/Tetris, Modern, " + date1)

            #F_2 = open("nofp_t_m", "r")
            #n = F_2.read()
            #ni = "0"
            #if n != "0":
               ## ni = n

            #ni = int(n) + 1
            #ni = str(ni)
            #F_3 = open("nofp_t_m", "w")
            #F_3.write(ni)

            #self.file_name = "projects/" + "Tetris, Modern, " + date1 + ni

            user_file_name = self.lineEdit_build1.text()

            self.file_name = "projects/" + user_file_name + self.ni

            game_project = open("('tetris', 'modern')", "r")
            game_project_code = game_project.read()
            #self.velocity = 1
            self.velocity = self.horizontalSlider.value()
            #print(self.velocity)
            self.x = "velocity = " + str(self.velocity) + game_project_code

            F_project_names_write = open("projects/project_BYG_number", "r")
            project_names_write_number_of_projects = (F_project_names_write.read())
            project_names_write_number_of_projects = int(project_names_write_number_of_projects) + 1
            project_names_write_number_of_projects = str(project_names_write_number_of_projects)
            project_names_write_ = open("projects/project_BYG_number", "w")
            project_names_write_.write(project_names_write_number_of_projects)

            project_names_write_read = open("projects/project_BYG_names", "r")
            project_names_write_read_ = (project_names_write_read.read())

            if project_names_write_read_ == "":
                #print("no new line")
                project_names_write__ = open("projects/project_BYG_names", "a")
                project_names_write__.write(user_file_name + self.ni)
                project_names_write___ = open("projects/project_BYG_kinds", "a")
                project_names_write___.write(self.selection)
            else:
                #print("new line")
                project_names_write__ = open("projects/project_BYG_names", "a")
                project_names_write__.write("\n" + user_file_name + self.ni)
                project_names_write___ = open("projects/project_BYG_kinds", "a")
                project_names_write___.write("\n" + self.selection)

        if self.selection == "jumpnrunpixelart":

            #self.jumpnrun_values = "#print('Hello World!')"

            #src = self.instalation_path_byg
            #dst = self.instalation_path_byg + "/projects"
            #date = time.gmtime()
            #date1 = date[0], date[1], date[2]
            #date1 = str(date1)
            #shutil.copyfile(src=src + "/('jumpnrun', 'pixelart')", dst=dst + "/Jump'n Run, Pixel Art, " + date1)
            #F_2 = open("nofp_j_p", "r")
            #n = F_2.read()
            #ni = "0"
            #if n != "0":
                #ni = n

            #ni = int(n) + 1
            #ni = str(ni)
            #F_3 = open("nofp_j_p", "w")
            #F_3.write(ni)

            #self.file_name = "projects/" + "Jump'n Run, Pixel Art, " + date1 + ni

            user_file_name = self.lineEdit_build1.text()

            self.file_name = "projects/" + user_file_name + self.ni

            game_project = open("('jumpnrun', 'pixelart')", "r")
            game_project_code = game_project.read()
            #self.velocity = 1
            self.velocity = self.horizontalSlider.value()
            #print(self.velocity)
            self.x = "velocity = " + str(self.velocity) + "\n" + self.jumpnrun_values + game_project_code

            F_project_names_write = open("projects/project_BYG_number", "r")
            project_names_write_number_of_projects = (F_project_names_write.read())
            project_names_write_number_of_projects = int(project_names_write_number_of_projects) + 1
            project_names_write_number_of_projects = str(project_names_write_number_of_projects)
            project_names_write_ = open("projects/project_BYG_number", "w")
            project_names_write_.write(project_names_write_number_of_projects)

            project_names_write_read = open("projects/project_BYG_names", "r")
            project_names_write_read_ = (project_names_write_read.read())

            if project_names_write_read_ == "":
                #print("no new line")
                project_names_write__ = open("projects/project_BYG_names", "a")
                project_names_write__.write(user_file_name + self.ni)
                project_names_write___ = open("projects/project_BYG_kinds", "a")
                project_names_write___.write(self.selection)
            else:
                #print("new line")
                project_names_write__ = open("projects/project_BYG_names", "a")
                project_names_write__.write("\n" + user_file_name + self.ni)
                project_names_write___ = open("projects/project_BYG_kinds", "a")
                project_names_write___.write("\n" + self.selection)

        if self.selection == "jumpnrunmodern":
            # #print(self.instalation_path_byg)
            # src = self.instalation_path_byg
            # dst = self.instalation_path_byg + "/projects"
            #date = time.gmtime()
            #date1 = date[0], date[1], date[2]
            #date1 = str(date1)
            # shutil.copyfile(src=src + "/('jumpnrun', 'modern')", dst=dst + "/Jump'n Run, Modern, " + date1)

            #F_2 = open("nofp_j_m", "r")
            #n = F_2.read()
            #ni = "0"
            #if n != "0":
                #ni = n

            #ni = int(n) + 1
            #ni = str(ni)
            #F_3 = open("nofp_j_m", "w")
            #F_3.write(ni)

            #self.file_name = "projects/" + "Jump'n Run, Modern, " + date1 + ni

            user_file_name = self.lineEdit_build1.text()

            self.file_name = "projects/" + user_file_name + self.ni

            game_project = open("('jumpnrun', 'modern')", "r")
            game_project_code = game_project.read()
            #self.velocity = 1
            self.velocity = self.horizontalSlider.value()
            #print(self.velocity)
            #self.x = "velocity = " + str(self.velocity) + game_project_code
            self.x = "velocity = " + str(self.velocity) + "\n" + self.jumpnrun_values + game_project_code

            F_project_names_write = open("projects/project_BYG_number", "r")
            project_names_write_number_of_projects = (F_project_names_write.read())
            project_names_write_number_of_projects = int(project_names_write_number_of_projects) + 1
            project_names_write_number_of_projects = str(project_names_write_number_of_projects)
            project_names_write_ = open("projects/project_BYG_number", "w")
            project_names_write_.write(project_names_write_number_of_projects)

            project_names_write_read = open("projects/project_BYG_names", "r")
            project_names_write_read_ = (project_names_write_read.read())

            if project_names_write_read_ == "":
                #print("no new line")
                project_names_write__ = open("projects/project_BYG_names", "a")
                project_names_write__.write(user_file_name + self.ni)
                project_names_write___ = open("projects/project_BYG_kinds", "a")
                project_names_write___.write(self.selection)
            else:
                #print("new line")
                project_names_write__ = open("projects/project_BYG_names", "a")
                project_names_write__.write("\n" + user_file_name + self.ni)
                project_names_write___ = open("projects/project_BYG_kinds", "a")
                project_names_write___.write("\n" + self.selection)

        #print(self.file_name)
        print("Das Programm kann neugestartet werden.")
        F_1 = open(self.file_name, "w")
        F_1.write(self.x)

        self.horizontalSlider.hide()
        self.label.hide()
        self.textBrowser_5.setHtml((
            "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
            "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
            "p, li { white-space: pre-wrap; }\n"
            "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
            "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:36pt; font-weight:600;\">Dein Spiel wurde erfolgreich gespeichert!</span></p></body></html>"))
        #time.sleep(5)
        self.open_main_menue()
        self.textBrowser_5.hide()
        sys.exit(app.exec_())

    def build1_code_show_jumpnrun_modern(self):
        game_project = open("('jumpnrun', 'modern')", "r")
        game_project_code = game_project.read()
        #print(game_project_code)
        self.textBrowser_6.show()
        self.textBrowser_6.setText(game_project_code)
        self.pushButton_10.show()

        self.comboBox_build1_0.hide()
        self.label_build1_1.hide()
        self.label_build1_2.hide()
        self.label_build1_3.hide()
        self.label_build1_4.hide()
        self.horizontalSlider_build1_1.hide()
        self.horizontalSlider_build1_2.hide()
        self.horizontalSlider_build1_3.hide()
        self.label_build1_5.hide()
        self.textBrowser_build1_7_bg.hide()
        self.textBrowser_build1_7_fg1.hide()
        self.textBrowser_build1_7_fg2.hide()
        self.textBrowser_build1_7_fg3.hide()
        self.textBrowser_build1_7_fg4.hide()
        self.textBrowser_build1_7_fg5.hide()
        self.textBrowser_build1_7_fg6.hide()
        self.textBrowser_build1_7_fg7.hide()
        self.textBrowser_build1_7_fg8.hide()

        self.label_build1_6.hide()
        self.lineEdit_build1.hide()

    def build1_code_show_jumpnrun_pixel_art(self):
        game_project = open("('jumpnrun', 'pixelart')", "r")
        game_project_code = game_project.read()
        #print(game_project_code)
        self.textBrowser_6.show()
        self.textBrowser_6.setText(game_project_code)
        self.pushButton_10.show()

        self.comboBox_build1_0.hide()
        self.label_build1_1.hide()
        self.label_build1_2.hide()
        self.label_build1_3.hide()
        self.label_build1_4.hide()
        self.horizontalSlider_build1_1.hide()
        self.horizontalSlider_build1_2.hide()
        self.horizontalSlider_build1_3.hide()
        self.label_build1_5.hide()
        self.textBrowser_build1_7_bg.hide()
        self.textBrowser_build1_7_fg1.hide()
        self.textBrowser_build1_7_fg2.hide()
        self.textBrowser_build1_7_fg3.hide()
        self.textBrowser_build1_7_fg4.hide()
        self.textBrowser_build1_7_fg5.hide()
        self.textBrowser_build1_7_fg6.hide()
        self.textBrowser_build1_7_fg7.hide()
        self.textBrowser_build1_7_fg8.hide()

        self.label_build1_6.hide()
        self.lineEdit_build1.hide()

    def build1_code_show_tetris_modern(self):
        game_project = open("('tetris', 'modern')", "r")
        game_project_code = game_project.read()
        #print(game_project_code)
        self.textBrowser_6.show()
        self.textBrowser_6.setText(game_project_code)
        self.pushButton_10.show()

        self.label_build1_6.hide()
        self.lineEdit_build1.hide()

    def build1_code_show_tetris_pixel_art(self):
        game_project = open("('tetris', 'pixelart')", "r")
        game_project_code = game_project.read()
        #print(game_project_code)
        self.textBrowser_6.show()
        self.textBrowser_6.setText(game_project_code)
        self.pushButton_10.show()

        self.label_build1_6.hide()
        self.lineEdit_build1.hide()

    def close_show_code(self):
        self.textBrowser_6.hide()
        self.pushButton_10.hide()

        self.comboBox_build1_0.show()
        self.label_build1_2.show()
        self.label_build1_3.show()
        self.label_build1_4.show()
        self.horizontalSlider_build1_1.show()
        self.horizontalSlider_build1_2.show()
        self.horizontalSlider_build1_3.show()
        self.label_build1_5.show()
        self.textBrowser_build1_7_bg.show()
        self.textBrowser_build1_7_fg1.show()
        self.textBrowser_build1_7_fg2.show()
        self.textBrowser_build1_7_fg3.show()
        self.textBrowser_build1_7_fg4.show()
        self.textBrowser_build1_7_fg5.show()
        self.textBrowser_build1_7_fg6.show()
        self.textBrowser_build1_7_fg7.show()
        self.textBrowser_build1_7_fg8.show()

        self.label_build1_6.show()
        self.lineEdit_build1.show()

    def hs_value(self):

        if self.selection == "jumpnrunmodern":
            game_project = open("('jumpnrun', 'modern')", "r")
            game_project_code = game_project.read()
            self.velocity = self.horizontalSlider.value()
            #print(self.velocity)
            self.x = "velocity = " + str(self.velocity) + game_project_code
        if self.selection == "jumpnrunpixelart":
            game_project = open("('jumpnrun', 'pixelart')", "r")
            game_project_code = game_project.read()
            self.velocity = self.horizontalSlider.value()
            #print(self.velocity)
            self.x = "velocity = " + str(self.velocity) + game_project_code
        if self.selection == "tetrismodern":
            game_project = open("('tetris', 'modern')", "r")
            game_project_code = game_project.read()
            self.velocity = self.horizontalSlider.value()
            #print(self.velocity)
            self.x = "velocity = " + str(self.velocity) + game_project_code
        if self.selection == "tetrispixelart":
            game_project = open("('tetris', 'pixelart')", "r")
            game_project_code = game_project.read()
            self.velocity = self.horizontalSlider.value()
            #print(self.velocity)
            self.x = "velocity = " + str(self.velocity) + game_project_code

    def hs_value_changed(self):

        ##print(self.horizontalSlider.value())

        if self.selection == "jumpnrunmodern":
            velocity = self.horizontalSlider.value()
            if velocity < 11:
                assessment = "langsam"
            if velocity > 10 and velocity < 50:
                assessment = "schnell"
            if velocity > 49:
                assessment = "extrem schnell"
            self.label.setText("Tempo des Spielcharachters " + "(" + str(velocity) + "), " + assessment)

        if self.selection == "jumpnrunpixelart":
            velocity = self.horizontalSlider.value()
            if velocity < 11:
                assessment = "langsam"
            if velocity > 10 and velocity < 50:
                assessment = "schnell"
            if velocity > 49:
                assessment = "extrem schnell"
            self.label.setText("Tempo des Spielcharachters " + "(" + str(velocity) + "), " + assessment)

        if self.selection == "tetrismodern":
            velocity = self.horizontalSlider.value()
            if velocity < 11000:
                assessment = "schneller Wechsel"
            if velocity > 10000 and velocity < 50000:
                assessment = "mäßig schneller Wechsel"
            if velocity > 49000:
                assessment = "langsamer Wechsel"
            self.label.setText("Rythmuslänge der Geschwindigkeitswechsel " + "(" + str(velocity) + "ms), " + assessment)

        if self.selection == "tetrispixelart":
            velocity = self.horizontalSlider.value()
            if velocity < 11000:
                assessment = "schneller Wechsel"
            if velocity > 10000 and velocity < 50000:
                assessment = "mäßig schneller Wechsel"
            if velocity > 49000:
                assessment = "langsamer Wechsel"
            self.label.setText("Rythmuslänge der Geschwindigkeitswechsel " + "(" + str(velocity) + "ms), " + assessment)

    def build1_cb_barrier_changed(self):
        #print(self.comboBox_build1_0.currentIndex())
        self.build1_current_barrier = self.comboBox_build1_0.currentIndex() + 1
        #print(self.build1_current_barrier)
        #self.build1_write_hob1, self.build1_write_le1, self.build1_write_wi1 = 50, 100, 30

        if self.build1_current_barrier == 1:
            self.horizontalSlider_build1_1.setValue(self.build1_write_hob1)
            self.horizontalSlider_build1_2.setValue(self.build1_write_le1)
            self.horizontalSlider_build1_3.setValue(self.build1_write_wi1)

        if self.build1_current_barrier == 2:
            self.horizontalSlider_build1_1.setValue(self.build1_write_hob2)
            self.horizontalSlider_build1_2.setValue(self.build1_write_le2)
            self.horizontalSlider_build1_3.setValue(self.build1_write_wi2)

        if self.build1_current_barrier == 3:
            self.horizontalSlider_build1_1.setValue(self.build1_write_hob3)
            self.horizontalSlider_build1_2.setValue(self.build1_write_le3)
            self.horizontalSlider_build1_3.setValue(self.build1_write_wi3)

        if self.build1_current_barrier == 4:
            self.horizontalSlider_build1_1.setValue(self.build1_write_hob4)
            self.horizontalSlider_build1_2.setValue(self.build1_write_le4)
            self.horizontalSlider_build1_3.setValue(self.build1_write_wi4)

        if self.build1_current_barrier == 5:
            self.horizontalSlider_build1_1.setValue(self.build1_write_hob5)
            self.horizontalSlider_build1_2.setValue(self.build1_write_le5)
            self.horizontalSlider_build1_3.setValue(self.build1_write_wi5)

        if self.build1_current_barrier == 6:
            self.horizontalSlider_build1_1.setValue(self.build1_write_hob6)
            self.horizontalSlider_build1_2.setValue(self.build1_write_le6)
            self.horizontalSlider_build1_3.setValue(self.build1_write_wi6)

        if self.build1_current_barrier == 7:
            self.horizontalSlider_build1_1.setValue(self.build1_write_hob7)
            self.horizontalSlider_build1_2.setValue(self.build1_write_le7)
            self.horizontalSlider_build1_3.setValue(self.build1_write_wi7)

        if self.build1_current_barrier == 8:
            self.horizontalSlider_build1_1.setValue(self.build1_write_hob8)
            self.horizontalSlider_build1_2.setValue(self.build1_write_le8)
            self.horizontalSlider_build1_3.setValue(self.build1_write_wi8)
            
    def build1_hsbuild1_1_value_changed(self):
        ##print(self.horizontalSlider_build1_1.value())

        if self.build1_current_barrier == 1:
            self.build1_preview_hob1 = 686 - self.horizontalSlider_build1_1.value() // 5
            self.build1_write_hob1 = self.horizontalSlider_build1_1.value()
            ##print(self.build1_preview_hob1)
            self.textBrowser_build1_7_fg1.setGeometry(70, self.build1_preview_hob1, self.build1_preview_le1, self.build1_preview_wi1)
            # 686 = 470 + 216, untere Kante des "Fensterns", 1build1_ / 5 = 20, 30 / 5 = 6, 50 / 5 = 10, also 686 - 10 <- Höhe überm Boden

        if self.build1_current_barrier == 2:
            self.build1_preview_hob2 = 686 - self.horizontalSlider_build1_1.value() // 5
            self.build1_write_hob2 = self.horizontalSlider_build1_1.value()
            self.textBrowser_build1_7_fg2.setGeometry(self.build1_preview_dfe2, self.build1_preview_hob2, self.build1_preview_le2, self.build1_preview_wi2)

        if self.build1_current_barrier == 3:
            self.build1_preview_hob3 = 686 - self.horizontalSlider_build1_1.value() // 5
            self.build1_write_hob3 = self.horizontalSlider_build1_1.value()
            self.textBrowser_build1_7_fg3.setGeometry(self.build1_preview_dfe3, self.build1_preview_hob3, self.build1_preview_le3, self.build1_preview_wi3)

        if self.build1_current_barrier == 4:
            self.build1_preview_hob4 = 686 - self.horizontalSlider_build1_1.value() // 5
            self.build1_write_hob4 = self.horizontalSlider_build1_1.value()
            self.textBrowser_build1_7_fg4.setGeometry(self.build1_preview_dfe4, self.build1_preview_hob4, self.build1_preview_le4, self.build1_preview_wi4)

        if self.build1_current_barrier == 5:
            self.build1_preview_hob5 = 686 - self.horizontalSlider_build1_1.value() // 5
            self.build1_write_hob5 = self.horizontalSlider_build1_1.value()
            self.textBrowser_build1_7_fg5.setGeometry(self.build1_preview_dfe5, self.build1_preview_hob5, self.build1_preview_le5, self.build1_preview_wi5)

        if self.build1_current_barrier == 6:
            self.build1_preview_hob6 = 686 - self.horizontalSlider_build1_1.value() // 5
            self.build1_write_hob6 = self.horizontalSlider_build1_1.value()
            self.textBrowser_build1_7_fg6.setGeometry(self.build1_preview_dfe6, self.build1_preview_hob6, self.build1_preview_le6, self.build1_preview_wi6)

        if self.build1_current_barrier == 7:
            self.build1_preview_hob7 = 686 - self.horizontalSlider_build1_1.value() // 5
            self.build1_write_hob7 = self.horizontalSlider_build1_1.value()
            self.textBrowser_build1_7_fg7.setGeometry(self.build1_preview_dfe7, self.build1_preview_hob7, self.build1_preview_le7, self.build1_preview_wi7)

        if self.build1_current_barrier == 8:
            self.build1_preview_hob8 = 686 - self.horizontalSlider_build1_1.value() // 5
            self.build1_write_hob8 = self.horizontalSlider_build1_1.value()
            self.textBrowser_build1_7_fg8.setGeometry(self.build1_preview_dfe8, self.build1_preview_hob8, self.build1_preview_le8, self.build1_preview_wi8)
            
    def build1_hsbuild1_1_build1_3_value(self):

        w_line1 = "hob1, le1, wi1 = " + str(self.build1_write_hob1) + ", " + str(self.build1_write_le1) + ", " + str(self.build1_write_wi1)
        w_line2 = "hob2, le2, wi2 = " + str(self.build1_write_hob2) + ", " + str(self.build1_write_le2) + ", " + str(self.build1_write_wi2)
        w_line3 = "hob3, le3, wi3 = " + str(self.build1_write_hob3) + ", " + str(self.build1_write_le3) + ", " + str(self.build1_write_wi3)
        w_line4 = "hob4, le4, wi4 = " + str(self.build1_write_hob4) + ", " + str(self.build1_write_le4) + ", " + str(self.build1_write_wi4)
        w_line5 = "hob5, le5, wi5 = " + str(self.build1_write_hob5) + ", " + str(self.build1_write_le5) + ", " + str(self.build1_write_wi5)
        w_line6 = "hob6, le6, wi6 = " + str(self.build1_write_hob6) + ", " + str(self.build1_write_le6) + ", " + str(self.build1_write_wi6)
        w_line7 = "hob7, le7, wi7 = " + str(self.build1_write_hob7) + ", " + str(self.build1_write_le7) + ", " + str(self.build1_write_wi7)
        w_line8 = "hob8, le8, wi8 = " + str(self.build1_write_hob8) + ", " + str(self.build1_write_le8) + ", " + str(self.build1_write_wi8)

        w_line9 = "hob9, le9, wi9 = " + str(self.build1_write_hob1) + ", " + str(self.build1_write_le1) + ", " + str(self.build1_write_wi1)
        w_line10 = "hob10, le10, wi10 = " + str(self.build1_write_hob2) + ", " + str(self.build1_write_le2) + ", " + str(self.build1_write_wi2)
        w_line11 = "hob11, le11, wi11 = " + str(self.build1_write_hob3) + ", " + str(self.build1_write_le3) + ", " + str(self.build1_write_wi3)
        w_line12 = "hob12, le12, wi12 = " + str(self.build1_write_hob4) + ", " + str(self.build1_write_le4) + ", " + str(self.build1_write_wi4)
        w_line13 = "hob13, le13, wi13 = " + str(self.build1_write_hob5) + ", " + str(self.build1_write_le5) + ", " + str(self.build1_write_wi5)
        w_line14 = "hob14, le14, wi14 = " + str(self.build1_write_hob6) + ", " + str(self.build1_write_le6) + ", " + str(self.build1_write_wi6)
        w_line15 = "hob15, le15, wi15 = " + str(self.build1_write_hob7) + ", " + str(self.build1_write_le7) + ", " + str(self.build1_write_wi7)
        w_line16 = "hob16, le16, wi16 = " + str(self.build1_write_hob8) + ", " + str(self.build1_write_le8) + ", " + str(self.build1_write_wi8)

        w_line17 = "hob17, le17, wi17 = " + str(self.build1_write_hob1) + ", " + str(self.build1_write_le1) + ", " + str(self.build1_write_wi1)
        w_line18 = "hob18, le18, wi18 = " + str(self.build1_write_hob2) + ", " + str(self.build1_write_le2) + ", " + str(self.build1_write_wi2)
        w_line19 = "hob19, le19, wi19 = " + str(self.build1_write_hob3) + ", " + str(self.build1_write_le3) + ", " + str(self.build1_write_wi3)
        w_line20 = "hob20, le20, wi20 = " + str(self.build1_write_hob4) + ", " + str(self.build1_write_le4) + ", " + str(self.build1_write_wi4)
        w_line21 = "hob21, le21, wi21 = " + str(self.build1_write_hob5) + ", " + str(self.build1_write_le5) + ", " + str(self.build1_write_wi5)
        w_line22 = "hob22, le22, wi22 = " + str(self.build1_write_hob6) + ", " + str(self.build1_write_le6) + ", " + str(self.build1_write_wi6)
        w_line23 = "hob23, le23, wi23 = " + str(self.build1_write_hob7) + ", " + str(self.build1_write_le7) + ", " + str(self.build1_write_wi7)
        w_line24 = "hob24, le24, wi24 = " + str(self.build1_write_hob8) + ", " + str(self.build1_write_le8) + ", " + str(self.build1_write_wi8)

        w_line25 = "hob25, le25, wi25 = " + str(self.build1_write_hob1) + ", " + str(self.build1_write_le1) + ", " + str(self.build1_write_wi1)
        w_line26 = "hob26, le26, wi26 = " + str(self.build1_write_hob2) + ", " + str(self.build1_write_le2) + ", " + str(self.build1_write_wi2)
        w_line27 = "hob27, le27, wi27 = " + str(self.build1_write_hob3) + ", " + str(self.build1_write_le3) + ", " + str(self.build1_write_wi3)
        w_line28 = "hob28, le28, wi28 = " + str(self.build1_write_hob4) + ", " + str(self.build1_write_le4) + ", " + str(self.build1_write_wi4)
        w_line29 = "hob29, le29, wi29 = " + str(self.build1_write_hob5) + ", " + str(self.build1_write_le5) + ", " + str(self.build1_write_wi5)
        w_line30 = "hob30, le30, wi30 = " + str(self.build1_write_hob6) + ", " + str(self.build1_write_le6) + ", " + str(self.build1_write_wi6)
        w_line31 = "hob31, le31, wi31 = " + str(self.build1_write_hob7) + ", " + str(self.build1_write_le7) + ", " + str(self.build1_write_wi7)
        w_line32 = "hob32, le32, wi32 = " + str(self.build1_write_hob8) + ", " + str(self.build1_write_le8) + ", " + str(self.build1_write_wi8)

        w_lines_0_8_package1 = w_line1  + "\n" + w_line2  + "\n" +  w_line3  + "\n" +  w_line4  + "\n" +  w_line5  + "\n" + w_line6  + "\n" +  w_line7  + "\n" +  w_line8

        w_lines_9_16_package2 = w_line9 + "\n" + w_line10 + "\n" + w_line11 + "\n" + w_line12 + "\n" + w_line13 + "\n" + w_line14 + "\n" + w_line15 + "\n" + w_line16

        w_lines_17_24_package3 = w_line17 + "\n" + w_line18 + "\n" + w_line19 + "\n" + w_line20 + "\n" + w_line21 + "\n" + w_line22 + "\n" + w_line23 + "\n" + w_line24

        w_lines_25_32_package4 = w_line25 + "\n" + w_line26 + "\n" + w_line27 + "\n" + w_line28 + "\n" + w_line29 + "\n" + w_line30 + "\n" + w_line31 + "\n" + w_line32

        ##print(w_lines_0_8_package1 + "\n" + w_lines_9_16_package2 + "\n" + w_lines_17_24_package3 + "\n" + w_lines_25_32_package4)

        self.jumpnrun_values = w_lines_0_8_package1 + "\n" + w_lines_9_16_package2 + "\n" + w_lines_17_24_package3 + "\n" + w_lines_25_32_package4 + "\n"
        
        
    def build1_hsbuild1_2_value_changed(self):
        ##print(self.horizontalSlider_build1_2.value())

        if self.build1_current_barrier == 1:
            self.build1_preview_le1 = self.horizontalSlider_build1_2.value() // 5
            self.build1_write_le1 = self.horizontalSlider_build1_2.value()
            ##print(self.build1_preview_le1)
            self.textBrowser_build1_7_fg1.setGeometry(70, self.build1_preview_hob1, self.build1_preview_le1, self.build1_preview_wi1)
            # 686 = 470 + 216, untere Kante des "Fensterns", 1build1_ / 5 = 20, 30 / 5 = 6, 50 / 5 = 10, also 10 <- Höhe überm Boden

        if self.build1_current_barrier == 2:
            self.build1_preview_le2 = self.horizontalSlider_build1_2.value() // 5
            self.build1_write_le2 = self.horizontalSlider_build1_2.value()
            self.textBrowser_build1_7_fg2.setGeometry(self.build1_preview_dfe2, self.build1_preview_hob2, self.build1_preview_le2, self.build1_preview_wi2)

        if self.build1_current_barrier == 3:
            self.build1_preview_le3 = self.horizontalSlider_build1_2.value() // 5
            self.build1_write_le3 = self.horizontalSlider_build1_2.value()
            self.textBrowser_build1_7_fg3.setGeometry(self.build1_preview_dfe3, self.build1_preview_hob3, self.build1_preview_le3, self.build1_preview_wi3)

        if self.build1_current_barrier == 4:
            self.build1_preview_le4 = self.horizontalSlider_build1_2.value() // 5
            self.build1_write_le4 = self.horizontalSlider_build1_2.value()
            self.textBrowser_build1_7_fg4.setGeometry(self.build1_preview_dfe4, self.build1_preview_hob4, self.build1_preview_le4, self.build1_preview_wi4)

        if self.build1_current_barrier == 5:
            self.build1_preview_le5 = self.horizontalSlider_build1_2.value() // 5
            self.build1_write_le5 = self.horizontalSlider_build1_2.value()
            self.textBrowser_build1_7_fg5.setGeometry(self.build1_preview_dfe5, self.build1_preview_hob5, self.build1_preview_le5, self.build1_preview_wi5)

        if self.build1_current_barrier == 6:
            self.build1_preview_le6 = self.horizontalSlider_build1_2.value() // 5
            self.build1_write_le6 = self.horizontalSlider_build1_2.value()
            self.textBrowser_build1_7_fg6.setGeometry(self.build1_preview_dfe6, self.build1_preview_hob6, self.build1_preview_le6, self.build1_preview_wi6)

        if self.build1_current_barrier == 7:
            self.build1_preview_le7 = self.horizontalSlider_build1_2.value() // 5
            self.build1_write_le7 = self.horizontalSlider_build1_2.value()
            self.textBrowser_build1_7_fg7.setGeometry(self.build1_preview_dfe7, self.build1_preview_hob7, self.build1_preview_le7, self.build1_preview_wi7)

        if self.build1_current_barrier == 8:
            self.build1_preview_le8 = self.horizontalSlider_build1_2.value() // 5
            self.build1_write_le8 = self.horizontalSlider_build1_2.value()
            self.textBrowser_build1_7_fg8.setGeometry(self.build1_preview_dfe8, self.build1_preview_hob8, self.build1_preview_le8, self.build1_preview_wi8)
            
    def build1_hsbuild1_3_value_changed(self):
        ##print(self.horizontalSlider_build1_3.value())

        if self.build1_current_barrier == 1:
            self.build1_preview_wi1 = self.horizontalSlider_build1_3.value() // 5
            self.build1_write_wi1 = self.horizontalSlider_build1_3.value()
            ##print(self.build1_preview_wi1)
            self.textBrowser_build1_7_fg1.setGeometry(70, self.build1_preview_hob1, self.build1_preview_le1, self.build1_preview_wi1)
            # 686 = 470 + 216, untere Kante des "Fensterns", 1build1_ / 5 = 20, 30 / 5 = 6, 50 / 5 = 10, also 10 <- Höhe überm Boden

        if self.build1_current_barrier == 2:
            self.build1_preview_wi2 = self.horizontalSlider_build1_3.value() // 5
            self.build1_write_wi2 = self.horizontalSlider_build1_3.value()
            self.textBrowser_build1_7_fg2.setGeometry(self.build1_preview_dfe2, self.build1_preview_hob2, self.build1_preview_le2, self.build1_preview_wi2)

        if self.build1_current_barrier == 3:
            self.build1_preview_wi3 = self.horizontalSlider_build1_3.value() // 5
            self.build1_write_wi3 = self.horizontalSlider_build1_3.value()
            self.textBrowser_build1_7_fg3.setGeometry(self.build1_preview_dfe3, self.build1_preview_hob3, self.build1_preview_le3, self.build1_preview_wi3)

        if self.build1_current_barrier == 4:
            self.build1_preview_wi4 = self.horizontalSlider_build1_3.value() // 5
            self.build1_write_wi4 = self.horizontalSlider_build1_3.value()
            self.textBrowser_build1_7_fg4.setGeometry(self.build1_preview_dfe4, self.build1_preview_hob4, self.build1_preview_le4, self.build1_preview_wi4)

        if self.build1_current_barrier == 5:
            self.build1_preview_wi5 = self.horizontalSlider_build1_3.value() // 5
            self.build1_write_wi5 = self.horizontalSlider_build1_3.value()
            self.textBrowser_build1_7_fg5.setGeometry(self.build1_preview_dfe5, self.build1_preview_hob5, self.build1_preview_le5, self.build1_preview_wi5)

        if self.build1_current_barrier == 6:
            self.build1_preview_wi6 = self.horizontalSlider_build1_3.value() // 5
            self.build1_write_wi6 = self.horizontalSlider_build1_3.value()
            self.textBrowser_build1_7_fg6.setGeometry(self.build1_preview_dfe6, self.build1_preview_hob6, self.build1_preview_le6, self.build1_preview_wi6)

        if self.build1_current_barrier == 7:
            self.build1_preview_wi7 = self.horizontalSlider_build1_3.value() // 5
            self.build1_write_wi7 = self.horizontalSlider_build1_3.value()
            self.textBrowser_build1_7_fg7.setGeometry(self.build1_preview_dfe7, self.build1_preview_hob7, self.build1_preview_le7, self.build1_preview_wi7)

        if self.build1_current_barrier == 8:
            self.build1_preview_wi8 = self.horizontalSlider_build1_3.value() // 5
            self.build1_write_wi8 = self.horizontalSlider_build1_3.value()
            self.textBrowser_build1_7_fg8.setGeometry(self.build1_preview_dfe8, self.build1_preview_hob8, self.build1_preview_le8, self.build1_preview_wi8)
            
            
    def build1_hs_dfe(self):
        self.build1_preview_dfe2 = 70 + self.build1_preview_le1
        self.build1_preview_dfe3 = 70 + self.build1_preview_le1 + self.build1_preview_le2
        self.build1_preview_dfe4 = 70 + self.build1_preview_le1 + self.build1_preview_le2 + self.build1_preview_le3
        self.build1_preview_dfe5 = 70 + self.build1_preview_le1 + self.build1_preview_le2 + self.build1_preview_le3 + self.build1_preview_le4
        self.build1_preview_dfe6 = 70 + self.build1_preview_le1 + self.build1_preview_le2 + self.build1_preview_le3 + self.build1_preview_le4 + self.build1_preview_le5
        self.build1_preview_dfe7 = 70 + self.build1_preview_le1 + self.build1_preview_le2 + self.build1_preview_le3 + self.build1_preview_le4 + self.build1_preview_le5 + self.build1_preview_le6
        self.build1_preview_dfe8 = 70 + self.build1_preview_le1 + self.build1_preview_le2 + self.build1_preview_le3 + self.build1_preview_le4 + self.build1_preview_le5 + self.build1_preview_le6 + self.build1_preview_le7

        self.textBrowser_build1_7_fg2.setGeometry(self.build1_preview_dfe2, self.build1_preview_hob2, self.build1_preview_le2, self.build1_preview_wi2)
        self.textBrowser_build1_7_fg3.setGeometry(self.build1_preview_dfe3, self.build1_preview_hob3, self.build1_preview_le3, self.build1_preview_wi3)
        self.textBrowser_build1_7_fg4.setGeometry(self.build1_preview_dfe4, self.build1_preview_hob4, self.build1_preview_le4, self.build1_preview_wi4)
        self.textBrowser_build1_7_fg5.setGeometry(self.build1_preview_dfe5, self.build1_preview_hob5, self.build1_preview_le5, self.build1_preview_wi5)
        self.textBrowser_build1_7_fg6.setGeometry(self.build1_preview_dfe6, self.build1_preview_hob6, self.build1_preview_le6, self.build1_preview_wi6)
        self.textBrowser_build1_7_fg7.setGeometry(self.build1_preview_dfe7, self.build1_preview_hob7, self.build1_preview_le7, self.build1_preview_wi7)
        self.textBrowser_build1_7_fg8.setGeometry(self.build1_preview_dfe8, self.build1_preview_hob8, self.build1_preview_le8, self.build1_preview_wi8)
        

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Build.Your.Game"))
        self.toolButton.setText(_translate("Form", "..."))
        self.pushButton.setText(_translate("Form", "Meine Spiele"))
        self.pushButton_2.setText(_translate("Form", "Erstellen"))
        self.textBrowser.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:72pt;\">Build.Your.Game.</span></p></body></html>"))
        self.textBrowser_2.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; color:#797979;\">Version: 1.2.3 Beta by </span><a href=\"https://www.youtube.com/channel/UCANAe4mkm2vCSdA22uqZ4qA\"><span style=\" font-size:8pt; text-decoration: underline; color:#797979;\">Jonas</span></a><span style=\" font-size:8pt; color:#797979;\"> and Robert</span></p></body></html>"))
        self.toolButton_2.setText(_translate("Form", "Zurück zum Hauptmenü"))
        self.textBrowser_3.setHtml(_translate("Form",
                                            "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                            "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                            "p, li { white-space: pre-wrap; }\n"
                                            "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
                                            "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:48pt;\">Build.Your.Game ist eine Open Source GameEngine für Jedermann.</span></p>\n"
                                            "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:48pt;\">Entwickelt wurde sie von </span><a href=\"https://www.youtube.com/channel/UCANAe4mkm2vCSdA22uqZ4qA\"><span style=\" font-size:48pt; text-decoration: underline; color:#0000ff;\">RoJoSciences</span></a><span style=\" font-size:48pt;\">.</span></p>\n"
                                            "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:48pt;\">Version 1.2.3 Beta</span></p>\n"
                                            "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:48pt;\">Release: 22.11.2020</span></p></body></html>"))
        self.pushButton_3.setText(_translate("Form", "Beenden"))
        self.pushButton_4.setText(_translate("Form", "Ins.Aen."))
        self.toolButton_3.setText(_translate("Form", "Zurück zum Hauptmenü"))
        self.toolButton_4.setText(_translate("Form", "..."))
        self.pushButton_5.setText(_translate("Form", "Abbrechen"))
        self.textBrowser_4.setHtml(_translate("Form",
                                            "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                            "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                            "p, li { white-space: pre-wrap; }\n"
                                            "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
                                            "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:36pt; font-weight:600;\">Jump\'n Run oder Tetris?</span></p></body></html>"))
        self.pushButton_6.setText(_translate("Form", "Jump\'n Run"))
        #self.pushButton_11.setText(_translate("Form3", "#############"))
        self.pushButton_7.setText(_translate("Form", "Tetris"))
        self.pushButton_8.setText(_translate("Form", "Speichern"))
        self.pushButton_9.setText(_translate("Form", "Code Ansehen"))
        self.textBrowser_5.setHtml(_translate("Form",
                                            "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                            "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                            "p, li { white-space: pre-wrap; }\n"
                                            "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
                                            "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt;\">Hier ist deine Auswahl, verändere die Werte, um dein Spiel individueller zu gestalten.</span></p></body></html>"))
        self.label.setText(_translate("Form", "Tempo des Spielcharachters"))
        self.pushButton_008.setText(_translate("Form", "Speichern"))
        self.pushButton_009.setText(_translate("Form", "Code Ansehen/Bearbeiten"))
        self.textBrowser_005.setHtml(_translate("Form",
                                              "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                              "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                              "p, li { white-space: pre-wrap; }\n"
                                              "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
                                              "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt;\">Hier ist deine Auswahl, verändere die Werte, um dein Spiel individueller zu gestalten.</span></p></body></html>"))
        self.label_000.setText(_translate("Form", "Tempo des Spielcharachters"))
        self.pushButton_008_.setText(_translate("Form", "Umwandeln in .py"))
        self.toolButton_002.setText(_translate("Form", "Beenden"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
