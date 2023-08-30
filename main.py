from PyQt5.QtWidgets import (QApplication, QMainWindow)
import cv2 as cv
from MainPage import Ui_MainWindow as mainPage
from Task1Page import Ui_MainWindow as task1

cap = cv.VideoCapture(0)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.mainWindow = mainPage()
        self.mainWindow.setupUi(self)

        self.window2 = QMainWindow()
        self.task1Window = task1()
        self.task1Window.setupUi(self.window2)

        self.mainWindow.task1Btn.clicked.connect(self.openTask1Page)

    def openTask1Page(self):
        self.window2.show()


if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()
