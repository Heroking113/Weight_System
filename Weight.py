from PyQt5.QtWidgets import QApplication, QSplashScreen
from libraries.MainWindow import *
from sys import argv, exit

if __name__=="__main__":
    app=QApplication(argv)
    qsplash = QSplashScreen(QPixmap("./static/image/startup.png"))
    # qsplash.showMessage(u"程序正在加载,请稍后。。。", Qt.AlignHCenter | Qt.AlignVCenter, Qt.red)
    qsplash.show()
    # 防止界面被卡死
    app.processEvents()

    # 然后再初始化主窗体
    mainwindow=QMainWindow()
    ui=Ui_MainWindow()
    ui.setupUi(mainwindow)
    icon=QIcon()
    icon.addPixmap(QPixmap('./static/image/icon_128px.ico'), QIcon.Normal, QIcon.Off)
    mainwindow.setWindowIcon(icon)
    mainwindow.show()
    qsplash.finish(mainwindow)
    exit(app.exec_())
