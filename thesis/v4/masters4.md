---
title: NB-IoT vs Dash7 in ambulatory wearable applications
author: Daniel Robinson
date: Jan 2019
tags: [LTE, wearables, healthcare, safety, critical, life-threatening, SDR, NB-IoT, Dash7, localization]
abstract: |
  NB-IoT, GPRS, LoRaWAN, SigFox and Dash7 are among a few wireless technologies contending for a dominant market share in the IoT sphere. Each fulfills a niche in different user applications, yet common drawbacks limit the chance of taking the lions share. In wearables,

toc: true
lof: false
lot: false
link-citations: true
csl: ieee.csl
linkcolor: blue
+ni: NB-IoT
++: +
---

\vspace{10 mm}

> *Dedicated to bidirectionality*

# Introduction

The scope of this thesis is limited to the use of bidirectional wireless networks in wearables. Unidirectionality 

In terms of data transmission, unidirectionality means that it is sent in one direction only. Since the role of an endpoint is to capture data and react on it, it makes sense that an endpoint would transmit its data towards a central node. This is true in the case of LoRaWAN and SigFox.



it can be considered that their are two modes of operation. In the first, data the device will be event triggered or send data periodically 

# Literature Study

The first wearable in history was used to tell the time. Five hundred years ago, German inventor Paul Henlein created small watches which hung from the neck as pendants. It evolved fashionably into pocket watches for waistcoats, a form of bracelet for women, and became smaller and more precise over time. By 1904, it kept an aviator's hands free as a wristwatch when piloting a plane. This form of autonomy has grown into the diverse field one sees today. For example, they are used as advanced wearables
• Health/fitness sensor and monitor devices
• Wireless payment enabled devices

> Wearables make technology pervasive by incorporating it into daily life. Through the history and development of wearable computing, pioneers have attempted to enhance or extend the functionality of clothing, or to create wearables as accessories able to provide users with sousveillance — the recording of an activity typically by way of small wearable or portable personal technologies. Tracking information like movement, steps, and heart rate is part of the quantified self movement.

> The origins of modern wearable technology are influenced by both of these responses to the vision of ubiquitous computing. One early piece of widely adopted wearable technology was the calculator watch, which was introduced in the 1980s. An even earlier wearable technology was the hearing aid.

Adding bluetooth has created another leap where data can be collected and linked to a smartphone, extending its functionality.

Bluetooth wearables have been well refined, as the bidirectional protocol has been slimmed down to even the BLE low energy form. They last a reasonable amount of time, and the datarate even allows for voice communications amongst many others. However, even as manufacturers claim, it  really is a short range radio technology, with a reasonable expectation of around 10m.

One can also look at Zigbee etc for home automation, yet tied to a central gateway node.

The problem with bluetooth wearables is that it is ultimately tied to the high-powered battery life of a cellphone, which doesn't last more than 1-2 days. In our culture, we're used to charging a phone every night as we've become increasingly attached to the every day functionality augmentation it offers. Emails on the go, calls over coffee, company-wide decisions can be made at a few clicks.

To release a wearable from the short range shackles of bluetooth and similar, one should consider LPWAN technologies.

Combinations mean multiple radios, which exist outside the scope as although possible to enhance functionality, it is already more expensive.

A major use case for wearables is asset tracking.

A SigFox wearable is fine in ambulatory cases, provided emergency services reach the source of the distress signal within an hour. This is if a GPS location is sent every 30 seconds, until the daily 144 message limit has been used up.

A LoRaWAN wearable is similar to the SigFox one, except one will be able to send more data at less range.

A GPRS wearable will have high battery consumption during the (on average) 1 minute long transmission sequence.

An NB-IoT wearable will be fine as long as there's coverage.

Likewise for a Dash7 wearable.

As we can see in the kiviet diagram, there is no clear winner.

\onecolumn



Table: Brief comparison of different wireless technologies

|                 | Range      | Bidirectional | Power saving limitation                                   | Major drawback                    |
| --------------- | ---------- | ------------- | --------------------------------------------------------- | --------------------------------- |
| Bluetooth / BLE | 10 - 100m  | Yes           | None                                                      | Extremely low range               |
| LoRaWAN         | 2 - 7km    | No            |                                                           | Poor scalability.                 |
| SigFox          | 3 - 50km   | No            | A few seconds to transmit a message                       | Only 144 12-byte messages per day |
| GPRS            |            |               | Constant synchronisation when active. No PSM, eDRX. Heavy | Sunsetting technology             |
| NB-IoT          | 2-5km      | Yes           | Edge cases                                                | Slow roll-out                     |
| Dash7           | 0.2 - 2 km | Yes           | None                                                      | No public coverage                |

Table: LPWAN limitations in localization

|         | Localization     | RSSI | TOF/TDoA | Limitation                   |
| ------- | ---------------- | ---- | ---------------------------- | ---------------------------- |
| SigFox  | RSSI ++ GPS/GNSS | > 500m | No | > 500m and periodic checking |
| LoRaWAN | RSSI ++ GPS?     |  | > 925m | > 925m                       |
| GPRS    |                  | 50 - 2000m |  |                              |
| Dash7   | RSSI ++ A-GPS    | Yes  |   |                              |
|         |                  |      |      |                              |

Use cases

- predictive maintenance
- tracking
- Smart Lost and Found
- Drones
- Mobile Advertising
- Social Discovery
- Environmental Control Systems
- Industrial Automation Systems

![Kiviet comparing different technologies](C:\Users\d7rob\AppData\Roaming\Typora\typora-user-images\1547712492084.png)

\twocolumn

# Design

https://www.electronicdesign.com/displays/designing-low-power-displays-battery-powered-iot

https://bengoncalves.wordpress.com/2015/10/01/oled-display-and-arduino-with-power-save-mode/

https://learn.sparkfun.com/tutorials/reducing-arduino-power-consumption/all

https://www.electro-tech-online.com/articles/achieving-low-power-on-adafruit-trinket.830/

https://community.atmel.com/forum/samd21-sleep-current

[nrf52832 is BLE and is quite awesome, but the extra features are perhaps unecessary](https://learn.sparkfun.com/tutorials/nrf52832-breakout-board-hookup-guide/all#adding-arduino-compatibility) The board can even take Arduino, that being said. Look at Arduino Primo with the nrf52 + wifi

Charging LiPo with TP4056. Or TPS61200  https://github.com/sparkfun/LiPower_Boost_Converter

stm32duino

https://lcsc.com/product-detail/ST-Microelectronics_STMicroelectronics_STM32F103C8T6_STM32F103C8T6_C8734.html $1.9 or less.. $1.4 for 10+

https://lcsc.com/product-detail/ATMEL-AVR_ATMEL_ATSAMD21G18A-AU_ATSAMD21G18A-AU_C78624.html $4.3 or less.. $3.7 for 10+

http://wiki.stm32duino.com/index.php?title=Eclipse_%2B_PlatformIO

https://community.particle.io/t/tutorial-using-eclipse-st-link-v2-openocd-to-debug/10042

[stm32 has built-in RTC](http://www.stm32duino.com/viewtopic.php?f=13&t=924)

[stm32 schematic](https://robotdyn.com/pub/media/0G-00005692==STM32F103C8T6-STM32MiniSystem/DOCS/Schematic==0G-00005692==STM32F103C8T6-STM32MiniSystem.pdf)

stm32f103 has CAN protocol.  with 64
or 128 KB Flash, USB, CAN, 7 timers, 2 ADCs, 9 com. interfaces. 72MHz. 20 kbytes SRAM

https://github.com/blacksphere/blackmagic/wiki





# References

