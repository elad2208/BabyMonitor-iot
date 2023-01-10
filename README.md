# BabyMonitor
### Smart car child monitor

## Description

This application simulates sensor which installed in a car, and detects movement/sound, then using MQTT protocol sends message to the MQTT broker.  
Then, there is a smartphone app which identifies that new message was sent, and alerts for movement/sound in the car.  
The purpose of the system is to prevent child being forgotten in the car.  

## How to run the code
Run the following commands in the project directory:  
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Then open two terminals, in the first terminal run:
```bash
python car_monitor_simulator.py
```

And in the second terminal run:
```bash
python smartphone_app_simulator.py
```
