from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtMultimedia import *
from PyQt5.QtMultimediaWidgets import *
from PyQt5.QtCore import *

from MainPage import Ui_MainWindow as mainPage
from Task1Page import Ui_MainWindow as task1
from cameraFeed import Worker1 as cameraFeed

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowIcon(QIcon('player.png'))
        # initializing the main window
        self.main_window = mainPage()
        self.main_window.setupUi(self)

        # initializing IP task 1 window
        self.window2 = QMainWindow()
        self.window2.setWindowTitle("Task 1")
        self.task1_window = task1()
        self.task1_window.setupUi(self.window2)

        # setting video players for IP task 1
        self.vid_widget1 = QVideoWidget()
        self.task1_window.vid1VLayout.addWidget(self.vid_widget1)
        self.media_player1 = QMediaPlayer(None, QMediaPlayer.VideoSurface)
        self.media_player1.setVideoOutput(self.vid_widget1)
        self.media_player1.setMedia(QMediaContent(QUrl.fromLocalFile("images\\IPvid.mp4")))
        self.media_player1.stateChanged.connect(self.mediastate1_changed)

        self.vid_widget2 = QVideoWidget()
        self.task1_window.vid2VLayout.addWidget(self.vid_widget2)
        self.media_player2 = QMediaPlayer(None, QMediaPlayer.VideoSurface)
        self.media_player2.setVideoOutput(self.vid_widget2)
        self.media_player2.setMedia(QMediaContent(QUrl.fromLocalFile("images\\IPvid.mp4")))
        self.media_player1.stateChanged.connect(self.mediastate2_changed)

        self.vid_widget3 = QVideoWidget()
        self.task1_window.outputVidHLayout.addWidget(self.vid_widget3)
        self.media_player3 = QMediaPlayer(None, QMediaPlayer.VideoSurface)
        self.media_player3.setVideoOutput(self.vid_widget3)
        self.media_player3.setMedia(QMediaContent(QUrl.fromLocalFile("images\\IPvid.mp4")))
        self.media_player1.stateChanged.connect(self.mediastate3_changed)

        self.main_window.task1Btn.clicked.connect(self.open_task1_page)  # opening task-1 page event
        self.task1_window.exitButton.clicked.connect(self.close_task1_page)  # closing task-1 page event

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

        self.task1_page_opened = False # to detect if task 1 page opened or not
    def image_update_slot(self, Image):  # shows camera feed (always running)
        self.main_window.camerFeed.setPixmap(QPixmap.fromImage(Image))

    def open_task1_page(self):  # opens task-1 page when called
        self.task1_page_opened = True
        self.window2.show()
        self.media_player1.play()
        self.media_player2.play()
        self.media_player3.play()

    def close_task1_page(self):  # closes task-1 page
        self.task1_page_opened = False
        self.window2.close()
        self.media_player1.stop()
        self.media_player2.stop()
        self.media_player3.stop()

    def mediastate1_changed(self):  # puts input video 1 in loop ONLY when task 1 page is opened
        if self.media_player1.state() == QMediaPlayer.StoppedState and self.task1_page_opened:
            self.media_player1.play()

    def mediastate2_changed(self):  # puts input video 2 in loop ONLY when task 1 page is opened
        if self.media_player2.state() == QMediaPlayer.StoppedState and self.task1_page_opened:
            self.media_player2.play()

    def mediastate3_changed(self):  # puts output video in loop ONLY when task 1 page is opened
        if self.media_player3.state() == QMediaPlayer.StoppedState and self.task1_page_opened:
            self.media_player3.play()

    def move_forward(self):  # sends a signal to move the car forward via the communication protocol
        print("Forward")

    def move_backward(self):  # sends a signal to move the car backward via the communication protocol
        print("Backward")

    def move_right(self):  # sends a signal to turn the car right via the communication protocol
        print("Right")

    def move_left(self):  # sends a signal to turn the car left via the communication protocol
        print("Left")

    def low_speed(self):  # sets the speed mode to low
        self.main_window.speedSpinBox.setValue(85)

    def mid_speed(self):  # sets the speed mode to medium
        self.main_window.speedSpinBox.setValue(170)

    def high_speed(self):  # sets the speed mode to high
        self.main_window.speedSpinBox.setValue(255)

    def speed_value_changed(self):  # tells which speed mode we are in, depending on the value in the spin box
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
