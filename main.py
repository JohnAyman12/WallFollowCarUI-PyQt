from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from MainPage import Ui_MainWindow as mainPage
from Task1Page import Ui_MainWindow as task1
from cameraFeed import Worker1 as cameraFeed

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # initializing the main window
        self.main_window = mainPage()
        self.main_window.setupUi(self)

        # initializing IP task 1 window
        self.window2 = QMainWindow()
        self.task1_window = task1()
        self.task1_window.setupUi(self.window2)

        self.main_window.task1Btn.clicked.connect(self.open_task1_page)  # setting task-1 page event

        # setting main page camera feed
        self.camera = cameraFeed()
        self.camera.start()
        self.camera.ImageUpdate.connect(self.image_update_slot)
        self.main_window.screenShotBtn.clicked.connect(self.camera.savePhoto)

        # setting team logo part in main window
        pixmap = QPixmap("images\\teamLogo.png")
        self.main_window.logoLbl.setPixmap(pixmap)

        # setting motion control buttons slots
        self.main_window.forwardBtn.pressed.connect(self.move_forward)
        self.main_window.backwardBtn.pressed.connect(self.move_backward)
        self.main_window.rightBtn.pressed.connect(self.move_right)
        self.main_window.leftBtn.pressed.connect(self.move_left)

        # setting speed control part
        self.main_window.lowSpeedRadioBtn.clicked.connect(self.low_speed)
        self.main_window.midSpeedRadioBtn.clicked.connect(self.mid_speed)
        self.main_window.highSpeedRadioBtn.clicked.connect(self.high_speed)
        self.main_window.speedSpinBox.valueChanged.connect(self.speed_value_changed)

    def image_update_slot(self, Image):  # shows camera feed (always running)
        self.main_window.camerFeed.setPixmap(QPixmap.fromImage(Image))

    def open_task1_page(self):  # opens task-1 page when called
        self.window2.show()

    def move_forward(self):
        print("Forward")

    def move_backward(self):
        print("Backward")

    def move_right(self):
        print("Right")

    def move_left(self):
        print("Left")

    def low_speed(self):
        self.main_window.speedSpinBox.setValue(85)

    def mid_speed(self):
        self.main_window.speedSpinBox.setValue(170)

    def high_speed(self):
        self.main_window.speedSpinBox.setValue(255)

    def speed_value_changed(self):
        speed = self.main_window.speedSpinBox.value()
        print(speed)
        if speed <= 85:
            print("Low")
            self.main_window.lowSpeedRadioBtn.setChecked(True)
        elif speed <= 170:
            print("Mid")
            self.main_window.midSpeedRadioBtn.setChecked(True)
        else:
            print("High")
            self.main_window.highSpeedRadioBtn.setChecked(True)

if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()
