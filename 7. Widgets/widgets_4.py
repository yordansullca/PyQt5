import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QComboBox, QMainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("My App")
        
        widget = QComboBox()
        widget.addItems(['One', 'Two', 'Three'])
        
        
        widget.currentIndexChanged.connect(self.index_changed)
        widget.currentTextChanged.connect(self.text_changed)
        widget.setInsertPolicy(QComboBox.InsertAtTop)
        widget.setEditable(True)
        widget.setMaxCount(5)
        self.setCentralWidget(widget)
    
    def index_changed(self, i):
        print(i)
    
    def text_changed(self, s):
        print(s)

app = QApplication(sys.argv)
window = MainWindow()
window.show()

app.exec_()