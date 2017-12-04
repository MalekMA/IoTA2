import time
from datetime import datetime

import SensorsInterface as sensor
import paho.mqtt.publish as publish

MQTT_Broke = "iot.eclipse.org"
MQTT_Port = 1883
Keep_Alive_Interval = 45
topic_temp = "/IoT/Temperature"
topic_light = "/IoT/Light"
topic_press = "IoT/Pressure"
topic_alt = "IoT/Altitude"

def on_connect(client, userdata, rc):
	if rc != 0:
		pass
		print "Unable to connect to MQTT Broker..."
	else:
		print "Connected with MQTT Broker: " + str(MQTT_Broker)

def on_publish(client, userdata, mid):
	pass
		
def on_disconnect(client, userdata, rc):
	if rc !=0:
		pass

mqttc = mqtt.Client()
mqttc.on_connect = on_connect
mqttc.on_disconnect = on_disconnect
mqttc.on_publish = on_publish
mqttc.connect(MQTT_Broker, int(MQTT_Port), int(Keep_Alive_Interval))	

SensorsInterface.setupSensorian()

time.sleep(10)

while True:
	temp = str(sensor.getTemperature())
	light = str(sensor.getAmbientLight())
	press = str(sensor.getBarometricPressure())
	alt = str(sensor.getAltitude())

	publish.single(topic_temp, temp)
	publish.single(topic_light, light)
	publish.single(topic_press, press)
	publish.single(topic_alt, alt)

	time.sleep(30)