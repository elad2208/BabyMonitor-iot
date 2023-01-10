import socket


broker_host = str(socket.gethostbyname('broker.hivemq.com'))
broker_port = '1883'
topic = 'IoTFinalProject'
publisher_client_name = "car_monitor_publisher"
subscriber_client_name = "smartphone_app_subscriber"
username = ''
password = ''