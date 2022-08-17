import sys
from menu1 import *
from PyQt5 import QtCore
from PyQt5.QtCore import QPropertyAnimation
from PyQt5 import QtCore, QtGui, QtWidgets
from calculadora1 import Ui_MainWindow
from imagesdev import *
from imagesint import *
import webbrowser

class MiApp(QMainWindow):
	def __init__(self):
		super().__init__()
		self.ui = Ui_Menu() 
		self.ui.setupUi(self)
        #eliminar barra y de titulo - opacidad
		self.setWindowFlag(Qt.FramelessWindowHint)
		self.setWindowOpacity(1)
        #SizeGrip
		self.gripSize = 10
		self.grip = QtWidgets.QSizeGrip(self) 
		self.grip.resize(self.gripSize, self.gripSize)
		# mover ventana 
		self.ui.frame_superior.mouseMoveEvent = self.mover_ventana
		#acceder a las paginas
		self.ui.bt_inicio.clicked.connect(lambda: self.ui.stackedWidgetPages.setCurrentWidget(self.ui.page_inicio))
		self.ui.bt_derivada.clicked.connect(lambda: self.ui.stackedWidgetPages.setCurrentWidget(self.ui.page_dev))
		self.ui.bt_integral.clicked.connect(lambda: self.ui.stackedWidgetPages.setCurrentWidget(self.ui.page_int))
		self.ui.bt_manual.clicked.connect(lambda: self.ui.stackedWidgetPages.setCurrentWidget(self.ui.page_manual))
		#control barra de titulos
		self.ui.bt_minimizar.clicked.connect(self.control_bt_minimizar)	
		self.ui.bt_maximizar.clicked.connect(self.control_bt_maximizar)
		self.ui.bt_restaurar.clicked.connect(self.control_bt_normal)
		self.ui.bt_cerrar.clicked.connect(lambda: self.close())
		self.ui.bt_restaurar.hide()
		self.ui.bt_calculadora.clicked.connect(self.cambiarmenu)
		
        #menu lateral
		self.ui.bt_menu.clicked.connect(self.mover_menu)
		#seleccion de imagen
		self.ui.comboBox_dev.currentIndexChanged.connect(self.derv_box)
		self.ui.comboBox_int.currentIndexChanged.connect(self.int_box)
		self.ui.button_formulario_dev.clicked.connect(self.botonformulariodev)
		self.ui.button_formuarlio_int.clicked.connect(self.botonformularioint)

		self.ui.button_mascontenido_dev.clicked.connect(self.mascontenidodev)
		self.ui.button_mascontenido_int.clicked.connect(self.mascontenidoint)
		
	def cambiarmenu(self):
		self.window = QtWidgets.QMainWindow()
		self.ai = Ui_MainWindow() 
		self.ai.setupUi(self.window) 
		self.window.show()

	def control_bt_normal(self):
		self.showNormal()
		self.ui.bt_restaurar.hide()
		self.ui.bt_maximizar.show()	
	def control_bt_maximizar(self):
		self.showMaximized()
		self.ui.bt_maximizar.hide()
		self.ui.bt_restaurar.show()
	def control_bt_minimizar(self):
		self.showMinimized()
	## SizeGrip
	def resizeEvent(self, event):
		rect = self.rect()
		self.grip.move(rect.right() - self.gripSize, rect.bottom() - self.gripSize)
	## mover ventana
	def mousePressEvent(self, event):
		self.clickPosition = event.globalPos()
	def mover_ventana(self, event):
		if self.isMaximized() == False:			
			if event.buttons() == Qt.LeftButton:
				self.move(self.pos() + event.globalPos() - self.clickPosition)
				self.clickPosition = event.globalPos()
				event.accept()

		if event.globalPos().y() <=20:
			self.showMaximized()
		else:
			self.showNormal()		
    #Mover Menu
	def mover_menu(self):
		if True:
			width = self.ui.frame_lateral.width()
			normal = 0
			if width == 0:
				extender = 200
			else: 
				extender = normal
			self.animacion = QPropertyAnimation(self.ui.frame_lateral, b'minimumWidth')  
			self.animacion.setDuration(300)
			self.animacion.setStartValue(width)
			self.animacion.setEndValue(extender)
			self.animacion.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
			self.animacion.start() 
	#mostrar imagenes
	def derv_box(self):
		dev = self.ui.comboBox_dev.currentText()
		image = iconodesdeBase64(EJEMDEV1)
		image1 = iconodesdeBase64(EJEMDEV2)
		image2 = iconodesdeBase64(EJEMDEV3)
		if dev == "Ejemplo1":
			self.ui.label_dev.setPixmap(QtGui.QPixmap(image))
		if dev == "Ejemplo2":
			self.ui.label_dev.setPixmap(QtGui.QPixmap(image1))	
		if dev == "Ejemplo3":
			self.ui.label_dev.setPixmap(QtGui.QPixmap(image2))	

	def int_box(self):
		int = self.ui.comboBox_int.currentText()
		image = iconodesdeBase64(EJEMIN1)
		image1 = iconodesdeBase64(EJEMIN2)
		image2 = iconodesdeBase64(EJEMIN3)
		image3 = iconodesdeBase64(EJEMIN4)
		if int == "Ejemplo1":
			self.ui.label_int.setPixmap(QtGui.QPixmap(image))
		if int == "Ejemplo2":
			self.ui.label_int.setPixmap(QtGui.QPixmap(image1))	
		if int == "Ejemplo3":
			self.ui.label_int.setPixmap(QtGui.QPixmap(image2))	
		if int == "Ejemplo4":
			self.ui.label_int.setPixmap(QtGui.QPixmap(image3))
	def botonformulariodev(self):
		image = iconodesdeBase64(FORMDEV)
		self.ui.label_dev.setPixmap(QtGui.QPixmap(image))
	def botonformularioint(self):
		image = iconodesdeBase64(FORMINT)
		self.ui.label_int.setPixmap(QtGui.QPixmap(image))
	def mascontenidoint(self):
		webbrowser.open("https://www.youtube.com/watch?v=d7Y9Om4KCUM&list=PLrRyf2WHbKIu6Vz3eAwXW7cWtLwCBSpMg")
	def mascontenidodev(self):	
		webbrowser.open("https://www.youtube.com/watch?v=uK4-s0ojHFg&list=PLeySRPnY35dG2UQ35tPsaVMYkQhc8Vp__")
def iconodesdeBase64(base64):
	pixmap = QPixmap()
	pixmap.loadFromData(QByteArray.fromBase64(base64))
	return pixmap
	
if __name__ == "__main__":
     app = QApplication(sys.argv)
     mi_app = MiApp()
     mi_app.show()
     sys.exit(app.exec_())	