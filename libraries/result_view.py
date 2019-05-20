from PyQt5.QtWidgets import QWidget, QTableView, QHeaderView, QVBoxLayout
from PyQt5.QtGui import QStandardItemModel, QStandardItem

class Table(QWidget):
    def __init__(self,parent=None):
        super(Table, self).__init__(parent)
        #设置标题与初始大小
        self.setWindowTitle('QTableView表格视图的例子')
        self.resize(500,300)

    # 设置表格的行列值
    def result_set_rows_cols(self,rows, cols=8):
        self.model=QStandardItemModel(rows,cols)

        #设置水平方向四个头标签文本内容
        self.cols_title=[]
        for i in range(cols):
            if(i%2):
                self.cols_title.append(u'体重(kg)')
            else:
                self.cols_title.append(u'编号')
        self.model.setHorizontalHeaderLabels(self.cols_title)

    #     设置文本值
    def result_set_values(self, rows, data_list, cols=8):
        number = 1
        k=0
        for column in range(cols):
            for row in range(rows):
                #设置每个位置的文本值
                if(column%2==0 and number<=len(data_list)):
                    self.model.setItem(row, column, QStandardItem("%s"%str(number)))
                    number+=1
                elif(column%2!=0 and k<len(data_list)):
                    self.model.setItem(row, column, QStandardItem("%s"%str(data_list[k])))
                    k+=1

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
        # print(indexs)
        if len(indexs)>0:
            index=indexs[0]
            self.model.removeRows(index.row(),1)

        #设置布局
        layout=QVBoxLayout()
        layout.addWidget(self.tableView)
        self.setLayout(layout)