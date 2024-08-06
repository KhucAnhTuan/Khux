import sys
import time
import os
from pynput import mouse, keyboard
import datetime
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel , QPushButton, QWidget , QVBoxLayout
from PyQt6.QtCore import Qt ,QTimer, QTime
from PyQt6 import QtGui, QtCore
from PyQt6.QtGui import QDragEnterEvent, QDropEvent, QClipboard

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Nheo")
        self.setFixedSize(300, 330)

        # Create a label widget
        self.label = QLabel("This window will stay on top")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Set the "Always On Top" flag
        self.setWindowFlag(Qt.WindowType.WindowStaysOnTopHint)



        self.setWindowIcon(QtGui.QIcon("C:/Temp/Hinh.jpg"))

        self.button = QPushButton("")
        self.button.setIcon(QtGui.QIcon("C:/Temp/Hinh.jpg"))
        self.button.setIconSize(QtCore.QSize(350,450))

        self.button.clicked.connect(self.sleep)

        self.last_activity_time = time.time()

        timer = QTimer(self)
        self.seconds = 1
        # adding action to timer
        timer.timeout.connect(self.showTime)

        # update the timer every second
        timer.start(1000)


        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        main_layout = QVBoxLayout()
        central_widget.setLayout(main_layout)
        main_layout.addWidget(self.button) 
        main_layout.addWidget(self.label)

        mouse_listener = mouse.Listener(on_move=self.on_mouse_move)
        mouse_listener.start()

        keyboard_listener = keyboard.Listener(on_press=self.on_key_press)
        keyboard_listener.start()

        self.setAcceptDrops(True)


    def dragEnterEvent(self, event: QDragEnterEvent):
        # Check if the event has file or URL data
        if event.mimeData().hasUrls():
            event.acceptProposedAction()

    def dropEvent(self, event: QDropEvent):
        # Retrieve the file URL from the event
        url = event.mimeData().urls()[0]
        self.file_path = url.toLocalFile()
        self.label.setText(self.file_path)
        self.copy_file_location(self.file_path)

    def on_mouse_move(self,x, y,):

        self.last_activity_time = time.time()

    def on_key_press(self,key):

        self.last_activity_time = time.time()



    def sleep(self):
        os.system("rundll32.exe powrprof.dll, SetSuspendState Sleep")




    # method called by timer
    def showTime(self):



   

        hour = str(datetime.timedelta(seconds = self.seconds))
        if time.time() - self.last_activity_time < 5:
            self.seconds += 1
            self.label.setText(str(hour))

        else:
            self.label.setText(str(hour))       


        # getting current time
        current_time = QTime.currentTime()

        # converting QTime object to string
        #label_time = current_time.toString('hh:mm:ss')

        # showing it to the label
        #self.label.setText(label_time)

    def copy_file_location(self,cop):
        file_location = self.label.text()
        clipboard = QApplication.clipboard()
        clipboard.setText(cop)







if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MyWindow()
    window.show()

    sys.exit(app.exec())
