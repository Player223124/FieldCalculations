from PyQt5 import QtWidgets
from ui import Ui_MainWindow
import algorithm 

def res():
    if ui.Expression.isChecked() == True:
        if algorithm.IsPrime(ui.FieldEnter.toPlainText()):
            ui.TextOut.setText(str(algorithm.counting(ui.TextEnter.toPlainText(), ui.FieldEnter.toPlainText())))
        else:
            ui.TextOut.setText('Поле не является простым числом.')
            
    elif ui.Reverse.isChecked() == True:
        if algorithm.IsPrime(ui.FieldEnter.toPlainText()):
            ui.TextOut.setText(str(algorithm.revers2(ui.TextEnter.toPlainText(), ui.FieldEnter.toPlainText())))
        else:
            ui.TextOut.setText('Поле не является простым числом.')

if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()

    ui.Button.clicked.connect(lambda: res())

    sys.exit(app.exec_())