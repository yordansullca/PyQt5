import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication,
    QHBoxLayout,
    QMainWindow,
    QPushButton,
    QStackedLayout,
    QVBoxLayout,
    QWidget,
)

from layout_colorwidget import Color

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("My App")
        pageLayout = QVBoxLayout()
        button_layout = QHBoxLayout()
        self.stackLayout = QStackedLayout()
        
        pageLayout.addLayout(button_layout)
        pageLayout.addLayout(self.stackLayout)
        
        btn = QPushButton("Red")
        btn.pressed.connect(self.activate_tab_1)
        button_layout.addWidget(btn)
        self.stackLayout.addWidget(Color("red"))
        
        btn = QPushButton("Green")
        btn.pressed.connect(self.activate_tab_2)
        button_layout.addWidget(btn)
        self.stackLayout.addWidget(Color("green"))
        
        btn = QPushButton("Blue")
        btn.pressed.connect(self.activate_tab_3)
        button_layout.addWidget(btn)
        self.stackLayout.addWidget(Color("blue"))
        
        btn = QPushButton("Yellow")
        btn.pressed.connect(self.activate_tab_4)
        button_layout.addWidget(btn)
        self.stackLayout.addWidget(Color("yellow"))
        
        widget = QWidget()
        widget.setLayout(pageLayout)
        self.setCentralWidget(widget)
        
    def activate_tab_1(self):
        self.stackLayout.setCurrentIndex(0)
    
    def activate_tab_2(self):
        self.stackLayout.setCurrentIndex(1)
        
    def activate_tab_3(self):
        self.stackLayout.setCurrentIndex(2)
    
    def activate_tab_4(self):
        self.stackLayout.setCurrentIndex(3)

app = QApplication(sys.argv)
window = MainWindow()
window.show()

app.exec_()