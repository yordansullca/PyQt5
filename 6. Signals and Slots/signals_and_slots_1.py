from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
from PyQt5.QtCore import Qt

import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("My App")
        
        self.button = QPushButton("Press Me!")
        self.button.setCheckable(False)
        self.button.clicked.connect(self.the_button_was_clicked)

        self.setCentralWidget(self.button)
    
    def the_button_was_clicked(self):
        if self.button.isChecked():
            print('El botón está presionado')
        else:
            print('El botón no está presionado')
        
app = QApplication(sys.argv)
window = MainWindow()
window.show()

app.exec_()