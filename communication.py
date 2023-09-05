from PyQt5.QtCore import *
import time
import urllib.request

# receiving data
url = "http://IP-ADRESS-OF-ESP"
# ESP's IP, ex: http://192.168.102 (Esp prints it to serial console when connected to wifi)

# sending data url
root_url = "http://IP-ADRESS-OF-ESP"
# ESP's url, ex: http://192.168.102 (Esp prints it to serial console when connected to wifi)


class Communication(QThread):
    # def get_data(self):  # receive data
    #     global data
    #
    #     n = urllib.request.urlopen(url).read()  # get the raw html data in bytes (sends request and warn our esp8266)
    #     n = n.decode("utf-8")  # convert raw html bytes format to string :3
    #
    #     data = n

    # data = n.split() #<optional> split datas we got. (if you programmed it to send more than one value)
    # It splits them into separate list elements.
    # data = list(map(int, data)) #<optional> turn datas to integers, now all list elements are integers.

    # def send_request(url):  # sending data
    #     n = urllib.request.urlopen(url)  # send request to ESP

    def run(self):
        while True:
            # # receive data
            # self.get_data()
            # print("Your data(s) which we received from ESP: " + data)
            #
            # # send data
            # self.send_request(root_url + "/SENT_DATA")

            # next part will be deleted in realtime run
            print("sending and receiving data", end=" ")
            time.sleep(0.5)
            print(".", end="")
            time.sleep(0.5)
            print(".", end="")
            time.sleep(0.5)
            print(".")
            time.sleep(2)
