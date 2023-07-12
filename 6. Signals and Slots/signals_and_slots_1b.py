import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My App")
        
        button = QPushButton("Press Me!")
        button.setCheckable(True)
        button.clicked.connect(self.the_button_was_clicked)
        button.clicked.connect(self.the_button_was_toggled)
        self.setCentralWidget(button)
        
    def the_button_was_clicked(self):
        print('Clicked!', self)
        
    def the_button_was_toggled(self, x):
        print('Checked?: ', x)
        
app = QApplication(sys.argv)
window = MainWindow()
window.show()

app.exec_()