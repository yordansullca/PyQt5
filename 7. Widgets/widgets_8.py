import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QSlider
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle('My App')
        
        widget = QSlider()
        widget.setMinimum(-10)
        widget.setMaximum(3)
        # Tambien se puede establecer un rango.
        # widget.setRange(-10, 3)
        
        #widget.setSingleStep(3)
        widget.setOrientation(Qt.Horizontal)
        
        
        widget.valueChanged.connect(self.value_changed)
        widget.sliderMoved.connect(self.slider_position)
        widget.sliderPressed.connect(self.slider_pressed)
        widget.sliderReleased.connect(self.slider_released)
        
        self.setCentralWidget(widget)
    
    def mousePressEvent(self, e):
        if e.button() == Qt.LeftButton:
            print(self.centralWidget().value())
            
    def value_changed(self, i):
        print(i)
    
    def slider_position(self, p):
        print('position ', p)
    
    def slider_pressed(self, x):
        print('Pressed!', x)
    
    def slider_released(self):
        print('Released!')
    
app = QApplication(sys.argv)
window = MainWindow()
window.show()

app.exec_()