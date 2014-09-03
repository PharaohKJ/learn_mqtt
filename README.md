# About

MQTT の Server/Client を調査 & 試したときの記録。テスト環境と実際のサンプルテストまで。



# 参考URL

- [https://gist.github.com/voluntas/8238751](https://gist.github.com/voluntas/8238751)
- [http://tdoc.info/blog/2014/01/27/mqtt.html](http://tdoc.info/blog/2014/01/27/mqtt.html)
- [http://it.impressbm.co.jp/articles/-/10773](http://it.impressbm.co.jp/articles/-/10773)

# MQTTとは1

http://tdoc.info/blog/2014/01/27/mqtt.html より引用

> MQTT(MQ Telemetry Transport) とは、publish/subscribeモデルに基づく軽量なメッセージプロトコルです。
> ネットワークが不安定な場所で動作するための機能や非力なデバイスで動くための軽量化などが特徴です。

... 

> また、軽量な点と同期通信な点を生かして、リアルタイム通信が必要な用途にも使われています。

## publish/subscribeとは

[http://ja.wikipedia.org/wiki/出版-購読型モデル](http://ja.wikipedia.org/wiki/出版-購読型モデル)

# MQTTとは2

http://it.impressbm.co.jp/articles/-/10773 より引用

> はじめからIoTやM2Mに最適化させるために開発された、デバイス間通信のための新しい
> プロトコルだ。仕様はオープンソースで公開されており、Facebookメッセンジャーに実装
> されていることでも知られている。

httpとのプロトコル比較も上記記事参照のこと。

> まず、HTTPに比べて圧倒的に軽量であるという点だ。ヘッダサイズはわずかに2バイト
> ながらも、APIとしてきちんと定義されているのでデータを生でpushすることができる。
> トラフィック量はHTTPの1/10になるため、実質的にスループットが10倍になる。

...

> 2つめは非同期/双方向通信を実現するプロトコルである点だ。

...

> MQTTは1対Nの通信を実現するPublish/Subscribe型メッセージ通信を実装しており、大量の同報通知なども可能にする。
...
> 誰もが無料で利用できる点だ。標準化を進めれば、サードパーティによるデバイス開発
> コストの削減にもつながる。現バージョンのMQTT v3.1はOASIS標準化作業を進めており、
> M2M標準のプロトコルとしてさらに広く普及を図っていく構えだ。

## M2M

[http://ja.wikipedia.org/wiki/マシンツーマシン](http://ja.wikipedia.org/wiki/マシンツーマシン)

> マシンツーマシン（Machine-to-Machine）とは、コンピュータネットワークに繋がれた機械同士が人間を介在せずに相互に情報交換し、自動的に最適な制御が行われるシステムを指す。

## IoT

[http://ja.wikipedia.org/wiki/モノのインターネット](http://ja.wikipedia.org/wiki/モノのインターネット)

> モノのインターネット（Internet of Things、IoT）は、一意に識別可能な「もの」がインターネット/クラウドに接続され、情報交換することにより相互に制御する仕組みである



# テスト環境構築

- OS:OSX 10.9.4 brew
- Server Mosquitto
- Client paho + Python


## MQTT-Server Setup

今回は MQTT参照実装の *Mosquitto* を選択

### rabbitmq

https://www.rabbitmq.com/mqtt.html
http://momijiame.tumblr.com/post/50094875747/mac-os-x-rabbitmq

> RabbitMQ(ラビットエムキュー)は、Advanced Message Queuing Protocol(AMQP)を使用した、オープンソースのメッセージ指向ミドルウェアである。

> RabbitMQはerlang製の定評あるMQサーバーです。AMQPなどにも対応していますが、MQTTにも対応しています。


```
$ brew install rabbitmq
$ rabbitmq-server
```

###  Mosquitto

```
$ brew install mosquitto
$ mosquitto
```


## MQTT-Client

いろいろ調べたが、以下のなかから *paho*  *python* を選択

### ruby gem

https://github.com/njh/ruby-mqtt
http://hiyosi.tumblr.com/post/74515559234/mqtt

> Only QOS 0 currently supported

なので今回は見送り


### knolleary/pubsubclient

http://knolleary.net/arduino-client-for-mqtt/
https://github.com/knolleary/pubsubclient
1年前からメンテされてない？


### Paho C/C++/Java/JavaScript/Python/Go
http://www.eclipse.org/paho/


### mqtt.js - JavaScript

https://www.npmjs.org/package/mqtt
https://github.com/adamvr/MQTT.js


## paho の Python ライブラリ準備

```
$ brew install python --framework
$ python --version
Python 2.7.5
$ pip --version
pip 1.5.6 from /usr/local/Cellar/python/2.7.8_1/Frameworks/Python.framework/Versions/2.7/lib/python2.7/site-packages/pip-1.5.6-py2.7.egg (python 2.7)

$ pip install paho-mqtt
Downloading/unpacking paho-mqtt
  Downloading paho-mqtt-1.0.tar.gz (40kB):
  10  Downloading paho-mqtt-1.0.tar.gz (40kB):
  20  Downloading paho-mqtt-1.0.tar.gz (40kB):
  30  Downloading paho-mqtt-1.0.tar.gz (40kB):
  40  Downloading paho-mqtt-1.0.tar.gz (40kB):
  50  Downloading paho-mqtt-1.0.tar.gz (40kB):
  60  Downloading paho-mqtt-1.0.tar.gz (40kB):
  70  Downloading paho-mqtt-1.0.tar.gz (40kB):
  80  Downloading paho-mqtt-1.0.tar.gz (40kB):
  90  Downloading paho-mqtt-1.0.tar.gz (40kB):
  100  Downloading paho-mqtt-1.0.tar.gz (40kB):
  Downloading paho-mqtt-1.0.tar.gz (40kB): 40kB downloaded
  Running setup.py (path:/private/var/folders/wl/jl1lhcz52lbfb5n6ryrrjt_00000gn/T/pip_build_pharaohkj/paho-mqtt/setup.py) egg_info for package paho-mqtt

Installing collected packages: paho-mqtt
  Running setup.py install for paho-mqtt

Successfully installed paho-mqtt
Cleaning up...
```

## paho の python ライブラリ準備(自前ビルド編

```
$ mkdir mqtt.py
$ cd mqtt.py
$ git clone http://git.eclipse.org/gitroot/paho/org.eclipse.paho.mqtt.python.git ./
$ sudo python setup.py install
Password:
running install
running build
running build_py
running install_lib
creating /Library/Python/2.7/site-packages/paho
copying build/lib/paho/__init__.py -> /Library/Python/2.7/site-packages/paho
creating /Library/Python/2.7/site-packages/paho/mqtt
copying build/lib/paho/mqtt/__init__.py -> /Library/Python/2.7/site-packages/paho/mqtt
copying build/lib/paho/mqtt/client.py -> /Library/Python/2.7/site-packages/paho/mqtt
copying build/lib/paho/mqtt/publish.py -> /Library/Python/2.7/site-packages/paho/mqtt
byte-compiling /Library/Python/2.7/site-packages/paho/__init__.py to __init__.pyc
byte-compiling /Library/Python/2.7/site-packages/paho/mqtt/__init__.py to __init__.pyc
byte-compiling /Library/Python/2.7/site-packages/paho/mqtt/client.py to client.pyc
byte-compiling /Library/Python/2.7/site-packages/paho/mqtt/publish.py to publish.pyc
running install_egg_info
Writing /Library/Python/2.7/site-packages/paho_mqtt-1.0-py2.7.egg-info
```

### sudo いるのか？

`http://www.eclipse.org/paho/clients/python/` にも

> The final step may need to be run with sudo if you are using Linux or similar system.

とあるので必須。

```
$ python setup.py install
running install
running build
running build_py
creating build
creating build/lib
creating build/lib/paho
copying src/paho/__init__.py -> build/lib/paho
creating build/lib/paho/mqtt
copying src/paho/mqtt/__init__.py -> build/lib/paho/mqtt
copying src/paho/mqtt/client.py -> build/lib/paho/mqtt
copying src/paho/mqtt/publish.py -> build/lib/paho/mqtt
running install_lib
creating /Library/Python/2.7/site-packages/paho
error: could not create '/Library/Python/2.7/site-packages/paho': Permission denied
```

# sample 実装

## reference

http://www.eclipse.org/paho/clients/python/docs/

## 参考

下記ページを参考に `pub.py` と `sub.py` を作成。

https://gist.github.com/voluntas/8238751


# Test

1. MQTT Server開始 `mosquitto`
1. subscriber開始 `python sub.py`
1. publisherで送信 `puthon pub.py`

## Perfomance Test

パフォーマンステストのために1000回 insntance.publish をループするように作ってみたが、
20回しか実行されない・・・。→ Mosquitto側の制限らしい。
