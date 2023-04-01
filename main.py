from PyQt5 import QtWidgets, uic
import random
import time

app = QtWidgets.QApplication([])
ui = uic.loadUi("passwordTwo.ui")
ui.setWindowTitle("PasswordTwo")
entryTime = time.time()


def is_int(str):
    try:
        int(str)
        return True
    except ValueError:
        return False


def passwordMaker(seed, length):
    random.seed(seed)
    a = ''
    for i in range(length):
        a += chr(random.randint(33, 126))
    return a


def buttonActivated():
    seed = time.time() * (time.time() - entryTime)
    a = ui.lengthPassword.text()
    if is_int(a) and 0 < int(a) < 32768:
        length = int(a)
        ui.generatedPassword.setText(passwordMaker(seed, length))
    else:
        ui.generatedPassword.setText("Invalid password length")


ui.pushButton.clicked.connect(buttonActivated)
ui.show()
app.exec()
