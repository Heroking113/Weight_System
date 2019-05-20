from PyQt5.QtWidgets import QWidget, QHeaderView, QVBoxLayout, QTableView
from PyQt5.QtGui import QStandardItem, QStandardItemModel

class Data_Analysis_1(QWidget):
    def __init__(self,parent=None):
        super(Data_Analysis_1, self).__init__(parent)
        #设置标题与初始大小
        self.setWindowTitle('QTableView表格视图的例子')
        self.resize(500,300)

    # 分段分析,获取每一列的值
    def analysis1_subsection(self, data_list):
        self.up = int(10*(1+max(data_list)//10)+1)
        self.down = int(10*(min(data_list)//10))

        self.subsection=[]
        for i in range(self.down, self.up, 5):
            self.subsection.append(i)

        self.subsection_num = [0 for i in range(len(self.subsection))]
        for i in range(len(self.subsection)):
            for j in data_list:
                if float(self.subsection[i])<=j<=float(self.subsection[i+1]):
                    self.subsection_num[i]+=1

        self.indexs=[]
        self.indexs = [i for i, x in enumerate(self.subsection_num) if x==0]
        while 0 in self.subsection_num:
            self.subsection_num.remove(0)

        for i in [self.subsection[i] for i in self.indexs]:
            self.subsection.remove(i)

        self.subsection_proportion=[]
        for i in range(len(self.subsection)):
            self.subsection_proportion.append(str("{:.2f}%".format((self.subsection_num[i]/len(data_list))*100)))
        self.rows=len(self.subsection)

        self.analysis1_set_rows_cols()

    # 设置表格的行列值
    def analysis1_set_rows_cols(self):

        self.model=QStandardItemModel(self.rows,3)
        self.cols_title = [u'分段统计(5kg一段)', u'数量', u'比例']
        self.model.setHorizontalHeaderLabels(self.cols_title)

        for i in range(self.rows):
            self.model.setItem(i, 0, QStandardItem("%s"%(str(self.subsection[i])+'~'+str(self.subsection[i]+5))))
            self.model.setItem(i, 1, QStandardItem("%s"%str(self.subsection_num[i])))
            self.model.setItem(i, 2, QStandardItem("%s"%str(self.subsection_proportion[i])))


        #实例化表格视图，设置模型为自定义的模型
        self.tableView=QTableView()
        self.tableView.setModel(self.model)

        #todo 优化1 表格填满窗口
        #水平方向标签拓展剩下的窗口部分，填满表格
        self.tableView.horizontalHeader().setStretchLastSection(True)
        self.tableView.verticalHeader().setVisible(False)
        #水平方向，表格大小拓展到适当的尺寸
        self.tableView.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        #TODO 优化3 删除当前选中的数据
        indexs=self.tableView.selectionModel().selection().indexes()
        if len(indexs)>0:
            index=indexs[0]
            self.model.removeRows(index.row(),1)

        #设置布局
        layout=QVBoxLayout()
        layout.addWidget(self.tableView)
        self.setLayout(layout)

class Data_Analysis_2(QWidget):
    def __init__(self,parent=None):
        super(Data_Analysis_2, self).__init__(parent)
        #设置标题与初始大小
        self.setWindowTitle('QTableView表格视图的例子')
        self.resize(500,300)

    # 设置表格的行列值
    def analysis2_set_rows_cols(self, data_list):
        self.model=QStandardItemModel(1,3)
        self.cols_title = [u'体重最大值(kg)', u'体重最小值(kg)', u'差值(kg)']
        self.model.setHorizontalHeaderLabels(self.cols_title)
        self.mx=max(data_list)
        self.mn=min(data_list)
        self.model.setItem(0, 0, QStandardItem("%s"%str(self.mx)))
        self.model.setItem(0, 1, QStandardItem("%s"%str(self.mn)))
        self.model.setItem(0, 2, QStandardItem("{:.3f}".format(float(float(self.mx)-float(self.mn)))))

        #实例化表格视图，设置模型为自定义的模型
        self.tableView=QTableView()
        self.tableView.setModel(self.model)

        #todo 优化1 表格填满窗口
        #水平方向标签拓展剩下的窗口部分，填满表格
        self.tableView.horizontalHeader().setStretchLastSection(True)
        self.tableView.verticalHeader().setVisible(False)
        #水平方向，表格大小拓展到适当的尺寸
        self.tableView.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        # 不可编辑
        # self.setEditable(False)

        #TODO 优化3 删除当前选中的数据
        indexs=self.tableView.selectionModel().selection().indexes()
        if len(indexs)>0:
            index=indexs[0]
            self.model.removeRows(index.row(),1)

        #设置布局
        layout=QVBoxLayout()
        layout.addWidget(self.tableView)
        self.setLayout(layout)