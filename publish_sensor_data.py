import time
from datetime import datetime

import SensorsInterface as sensor
import paho.mqtt.client as mqtt

MQTT_Broker = "iot.eclipse.org"
MQTT_Port = 1883
Keep_Alive_Interval = 45
topic_temp = "IoT/Temperature"
topic_light = "IoT/Light"
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

sensor.setupSensorian()

time.sleep(2)

while True:
        temp = str(sensor.getTemperature())
        light = str(sensor.getAmbientLight())
        press = str(sensor.getBarometricPressure())
        alt = str(sensor.getAltitude())

        mqttc.publish(topic_temp, temp)
        time.sleep(2)
        print temp
        mqttc.publish(topic_light, light)
        time.sleep(2)
        print light
        mqttc.publish(topic_press, press)
        time.sleep(2)
        print press
        mqttc.publish(topic_alt, alt)
        print alt

        time.sleep(5)
