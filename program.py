from PyQt5 import QtCore, QtGui, QtWidgets
from functions import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(640, 480)
        MainWindow.setMaximumSize(QtCore.QSize(16777215, 16777215))
        MainWindow.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        MainWindow.setFocusPolicy(QtCore.Qt.NoFocus)
        MainWindow.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        MainWindow.setAnimated(True)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 2, 1, 1, 1)
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.gridLayout_3.setSpacing(7)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.result_lb = QtWidgets.QLabel(self.centralwidget)
        self.result_lb.setAlignment(QtCore.Qt.AlignCenter)
        self.result_lb.setObjectName("result_lb")
        self.gridLayout_3.addWidget(self.result_lb, 3, 0, 1, 2)
        self.second_arg = QtWidgets.QLabel(self.centralwidget)
        self.second_arg.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.second_arg.setAlignment(QtCore.Qt.AlignCenter)
        self.second_arg.setObjectName("label")
        self.gridLayout_3.addWidget(self.second_arg, 1, 0, 1, 2)
        self.first_arg = QtWidgets.QLabel(self.centralwidget)
        self.first_arg.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.first_arg.setAlignment(QtCore.Qt.AlignCenter)
        self.first_arg.setObjectName("first_arg")
        self.gridLayout_3.addWidget(self.first_arg, 0, 0, 1, 2)
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setReadOnly(True)
        self.textEdit.setObjectName("textEdit")
        self.gridLayout_3.addWidget(self.textEdit, 3, 3, 1, 1)
        self.text_second_arg = QtWidgets.QTextEdit(self.centralwidget)
        self.text_second_arg.setObjectName("text_second_arg")
        self.gridLayout_3.addWidget(self.text_second_arg, 1, 3, 1, 1)
        self.text_first_arg = QtWidgets.QTextEdit(self.centralwidget)
        self.text_first_arg.setObjectName("text_first_arg")
        self.gridLayout_3.addWidget(self.text_first_arg, 0, 3, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_3, 0, 0, 1, 2)
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.gridLayout.addWidget(self.comboBox, 2, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.comboBox.activated.connect(self.choiced)
        self.pushButton.clicked.connect(self.calculate)

    def choiced(self):
        if self.comboBox.currentText() == 'Знаходження оберненої матриці' or self.comboBox.currentText() == 'Знаходження визначника' or self.comboBox.currentText() == 'Знаходження транспонованої матриці':
            self.second_arg.setText('Другий елемент')
            self.second_arg.setDisabled(True)
            self.text_second_arg.setDisabled(True)
        elif self.comboBox.currentText() == 'Множення на скаляр':
            self.second_arg.setText('Скаляр')
            self.second_arg.setDisabled(False)
            self.text_second_arg.setDisabled(False)
        else:
            self.second_arg.setText('Другий елемент')
            self.second_arg.setDisabled(False)
            self.text_second_arg.setDisabled(False)
        
        

    
    def calculate(self):
            if self.comboBox.currentText() == 'Додавання':
                try:
                    arg1, arg2 = convertIn(self.text_first_arg.toPlainText(), self.text_second_arg.toPlainText())
                except:
                    self.textEdit.setPlainText(f'Невірно введені дані')
                else:
                    if type(arg1) == type(arg2) and type(arg1) == tuple:
                        result = convertOut(add_vectors(arg1, arg2))
                        self.textEdit.setPlainText(f'{result}')
                    elif type(arg1) == type(arg2) and type(arg1) == list:
                        result = convertOut(add_matrices(arg1, arg2))
                        self.textEdit.setPlainText(f'{result}')
                    else:
                        self.textEdit.setPlainText(f'Невірно введені дані')
            elif self.comboBox.currentText() == 'Віднімання':
                try:
                    arg1, arg2 = convertIn(self.text_first_arg.toPlainText(), self.text_second_arg.toPlainText())
                except:
                    self.textEdit.setPlainText(f'Невірно введені дані')
                else:
                    if type(arg1) == type(arg2) and type(arg1) == tuple:
                        result = convertOut(subtract_vectors(arg1, arg2))
                        self.textEdit.setPlainText(f'{result}')
                    elif type(arg1) == type(arg2) and type(arg1) == list:
                        result = convertOut(subtract_matrices(arg1, arg2))
                        self.textEdit.setPlainText(f'{result}')
                    else:
                        self.textEdit.setPlainText(f'Невірно введені дані')
            elif self.comboBox.currentText() == 'Множення':
                try:
                    arg1, arg2 = convertIn(self.text_first_arg.toPlainText(), self.text_second_arg.toPlainText())
                except:
                    self.textEdit.setPlainText(f'Невірно введені дані')
                else:
                    result = convertOut(multiplication(arg1, arg2))
                    self.textEdit.setPlainText(f'{result}')
            elif self.comboBox.currentText() == 'Векторне множення':
                try:
                    arg1, arg2 = convertIn(self.text_first_arg.toPlainText(), self.text_second_arg.toPlainText())
                except:
                    self.textEdit.setPlainText(f'Невірно введені дані')
                else:
                    result = convertOut(vectors_multiplication(arg1, arg2))
                    self.textEdit.setPlainText(f'{result}')
            elif self.comboBox.currentText() == 'Знаходження оберненої матриці':
                try:
                    arg1 = convertIn(self.text_first_arg.toPlainText())
                except:
                    self.textEdit.setPlainText(f'Невірно введені дані')
                else:
                    result = convertOut(inverse_matrix(arg1))
                    self.textEdit.setPlainText(f'{result}')
            elif self.comboBox.currentText() == 'Множення на скаляр':
                try:
                    arg1 = convertIn(self.text_first_arg.toPlainText())
                    scalar = float(self.text_second_arg.toPlainText())
                except:
                    self.textEdit.setPlainText(f'Невірно введені дані')
                else:
                    result = convertOut(multiplication_scalar(arg1, scalar))
                    self.textEdit.setPlainText(f'{result}')
            elif self.comboBox.currentText() == 'Знаходження визначника':
                try:
                    arg1 = convertIn(self.text_first_arg.toPlainText())
                except:
                    self.textEdit.setPlainText(f'Невірно введені дані')
                else:
                    result = convertOut(determinant(arg1))
                    self.textEdit.setPlainText(f'{result}')
            elif self.comboBox.currentText() == 'Знаходження транспонованої матриці':
                try:
                    arg1 = convertIn(self.text_first_arg.toPlainText())
                except:
                    self.textEdit.setPlainText(f'Невірно введені дані')
                else:
                    result = convertOut(transpose_matrix(arg1))
                    self.textEdit.setPlainText(f'{result}')


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Calculator"))
        self.pushButton.setText(_translate("MainWindow", "Обрахувати"))
        self.result_lb.setText(_translate("MainWindow", "Відповідь"))
        self.second_arg.setText(_translate("MainWindow", "Другий елемент"))
        self.first_arg.setText(_translate("MainWindow", "Перший елемент"))
        self.text_first_arg.setPlaceholderText(_translate("MainWindow", " Матриця записується у такому вигляді\n 0 1 0 1\n 0 1 0 1\n 0 1 0 1\n Вектор у такому (1 2 3)"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Додавання"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Віднімання"))
        self.comboBox.setItemText(2, _translate("MainWindow", "Множення"))
        self.comboBox.setItemText(3, _translate("MainWindow", "Векторне множення"))
        self.comboBox.setItemText(4, _translate("MainWindow", "Знаходження оберненої матриці"))
        self.comboBox.setItemText(5, _translate("MainWindow", "Множення на скаляр"))
        self.comboBox.setItemText(6, _translate("MainWindow", "Знаходження визначника"))
        self.comboBox.setItemText(7, _translate("MainWindow", "Знаходження транспонованої матриці"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
