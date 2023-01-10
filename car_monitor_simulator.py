import sys
from datetime import datetime
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from config import *
from mqtt_client import Mqtt_client


class PublisherDock(QDockWidget):
    def __init__(self, mc):
        QDockWidget.__init__(self)

        self.mc = mc
        self.mc.set_on_connect_gui_function(self.on_connected)
        self.mc.set_on_disconnect_gui_function(self.on_disconnected)
        self.eHostInput = QLineEdit()
        self.eHostInput.setInputMask('999.999.999.999')
        self.eHostInput.setText(broker_host)

        self.ePort = QLineEdit()
        self.ePort.setValidator(QIntValidator())
        self.ePort.setMaxLength(4)
        self.ePort.setText(broker_port)

        self.eClientID = QLineEdit()
        self.eClientID.setText(publisher_client_name)

        self.eUserName = QLineEdit()
        self.eUserName.setText(username)

        self.ePassword = QLineEdit()
        self.ePassword.setEchoMode(QLineEdit.Password)
        self.ePassword.setText(password)

        self.eConnectbtn = QPushButton("connect/disconnect", self)
        self.eConnectbtn.setToolTip("connect/disconnect")
        self.eConnectbtn.clicked.connect(self.on_button_connect_disconnect_click)
        self.eConnectbtn.setStyleSheet("background-color: red")

        self.eSendbtn = QPushButton("simulate movement/sound", self)
        self.eSendbtn.setToolTip("simulate movement/sound")
        self.eSendbtn.clicked.connect(self.on_buttion_simulate_click)
        self.eSendbtn.setStyleSheet("background-color: gray")

        self.ePublisherTopic = QLineEdit()
        self.ePublisherTopic.setText(topic)

        formLayot = QFormLayout()
        formLayot.addRow("", self.eConnectbtn)
        formLayot.addRow("", self.eSendbtn)
        formLayot.addRow("Pub topic", self.ePublisherTopic)

        widget = QWidget(self)
        widget.setLayout(formLayot)
        self.setTitleBarWidget(widget)
        self.setWidget(widget)

    def on_connected(self):
        self.eConnectbtn.setStyleSheet("background-color: green")
    
    def on_disconnected(self):
        self.eConnectbtn.setStyleSheet("background-color: red")

    def on_button_connect_disconnect_click(self):
        self.mc.set_broker_host(self.eHostInput.text())
        self.mc.set_broker_port(int(self.ePort.text()))
        self.mc.set_client_name(self.eClientID.text())
        self.mc.set_username(self.eUserName.text())
        self.mc.set_password(self.ePassword.text())

        if not self.mc.connected:
            self.mc.connect_to()
            self.mc.start_listening()
        else:
            self.mc.disconnect_from()

    def on_buttion_simulate_click(self):
        self.mc.publish_to(topic, message=f"{datetime.now()} movement/sound detected", qos=2)


class MainWindow(QMainWindow):
    def __init__(self, parent = None):
        QMainWindow.__init__(self, parent)
        self.mc = Mqtt_client()
        self.setUnifiedTitleAndToolBarOnMac(True)
        self.setGeometry(30, 600, 300, 150)
        self.setWindowTitle('Car Monitor Simulator')
        self.connectionDock = PublisherDock(self.mc)
        self.addDockWidget(Qt.TopDockWidgetArea, self.connectionDock)


app = QApplication(sys.argv)
mainwin = MainWindow()
mainwin.show()
app.exec_()
