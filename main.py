from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtMultimedia import *
from PyQt5.QtMultimediaWidgets import *
from PyQt5.QtCore import *

from MainPage import Ui_MainWindow as mainPage
from Task1Page import Ui_MainWindow as Task1
from cameraFeed import Worker1 as cameraFeed


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # initializing the main window
        self.main_window = mainPage()
        self.main_window.setupUi(self)

        # modifying main page appearance
        self.setStyleSheet("background-color: #001522;")
        self.main_window.sensorReadingBox.setStyleSheet('color: white')
        self.main_window.ipTasksBox.setStyleSheet('color: white')
        self.main_window.task1Btn.setStyleSheet('background-color: white; color: #001522')
        self.main_window.task2Btn.setStyleSheet('background-color: white; color: #001522')
        self.main_window.task3Btn.setStyleSheet('background-color: white; color: #001522')
        self.main_window.cameraFeedBox.setStyleSheet('color: white')
        self.main_window.screenShotBtn.setStyleSheet('background-color: white; color: #001522')
        self.main_window.teamLogoBox.setStyleSheet('color: white')
        self.main_window.motionControlBox.setStyleSheet('color: white')
        self.main_window.forwardBtn.setStyleSheet('background-color: white; color: #001522')
        self.main_window.backwardBtn.setStyleSheet('background-color: white; color: #001522')
        self.main_window.rightBtn.setStyleSheet('background-color: white; color: #001522')
        self.main_window.leftBtn.setStyleSheet('background-color: white; color: #001522')
        self.main_window.speedControlBox.setStyleSheet('color: white')
        self.main_window.motionModeBox.setStyleSheet('color: white')
        self.main_window.connectivityBox.setStyleSheet('color: white')

        # initializing IP task 1 window
        self.window2 = QMainWindow()
        self.task1_window = Task1()
        self.task1_window.setupUi(self.window2)

        # modifying task-1 page appearance
        self.window2.setStyleSheet("background-color: #001522;")
        self.task1_window.input1Lbl.setStyleSheet('color: white')
        self.task1_window.input2Lbl.setStyleSheet('color: white')
        self.task1_window.outputLbl.setStyleSheet('color: white')
        self.task1_window.exitButton.setStyleSheet('background-color: white; color: #001522')

        # setting main page camera feed
        self.camera = cameraFeed()
        self.camera.start()
        self.camera.ImageUpdate.connect(self.image_update_slot)
        self.main_window.screenShotBtn.clicked.connect(self.camera.savePhoto)

        # setting team logo part in main window
        pixmap = QPixmap("images\\teamLogo3.png")
        self.main_window.logoLbl.setPixmap(pixmap)

        # setting speed control part
        self.main_window.lowSpeedRadioBtn.clicked.connect(self.low_speed)
        self.main_window.midSpeedRadioBtn.clicked.connect(self.mid_speed)
        self.main_window.highSpeedRadioBtn.clicked.connect(self.high_speed)
        self.main_window.speedSpinBox.valueChanged.connect(self.speed_value_changed)

        # setting control buttons
        self.main_window.forwardBtn.pressed.connect(self.forward_btn_clicked)
        self.main_window.backwardBtn.pressed.connect(self.backward_btn_clicked)
        self.main_window.rightBtn.pressed.connect(self.right_btn_clicked)
        self.main_window.leftBtn.pressed.connect(self.left_btn_clicked)

        # setting video players for IP task 1
        self.vid_widget1 = QVideoWidget()
        self.task1_window.vid1VLayout.addWidget(self.vid_widget1)
        self.media_player1 = QMediaPlayer(None, QMediaPlayer.VideoSurface)
        self.media_player1.setVideoOutput(self.vid_widget1)
        self.media_player1.setMedia(QMediaContent(QUrl.fromLocalFile("images\\IP_vid.mp4")))
        self.media_player1.stateChanged.connect(self.mediastate1_changed)

        self.vid_widget2 = QVideoWidget()
        self.task1_window.vid2VLayout.addWidget(self.vid_widget2)
        self.media_player2 = QMediaPlayer(None, QMediaPlayer.VideoSurface)
        self.media_player2.setVideoOutput(self.vid_widget2)
        self.media_player2.setMedia(QMediaContent(QUrl.fromLocalFile("images\\IP_vid.mp4")))
        self.media_player1.stateChanged.connect(self.mediastate2_changed)

        self.vid_widget3 = QVideoWidget()
        self.task1_window.outputVidHLayout.addWidget(self.vid_widget3)
        self.media_player3 = QMediaPlayer(None, QMediaPlayer.VideoSurface)
        self.media_player3.setVideoOutput(self.vid_widget3)
        self.media_player3.setMedia(QMediaContent(QUrl.fromLocalFile("images\\IP_vid.mp4")))
        self.media_player1.stateChanged.connect(self.mediastate3_changed)

        self.main_window.task1Btn.clicked.connect(self.open_task1_page)  # opening task-1 page event
        self.task1_window.exitButton.clicked.connect(self.close_task1_page)  # closing task-1 page event

        self.task1_page_opened = False  # to detect if task 1 page opened or not

        self.window2.setWindowFlag(Qt.WindowCloseButtonHint, False)

    def closeEvent(self, event):  # closes task-1 page when main page is closed
        self.window2.close()

    def image_update_slot(self, image):  # shows camera feed (always running)
        self.main_window.camerFeed.setPixmap(QPixmap.fromImage(image))

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

    def keyPressEvent(self, event):
        if event.key() > 1000:
            print("Make keyboard english, please!")
        if event.key() == 87:
            print("Forward")
            self.main_window.forwardBtn.animateClick()
        elif event.key() == 83:
            print("Backward")
            self.main_window.backwardBtn.animateClick()
        elif event.key() == 68:
            print("Right")
            self.main_window.rightBtn.animateClick()
        elif event.key() == 65:
            print("Left")
            self.main_window.leftBtn.animateClick()

    def forward_btn_clicked(self):
        print("Forward")

    def backward_btn_clicked(self):
        print("Backward")

    def right_btn_clicked(self):
        print("Right")

    def left_btn_clicked(self):
        print("Left")

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


if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()
