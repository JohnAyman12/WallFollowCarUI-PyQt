from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from MainPage import Ui_MainWindow as mainPage
from Task1Page import Ui_MainWindow as task1
from cameraFeed import Worker1 as cameraFeed

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # initializing the main window
        self.mainWindow = mainPage()
        self.mainWindow.setupUi(self)

        # initializing IP task 1 window
        self.window2 = QMainWindow()
        self.task1Window = task1()
        self.task1Window.setupUi(self.window2)

        self.mainWindow.task1Btn.clicked.connect(self.openTask1Page)  # setting task-1 page event

        # setting main page camera feed
        self.camera = cameraFeed()
        self.camera.start()
        self.camera.ImageUpdate.connect(self.imageUpdateSlot)
        self.mainWindow.screenShotBtn.clicked.connect(self.camera.savePhoto)

        # setting team logo part in main window
        pixmap = QPixmap("images\\teamLogo.png")
        self.mainWindow.logoLbl.setPixmap(pixmap)

        # setting control buttons slots
        self.mainWindow.forwardBtn.pressed.connect(self.moveForward)
        self.mainWindow.backwardBtn.pressed.connect(self.moveBackward)
        self.mainWindow.rightBtn.pressed.connect(self.moveRight)
        self.mainWindow.leftBtn.pressed.connect(self.moveLeft)

        self.mainWindow.speedSpinBox.valueChanged.connect(self.speedValueChanged)

    def imageUpdateSlot(self, Image):  # shows camera feed (always running)
        self.mainWindow.camerFeed.setPixmap(QPixmap.fromImage(Image))

    def openTask1Page(self):  # opens task-1 page when called
        self.window2.show()

    def moveForward(self):
        print("Forward")

    def moveBackward(self):
        print("Backward")

    def moveRight(self):
        print("Right")

    def moveLeft(self):
        print("Left")

    def speedValueChanged(self):
        speed = self.mainWindow.speedSpinBox.value()
        print(speed)
        if speed <= 85:
            print("Low")
        elif speed <= 170:
            print("Mid")
        else:
            print("High")

if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()
