from PySide6.QtWidgets import QLineEdit, QLabel
from PySide6.QtCore import Qt, Signal
from PySide6.QtGui import QKeyEvent
from utilities import isNumOrDot


class Display(QLineEdit):
    equalPressed = Signal()
    backPressed = Signal()
    delPressed = Signal()
    inputPressed = Signal(str)
    operatorPressed = Signal(str)
    negativePressed = Signal()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.configStyle()

    def configStyle(self):
        self.setStyleSheet('font-size: 25px')
        self.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.setMinimumHeight(50)
        self.setMinimumWidth(100)
    
    def keyPressEvent(self, event: QKeyEvent):
        text = event.text().strip()
        key = event.key()
        KEYS = Qt.Key

        isDel = key in [KEYS.Key_Escape, KEYS.Key_Delete]
        isBack = key in [KEYS.Key_Backspace]
        isNegative = key in [KEYS.Key_N]
        isEq = key in [KEYS.Key_Enter, KEYS.Key_Return, KEYS.Key_Equal]
        isOperator = key in [KEYS.Key_Plus, KEYS.Key_Minus, KEYS.Key_Slash,
                             KEYS.Key_Asterisk, KEYS.Key_P, KEYS.Key_N]

        if isDel:
            self.delPressed.emit()
            return event.ignore()

        if isBack:
            self.backPressed.emit()
            return event.ignore()
        
        if isNegative:
            self.negativePressed.emit()
            return event.ignore()

        if isEq:
            self.equalPressed.emit()
            return event.ignore()
        
        if isOperator:
            if text.upper() == 'P':
                text = '^'
            self.operatorPressed.emit(text)
            return event.ignore()

        if isNumOrDot(text):
            self.inputPressed.emit(text)
            return event.ignore()


class Info(QLabel):
    def __init__(self, text):
        super().__init__(text)
        self.configStyle()

    def configStyle(self):
        self.setStyleSheet('font-size: 15px')
        self.setAlignment(Qt.AlignmentFlag.AlignRight)

