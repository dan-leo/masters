---
title: P2P NB-IoT/LoRa and Dash7
author: Daniel Robinson
date: 10 June 2018
tags: [LTE, wearables, healthcare, safety, critical, life-threatening, SDR, NB-IoT, Dash7, localization]
abstract: |
  Upon the quest of finding the ultimate IoT solution for emergency response, an idea was borne which uses peer-to-peer networking and a suitable long-range LPWAN. Fast localization is key, along with the capability of sending critical physiological signals. A final practical PoC is presented and compared in the form of a LoRa or NB-IoT based system with Dash7 wireless P2P networking, RSSI trilateration engines and A-GPS. The LoRa-based system can be worn and tested, whereas the NB-IoT based system is merely SDR-based. The P2P network shines when gateways are unavailable or 

toc: true
lof: false
lot: false
link-citations: true
csl: ieee.csl
linkcolor: blue
---

# Introduction

Around [52 people](https://africacheck.org/factsheets/south-africas-crime-statistics-201617) are murdered every day in South Africa. This excludes rape, theft, assault, gang-related violence and other cases. This is not without effort to curb such activities. There exist many members of society on-duty such as the police force, neighbourhood watches, vigilantes etcetera to prevent or take control of life-threatening situations. Eyes cannot be everywhere, and thus government hospitals, clinics still fill up with new patients daily.

It is a common problem and easy to take to heart. Increasing security has a certain momentum, with \<insert examples\>.

\<Find the link between applying security, the flaws, and the proposed solution\>

\<Point out that criminal intelligence can never be underestimated, but proposed solution will certainly aid society\>

\<Find a blanket term for all these different dangers and situations\>

\<Move the following info to an appendix\>

Current people-tracking solutions today use high-powered cellular networks such as LTE/GSM and GPS. 

* The new Apple watch uses WiFi/LTE and GPS for SOS situations
* [Limmex](https://www.limmex.com/intl/en) emergency watch from Switzerland calls stored family/friends, besides normal watch functionality.
* [PAL wearable](http://www.projectlifesaver.org/Pal-info) from Project Lifesaver costs \$625 and \$30/month.
* [MindMe](http://www.mindme.care/payments/default.html) Alarm or Locate separately cost \£85.00 at \£16.50/month.
* [SafeLink](http://safelinkgps.com) watch costs \$200 and tracker costs \$150.

That is if they are independent. Some require a Bluetooth link to a cell phone to provide the necessary functionality. 

* [Revolar](https://revolar.com) comes in the form of jewellery and has a 3 layered alert system. Costs \$40-100.
* [mySOS](https://mysos.co.za/panicbutton) has a single alert and costs R499.

Or, they are connected to a home-based gateway and beacons to provide indoor tracking. 

* Tempo by [CareProtect](https://www.carepredict.com) looks after the elderly in this way.
* And so does the [Lively Safety Watch](http://www.mylively.com).
* There are many more on https://smartwatches.org/learn/best-senior-wearables-gps-trackers

Non-discrete solutions include rape whistles, mace, self-defence and so on.

When it comes to LoRa, \<insert examples\>

Haystack Technologies have created a clever Dash7 device called a [HayTag](http://haystacktechnologies.com/wp-content/uploads/2016/10/Haytag-Product-Sheet.pdf).

NB-IoT has some examples too, such as the [Connect Tag](https://www.zdnet.com/article/samsung-launches-nb-iot-gps-smart-tag), etcetra \<insert more\>

|                                 | NB-IoT/LoRa Gateway available | Unavailable |
| ------------------------------- | ----------------------------- | ----------- |
| **Dash7 P2P network available** |                               |             |
| **Unavailable**                 |                               |             |

MatLab have a downlink waveform generator class called [NBIoTDownlinkWaveformGenerator](https://www.mathworks.com/examples/lte-system/mw/lte_product-NBIoTDownlinkWaveformGenerationExample-nb-iot-downlink-waveform-generation).

It may be possible to have a single-feed antenna for both LoRa and NB-IoT as in the following paper: [Multi-feed RF front-ends and cellular antennas for next generation smartphones](https://pdfs.semanticscholar.org/ff3d/322286f70661360b0c87c4d0e49536cc2564.pdf).

Although aimed for South Africa, the principals can be applied world-wide.