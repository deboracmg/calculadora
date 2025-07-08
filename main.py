from PySide6.QtWidgets import QApplication
from PySide6.QtGui import QIcon
from pathlib import Path
from display import Display, Info
from style import setupTheme
from window import MyWindow
from buttons import SetupButtons


if __name__ == '__main__':
    ROOT_DIR = Path(__file__).parent
    ICON_PATH = ROOT_DIR / 'icon.ico'

    app = QApplication()
    setupTheme(app)
    window = MyWindow()

    icon = QIcon(str(ICON_PATH))
    window.setWindowIcon(icon)
    app.setWindowIcon(icon)

    info = Info('')
    window.addToLayout(info)

    display = Display()
    window.addToLayout(display)

    btnGrid = SetupButtons(display, info, window)
    window.vLayout.addLayout(btnGrid)

    window.adjustSize()
    window.setFixedSize(window.width(), window.height())

    window.show()
    app.exec()


# Para a criação de um aplicativo executável pode-se utilizar o pyinstaller,
# com o seguinte comando:
# 
# pyinstaller --name="Calculadora" --noconfirm --onefile --icon="calculadora\icon.ico"
# --noconsole --clean --distpath="appCalc\dist" --workpath="appCalc\build"
# --specpath=appCalc\ "calculadora\main.py"
