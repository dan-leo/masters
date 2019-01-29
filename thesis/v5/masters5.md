---
title: NB-IoT in standalone bidirectional IoT and wearable applications
author: Daniel Robinson, Prof MJ Booysen
date: Stellenbosch University, Jan 2019
tags: [LTE, wearables, healthcare, safety, critical, life-threatening, SDR, NB-IoT, Dash7, localization]
abstract: |
  NB-IoT, GPRS, LoRaWAN, SigFox and Dash7 are among a few wireless technologies contending for a niche in the IoT and wearable sphere. Building a standalone application in actuator control and localized use cases requires bi-directionality. This leaves NB-IoT and Dash7. This paper outlines why NB-IoT is the best technology to take into the future.

toc: false
lof: false
lot: false
link-citations: true
csl: ieee.csl
linkcolor: blue
+ni: NB-IoT
++: +
---

# Introduction

A common saying in today's world is "there's an app for that". This implies that cellphones, which constitute a major part of augmenting our daily lives by us becoming instantly accessible in the form of calls, SMS, emails and instant messaging applications such as WhatsApp and Telegram, can do almost anything for us. Unfortunately, there are some limitations that are unavoidable, such as:

- size and weight due to high-powered cellular networks such as LTE.
- app incompatibilities and bugs
- daily battery life
- WiFi is low powered but short range

That's where the internet-of-things (IoT) and wearables come in. 

Typical wearable applications use Bluetooth paired with a cellphone. Fitness tracking ones by Garmin, Fitbit etcetera use it to synchronize data with the cloud and apps to show progress. Insurance companies have taken this a step further (such as Discovery Health in South Africa) to use this data to incentivize an active exercising lifestyle (in the form of vitality rewards[^vitality]), which lowers premiums and ultimately lowers risk for life insurance / medical aid claims. Virgin Active, for example, offers gym facilities to enable this active lifestyle. Bluetooth also offers convenience by not having wires in other accessories such as headphones, car radios, speakers, keyboards and mice.

[^vitality]: Vitality rewards offer a plethora of discounts in flight, hotel, car rental, fuel, food, entertainment and other lifestyle choices. 

Bluetooth had teething problems in the beginning, and although incompatibilities have been smoothed out over the years, one should still factor in the technological literacy of the general population. What seems intuitive to developers may not seem to others, and striving for a plug-and-play nature of a device is always the best ideal.

For this, one desires a truly standalone solution. In a city, Wifi or Bluetooth is too short range and does not have the seamless cell reselection capabilities as cellular networks have. Consider the LTE variant of the Apple watch for $500-800. It only has 18 hours of battery life, so it is essentially a cellphone on your wrist.

IoT typically uses GSM or LPWAN networks to connect endpoints to the internet. GSM is great for bi-directionality, especially in  real-time applications as it is 'always-on' with constant synchronization on the physical RF layer between tower and endpoint. In battery-powered use cases, it is considered power hungry and takes approximately a minute to complete the network registration steps, packet switched context and tcp socket setup from modem boot. This is useful for data sent or received periodically. Unfortunately, it is also a sunsetting technology being switched off in certain countries around the world. Although, in SA it is still a great source of revenue for cellular service providers as many of the general population still use 'cheap' cellphones that can only call or SMS. LPWAN networks such as SigFox or LoRaWAN have great low battery usage, however are restricted by RF duty cycle limitations on the unlicensed frequency bands such as ISM that restrict the number of messages that can be sent per day. They can request a reply from the server, but most of the time the data transmission is unidirectional -- from endpoint to gateway. They can request a reply, but not passively listen for one from a gateway on demand. LoRaWAN also has low setup costs via the ability to install inexpensive public gateways with TTN (The Things Network). And SigFox has high range due to its ultra-narrow (carrier-phase) bandwidth.

![LTE variant of the Apple Watch Series 4](C:\GIT\masters\thesis\images\applewatch.JPG)

NB-IoT is the cellular-IoT response to LPWAN networks. It benefits from licensed frequencies which don't have restrictions on data throughput, except in monetary terms. Being bidirectional, it wins in localized and actuator control use cases. In localization, this is especially true in the case of assisted GPS/GNSS where sending ephemeral and almanac data from the internet via multi-cast to end points will enable a hot start of a few seconds as opposed to a few minutes. It saves precious battery life since GPS/GNSS broadcasts are sent from satellites at a rate of 50 bits per second. GPS/GNSS is becoming cheaper as time progresses, lowering the need for expensive TOF, TDoA, AoA (terrestrial localization) needs. NB-IoT is unique that it gains TDoA and AoA from a mere software upgrade of existing cellphone towers and eNodeBs, yet there are still licensing costs which can exceed a few million ZAR a year. With nationwide adoption from a demand in use cases, it becomes more viable for cellphone service providers to roll out coverage. NB-IoT touts that it is an easy software upgrade, but the current situation in South Africa with ICASA and licensing costs still make this expensive. Luckily it only requires one 200kHz channel out of many, and GSM/GPRS can be re-farmed to use it. Certainly less than the 1.4 MHz required by LTE-M. LTE-M does seem useful as well, yet it doesn't have as much range or power-saving capability as NB-IoT.

Another mysterious contender is Dash7. It has its origins in the ISO 18000-7 standard for active RFID, intended by the US Department of Defense for container inventory and grew to become a medium range bidirectional wireless network system [@Weyn2015]

Seeing NB-IoT and Dash7 as viable in IoT and wearables will fuel use cases. Use case demand is directly proportional to coverage, and vice versa.

# Lit Study

What is the power dbm of Dash7? Max? In the Wizzikit?

What metrics are typically useful to determine the viability of a wireless network in iot and wearables? Probably range, coverage, battery usage, SNR, PDR, power saving modes.

NB-IoT has power saving modes such as eDRX, PSM.

Cannot get in touch with Haystack?

Vodacom, MTN roll out NB-IoT in SA somewhat.

# Design

Since NB-IoT and Dash7 seem curiously interesting in the wearable and IoT world, a series of metrics will be tested to investigate their viability. The research seems promising. Because LPWAN networks such as LoRaWAN and SigFox are unidirectional, they will not be investigated.

First, the technologies must be connected to the internet.

End-2017, MTN set up a ZTE NB-IoT basestation in Stellenbosch for the use of research and testing. Unfortunately due to technical difficulties, a connection was unable to be made until July 2018. Nevertheless, a few tests were done at MTN's testplant in Johannesburg for two weeks during April. One of four faraday cages were made available, and also included LTE-M and GSM to test.

Vodacom have coverage in Gauteng with 1200 Huawei basestations, however Cape Town is quite limited, with currently only two working at Century city and the CTICC.

## NB-IoT modems

A suitable end-point is also required to test NB-IoT. The following boards and feedback is stated:

For a start, Pycom's FiPy was tested since it had multiple wireless technologies such as SigFox, LoRa, LTE-M and NB-IoT of which potential comparisons could be made. Unfortunately efforts were unsuccessful. During April 2018, the FiPy NB-IoT bootloader had just been released. It was loaded on the Sequans Monarch modem. The developers stated that at that point in time it only worked on Ericsson basestations. The 8th band was manually set but unfortunately it just couldn't connect. Noting the power usage of the ESP32 and combined modem it was actually quite hot to the touch.

Ublox's SARA N200 was tested, with a sample modem from RFDesign populated on a PCB designed by Thomas Durand and assembled by Barracuda Holdings. Efforts were unsuccessful until  visiting Vodacom World Campus in Midrand on the last day. They had a very specific setup procedure which unfortunately RFdesign failed to indicate in their support. Luckily it could also be tested later in the day in Randburg again at MTN's testplant. The problem was an SI_AVOID and SCRAMBLING parameter which had to be properly set.

The testplant also had one of two Sierra Wireless WP7702 development kits in South Africa provided for by Philip Nel of sierra Wireless. This board was used to test NB-IoT, LTE-M and GPRS.

The Quectel BG96 was tested on MTN's basestation in Stellenbosch and on Vodacom's towers in Cape Town.

Nordic nrf91 has yet to be tested.

## Dash7 modems

* MuRata CRWXM1ABZZ1
* Wizzikit

## Metrics

* SNR
* PDR
* Bandwidth, throughput
* Range, coverage



## PCB

Design a PCB to take these multiple wireless technologies. Do merely network tests.

It will be on a two layer board.