---
title: Narrow-Band Internet-of-Things Testing Framework for developers
author: Daniel Robinson, Prof MJ Booysen
date: Stellenbosch University, March 2019
tags: [LTE, NB-IoT]
abstract: |
  In South Africa, there is an attempt to add NB-IoT coverage. It is limited by use case demand, expensive licensing and general uncertainty about the technology. This thesis aims to highlight the challenges, advantages and disadvantages of the technology. By doing endpoint tests with multiple manufacturers one can paint an accurate picture of the capabilities of the technology. The technology is robust in certain test cases and scenarios, but additional work is required from the 3GPP to enhance the technology.

toc: true
lot: true
lof: true
link-citations: true
csl: ieee.csl
linkcolor: blue
+ni: NB-IoT
+lr: LoRa
+lw: LoRaWAN
++: +
---

# List of Abbreviations

**3GPP** Third Generation Partnership Project

**NB-IoT** Narrow-Band Internet of Things

# Introduction

There is fragmentation in the cellular industry (for manufacturers and service providers alike) when it comes to using certain technologies, standards and protocols. One of them in contention is NB-IoT, which is an LTE-based wireless technology which takes on the likes of LoRaWAN and SigFox.

Who is my target audience? Researchers, IoT enthusiasts. Myself.

## framework

- Background to the Research Problem/Question

  - What is the IoT?
    - It is a system of interconnected devices not requiring human interaction to transfer data. It started after the internet did.
    - The Internet of Things (IoT) is growing in popularity in the world. It connects many devices to the internet. These devices include sensors, actuators and event-monitoring systems and have applications in smart cities, agriculture, healthcare, manufacturing and more. This has also resulted in multiple IoT platforms in the cloud each with their own benefits [@Hejazi2018a], [@Lin2018b] and many connectivity options from endpoints to the cloud.
  - How does the IoT connect?
    - Connectivity options include wired, low-power local-area-networks (LPLAN) and low-power wide-area-networks (LPWAN). To reach the internet wired connections typically include Ethernet, fibre (FDDI) and telephone networks (if using ISDN or DSL). LPLAN connections are wireless with a range of up to 1000m and include Bluetooth Low Energy (BLE), Thread, 6LoPan, ZigBee and Wi-Fi. LPWAN connections are also wireless, but cover a much greater area with a few kilometers or more. These include LoRaWAN, SigFox, Neul, Nb-Fi and cellular networks such as LTE Cat-M, NB-IoT and EC-GSM-IoT.
  - What is NB-IoT?
    - 3GPP tech.
  - When did it start?
    - Release 13
  - What is it used for?
    - IoT and connecting smart devices to the internet
    - In terms of it's uses NB-IoT has applications in fog and edge computing, which means offloading cloud processing to the endpoint [@Chang2017],[@Jia2018a],[@Abedin2018a]. In localization it supports OTDOA and A-GPS positioning [@Korb2018], and aids other forms of navigation such as in the use of geomagnetism [@Liu2018g] and fingerprinting [@Nieuwenhuijzen1997]. Machine learning has helped to optimize nodes [@Goudos2018a], enhance coverage [@Chafii2018], with predictive approaches helping to extend battery life [@Karg2018a].
  - Coverage in SA?
    - Vodacom, MTN, Cape Town, Stellenbosch, Gauteng
  - Which manufacturers in SA provide the technology for basestations and endpoints?
    - ZTE, Huawei, Ericsson, Nokia
    - Quectel, Ublox, Simcom, Sierra Wireless, Pycom, Nordic





  - What alternatives are there already in SA?
    - Other LPWANs, SigFox, LoRaWAN
  - What problems do SigFox have?
    - Low bandwidth limits number of use cases.
  - SigFox benefits?
    - Long range, reuse cell towers.
  - LoRaWAN cons?
    - FastNet. TTN. Low coverage potential.



  - What advantages over other LPWANs?
    - It is bidirectional. This aids communication to the device and opens up more use cases.
    - Reuses licensed frequency. Unlicensed frequency has the ISM bands, but they are heavily duty cycle limited.
    - Long-range. On a par with SigFox.
  - Neutral?
    - Multi-year battery-life
  - Disadvantages?
    - Being locked down to a central cellular service provider.
    - Coverage rollout is dependent on user demand in the area





  - Why not look at an alternative? No.. every tech has its pros and cons.
    - The bidirectionality of it adds an extra dimension to the project which many unidirectional LPWANs do not have. Although there is no one-size-fits-all in the LPWAN sphere, NB-IoT can come close as it provides long range and covers a larger set of use cases than SigFox and LoRaWAN.
    - If NB-IoT is not good, the current alternatives are SigFox and LoRaWAN, but they each have their own problems.
  - Which LPWANs are more comparable to NB-IoT in terms of being bidirectional?
    - RPMA
  - And what are their barriers to entry in South Africa?
    - Licensed frequency. ICASA
  - 





  - Internet started. Very short. And how is it used today.
  - One way it is used is Mobile broadband
  - Which ones in SA? Vodacom, MTN, Cell C, Telkom, Rain
  - How is it used? Cellphones, dongles, laptops with 4G, mobile routers, vehicle tracking, high bandwidth video applications, social media. Split into high and low bandwidth. Low bandwidth results in IoT via LPWANs and cellular-IoT.
  - Internet of Things is connecting of smart devices to the internet. The idea is that there are many devices that can send or receive data from the internet and have a very long battery life.
  - It's not Technologies use to connect
  - GPRS, LoRaWAN, SigFox, NB-IoT
  - Fracturing in cellular industry among technologies, standards, manufacturers etc

- Research Question

- - Is NB-IoT a viable alternative to GPRS, SigFox and LoRaWAN in South Africa?

- Research/ Problem Statement

- - Increased fracturing in the cellular industry means unsurety when choosing NB-IoT as a technology among the list of LPWANs in South Africa.

- Hypotheses

- - It is a viable alternative
  - It is not a viable alternative

- Research Goals

  - If the technology proves promising, spur cellular ISPs such as Vodacom and MTN to roll out coverage nationally

- Research Aims and Objectives

  - Create a testing framework for the technology for multiple base stations and endpoints

  - Process the tests in a useful form
  - Identify challenges
  - Advantages and Disadvantages
  - There are many LPWANs to choose from, each with their own use cases, pros and cons. This thesis aims to highlight the challenges, advantages and disadvantages of NB-IoT, and find out whether or not it is a viable alternative to the others in South Africa. This will be done by means of performance testing.

- Significance of the Research

- - Useful for companies when making decisions regarding the technology.
  - Useful for researchers w.r.t testing and methods

- Scope or Limitations

- - Internal information of Cellular ISPs should not be revealed unless with explicit permission.

- Assumptions

- - NB-IoT is better than the other technologies

- Definitions of Key Terminology

- - NB-IoT Narrowband Internet of things, LTE-based tech
  - eNodeB - gateway
  - other abbreviations etc
  - endpoints - these are the devices or equipment that the user connects to the internet with

- Brief Chapter Overview

- - Lit review
  - Research Design & Methodology
  - Results
  - Discussion
  - Summary Chapter
  - Final Conclusions and Recommendations for Future Research



## Background to the Research Problem/Question

*Intro to the internet*

ARPANET adopted TCP/IP on January 1, 1983, and from there researchers began to assemble the “network of networks” that became the modern Internet. The online world then took on a more recognizable form in 1990, when computer scientist Tim Berners-Lee invented the World Wide Web. The first South African IP address was granted to Rhodes University in 1988. On 12 November 1991, the first IP connection was made between Rhodes' computing centre and the home of Randy Bush in Portland, Oregon. By November 1991, South African universities were connected through UNINET to the Internet. Commercial Internet access for businesses and private use began in June 1992 with the registration of the first .co.za subdomain.

![Internet users in South Africa showing penetration as a percentage of Internet users in the population](https://en.wikipedia.org/api/rest_v1/page/graph/png/Internet_in_South_Africa/0/475fb57b9d181a463240cc4efd04c5c5159e4fef.png)

In terms of Mobile broadband, we have multiple cellular ISPs. Both Vodacom and MTN Group Limited were founded in 1994, Cell C in 2001 and Telkom Mobile in 2010.

![Cellular ISPs in South Africa](C:\Users\d7rob\AppData\Roaming\Typora\typora-user-images\1552258651312.png)

The most recent entrant is Rain LTE which commercially launched in June 2018.

In terms of M2M connectivity, many options. Of the LPWANs we have FastNet, SquidNet etc. In terms of cellular we have GPRS and in some cases 3G. Both are considered high power. The cellular industry came up with LTE-M, NB-IoT and EC-GSM-IoT.

LTE-M is still considered high power, and due to the high ICASA costs for spectrum, it is not considered in the case of South Africa. NB-IoT is only 200 kHz, so more manageable. EC-GSM-IoT is only in trial stages still, but there is a move to turn off sunsetting GSM technologies and towers, it should be considered to move away from this technology altogether. It is also not gaining as much traction as LTE-NB and LTE-M. This leaves NB-IoT, which both MTN and Vodacom are actively pursuing.

**LTE Cat-M**

MTN considered it but ICASA spectrum costs.

**NB-IoT**

MTN and Vodacom.

**EC-GSM-IoT**

Not in SA.

**SigFox**

SquidNet

**LoRaWAN**

FastNet. TTN

# Literature review

What is NB-IoT?

What advantages does it have?

What disadvantages does it have?

What challenges does it have?

What is the 3GPPs specification for it?

What performance tests have been performed on it, and does it meet 3GPP spec?

- Which metrics? RSSI, MCL etc
- Antennae?
- Polarization?
- 

What tests have cellphone manufacturers done on it?

What do manufacturers say about their devices and base stations? Is there a comparison between them? Has research tested multiple devices?

# Research design and methodology

mini intro

mini lit review

methodology

results

discussion

conclusion

Making use of what is available in South Africa, there are four manufacturers, and going to use four endpoints.

What endpoint tests can I make?

* I can measure the RSSI
  * PDR
  * Connection / disconnection
  * COPS registration time
  * Current usage
  * Ping time

Reuse dev kits. Attach RF attenuator for me only.

# Results

The following tests were taken on the roof outside the HF RF lab on the 5th floor of the Electrical & Electronic Engineering building. The base station it connected to is on the General Building, and is just over 150m away.

![rooftop_maps](C:\GIT\masters\thesis\images\rooftop_maps.JPG)

The tests involve sending a set of 10 pings multiple times at a certain RSSI measurement.

With an antenna and the attenuator set to 0dB, we find most of the values around the mean of 185.2 ms, except for the tail at around 500 ms which is the time of the first ping in a set of 10.

![rooftest1](C:\GIT\masters\thesis\images\rooftest1.png)

Setting the attenuator to the max of 110 dB, we see no change in the ping measurements which have a mean of 185.9 ms. The tail has increased to a max of just over 600 ms.

![rooftest2](C:\GIT\masters\thesis\images\rooftest2.png)

Removing the antenna from the attenuator, we find that the data has a slightly thicker tail, and averages around 207.1 ms.

![rooftest3](C:\GIT\masters\thesis\images\rooftest3.png)

Lastly, having no attenuator nor antenna we still have a connection at -107 dBm.



![rooftest4](C:\GIT\masters\thesis\images\rooftest4.png)

Find the range where dev kit disconnects from tower without antenna.

Initial ping takes longer than the rest?

# Discussion

Paging the base station?

# Summary chapter

# Final conclusions and recommendations for future research

# Glossary

# Appendices

# (Things to keep in mind)

* Whatever your structure, there must be a logical progression of
  thought
* Think with the critic’s cap on – anticipate criticisms and proactively
  protect thesis from them. Also write thesis from reader’s
  perspective

# List of references