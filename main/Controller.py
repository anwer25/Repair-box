from main.login_main_ import MainLogin
from main.register_ import MainRegister
from main.main_ import Main
from main.loading_ import MainWindow

class controller:

    def __init__(self):
        pass
    def show_loding_from_login(self):
        self.loadingWindow = MainWindow()
        self.loadingWindow.switch_window.connect(self.show_login)

    def show_loding_from_register(self):
        self.loadingWindow = MainWindow()
        self.loadingWindow.switch_window.connect(self.show_register)

    def show_login(self):
        self.login_windo = MainLogin()
        self.loadingWindow.close()
        self.login_windo.switch_window.connect(self.show_main_from_login)

    def show_register(self):
        self.register_ = MainRegister()
        self.loadingWindow.close()
        self.register_.switch_window.connect(self.show_main_from_register)

    def show_main_from_login(self):
        self.mainWindow = Main()
        self.login_windo.close()

    def show_main_from_register(self):
        self.mainWindow__ = Main()
        self.register_.close()
