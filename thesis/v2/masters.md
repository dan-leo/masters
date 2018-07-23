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



## Networking

Cellular vs LPWAN. Licensed vs unlicensed. 

# Literature Review

NB-IoT is not as publicized as the technology it is to replace, GSM/2G/GPRS.

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