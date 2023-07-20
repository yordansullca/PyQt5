import sys

from PyQt5.QtWidgets import QApplication, QLineEdit, QMainWindow
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")
        self.widget = QLineEdit()
        self.widget.setMaxLength(10)
        self.widget.setPlaceholderText('Enter your text')
        self.widget.setInputMask('000.00.00')
        
        # Estable la edición o lectura del texto
        #widget.setReadOnly(True)
        
        #self.widget.returnPressed.connect(self.return_pressed)
        #self.widget.selectionChanged.connect(self.selection_changed)
        self.widget.textChanged.connect(self.text_changed)
        self.widget.textEdited.connect(self.text_edit)

        self.setCentralWidget(self.widget)

    def return_pressed(self):
        print("Return pressed!")
        text = self.widget.text()
        print(text)
        # Otra opcion
        self.centralWidget().setText("Hello " + text)
        
        
    def selection_changed(self):
        print("Selection changed")
        print(self.widget.selectedText())
        print(self.centralWidget().selectedText())
    
    def text_changed(self, s):
        print("Text changed...")
        print(s)
    
    def text_edit(self, s):
        print("Text edited...")
        print(s)
        
app = QApplication(sys.argv)
window = MainWindow()
window.show()

app.exec_()