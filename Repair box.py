from PyQt5.QtWidgets import QApplication
import sys
from os import path
from main.Controller import controller


def main_programme():
    if path.exists('db'):
        app = QApplication(sys.argv)
        controllers = controller()
        controllers.show_loding_from_login()
        sys.exit(app.exec_())

    else:
        app = QApplication(sys.argv)
        controllers = controller()
        controllers.show_loding_from_register()
        sys.exit(app.exec_())


if __name__ == '__main__':
    main_programme()
