from PyQt5.QtCore import Qt, pyqtBoundSignal, qWarning
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout

app = QApplication([])
main_win = QWidget()
main_win.setWindowTitle('Определитель победителя')
button = QPushButton('Сгенерировать')
text = QLabel('Нажми, что бы узнать победителя')
winner = QLabel('?')

line = QVBoxLayout()
line.addWidget(text, alignment = Qt.AlignCenter)
line.addWidget(winner, alignment = Qt.AlignCenter)
line.addWidget(button, alignment = Qt.AlignCenter)
main_win.setLayout(line)

main_win.show()
app.exec_()