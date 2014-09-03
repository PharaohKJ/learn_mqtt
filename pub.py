# coding=utf8

# https://gist.github.com/voluntas/8238751 pub.py

import paho.mqtt.client as paho
import json
json_data = {'DeviceName':'TestDevice',
             'Value':('value1','value2')}


def on_connect(mqttc, obj, rc):
    mqttc.subscribe("$SYS/#", 0)
    print("rc: "+str(rc))

def on_message(mqttc, obj, msg):
    print(msg.topic+" "+str(msg.qos)+" "+str(msg.payload))

def on_publish(mqttc, obj, mid):
    print("mid: "+str(mid))

def on_log(mqttc, obj, level, string):
    print(string)

if __name__ == '__main__':
    mqttc = paho.Client()
    mqttc.on_message = on_message
    mqttc.on_connect = on_connect
    mqttc.on_publish = on_publish
    # 一度のプロトコルで送ることのできる量を制限できる 標準は20なので
    # テストのために増量
    mqttc.max_inflight_messages_set(10000)
    mqttc.connect("localhost", 1883, 60)

    for i in range(0,1000):
        print i
        json_data['Value'] = i
        mqttc.publish("my/topic/string", json.dumps(json_data), 1)
