import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QSpinBox, QDoubleSpinBox
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        widget = QSpinBox()
        #widget = QDoubleSpinBox()
        widget.setMinimum(-10)
        widget.setMaximum(3)
        # Tambien podemos colocar rango en vez de maximo y minimo
        #widget.setRange(-10, 3)
        
        widget.setPrefix("$")
        widget.setSuffix("c")
        # Para QDoubleSpinBox podemos colocar la cantidad de decimales
        widget.setSingleStep(3)
        
        widget.valueChanged.connect(self.value_changed)
        widget.valueChanged[str].connect(self.value_changed_srt)
        
        self.setCentralWidget(widget)
        
    def value_changed(self, i):
        print(i)
    
    def value_changed_srt(self, s):
        print(s)
        
app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()