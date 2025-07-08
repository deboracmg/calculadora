from PySide6.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QMessageBox


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        central_widget = QWidget()
        self.vLayout = QVBoxLayout()

        self.setCentralWidget(central_widget)
        self.setWindowTitle('Calculadora')
        central_widget.setLayout(self.vLayout)
    
    def addToLayout(self, widget: QWidget):
        self.vLayout.addWidget(widget)
    
    def makeMsgBox(self):
        return QMessageBox(self)
    
