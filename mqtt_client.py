import paho.mqtt.client as mqtt


class Mqtt_client():
    def __init__(self, mainwin=None):
        self.broker_host = ''
        self.topic = ''
        self.broker_port = '' 
        self.client_name = ''
        self.username = ''
        self.password = ''
        self.on_connect_gui_function = ''
        self.connected = False
        self.mainwin = mainwin

    def get_broker_host(self):
        return self.broker_host

    def set_broker_host(self, broker_host):
        self.broker_host = broker_host

    def get_broker_port(self):
        return self.broker_port

    def set_broker_port(self, broker_port):
        self.broker_port = broker_port

    def get_client_name(self):
        return self.client_name

    def set_client_name(self, client_name):
        self.client_name = client_name

    def get_username(self):
        return self.username

    def set_username(self, username):
        self.username = username

    def get_password(self):
        return self.password

    def set_password(self, password):
        self.password = password

    def set_on_connect_gui_function(self, on_connect_gui_function):
        self.on_connect_gui_function = on_connect_gui_function

    def set_on_disconnect_gui_function(self, on_disconnect_gui_function):
        self.on_disconnect_gui_function = on_disconnect_gui_function

    def on_connect(self, client, userdata, flags, rc):
        if rc == 0:
            print("connected OK")
            self.connected = True
            self.on_connect_gui_function()
        else:
            print("Failed connect, returned code " + str(rc))

    def on_disconnect(self, client, userdata, flags, rc = 0):
        print("Disconnected result code " + str(rc))
        self.connected = False
        self.on_disconnect_gui_function()

    def on_message(self, client, userdata, msg):
        topic = msg.topic
        m_decode = str(msg.payload.decode("utf-8","ignore"))
        print(f"Got message {m_decode} from topic {topic}")
        if 'subscriber' in self.client_name:
            self.mainwin.subscribeDock.update_message_window(m_decode)

    def on_publish(self, client, userdata, mid):
        print(f"Sent message {mid}")

    def connect_to(self):
        self.client = mqtt.Client(self.client_name, clean_session=False)
        self.client.on_connect = self.on_connect
        self.client.on_disconnect = self.on_disconnect
        self.client.on_message = self.on_message
        self.client.on_publish = self.on_publish
        self.client.username_pw_set(self.username, self.password)
        print("Connecting to broker ", self.broker_host)
        self.client.connect(self.broker_host, self.broker_port)

    def disconnect_from(self):
        self.client.disconnect()

    def start_listening(self):
        self.client.loop_start()

    def stop_listening(self):
        self.client.loop_stop()
  
    def subscribe_to(self, topic, qos):
        if self.connected:
            self.client.subscribe(topic, qos)
        else:
            print("Can't subscribe. Connecection should be established first")

    def publish_to(self, topic, message, qos):
        if self.connected:
            self.client.publish(topic, message, qos)
        else:
            print("Can't publish. Connecection should be established first")
