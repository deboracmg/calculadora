from PySide6.QtWidgets import QGridLayout, QPushButton
from PySide6.QtCore import Slot
from utilities import isValidNumber, convertNumber
import math

# Apenas tipagem
from display import Display, Info
from window import MyWindow


class Button(QPushButton):
    def __init__(self, text):
        super().__init__(text)
        self.configStyle()

    def configStyle(self):
        self.setMinimumSize(50, 40)
        self.setStyleSheet('font-size: 20px;')


class SetupButtons(QGridLayout):
    def __init__(self, display: Display, info: Info, window: MyWindow):
        super().__init__()
        self._gridMask = [
            ['C', '◀', '^', '/'],
            ['7', '8', '9', '*'],
            ['4', '5', '6', '-'],
            ['1', '2', '3', '+'],
            ['N',  '0', '.', '='],]
        self.display = display
        self.info = info
        self.window = window
        self._equation = ''
        self._left = None
        self._right = None
        self._op = None
        self.makeGridAndConnection()

    @property
    def equation(self):
        return self._equation
    
    @equation.setter
    def equation(self, value):
        self._equation = value
        self.info.setText(value)

    def makeGridAndConnection(self):
        self.display.delPressed.connect(self._clear)
        self.display.backPressed.connect(self.display.backspace)
        self.display.negativePressed.connect(self._invertNumber)
        self.display.equalPressed.connect(self._equal)
        self.display.inputPressed.connect(self._insertToDisplay)
        self.display.operatorPressed.connect(self._operatorClicked)

        for rowNumber, row in enumerate(self._gridMask):
            for colNumber, text in enumerate(row):
                btn = Button(text)

                if text in 'C◀N^/*-+=':
                    btn.setProperty('cssClass', 'specialButton')
                    self.setupSpecialButton(btn)

                self.addWidget(btn, rowNumber, colNumber)
                slot = self._makeSlot(self._insertToDisplay, text)
                self._clickedConnectButton(btn, slot)
                

    def setupSpecialButton(self, button: Button):
        text = button.text()
        if text == 'C':
            self._clickedConnectButton(button, self._clear)
        elif text == 'N':
            self._clickedConnectButton(button, self._invertNumber)
        elif text == '◀':
            self._clickedConnectButton(button, self.display.backspace)
        elif text in '+-/*^':
            self._clickedConnectButton(button, self._makeSlot(self._operatorClicked, text))
        elif text == '=':
            self._clickedConnectButton(button, self._equal)
    
    def _clickedConnectButton(self, button: Button, slot):
        button.clicked.connect(slot)
    
    def _makeSlot(self, function, *args, **kwargs):
        @Slot()
        def mySlot():
            function(*args, **kwargs)
            self.display.setFocus()
        return mySlot

    @Slot()
    def _insertToDisplay(self, text):
        displayValue = self.display.text() + text
        if not isValidNumber(displayValue):
            return
        self.display.insert(text)

    @Slot()
    def _clear(self):
        self.equation = ''
        self._left = None
        self._right = None
        self._op = None
        self.display.clear()

    @Slot()
    def _invertNumber(self):
        displayText = self.display.text()

        if not isValidNumber(displayText):
            return
        
        number = convertNumber(displayText) * (-1)
        self.display.setText(str(number))

    @Slot()
    def _operatorClicked(self, text: str):
        displayText = self.display.text()
        self.display.clear()

        if not isValidNumber(displayText) and self._left is None:
            return    
        if isValidNumber(displayText):
            self._left = convertNumber(displayText)

        self._op = text
        self.equation = f'{self._left} {self._op} ??'

    @Slot()
    def _equal(self):
        displayText = self.display.text()
        if not isValidNumber(displayText) or self._left is None:
            return
        self._right = convertNumber(displayText)
        self.equation = f'{self._left} {self._op} {self._right}'
        result = 0

        try:
            if self._op == '^':
                result = math.pow(self._left, self._right)
            else:
                result = eval(self.equation)
        except ZeroDivisionError:
            self._showError('Divisão por zero')
            self._clear()
            return
        except OverflowError:
            self._showError('Número muito grande')
            self._clear()
            return

        result = convertNumber(str(result))
        self.display.clear()
        self.info.setText(f'{self.equation} = {result}')
        self._left = result
        self._right = None

    def _showError(self, text: str):
        msgBox = self.window.makeMsgBox()
        msgBox.setText(text)
        msgBox.setIcon(msgBox.Icon.Critical)
        msgBox.setWindowTitle('Error')
        msgBox.exec()

