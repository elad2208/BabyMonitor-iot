# Smart car child monitor

## Description

This application simulates sensor which installed in a car, and detects movement/sound, then using MQTT protocol sends message to the MQTT broker.  
Then, there is a smartphone app which identifies that new message was sent, and alerts for movement/sound in the car.  
The purpose of the system is to prevent child being forgotten in the car.  

## How to run the code
Open terminal, get into the project directory and run:
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```
And close this terminal.  

Then, open one terminal, get into the project directory and run:
```bash
source venv/bin/activate
python3 car_monitor_simulator.py
```

And open a second terminal, get into the project directory and run:
```bash
source venv/bin/activate
python3 smartphone_app_simulator.py
```
