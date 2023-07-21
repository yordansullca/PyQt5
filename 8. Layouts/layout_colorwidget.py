# Importamos la clase base widget que es la base de todos los widgets.
from PyQt5.QtWidgets import QWidget
'''
Importamos la clase QColor que nos permite definir un color.
Importamos la clase QPalette que nos permite definir la paleta de colores de un widget.
'''
from PyQt5.QtGui import QColor, QPalette
import sys

'''
Creamos una clase que hereda de QWidget, para crear un widget personalizado.
'''
class Color(QWidget):
    def __init__(self, color):
        super().__init__()
        '''
        Habilita la función de autorellenar el fondo del 
        widget con el color definido.
        '''
        self.setAutoFillBackground(True)
        
        '''
        Obtiene la paleta de colores actual del widget.
        La paleta contiene los colores y pinceles que 
        se utilizan para representar los diferentes
        elementos del widget.
        '''
        palette = self.palette()
        
        '''
        Establece el color de fondo(Window) de la paleta del widget
        utilizando el valor de color proporcionado.
        El parámetro color deber ser un objeto QColor, que representa
        un color RGB o RGBA.
        '''
        palette.setColor(QPalette.Window, QColor(color))
        
        '''
        Aplica la paleta actualizada al widget. Establece el color de fondo
        del wifget según el color proporcionado por la paleta.
        '''
        self.setPalette(palette)
        
