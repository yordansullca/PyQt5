import sys
from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
 
        self.setWindowTitle('My App')
        
        self.setFixedSize(QSize(400, 300))
        self.setMinimumSize(QSize(200, 200))
        self.setMaximumSize(QSize(600, 400))
        
        button = QPushButton('Press Me!')
        
        self.setCentralWidget(button)
    
        
app = QApplication(sys.argv)
window = MainWindow()
window.show()
print(QSize(410, 200))
app.exec_()