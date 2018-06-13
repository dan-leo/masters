---
title: P2P NB-IoT::LoRa::Dash7 WAGL Emergency Response wearable
author: Daniel Robinson
date: June 2018
tags: [LTE, wearables, healthcare, safety, critical, life-threatening, SDR, NB-IoT, Dash7, localization]
abstract: |
  Upon the quest of finding the ultimate IoT solution for emergency response, an idea was borne which uses peer-to-peer networking and a suitable long-range LPWAN. Fast localization is key, along with the capability of sending critical physiological signals. A final practical PoC can be worn and tested in the form of either a LoRa or NB-IoT based system, both with Dash7 wireless P2P networking, RSSI trilateration engines and A-GPS. The two comparable systems also aid the licensed vs unlicensed LPWAN debate. The P2P network is most useful in WAGL mode which guides a responder directly to the wearer, besides the ability to operate independently from gateways in constrained cases.

toc: true
lof: false
lot: false
link-citations: true
csl: ieee.csl
linkcolor: blue
---

\vspace{10 mm}

> *Dedicated especially to the women who fear being out there in the wild streets alone.*

# Introduction

Around [52 people](https://africacheck.org/factsheets/south-africas-crime-statistics-201617) are murdered every day in South Africa[^inTheWorldToo]. This excludes rape, theft, assault, gang-related violence and other cases. Efforts to curb such activities are performed by the police force, neighbourhood watches, vigilantes and many other members of society. Common measures include prevention, taking control of life-threatening situations and monitoring frequent hotspots.

[^inTheWorldToo]: Although system aimed for South Africa, can be used world-wide.

Since eyes and protection cannot be everywhere, lives are threatened continually. Simple proof is in how hospitals and clinics fill up with new patients daily, including victims of aforementioned cases.

> *The only thing necessary for the triumph of evil is for good men to do nothing. -- Edmund Burke* 

It is a common problem and easy to take to heart. Increasing security has a certain momentum, with \<insert examples\>.

\<Find the link between applying security, the flaws, and the proposed solution\>

\<Point out that criminal intelligence can never be underestimated, but proposed solution will certainly aid society\>

\<Find a blanket term for all these different dangers and situations\>

Non-discrete solutions include rape whistles, mace, self-defence and so on.

When it comes to LoRa, \<insert examples\>

Haystack Technologies had created a clever Dash7 device called the [HayTag](http://haystacktechnologies.com/wp-content/uploads/2016/10/Haytag-Product-Sheet.pdf), but it never reached production due to insufficient crowdfunding at only 3% of it's \$150k target.

NB-IoT has some examples too, such as the [Connect Tag](https://www.zdnet.com/article/samsung-launches-nb-iot-gps-smart-tag), etcetra \<insert more\>

Since most systems are limited to a GPS based long-range linkup solution, we explore the possibility of guiding the responder to the location of the wearer in situations where weak or no satellite signals exists, especially in the case of buildings.

## Localization

The following table explains different localization modes.

| Long-range linkup | Peer-to-peer/Dash7 | Location          |
| :---------------: | :----------------: | ----------------- |
|        No         |        Yes         | WAGL, RTLS        |
|        Yes        |         No         | A-GPS             |
|        Yes        |        Yes         | WAGL, RTLS, A-GPS |



## Networking

Cellular vs LPWAN. Licensed vs unlicensed. 

# Literature Review

NB-IoT is not as publicized the technology it is to replace, GSM/2G/GPRS.

# System Overview

## A-GPS

Assisted-satellite data includes orbitals etc. This packet is about 1kB in size, and it would be good to have this data periodically in order to have a hot-start location within 20 seconds, as opposed to 2 minutes from a cold start. It also draws way too much energy.

## Cellular IoT

### EC-GSM-IoT

Lower power form of GSM, with extended coverage. Unfortunately 2G is in the process of being turned of in countries around the world.

### eMTC

This is a high-powered form of IoT communications which includes VoLTE. Most likely to replace mainstream 2G/GPRS.

### NB-IoT

NB-IoT is the 3GPP's response to emerging unlicensed LPWANs. According to Ryan vd Bergh, it should achieve mainstream adoption within 2 years time.

It is simpler than eMTC, and doesn't include VoLTE. The project will focus on this technology.

## LPWAN

### LoRaWAN

Since the UE has LoRaWAN capabilities, it can query the GW for satellite-assist data. Unfortunately LoRaWAN doesn't have unicast, so it is advisable to do receive this data sparingly.

### Dash7

A D7 GW can do multicast, however. This is perfect for sending satellite-assit data or FOTA upgrades to multi devices in the field simultaneously.

### SigFox

30-50 km range in rural environments. 3-10 km in urban environments.

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