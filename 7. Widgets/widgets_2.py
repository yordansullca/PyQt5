import sys
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow
from PyQt5.QtGui import QPixmap

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("My App")
        
        widget = QLabel("Hello")
        widget.setPixmap(QPixmap("7. Widgets\inter.png"))
        widget.setScaledContents(True)
        
        self.setCentralWidget(widget)
        
app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec_()