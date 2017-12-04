import paho.mqtt.client as mqtt
from store_sensor_data import sensor_Data_Handler

MQTT_Broker = "iot.eclipse.org"
MQTT_Port = 1883
Keep_Alive_Interval = 45
MQTT_Topic = "IoT/#"

def on_connect(mosq, obj,flags, rc):
        mqttc.subscribe(MQTT_Topic, 0)

def on_message(mosq, obj, msg):
        print "MQTT Data Received..."
        print "MQTT Topic: " + msg.topic
        print "Data: " + msg.payload
        sensor_Data_Handler(msg.topic, msg.payload)

def on_subscribe(mosq, obj, mid, granted_qos):
    pass

mqttc = mqtt.Client()

mqttc.on_message = on_message
mqttc.on_connect = on_connect
mqttc.on_subscribe = on_subscribe

mqttc.connect(MQTT_Broker, int(MQTT_Port), int(Keep_Alive_Interval))

mqttc.loop_forever()
