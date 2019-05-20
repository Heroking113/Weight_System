import os
from time import strftime
from csv import writer,reader
from PyQt5.QtWidgets import QMessageBox, QWidget, QFileDialog
from libraries.Algorithm import *

class Data_Input(QWidget):
    def __init__(self):
        super(Data_Input, self).__init__()
        self.init_data = []
        self.middle_data = 0
        self.result_list = []
        self.analysis_pag = None
        self.init_data = None
        self.analysis_subsection = None
        self.analysis_extreme = None
        self.input_error_flag = 1
    # 导入数据并计算
    def msg(self, filename):
        with open(filename, 'r', newline='') as f_in:
            reade = reader(f_in)
            return list(reade)

    def loadDataFile(self):
        try:
            self.paths = QFileDialog.getOpenFileNames(self,
                                                  "导入初始数据",
                                                  "C:/",
                                                  "CSV Files (*.csv);;All Files (*)")
            self.result_list=[]
            for i in range(len(self.paths[0])):
                self.init_data=self.msg(self.paths[0][i])
                init_weight = [self.init_data[j][1] for j in range(len(self.init_data))]
                numbers=[self.init_data[k][0] for k in range(len(self.init_data))]
                self.first_data=average_filter(init_weight)
                self.middle_data=kalman_filter(self.first_data)
                self.middle_data = [int(self.middle_data[i]) for i in range(len(self.middle_data))]
                robust_linear = RANSACRegressor(LinearRegression())
                robust_linear.fit(np.mat(range(1, len(init_weight) + 1)).reshape(-1, 1), self.middle_data)
                self.result_list.append(str(float(int(robust_linear.predict([[len(self.middle_data) / 2]]))) / 1000))
        except:
            self.result_list=[0 for i in range(3)]
            self.message_hint("警告:采集到的数据格式有误，请检查数据源！！！", 3000)
            self.input_error_flag=0
        finally:
            pass

        if len(self.result_list):
            self.state=1
            title=['date', 'num', 'weight(kg)']
            all = []
            rows=0
            for i in range(len(self.result_list)):
                all.append([])
                all[rows].append((strftime("%Y/%m/%d")))
                all[rows].append(rows+1)
                all[rows].append(self.result_list[i])
                rows+=1

            path="./weight_result"
            file_na='{}'.format(strftime("%m_%d_%H_%M_%S"))
            if not os.path.exists(path):
                os.makedirs(path)
            try:
                with open(path + '/' + file_na + '.csv', 'w', newline='') as fi:
                    write=writer(fi)
                    write.writerow(title)
                    write.writerows(all)
                    if(self.input_error_flag):
                        self.message_hint("计算完成!保存完成！!", 1500)
            except:
                self.message_hint("警告：导入的数据格式有误，请检查数据源！！", 1500)

    def message_hint(self, str, times):
        self.infoBox = QMessageBox()
        self.infoBox.setIcon(QMessageBox.Information)
        self.infoBox.setText(str)
        self.infoBox.setWindowTitle("温馨提示：")
        self.infoBox.setStandardButtons(QMessageBox.Ok)
        self.infoBox.button(QMessageBox.Ok).animateClick(times)
        self.infoBox.exec_()
