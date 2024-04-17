
from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QLabel,
    QPushButton,
    QVBoxLayout,
    QHBoxLayout,
    QMessageBox,
)
import sys

from gui import MainMenuWidget, LoginWidget
from connection import AccountManager
from Login_form import AdvancedLoginForm
class HomePage(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Home Page")
        self.setGeometry(100, 100, 400, 300)

        self.login_button = QPushButton("Login")
        self.login_button.setStyleSheet("background-color: #4CAF50; color: white")
        self.login_button.clicked.connect(self.show_login_form)
        self.hide()
        layout = QVBoxLayout()
        layout.addWidget(QLabel("<h1>Welcome to Banking System</h1>"))
        layout.addWidget(self.login_button)

        self.setLayout(layout)

        self.login_form = AdvancedLoginForm()
        self.login_form.setWindowTitle("Login")
    
       def show_login_form(self):
        self.login_form.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    home_page = HomePage()
    home_page.show()
    sys.exit(app.exec_())
