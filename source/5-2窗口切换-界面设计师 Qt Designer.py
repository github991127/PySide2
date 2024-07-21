from PySide2 import QtWidgets
from PySide2.QtUiTools import QUiLoader
import sys
import os
envpath = r'E:\anaconda\Lib\site-packages\PySide2\plugins\platforms'
os.environ["QT_QPA_PLATFORM_PLUGIN_PATH"] = envpath
main_win = None

class LoginWin:

    def __init__(self):
        super().__init__()
        self.ui = QUiLoader().load('5-2/login.ui')
        self.ui.btn_login.clicked.connect(self.onLogin)

    def onLogin(self):
        global main_win
        main_win = Window_Main()
        # 显示新窗口
        main_win.ui.show()
        # 关闭自己
        self.ui.close()
        # 隐藏自己，数据不丢失
        # self.ui.hide()

class Window_Main:
    def __init__(self):
        super().__init__()
        self.ui = QUiLoader().load('5-2/main.ui')

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    wm = LoginWin()
    wm.ui.show()
    sys.exit(app.exec_())