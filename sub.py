# coding=utf8

# https://gist.github.com/voluntas/8238751
# sub.py

import paho.mqtt.client as paho
import json

def on_connect(mqttc, obj, rc):
    mqttc.subscribe("$SYS/#", 0)
    print("rc: "+str(rc))

def on_message(mqttc, obj, msg):
    try:
        st = str(msg.payload)
        decoded_str = json.loads(st)
        # print(decoded)

    except Exception as e:
        print '=== エラー内容 ==='
        print 'type:' + str(type(e))
        print 'args:' + str(e.args)
        print 'message:' + e.message
        print 'e自身:' + str(e)
    print(msg.topic+" "+str(msg.qos)+" "+str(msg.payload))
    

def on_publish(mqttc, obj, mid):
    print("mid: "+str(mid))

def on_subscribe(mqttc, obj, mid, granted_qos):
    print("Subscribed: "+str(mid)+" "+str(granted_qos))

def on_log(mqttc, obj, level, string):
    print(string)

if __name__ == '__main__':
    mqttc = paho.Client()
    mqttc.on_message = on_message
    mqttc.on_connect = on_connect
    mqttc.on_subscribe = on_subscribe

    mqttc.connect("localhost", 1883, 60)

    mqttc.subscribe("my/topic/string", 0)

    mqttc.loop_forever()
