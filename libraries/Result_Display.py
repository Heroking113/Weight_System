from datetime import datetime
from libraries.result_view import *
from libraries.Data_Input import *

class Result_Display(object):
    def __init__(self):
        super(Result_Display, self).__init__()
    def table_view_model(self):
        self.result_data = Data_Input()
        print(self.result_data.results)
        if(len(self.result_data.results)):
            try:
                self.path_in = self.new_file(u'../weight_result/')
                with open(self.path_in, 'r', encoding='utf-8') as csvfile:
                    self.rd = reader(csvfile)
                    self.answer = list(self.rd)
                self.answer = [float(self.answer[i][2]) for i in range(1, len(self.answer))]
            except:
                print('No such file!')

        # 计算table行数
        self.rows = 0
        if (len(self.answer) % 4 == 0):
            self.rows = len(self.answer) / 4
        else:
            self.rows = 1 + len(self.answer) // 4

        # 表格实例化
        self.tables = Table()
        self.tables.set_rows_cols(int(self.rows))
        self.tables.set_values(int(self.rows), self.answer)


    def new_file(self, testdir):
        list = os.listdir(testdir)
        list.sort(key=lambda fn: os.path.getmtime(testdir + '\\' + fn))
        filetime = datetime.fromtimestamp(os.path.getmtime(testdir + list[-1]))
        return os.path.join(testdir, list[-1])