from PyQt5.QtCore import QSize, QMetaObject, QCoreApplication
from PyQt5.QtWidgets import QSpacerItem, QLabel, QSizePolicy, QMainWindow,QFrame, QPushButton, QHBoxLayout, QStatusBar
from PyQt5.QtGui import QFont, QPixmap,QIcon
from PyQt5.QtCore import QDate, QTime, Qt, QTimer
from sip import delete
from libraries.Result_Display import *
from libraries.result_view import *
from libraries.Data_Input import *
from libraries.Data_Analysis import *
class Ui_MainWindow(QMainWindow):
    def __init__(self):
        super(Ui_MainWindow, self).__init__()
        self.run_analysis_display=1
        self.run_result_display=1
        self.saveas=0
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("动态称重系统")
        MainWindow.resize(800, 500)

        self.answer = []
        self.flag = 1
        self.counts = Data_Input()
        self.table_display = []
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 2)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame = QFrame(self.centralwidget)
        self.frame.setStyleSheet("background-color: rgb(56, 56, 56);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_3 = QHBoxLayout(self.frame)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.frame_2 = QFrame(self.frame)
        self.frame_2.setMinimumSize(QSize(0, 40))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout = QHBoxLayout(self.frame_2)
        self.horizontalLayout.setContentsMargins(0, 0, -1, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton = QPushButton(self.frame_2)
        self.pushButton.setMinimumSize(QSize(100, 40))
        font = QFont()
        font.setFamily("利方黑体")
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("color:rgb(255, 255, 255);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.counts.loadDataFile)
        self.horizontalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QPushButton(self.frame_2)
        self.pushButton_2.setMinimumSize(QSize(100, 40))
        font = QFont()
        font.setFamily("利方黑体")
        font.setPointSize(12)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("color:rgb(255, 255, 255);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.pushButton_3 = QPushButton(self.frame_2)
        self.pushButton_3.setMinimumSize(QSize(100, 40))
        font = QFont()
        font.setFamily("利方黑体")
        font.setPointSize(12)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("color:rgb(255, 255, 255);")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(self.analysis_display)
        self.horizontalLayout.addWidget(self.pushButton_3)
        self.horizontalLayout_3.addWidget(self.frame_2)
        self.frame_3 = QFrame(self.frame)
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout_2 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_2.setContentsMargins(-1, 0, 1, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.pushButton_4 = QPushButton(self.frame_3)
        self.pushButton_4.setMinimumSize(QSize(100, 40))
        font =QFont()
        font.setFamily("利方黑体")
        font.setPointSize(12)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet("color:rgb(255, 255, 255);")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.clicked.connect(self.save_as)
        self.horizontalLayout_2.addWidget(self.pushButton_4)
        self.horizontalLayout_3.addWidget(self.frame_3)
        self.verticalLayout_2.addWidget(self.frame)
        self.frame_4 = QFrame(self.centralwidget)
        self.frame_4.setMinimumSize(QSize(0, 70))
        self.frame_4.setMaximumSize(QSize(16777215, 70))
        self.frame_4.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.horizontalLayout_6 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_6.setContentsMargins(10, 5, 10, 0)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.frame_6 = QFrame(self.frame_4)
        self.frame_6.setMinimumSize(QSize(60, 60))
        self.frame_6.setMaximumSize(QSize(60, 80))
        self.frame_6.setStyleSheet("border-image: url(:/main/static/image/12.png);")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.horizontalLayout_6.addWidget(self.frame_6)
        self.frame_5 = QFrame(self.frame_4)
        self.frame_5.setMinimumSize(QSize(60, 60))
        self.frame_5.setMaximumSize(QSize(60, 60))
        self.frame_5.setStyleSheet("border-image: url(:/main/static/image/pw1.png);")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.horizontalLayout_6.addWidget(self.frame_5)
        spacerItem1 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem1)
        self.frame_7 = QFrame(self.frame_4)
        self.frame_7.setMinimumSize(QSize(400, 60))
        self.frame_7.setMaximumSize(QSize(200, 60))
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.verticalLayout = QVBoxLayout(self.frame_7)
        self.verticalLayout.setContentsMargins(10, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem2)
        self.label = QLabel(self.frame_7)
        self.label.setMinimumSize(QSize(200, 50))
        self.label.setStyleSheet("QLabel{color:rgb(300,300,300,120);font-size:14px;font-family:Farrington-7B-Qiqi;}")
        font = QFont()
        font.setFamily("A-OTF Midashi Go MB31 Pro")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignBottom|Qt.AlignRight|Qt.AlignTrailing)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.horizontalLayout_6.addWidget(self.frame_7)
        self.verticalLayout_2.addWidget(self.frame_4)
        self.frame_8 = QFrame(self.centralwidget)
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.horizontalLayout_4 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")

        # 按钮函数
        self.table_display.append(self.temp())
        self.horizontalLayout_4.addWidget(self.table_display[0])
        self.pushButton_2.clicked.connect(self.result_dis)

        self.verticalLayout_2.addWidget(self.frame_8)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusBar = QStatusBar(MainWindow)
        # font = QFont()
        # font.setPointSize(16)
        # self.statusbar.setFont(font)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.statusBar.showMessage("准备就绪")

        self.retranslateUi(MainWindow)
        QMetaObject.connectSlotsByName(MainWindow)

        timer = QTimer(self)
        timer.timeout.connect(self.showtime)
        timer.start()

    def showtime(self):
        self.now = QDate.currentDate()  # 获取当前日期
        self.time = QTime.currentTime()  # 获取当前时间
        self.time_time = self.time.toString(Qt.DefaultLocaleLongDate)
        self.label.setText("  " + self.now.toString(Qt.ISODate) + "  " + self.time_time)

    def temp(self):
        tableView = QTableView(self.frame_8)
        tableView.setStyleSheet("background-color: rgb(255, 255, 255);")
        tableView.setObjectName("tableView")
        return tableView

    # 数据分析显示函数
    def analysis_display(self):
        try:
            if (len(self.counts.result_list) and self.run_analysis_display):
                self.run_analysis_display = 0
                self.run_result_display=1
                try:
                    self.path_in = self.new_file(u'../weight_result/')
                    with open(self.path_in, 'r', encoding='utf-8') as csvfile:
                        self.rd = reader(csvfile)
                        self.answer = list(self.rd)
                    self.answer = [float(self.answer[i][2]) for i in range(1, len(self.answer))]
                except:
                    print('No such file!')
                finally:
                    pass

                self.analysis_subsection = Data_Analysis_1()
                self.analysis_extreme = Data_Analysis_2()
                self.analysis_subsection.analysis1_subsection(self.answer)
                self.analysis_extreme.analysis2_set_rows_cols(self.answer)

                for i in self.table_display:
                    self.horizontalLayout_4.removeWidget(i)
                    delete(i)
                self.table_display.clear()
                self.table_display.append(self.analysis_subsection)
                self.table_display.append(self.analysis_extreme)

                for i in self.table_display:
                    self.horizontalLayout_4.addWidget(i)
            else:
                pass
        except:
            pass
        finally:
            pass

    # 结果显示函数
    def result_dis(self):
        try:
            if (len(self.counts.result_list) and self.run_result_display):
                try:
                    self.run_analysis_display = 1
                    self.run_result_display = 0
                    self.path_in = self.new_file(u'../weight_result/')
                    with open(self.path_in, 'r', encoding='utf-8') as csvfile:
                        self.rd = reader(csvfile)
                        self.answer = list(self.rd)
                    self.answer = [float(self.answer[i][2]) for i in range(1, len(self.answer))]
                except:
                    print('No such file!')
                finally:
                    pass

        # 计算table行数
            self.rows = 0
            if (len(self.answer) % 4 == 0):
                self.rows = len(self.answer) / 4
            else:
                self.rows = 1 + len(self.answer) // 4

        # 表格实例化
            table_views = Table()
            table_views.result_set_rows_cols(int(self.rows))
            table_views.result_set_values(int(self.rows), self.answer)

            for i in self.table_display:
                self.horizontalLayout_4.removeWidget(i)
                delete(i)

            self.table_display.clear()
            self.table_display.append(table_views)
            self.horizontalLayout_4.addWidget(self.table_display[0])
        except:
            pass
        finally:
            pass

    def new_file(self, testdir):
        list = os.listdir(testdir)
        list.sort(key=lambda fn: os.path.getmtime(testdir + '\\' + fn))
        filetime = datetime.fromtimestamp(os.path.getmtime(testdir + list[-1]))
        return os.path.join(testdir, list[-1])

    def save_as(self):
        if (len(self.counts.result_list)):
            try:
                self.path_in = self.new_file(u'../weight_result/')
                with open(self.path_in, 'r', encoding='utf-8') as csvfile:
                    self.rd = reader(csvfile)
                    self.save = list(self.rd)
            except:
                print('No such file!')
            finally:
                pass
            try:
                self.fileName = QFileDialog.getSaveFileName(self,
                                                            r'创建表格文件并保存',
                                                            r'C:/',
                                                            r'Csv Files(*.csv)')
                with open(self.fileName[0], 'w', newline='') as f_out:
                    write = writer(f_out)
                    write.writerows(self.save)
                    self.statusBar.showMessage("另存数据成功！！")
            except:
                self.statusBar.showMessage("另存数据失败！！")
                print('save_to failed!')

    def retranslateUi(self, MainWindow):
        _translate = QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "动态生猪高精度称重系统"))
        self.pushButton.setText(_translate("MainWindow", "文件导入"))
        self.pushButton_2.setText(_translate("MainWindow", "结果显示"))
        self.pushButton_3.setText(_translate("MainWindow", "结果分析"))
        self.pushButton_4.setText(_translate("MainWindow", " 结果另存为 "))