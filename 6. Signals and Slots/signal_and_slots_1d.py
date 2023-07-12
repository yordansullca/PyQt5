import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.button_is_checked = True
        self.setWindowTitle("My App")
        
        self.button = QPushButton("Press Me!")
        self.button.setCheckable(True)
        self.button.released.connect(self.the_button_was_relesead)
        self.button.setChecked(self.button_is_checked)
        
        self.setCentralWidget(self.button)
        
    def the_button_was_relesead(self):
        self.button_is_checked = self.button.isChecked()
        print(self.button_is_checked)
        
app = QApplication(sys.argv)
window = MainWindow()
window.show()

app.exec_()