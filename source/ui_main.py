import PySide2
from qt_material import list_themes
from pprint import pprint  # 导入pprint接口，可以打印出更加漂亮的list列表数据
from qt_material import apply_stylesheet
from PySide2.QtWidgets import QApplication, QMessageBox
from PySide2.QtUiTools import QUiLoader
from threading import Thread
import os

envpath = r'E:\anaconda\Lib\site-packages\PySide2\plugins\platforms'
os.environ["QT_QPA_PLATFORM_PLUGIN_PATH"] = envpath

theme = ['dark_amber.xml',
         'dark_blue.xml',
         'dark_cyan.xml',
         'dark_lightgreen.xml',
         'dark_medical.xml',
         'dark_pink.xml',
         'dark_purple.xml',
         'dark_red.xml',
         'dark_teal.xml',
         'dark_yellow.xml',
         'light_amber.xml',
         'light_blue.xml',
         'light_blue_500.xml',
         'light_cyan.xml',
         'light_cyan_500.xml',
         'light_lightgreen.xml',
         'light_lightgreen_500.xml',
         'light_orange.xml',
         'light_pink.xml',
         'light_pink_500.xml',
         'light_purple.xml',
         'light_purple_500.xml',
         'light_red.xml',
         'light_red_500.xml',
         'light_teal.xml',
         'light_teal_500.xml',
         'light_yellow.xml']


class Stats:

    def __init__(self):
        # 从文件中加载UI定义

        # 从 UI 定义中动态 创建一个相应的窗口对象
        # 注意：里面的控件对象也成为窗口对象的属性了
        # 比如 self.ui.button , self.ui.textEdit
        self.ui = QUiLoader().load('6常用控件1.ui')

        self.ui.setWindowTitle('海运数据爬取分析')


x = 10
app = QApplication([])
apply_stylesheet(app, theme[x])
stats = Stats()
stats.ui.show()
app.exec_()

# pprint('总计主题样式：{} 种！'.format(len(list_themes())))
# pprint(list_themes())

# 'dark_amber.xml',
# 'dark_blue.xml',
# 'dark_cyan.xml',
# 'dark_lightgreen.xml',
# 'dark_medical.xml',
# 'dark_pink.xml',
# 'dark_purple.xml',
# 'dark_red.xml',
# 'dark_teal.xml',
# 'dark_yellow.xml',
# 'light_amber.xml',
# 'light_blue.xml',
# 'light_blue_500.xml',
# 'light_cyan.xml',
# 'light_cyan_500.xml',
# 'light_lightgreen.xml',
# 'light_lightgreen_500.xml',
# 'light_orange.xml',
# 'light_pink.xml',
# 'light_pink_500.xml',
# 'light_purple.xml',
# 'light_purple_500.xml',
# 'light_red.xml',
# 'light_red_500.xml',
# 'light_teal.xml',
# 'light_teal_500.xml',
# 'light_yellow.xml'
