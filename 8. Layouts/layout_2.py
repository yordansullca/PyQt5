import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget

from layout_colorwidget import Color

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle('My App')
        
        # Creamos un layout vertical
        layout = QVBoxLayout()
        
        # Agregamos un widget de color al layout
        layout.addWidget(Color('red'))
        layout.addWidget(Color('yellow'))
        layout.addWidget(Color('purple'))
        
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)
        
app = QApplication(sys.argv)
window = MainWindow()
window.show()

app.exec_()