---
title: Investigating LPWAN optimization of satellite localization in LTE NB-IoT and Dash7 Alliance Protocol
author: Daniel Robinson, Prof MJ Booysen
date: Stellenbosch University, March 2019
tags: [LTE, wearables, healthcare, safety, critical, life-threatening, SDR, NB-IoT, Dash7, localization]
abstract: |
  In critical use cases, localized wearables and assets require long-range bidirectional wireless networks such as GSM, NB-IoT and Dash7. Non-critical applications can make do with unidirectional LPWANs such as LoRaWAN and SigFox. This paper focuses on the requirements for critical IoT in a power efficient manner and in the indoor-outdoor realm.

toc: false
lof: false
lot: false
link-citations: true
csl: ieee.csl
linkcolor: blue
+ni: NB-IoT
+lr: LoRa
+lw: LoRaWAN
++: +
---

# Abstract

In this thesis, we are trying to solve for a better form of localization using LPWANs. Bidirectionality has multiple benefits.

# Introduction

This thesis is split up into sections, where the literature study introduces various topics and related work in LPWAN localization. The design chapter outlines the development methodology required and hardware created for the purpose of testing. Field testing involves taking the developed hardware indoors and outdoors and testing against multiple metrics. Simulations help to model the systems involved and predict how future enhancements could affect the outcome. The results from the simulations and field tests are compared, and the analysis forms suggestions for future work, until the work is concluded.

The appendix contains scripts, schematics and more documenting the entire process for the reader to reproduce.

The aim of the thesis is to identify how much of a benefit bidirectional LPWANs have in localization as opposed to a unidirectional one.

Consider a unidirectional wireless network that, although it has many kilometers of range, has limited capability in receiving downlink messages from gateways. Adding a GPS/GNSS module is increasingly trivial and inexpensive these days [@Allan2013], although one still has to deal with the occasional cold start and periodic receive windows to determine the whereabouts of the device in question [@Bulusu2000]. To avoid using the receive windows unless necessary, one can easily know when a device is static by observing movement via an accelerometer or similar [@Bujari2012], but purposefully locomotive devices require more computationally expensive means such as dead reckoning to determine if the endpoint has moved significantly to require another GPS/GNSS location update [@Goyal2011]. 

A more effective alternative can be periodically observing the receive signal strength indicator (RSSI) for changes which directly translate to movement in meters which warrant a GPS/GNSS location update. RSSI has been used in fingerprinting localization for GSM-based devices [@Ibrahim2012]. Listening for a terrestrial tower certainly doesn't require a lower receive sensitivity than for a satellite a few hundred kilometers in the sky, and with a much higher throughput than the typical 50 bit/s of GPS/GNSS. GPS/GNSS signals can also be relayed indoors using an outdoor and indoor antenna [@Haddrell2001].

One of the benefits of bidirectional LPWANs in satellite localization is the fact that they have the capability of beaconing a positioning reference signal [@Lin2017].

There are many LPWANs out there, but we can split them up into two groups. Just a few of the unidirectional ones there is:

* SigFox
* LoRaWAN
* NB-Fi

And of the bidirectional ones there is

* NB-IoT
* EC-GSM-IoT
* RPMA
* Weightless SIG
* Dash7
* WiFi HaLow

Briefly, SigFox is an ultra-narrow-band wireless technology that one can send 140 12-byte messages per day due to the duty cycle limitation of unlicensed frequencies. One can also receive 4 downlink ack messages, but this is not good enough when looking to optimize the sending of GPS/GNSS updates [@SigFox2016].

LoRaWAN uses chirp-spread-spectrum (CSS) and is publically accessible from networks such as The Things Network (TTN). Unfortunately, although that has the best coverage, it only uses class A which means it cannot listen for asynchronous downlink messages except after an uplink (which defeats the purpose of avoid unnecessary uplink transmissions which draw large current) [@Adelantado2017].

NB-IoT is LTE's replacement for the power hungry GSM that some IoT devices still use. GSM is an aging technology which is being turned off in some parts of the world. It has 7 times better range and coverage, and power saving which can let a device last 10+ years on a single charge [@Wang2017c].

EC-GSM-IoT is a form of eGPRS optimized for the IoT. It is still in the trial stages of development, however [@Bergman2017].

RPMA by Ingenu is a 2.4GHz technology for M2M communications. It is primarily used in North America for the oil & gas industry, amongst others [@Ingenu2016].

Weightless SIG reuses TV whitespace, and NB-IoT is actually formed off this protocol [@Weightless2015].

Dash7 is a military RFID standard that has also grown into a medium range LPWAN [@noraird7].

NB-Fi Protocol is an open LPWAN protocol, which operates in unlicensed ISM radio band. Using the NB-Fi Protocol in devices ensures stable data transmission range of up to 10 km in dense urban conditions, and up to 30 km in rural areas with up to 10 years on battery power [@Ikpehai2018b].

HaLow (pronounced halo) is a low-power, long-range version of the IEEE 802.11 Wi-Fi standard. HaLow is based on the Wi-Fi Alliance 802.11ah specification and is expected to play an important part in IoT.

**Localization --> LPWAN --> IoT**

In essence we're focusing on optimizing satellite localization for IoT via a certain kind of LPWAN.

[problem; bidirectionality; nb-iot; lorawan; gps; terrestrial localization; unidirectionality drains battery;]

# Literature Study

This section handles related work, and looks at NB-IoT and Dash7 in the IoT. It has a top-down approach and begins by introducing certain topics.

## The IoT

In today's world, smart devices are connected to the internet in various ways. In terms of wireless networks, we have many LPWANs and LPLANs that compete for adoption by enterprise and consumers alike. 

Gartner predicts that there will be more than 20.8 billions of smart things that will be connected to Internet by 2020, whereas the worldwide number of devices was 6.4 billions in 2016 [@Ayoub2018c].

## LPLANs

Low Power Local Area Networks (LPLANs) include BLE, 6LoPAN, Thread, ZigBee, WiFi and others. 
Unfortunately, due to country regulations the output power is limited especially for unlicensed frequencies. They may not even be suited for long range on the PHY layer, but they can essentially be considered indoor technologies with ranges of 10-100m [@Lee2007].

## LPWANs

Low Power Wide Area Networks (LPWANs) include SigFox, LoRaWAN, NB-IoT, Dash7, Weightless, N-Wave, NB-Fi, Thread and others. Some of these, like SigFox and LoRaWAN are unidirectional, which make them unsuitable for critical applications which require downlink acknowledgement or more. These have ranges from 2 - 20 km and can be considered outdoor technologies along with cellular IoT [@Ikpehai2018b].

## Cellular IoT

This includes LTE Cat-M, LTE Cat-NB or NB-IoT and EC-GSM-IoT. GSM has high battery usage due to constant synchronization in active mode, and un-optimized transmission of data. It is generally not considered in this thesis because it is a sunsetting technology. LTE-M is also considered a high-power technology and is not as suited for the IoT as NB-IoT is [@EricssonAB2016].

## Leo satellite constellation for the IoT

The potential use of constellations of satellites for IoT applications is of growing interest. With booming development in the IoT sector and as a powerful supplement to terrestrial systems, LEO constellation-based IoT is worth being focused and studied. To make this topic become a reliable cost-benefit solution, further research is required in transmission scheme, system security and low power consumption design. [@Qu2017c]

## Terrestrial vs satellite localization

TDoA, ToF, Aoa, RSSI, are all land-based techniques for pinpointing the location of an endpoint. They require real-time clocks accurate to the millionth of a second as well as expensive gateway hardware. Depending on the frequencies, wireless network and modulation, one can get different ranges. This is useful for the indoors.

Unfortunately, one has to sacrifice range for accuracy.

Satellites, on the other hand are in stable LEO or geostationary orbits and a constellation of satellites can keep in constant synchronization using atom clocks . One retains accuracy, even over long distances due to the ultra high precision of the clocks. This is useful for the outdoors.

Besides having the ability to measure RSSI which seems quite standard in wireless networks, NB-IoT is also lucky to have the benefits re-using the Timing-Advance (TDoA) hardware when upgrading cellphone towers with the capability. This means that one can reasonably approximate the position of an endpoint to within a 1000m.

## 3GPP Positioning for IoT

Many use cases in the Internet of Things (IoT) require or benefit from location information, making positioning a vital dimension in the IoT. The 3GPP has dedicated a significant effort during its Release 14 to enhance positioning support for its IoT technologies. There are still design challenges with regard to positioning support in LTE-M and NB-IoT that need to be taken into consideration. Nevertheless, the 3GPP is working on enhancing position support such as OTDOA, which is a downlink based positioning method. The OTDOA positioning reference signals can also be simulated to illustrate the positioning performance [@Lin2017],[@Miao2018].

## Fog computing

Fog computing is considered a good solution to address the demand for massive connections and low-latency applications by pushing some computing or processing tasks from the cloud servers to the Fog nodes, or close to the mobile edge. A Fog node can be viewed as a reduced capability of a cloud server and/or integrated with a small cell for handling the telecommunication services. There are several potential applications of the Fog computing node technology associated with NB-IoT small cell and the cloud services for smart parking, smart home, and smart retail and delivery services [@Chang2017].

## Massive IoT platforms

To be sure that LPWANs can be well scaled, they require a cloud platform well suited to the large number of connections such as Cisco-Jasper and ThingsBoard [@Hejazi2018a].

## Push vs pull model

Most LPWANs are unidirectional, meaning they transmit data in one direction only. This is especially true in the case of LoRaWAN and SigFox and means they use a push model.

A push model is bad for the battery when periodically sending data. It does help to make the data transmissions event-based, however.

NB-IoT and Dash7 for example, are bidirectional which means they can stay quiet for longer and only send data on-demand ~ when it is needed. This would make it a pull model and is useful for critical use cases as well [@Mekki2018a].

## Data on-demand

One thing to take into account when looking at bidirectionality vs unidirectionality is that transmit current is usually much more than the receive current required. By limiting TX transmissions such that the user only requests data on-demand when it is required, battery savings ensue.

## Stealth vs discovery beacons.

Stealth is useful for a device to remain hidden unless queried by an authorized network. It's not necessary to send out data unnecessarily else it's essentially a beacon mode for hackers and the like to discover where the device is and gain unauthorized access.

## IoT Data Tsunami vs "Google-like" IoT search

It has been suggested that periodically sending data, and seeing how many millions of devices will eventually be in use it will create a data tsunami of information too large to process. It can be argued that it'll be one of the sources that feed the field of machine learning, however.

On the other hand, imagine a kind of IoT where the user queries IoT devices manually for tailored search queries, like "get me a list of the devices currently in room 4A and tell them to turn on for half an hour?" or "where is my stuff?".

## NB-IoT

NB-IoT is the cellular industry's response to creating an LPWAN which will last many years into the future.

### Releases

In 3GPP Release 13, NB-IoT was introduced to support low-cost, low-power wide-area communications for Internet of Things (IoT) using LTE technology. NB-IoT has been designed to meet the following objectives [@Ratasuk2017a]:

* Ultra-low complexity and low-cost IoT devices.
* Indoor coverage improvement of 20 dB compared to legacy GPRS, corresponding to a Maximum Coupling Loss (MCL) of 164 dB, while supporting a data rate of at least 160 bps at layer 3.
* Support of massive number of low-throughput devices – at least 52547 devices within a cell-site sector.
* Improved power efficiency – battery life of ten years with battery capacity of 5 Wh.
* Exception report latency of 10 seconds or less for 99% of the devices.

In 3GPP Release 14, these major enhancements were introduced for NB-IoT: 

* Location services based on Enhanced Cell-ID (E-CID) and Observed Time Difference of Arrival (OTDOA).
* Multicast downlink transmission based on using single- cell point-to-multipoint.
* Higher peak data rates for NB-IoT user equipment. 
* Support of paging and random access procedures on non-anchor carriers.

In 3GPP Release 15, work on NB-IoT should be completed by June 2018. The following features are expected to be introduced :

* Latency and power consumption reduction – techniques to be considered can include wake-up channel, data transmission during random access procedure, quick RRC release, etc.
* Narrowband measurement accuracy improvements by using additional existing signals.
* Increase NPRACH reliability and support cell range of up to 100 km.
* NB-IoT small cell support.
* Reduced system acquisition time by improving cell search and system information acquisition performance.
* UE differentiation by considering additional UE-specific information in the UE information transfer procedure.
* Support for TDD for in-band, guard-band, and standalone operation modes of NB-IoT.
* Access barring enhancement. 
* Enhancements to support pairing of standalone carrier with in-band/guard-band carrier.
* Support of extended NB-IoT power headroom report range and finer granularity 

### Criticism

It has picked up criticsm for it's seemingly low battery life and high cost of infrastructure (Pat Burns et al).

### Forecast

Over time the 3GPP will refine the standards such that it should become the main LPWAN that enterprises, industry and consumers use.

## Dash7

Dash7 is considered a medium range LPWAN and is made for the full networking stack. It delivers an open standard for ultra low power mid-range sensor and actuator communication known as DASH7 Alliance Protocol (D7AP). D7AP is based on active RFID standards ISO 18000-7 for 433 MHz communication, however it has been significantly extended. It was originally intended by the US Department of Defense for container inventory and grew to become a medium range bidirectional wireless network system [@Weyn2015] useful in the indoor-outdoor realm. D7AP is modelled after a BLAST (Burst, Light, Asynchronous, Stealth, and Transitional) communication system which enables it to be a LPWAN competitor. D7AP is a full-stack protocol defining the complete OSI model, with support for three sub-GHz ISM bands, and three data rates (9.6 kbps, 55.55 kbps, and 166.67 kbps), as discussed above. D7AP uses 2-GFSK, the modulation schemes.

D7AP can also re-use the PHY layer (radio frontend) of other LPWANs.

Wizzilab is one of three main users of Dash7. It offers the only full-kit open to development (at least in the form of an application processor).

Haystack is another user of Dash7.

[https://github.com/jpnorair/OpenTag](https://github.com/jpnorair/OpenTag)

Lastly, the developer community. 

[https://github.com/MOSAIC-LoPoW/dash7-ap-open-source-stack](https://github.com/MOSAIC-LoPoW/dash7-ap-open-source-stack)

Also, it should be possible to reuse the RF PHY layer of NB-IoT for Dash7's OSI stack, resulting in a compressed tracking solution that works well both indoors and outdoors.

## Other LPWANs

Other LPWANs will be compared in this thesis, but not in-depth with regard to field tests as NB-IoT and Dash7. The point of the thesis is to evaluate how a bidirectional network can optimize satellite localization, and not merely comparison of all the bi-directional LPWANs. There is great info on this in [@Ikpehai2018b].

### LoRa

LoRa is a PHY layer Radio implentation that uses Chirp Spread Spectrum (CSS). Depending on how it is implemented in the rest of the OSI levels, it can be quite useful.

#### LoRaWAN

##### TTN

The Things Network (TTN) is a public platform for developers to create free global coverage over LoRAWAN

##### LoRaServer

Can do class B and C LoRaWAN.

### SigFox

Unidirectional.

### NB-Fi

Unidirectional. WavIoT.

### EC-GSM-IoT

Simulations and trials.

### RPMA

North America. Equivalent to cellular standard but expensive .

### Weightless SIG

Uses TV whitespace but.. [@Raza2017].

### Dash7

Too many benefits which raise an eyebrow. Would be great to do a few field tests to see how it really fares, and compare it to things like Dash7 over LoRa.

### WiFi HaLow

No traction.

# Design



## Devices

There exist many devices to test:

* Nordic NRF91 with firmware mfw-m1_nrf9160_0.6.6-13.prealpha
* Ublox N200
* Simcom 7000E
* Quectel BG96
* Sierra wireless WP7702
* etc

## PCB hardware

Useful to monitor the current directly. The BG96 will be used as it has GPS on-board as well as NB-IoT.

## RF attenuation

Added UFL connector instead of.

-140 + 66 dBm,

, +17 trace cut

0 dBm trace 2 cut

-70 dBm @ zte antenna



# Field Tests

## Measuring current

Using an MX 58HD DMM, one can measure 4.501 mA through a 4615 ohm resistor at 21.15V. Theoretically it should be 4.582 mA so that gives an error of 1.82% or ~2%.

## Current vs RSSI

To measure the current, a Max 58HD DMM will be used at the 5mA, 50mA and 500mA settings respectively. The peak setting will be used, which can measure 1ms signals. The burden voltage will be taken into account.

The endpoints can measure the TX and RX dBm themselves, but to change the RSSI values on needs attenuation.

![Variable RF attenuator](C:\GIT\masters\thesis\images\circuit-symbol-attenuator-variable-01.svg)

Two of these will be used in series: the HP8494B and the HP8496A. One has a range of 11dB in 1dB steps, and the other has a range of 110dB in 10dB steps, so it is possible to get a full range of 110dB in 1dB steps.

## Distance vs RSSI

This test will require multiple points in a line spaced approximately x meters apart. Since the tower to be tested against is based in a town, a straight line test is not directly possible, but a reasonable approximation can be made, especially with more points it should tend closer to the true model of signal propagation.

![The data can be collected along roads concentrically from the base station.](C:\Users\d7rob\AppData\Roaming\Typora\typora-user-images\1551192803520.png)

![The data can also be collected radially from the base station](C:\Users\d7rob\AppData\Roaming\Typora\typora-user-images\1551194001439.png)

## Cold start vs Hot start

This will involve tests inside buildings and outside of them. At the same time, RSSI values will be gathered to determine if the device is indoors or outdoors. Perhaps it is possible to grab a gps signal just as a person is entering a building.

![Tests inside and outside these building perimeters](C:\Users\d7rob\AppData\Roaming\Typora\typora-user-images\1551193534309.png)

# Simulations

Used to model the field tests for repeatibility and also to see the impact of future changes, releases and suggestions.

# Analysis and results

It either seems effective or it does not. If inbetween, it requires a specific setup, and that would be discovered soon.

# Conclusion

This thesis set out to find what benefits bi-directionality brings to LPWANs in satellite localization. Although there are terrestrial means of localization available, these are only catered for in the literature and simulations as they are expensive to set up otherwise.

It also aims to bring to light the pitfalls that many companies and developers make when using unidirectional LPWANs in asset and personnel tracking solutions, such that a battery life of only a couple of days ensues, where one is aiming for a couple years at least.

# Questions

How come Dash7 can communicate more than LoRaWAN?

LoRaWAN can transmit more often than every few minutes?

Cortus?

Can we prove that NB-IoT truly is low powered?

Is RTK too short range?

NB-IoT broadcast?

NB-IoT P2P?

Am I refining asset tracking for NB-IoT?

Does moving along a circumference of RSSI change significantly with building interference involved?

Indoor tracking always uses a specific custom gateway.

Does OTDOA overcome Fresnel zone inaccuracies?

How accurate is OTDOA?

Can NB-IoT support “hot start” GPS location acquisition?

Are Vodacom's towers release 14?

Can I make my research more bottoms up?

Can I make a masters on a single sentence? Haha..

What does the Gartner IoT forecast say and is it true a few years later?

Can I do a bottoms up approach in my masters?

What is so bad about LoRa?

Define topics then talk about them?

# Answers

Does the IoT data tsunami feed machine learning?

- Yes. So what's wrong?
- The problem is that many devices are unidirectional.

NB-IoT P2P? 

- Yes, it is included in the spec in future
- One could also re-use the RF frontend and add Dash7
- MSK downlink, OFDM uplink
- Am I going to consider it? I don't know

LoRaServer can interface with Class B and C gateways..

- Is it worth setting up? No. Time and budget constraints.

Can NB-IoT's indoor penetration be used to determine where something is?

- Apparently GSM can be used to achieve 4m horizontal accuracy and a 60% chance of determining which floor something is on.
- There is also a paper which suggests using the information from GSM towers in GPS/GNSS-denied areas, although GSM is a sunsetting technology therefore it is not considered in this paper. They even suggest that their approach can be more accurate using open databases of cell tower locations and not requiring synchronization with any towers.
- However, although can be assumed that similar approaches can be used using the NPRS (Narrowband Positioning Reference Signal), OTDOA's downlink approach using assist information from the tower should be more accurate.

Doesn't NB-IoT come with some kind of localization?

- CellID
- OTDOA

OTDOA?

- Can only be field tested this year. Out of scope of time and resource constraints.
- RSSI can be used for now.

LoRaWAN vs Dash7 is well-documented. 

- except TTN? Should be fine.

Dash7 vs NB-IoT?

- If I compared the two, I'd find that coverage, infrastructure cost is significantly different, otherwise same in bidirectionality. Both can exhibit P2P, except NB-IoT only in future.
- They are essentially similar

Haystack claims 1m indoor accuracy using Dash7. What are the challenges?

- Apparently it uses vertex data from reference nodes for RSSI & RF fingerprinting

How to fingerprint?

- Too complicated in dynamic environments

Indoor-Outdoor is the third realm?

- It is considered an IoT blindspot, because there are few solutions to cater for both short of using multiple radios.
- Usually we can consider IoT to be segmented into two realms, the indoor and outdoor realm.
  - WiFi, ZigBee, BLE are all great for indoors, while cellular networks and LPWANs compete in the outdoor sphere.
- What about use cases that require both realms?
  - A major use case is precisely locating things in real time.
  - For example, 
    - in access control one wants to locate a person inside and among multiple buildings in a secure area.
    - in the supply chain one wants to monitor critical shipments in-transit, in and around warehouses.
    - asset management
  - this is useful for critical applications and the IoMT

Although Dash7 bridges the gap between LPLAN and LPWAN, wouldn't it be better if LPWANs can handle all three realms?

- There will always be PAN/WLAN networks, and BLE and WiFi is the dominant network technology here, but it only works well within room or building sized environments respectively.
- Long range cellular networks such as GSM and LTE are optimized for low bandwidth and high battery life in the form of LTE-M and NB-IoT. There also exist LPWAN solutions such as SigFox and LoRaWAN. These work well for the outdoors
- Dash7 is hoping to bridge the gap by?
  - Encompassing both LAN coverage as well as WAN coverage in a low powered form.
- Dash7 is also a full networking stack which can reuse the PHY RF layer of other network standards, which means it is quite versatile. 
- Would it pass 3GPP / FCC standards if it reused NB-IoT's frontend?
- It's a tough question for NB-IoT because it remains to have a high cost of infrastructure (CAPEX and OPEX) required for cell tower, eNodeB, spectrum licensing etc.
  - But Release 15 does state picocell / small cell usage.
- Dash7 is good for now, NB-IoT is good for the future.
- Can Dash7 live on if it reuses NB-IoT's RF frontend? 
  - It is not likely that it would become the defacto standard as 3GPP is creating that for the cellular industry. But if it can work concurrently on a modem, then it adds useful features such as P2P. Is it worth the capital outlay to implement this if future LTE releases specify P2P communications? No.
- To answer the question, it would seem possible for NB-IoT to be the winner in future with its P2P and small cell in future releases.
- Can Dash7 have the same range as NB-IoT?
  - Dash7 can output at 27 dBm and NB-IoT at 23 dBm. This means that it only really depends on the gateways. In fact, the final answer is the MCL that the technology supports, and NB-IoT can support 164 dBm whilst Dash7 only 

Is it always good to aim for decentralization?

- Yes. The more one can do away with the man-in-the-middle, the better.

# References

