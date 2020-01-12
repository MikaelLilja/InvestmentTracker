from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPalette
from PyQt5.QtWidgets import QApplication, QLabel, QPushButton, QMessageBox

app = QApplication([])
app.setStyle('Fusion')

palette = QPalette()
palette.setColor(QPalette.ButtonText, Qt.darkBlue)
app.setPalette(palette)

app.setStyleSheet("QPushButton { margin: 5ex; }")

button = QPushButton('Hello World!')

def on_button_clicked():
    alert = QMessageBox()
    alert.setText('You clicked the button!')
    alert.exec_()

button.clicked.connect(on_button_clicked)
button.show()
app.exec_()
