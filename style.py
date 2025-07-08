import qdarkstyle

# Apenas tipagem
from PySide6.QtWidgets import QApplication
                                   

def setupTheme(app: QApplication):
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyside6())
    app.setStyleSheet(app.styleSheet() + qss)


qss = """
    QPushButton[cssClass="specialButton"] {
        color: #fff;
        background: #1e81b0;
        border-radius: 5px;
    }
    QPushButton[cssClass="specialButton"]:hover {
        color: #fff;
        background: #16658a;
    }
    QPushButton[cssClass="specialButton"]:pressed {
        color: #fff;
        background: #115270;
    }
"""

