from PySide2.QtWidgets import QApplication, QMessageBox
from PySide2.QtUiTools import QUiLoader
from threading import Thread
import os
envpath = r'E:\anaconda\Lib\site-packages\PySide2\plugins\platforms'
os.environ["QT_QPA_PLATFORM_PLUGIN_PATH"] = envpath

class Stats:

    def __init__(self):
        # 从文件中加载UI定义

        # 从 UI 定义中动态 创建一个相应的窗口对象
        # 注意：里面的控件对象也成为窗口对象的属性了
        # 比如 self.ui.button , self.ui.textEdit
        self.ui = QUiLoader().load('6常用控件1.ui')

        
        self.ui.setWindowTitle('海运数据爬取分析')


app = QApplication([])
stats = Stats()
stats.ui.show()
app.exec_()