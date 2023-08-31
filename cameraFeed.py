import sys
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import cv2
import time

class MainWindow(QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.VBL = QVBoxLayout()

        self.FeedLabel = QLabel()
        self.VBL.addWidget(self.FeedLabel)

        self.CancelBTN = QPushButton("Cancel")
        self.CancelBTN.clicked.connect(self.CancelFeed)
        self.VBL.addWidget(self.CancelBTN)

        self.Worker = Worker1()
        self.Worker.start()
        self.Worker.ImageUpdate.connect(self.ImageUpdateSlot)
        self.setLayout(self.VBL)

        self.ScreenShotBTN = QPushButton("Screen Shot")
        self.ScreenShotBTN.clicked.connect(self.Worker.savePhoto)
        self.VBL.addWidget(self.ScreenShotBTN)


    def ImageUpdateSlot(self, Image):
        self.FeedLabel.setPixmap(QPixmap.fromImage(Image))
        # print("camera on")

    def CancelFeed(self):
        self.Worker.stop()


class Worker1(QThread):
    ImageUpdate = pyqtSignal(QImage)
    Capture = cv2.VideoCapture(0)

    def run(self):
        self.ThreadActive = True
        while self.ThreadActive:
            ret, frame = self.Capture.read()
            if ret:
                Image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                FlippedImage = cv2.flip(Image, 1)
                ConvertToQtFormat = QImage(FlippedImage.data, FlippedImage.shape[1], FlippedImage.shape[0], QImage.Format_RGB888)
                Pic = ConvertToQtFormat.scaled(640, 480, Qt.KeepAspectRatio)
                self.ImageUpdate.emit(Pic)

    def stop(self):
        self.ThreadActive = False
        self.quit()

    def savePhoto(self):
        img, image = self.Capture.read()
        """ This function will save the image"""
        self.filename = 'Snapshot ' + str(time.strftime("%Y-%b-%d at %H.%M.%S %p")) + '.png'
        print(self.filename)
        cv2.imwrite(self.filename, image)
        print('Image saved as:', self.filename)


if __name__ == "__main__":
    App = QApplication(sys.argv)
    Root = MainWindow()
    Root.show()
    sys.exit(App.exec())