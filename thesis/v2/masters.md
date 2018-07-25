---
title: P2P NB-IoT::LoRa::Dash7 WAGL Emergency Response wearable
author: Daniel Robinson
date: June 2018
tags: [LTE, wearables, healthcare, safety, critical, life-threatening, SDR, NB-IoT, Dash7, localization]
abstract: |
  Upon the quest of finding the ultimate IoT solution for emergency response, an idea was borne which uses peer-to-peer networking and a suitable long-range LPWAN. Fast localization is key, along with the capability of sending critical physiological signals. A final practical PoC can be worn and tested in the form of either a LoRa or NB-IoT based system, both with Dash7 wireless P2P networking, land-based localization and A-GPS. The two comparable systems also aid the licensed vs unlicensed LPWAN debate. The P2P network is most useful in WAGL mode which guides a responder directly to the wearer, besides the ability to operate independently from gateways in constrained cases.

toc: true
lof: false
lot: false
link-citations: true
csl: ieee.csl
linkcolor: blue
---

\vspace{10 mm}

> *Dedicated especially to the women who fear the unknown out there in the wild streets.*

# Introduction

Ideally, the more features, the better. For the purposes of clarity, the scope of the project will remain mostly in the region of LPWAN technologies. Nevertheless, it is interesting to note that piezoelectric and thermal energy harvesting can be used, besides solar. There are existing GSM + GNSS solutions in the market today which provide satisfactory performance, but the techniques can be considered archaic and not future-proof.

Around [52 people](https://africacheck.org/factsheets/south-africas-crime-statistics-201617) are murdered every day in South Africa[^inTheWorldToo]. This excludes rape, theft, assault, gang-related violence and other cases. Efforts to curb such activities are performed by the police force, neighbourhood watches, vigilantes and many other members of society. Common measures include prevention, taking control of life-threatening situations and monitoring frequent hotspots.

[^inTheWorldToo]: Although the system is aimed for South Africa, it can be used world-wide.

Since eyes and protection cannot be everywhere, lives are threatened continually. Simple proof is in how hospitals and clinics still fill up with new patients daily, including victims of aforementioned cases.

> *The only thing necessary for the triumph of evil is for good men to do nothing. -- Edmund Burke* 

It is a common problem and easy to take to heart. Increasing security has a certain momentum, with \<insert examples\>.

\<Find the link between applying security, the flaws, and the proposed solution\>

\<Point out that criminal intelligence can never be underestimated, but proposed solution will certainly aid society\>

\<Find a blanket term for all these different dangers and situations\>

Non-discrete solutions include rape whistles, mace, self-defence and so on.

When it comes to LoRa, \<insert examples\>

Haystack Technologies had created a clever Dash7 device called the [HayTag](http://haystacktechnologies.com/wp-content/uploads/2016/10/Haytag-Product-Sheet.pdf), but it never reached production due to insufficient crowdfunding at only 3% of it's \$150k target.

NB-IoT has some examples too, such as the [Connect Tag](https://www.zdnet.com/article/samsung-launches-nb-iot-gps-smart-tag), etcetra \<insert more\>

Since efforts in localization typically use GPS/GNSS, weak or no satellite signal creates a compelling case for guiding a responder to the distressed user.

Adding P2P capabilities adds decentralization to the centralized nature of the system, bringing the best of both worlds into a hybrid.

## Localization

The following table explains different localization modes.

| Centralized | Decentralized | Location          |
| :---------: | :-----------: | ----------------- |
|     No      |      Yes      | WAGL, RTLS        |
|     Yes     |      No       | A-GPS             |
|     Yes     |      Yes      | WAGL, RTLS, A-GPS |

Decentralized networks can reach centralized ones by multi-hops. Using a self-healing system of updating nodes that haven't reached a centralized gateway, one can make sure that messages get through as soon as possible.

## Networking

Cellular vs LPWAN. Licensed vs unlicensed. 

# Literature Review

NB-IoT is not as publicized as the technology it is to replace, GSM/2G/GPRS.

Current literature suggests common methods such as GSM, Bluetooth and GPS. Still, there are a number of localized applications beneficial to health and safety. A GPS solar powered GSM wearable which monitors autism in children is proposed in [@Ahmed2017c], but lacks details on extending battery life, coverage etc. A thorough investigation in elderly assistance, including fall detection (also in @Chavan2017a), heartrate and movement activity, is proposed in [@Bizjak2017a].

PPG sensor to detect heart attacks as in [@Valliappan2017], also uses GSM. ZigBee to base station monitors chronic diseases for elderly patients [@Jian2010]. Vital signs are monitored and sent via bluetooth in [@Wu2008a], [@Kale2017a], [@Rathi2017] and in the form of jewellery in [@Patel2018].

Kalman filters in [@Wu2016]. Sarsat 406 MHz life jacket in [@Serra2011]. GSM and GPS Telemedicine in [@Suganthi.2012a] and [@Tewary2016b]. Autonomous emergency bracelet for women proposed in [@Harikiran2016]. 

# Theoretical System Overview

## A-GPS

Assisted-satellite data includes orbitals etc. This packet is about 1kB in size, and it would be good to have this data periodically in order to have a hot-start location within 20 seconds, as opposed to 2 minutes from a cold start. It also draws way too much energy.

https://www.gps.gov/cgsic/meetings/2009/gakstatter1.pdf

UHF/VHF data radios - Pro: proven to be very reliable for RTK, free of charge. Con: requires licensing, limited distance, user managed. • Spread-spectrum (900MHz) data radios – Pro: license-free, free of charge, proven technology. Con: very limited dist., sensitive topo/obstructions, user managed. • GSM/CDMA wireless networks - Pro: wide area coverage, license-free. Con: coverage may not exist in work area, dropped calls, cost. WiFi/WiMax?

## Cellular IoT

### EC-GSM-IoT

Lower power form of GSM, with extended coverage. Unfortunately 2G is in the process of being turned off in countries around the world.

### eMTC

This is a high-powered form of IoT communications which includes VoLTE. Most likely to replace mainstream 2G/GPRS.

### NB-IoT

NB-IoT is the 3GPP's response to emerging unlicensed LPWANs. According to Ryan vd Bergh, it should achieve mainstream adoption within 2 years time.

It is simpler than eMTC, and doesn't include VoLTE. On the licensed side the focus will mainly be on this technology.

## LPWAN

### LoRaWAN

Since the UE has LoRaWAN capabilities, it can query the GW for satellite-assist data. Unfortunately LoRaWAN doesn't have unicast, so it is advisable to do receive this data sparingly.

### Dash7

A D7 GW can do multicast, however. This is perfect for sending satellite-assit data or FOTA upgrades to multi devices in the field simultaneously.

### SigFox

30-50 km range in rural environments. 3-10 km in urban environments.

## Physical characteristics

The device must be able to be worn discretely. Having it on the wrist, arm, etc. will help to measure physiological signals as well.

## Battery life

Deep sleep and the varying power-saving modes are crucial to extend the battery life of the system to at least a week on standby mode ( assuming a small LiPo between 85 - 150 mAh).

## Range

P2P has a medium range less than what one would expect from the different types of gateways.

## QoS

The quality of signal, SNR etc is also important. It helps to acknowledge data packets, and use listen-before-talk to increase duty cycle limitations etc.

# Simulated results

Using Jupyter, Python, MatLab etc to model a system using theoretical values.

# Experimental design

## Hardware

PCB designs to test the system.

* NB-IoT (Ublox SARA R412M or BG96) + GNSS (Ublox M8N) + MCU (ATSAMD21G18a)
* LoRaWan/Dash7/SigFox (B-L072Z-LRWAN1) + STM32L

![Ublox R412M + SAMD21G18a + Neo 7M](C:\GIT\masters\thesis\images\nbiot_pcb.JPG)

## Software

* C++

* Python

* Whatever it takes.

# Field Trials  

Testing testing and more testing.

# Data processing

Evaluating data.

# Results

Successful? Comparison?

# Conclusion

Useful to science? Beneficial to mankind?

# Ideas, questions, thoughts and answers?

* References
* Is NB-IoT the best?
  * Unfortunately depends on cellular operators, but everyone listens if one has money
  * Seems to have the best link budget, and slightly better than SigFox at indoor penetration
  * Ublox R412M has LTE Cat-NB1, Cat-M and EC-GSM.
  * Quectel BG96 also does, but GNSS integrated as well. It is expensive at about R1000 a pop.
  * NRF091 is still on it's way, but my favourite so far due to it's small form factor
* LoRa?
  * Despite it's promising characteristics, LoRaWAN is seemingly a failure
    * No listen-before-talk, 20% success rate
    * SF12 means one cannot send data frequently, but that's where one gets ones range.
    * No P2P
    * Simple, incomplete networking stack
  * Dash7 seems to address most of it's issues.
    * B.U.R.S.T.Y data
    * Bidirectional, broadcasting
    * P2P
  * Other networking stacks?
  * Wireless MBus?
* SigFox?
  * No.. low bandwidth, duty cycle limitations.
  * Good range, but unreliable after 6kmph.
* GNSS
  * TrigNet base stations across SA?
    * RTK corrections?
  * Built-in to modem chips seem more favorable
  * Keeping RTC alive and almanac stored will ensure a hot start of around 5 seconds.
  * Managed to capture some data between Stellenbosch, Somerset West and Cape Town International
  * Ublox M8N seems quite robust. An active antenna helps significantly for an ideal HDOP < 1.0
  * Ublox M7 is discontinued.
  * Satellite localization is definitely necessary for outdoor or the majority of use cases.
* Indoor localization?
  * Fingerprinting seems to be the best method
  * Universities in the Netherlands have managed to get under 1m accuracy using Dash7
* IMU data for dead reckoning?
  * Pitch, Roll, Yaw from Quaternions
  * Heading from magnetometer and GPS
  * MPU9250 has a dedication MPU (motion processing unit) for things like number of steps etc.
  * Could be useful to send an estimate back in real time.
  * It can also be used to determine if the wearer has crashed/fallen and needs help.
* What kind of battery does one need?
  * 85mAh seems to last about 4 days using a constant BLE connection to a phone 1m away.
  * 150mAh seems ideal for event based comms
  * LiPo
  * Button cell?
  * Wireless charging?
  * Energy harvesting?
    * thermal potential difference
    * piezoelectric (sound, vibrations, light)
* Dash7 seems to solve LoRaWANs challenges?
  * There's a very cool modem out there being the LRWAN1 which can handle SigFox and LoRa
    * Unfortunately a dual-boot solution has to be built to accommodate both
    * OSS-7, Haystack and Wizzilab have built a concurrent Dash7::LoRaWAN stack (must verify)
  * To be able to reuse the RF frontend is incredibly useful to save on space and power constraints.
  * Cortex build SoCs, and they have a private contract to integrate NB-IoT and Dash7.
    * These things usually cost millions of dollars.
  * Medium range, around 3km
* How can animal tracking be applied in our system?
  * They use VHF hand-held directional antennae to locate the animal.
  * Seems to be a purely RSSI based system
* How does a clap sensor apply to TOF?
  * Interesting as clap sensor needs filters
  * Speed of sound (340 m/s) is much slower than light and RF at 299794258 m/s.
  * TOF requires incredible accurate RTC, and synchronized. GNSS can help perhaps, but the ionosphere also causes interference.
* Which physiological signals could be most useful?
  * Heightened heartrate could signal a frightened state. If IMU says that the wearer has fallen/crashed and heartrate still low, then possibly unconscious.
  * Respiration can be determined from the IMU data as well.
  * Skin conductivity indicates sweat and possible stress.
* Where can I find data to test physiological signals?
  * HealthQ
  * They mentioned a website which I have somewhere..
* When will I have a device ready?
  * End of this year.
* What do I expect a device to do?
* Can Haystack help me?
  * Yes, but under their PSA (professional services agreement) they keep the IP and expect about $200/hr for 100 hours of work.
* How about an FPGA?
  * Yes, there is even an existing SDR solution for NB-IoT, but it costs at least $500k.
* SDR?
  * Well, yes.. the B200 but the open source software (OpenAIR interface) doesn't have NB-IoT yet, otherwise one has to pay yet again using other sources.
* Matlab for simulations?
  * Not really.. there were two small things they have in their toolbox, but no-where near complete.
* Even simulations cost money!
* What will I use for simulations?
  * Jupyter, python etc
* Will I even use machine learning?
  * It depends if I amass a huge amount of data that can only be optimized in a data science method.
* What do I want to have done before leaving to America in August?
  * I will buy a LTE Cat-M, Cat-NB1, EC-GSM board with GNSS and use a Hologram.io sim to test coverage in a few major cities in the U.S. like New York, Atlanta, Washington DC.
  * I'll have a PCB design on the way from China
  * Preliminary Lit study!!
  * LRWAN1 board familiarity with OSS-7
  * Wizzilab Dash7 modems work already in sending sensor data to the web. Haven't tested P2P functionality yet.
* What am I adding to society?
  * A solution which if taken up seriously can add peace of mind and alleviate crime starting in small towns.
* What am I adding to science?
  * Cortex also contributes to OSS-7. I consider it something big with a group of active developers who I am in touch with. Contributing to it will add value for science.
  * By trying both licensed and unlicensed LPWANs one aids the debate between the two.
  * Thomas is already comparing LoRa, SigFox, GSM and NB-IoT thouroughly and this provides a great background to the application in question.
* Am I still on track?
  * Well, I have a year left. I still think I can get a great deal done in this time.
  * For these last few weeks before America?
    * Well, at least I've gotten the Wizzikit to work, and explored some of the LRWAN1. Lit Study still needs work!, and the PCB is (can you believe) still in the process of being designed.
    * Seriously, the weeks go by rather quickly and I do a couple of other things in the mean time.
    * Perhaps I've taken a bit of a holiday from masters, but I'm back now!
* Last thoughts?
  * I think one of the things I've done is speak to numerous people about this problem, and it helps to slowly build up a clear, realistic picture of expectations and the technology.

# Appendix

Current people-tracking solutions today use high-powered cellular networks such as LTE/GSM and GPS. 

- The new Apple watch uses WiFi/LTE and GPS for SOS situations
- [Limmex](https://www.limmex.com/intl/en) emergency watch from Switzerland calls stored family/friends, besides normal watch functionality.
- [PAL wearable](http://www.projectlifesaver.org/Pal-info) from Project Lifesaver costs \$625 and \$30/month.
- [MindMe](http://www.mindme.care/payments/default.html) Alarm or Locate separately cost \£85.00 at \£16.50/month.
- [SafeLink](http://safelinkgps.com) watch costs \$200 and tracker costs \$150.

That is if they are independent. Some require a Bluetooth link to a cell phone to provide the necessary functionality. 

- [Revolar](https://revolar.com) comes in the form of jewellery and has a 3 layered alert system. Costs \$40-100.
- [mySOS](https://mysos.co.za/panicbutton) has a single alert and costs R499.

Or, they are connected to a home-based gateway and beacons to provide indoor tracking. 

- Tempo by [CareProtect](https://www.carepredict.com) looks after the elderly in this way.
- And so does the [Lively Safety Watch](http://www.mylively.com).
- There are many more on https://smartwatches.org/learn/best-senior-wearables-gps-trackers

# References