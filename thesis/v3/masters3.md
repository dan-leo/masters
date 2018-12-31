---
title: Choosing an LTE/LPWAN Wireless Technology for Wearables in South Africa
author: Daniel Robinson
date: Jan 2019
tags: [LTE, wearables, healthcare, safety, critical, life-threatening, SDR, NB-IoT, Dash7, localization]
abstract: |
  There are multiple wireless network contenders each suitable for certain use cases. The following: NB-IoT, GPRS, LoRaWAN, SigFox and Dash7 are investigated. A winner is chosen and a useful proof of concept is designed and developed. The results of this research can be applied broadly to wireless development, as wearable design overlaps with battery-life, range, reliability etcetera which overlaps with other use cases.

toc: true
lof: false
lot: false
link-citations: true
csl: ieee.csl
linkcolor: blue
---

\vspace{10 mm}

> *Dedicated to all who lost their lives when help could have been at hand.*

# Introduction

**This will be the structure of the literature study and design chapters**

What technologies are available, and what do they offer?

- These are the limitations. 
- Based on those limitations, NB-IoT is chosen / justified

Which NB-IoT devices are available?

What devices are readily available, and how do they differ?

> Technologies? Choose a technology. Devices? Choose a device.





What are the typical use cases for wearables, and what are the requirements for wireless applications.

1. Application requirements
   1. Use cases requirements
      1. **It must satisfy battery life, range, reliability and localization.**
      2. **Size is not the focus as it takes business, money, effort.**
2. Available technologies to satisfy those requirements
   1. **There are currently wearables that use bluetooth. Satellite phones. GSM wearables. GPS.**
   2. **In terms of localization, there's satellite, TOF, TDOA, GPS**
   3. **In wireless networking terms there's LTE-M, GSM, NB-IoT, LoRaWAN, SigFox, Dash7, weightless, RPMA**
3. Choose a technology that satisfies the specific requirements. This is how NB-IoT applies to wearables.
   1. **NB-IoT**
   2. **GPS**
   3. **Dash7. It uses stealth and no discovery beacons, so it won't transmit until in a known environment.**
4. Choose a device
   1. **Nordic have the right sized device. It will be used in the next version.**
   2. What challenges are there when working with a specific device
      1. Power levy, quirks, too big
   3. Section to compare. As part of this evaluation of the technology, table to compare the different aspects of technologies that one cares about on vertical axis and properties one wants to explore on horizontal axis. Oxo chart.
      1. Do the same for different devices
         1. Traits, characteristics
         2. Highlight the weak, strong points

A personal challenge is to separate literature aspect into chapter 2 and design into chapter 3. It's about gathering information and making choices, and making logical conclusions about those choices. So the one chapter is background information, and the other is about decision making which is synthesis which is design. Must think about this distinction as I write. When regarding a sentence, ask if it is literature i.e. "did I take the information from somewhere else?" or is it applying information to make a choice. Essentially, "This is the literature, here's my design".

Literature sections:

* application
* technology
* device that one wants. Or put device literature in design chapter.

Design section:

* mirror structure exactly the same
  * design section on application. This may be empty. More about the background info.
  * design section on technology
  * design section on device

Application description in chapter 1.

Wireless technologies in chapter 2, also what other people have done that is similar to what I am trying to do. Related work. Similar stuff evaluating the same type of thing. At least what others have done. Other technology applications for wearables. Concept and broad idea of wearables put in lit study. 

Very broad context and background, very focused related work, very focused study of the literature on the technology, application of this knowledge and this background into a design.

Do before mid January. 

Don't focus too much on market activity. I'm doing research. I'm looking at literature.

The market is conceptually the application of research. Proprietary. 



# Literature Study

There are over 30 IoT platforms available and the number continues to rise. Only a few are capable of device control and real-time analysis. It is seen as the "backbone" in a centralized system [@Hejazi2018a].

Theoretically it is possible to extend terrestrial NB-IoT coverage to world-wide using a constellation of LEO satellites [@Cluzel2018a].

An Early Data Transmission (EDT) mechanism during the random access procedure will improve the device battery life by 3 years and reduces the message latency by up to 3 seconds especially in challenging radio conditions. The values at 164 dB are simulated [@Hoglund2018a]. The Back-off mechanism will increase capacity by 3-6% according to simulations [@Zhao2017]. SC-FDMA with Index Modulation increases energy efficiency by 50% [@Chafii2018b].

There are great cellular-IoT possibilities when dropping 3GPP standards and redesigning the protocol from scratch such that there's up to 260% improvement over NB-IoT and other cellular standards. It's a connectionless protocol that can serve millions with only 10 MHz of bandwidth. When using the control plane data transmission scheme, NB-IoT is able to offer system capacities relatively close to this 5G protocol proposal [@Tavares2017a].

NB-IoT supports mobility only with cell-reselection in idle state. Test-bed and field results provide cell-reselection mobility optimization [@Moon2018a].

Considering coexistence between NB-IoT and LTE, throughput loss shouldn't exceed 5% [@Wang2016a].

NB-IoT is ideal for guaranteed QoS [@Gaddam2018b] such as in air pollution sensors [@Duangsuwan2018b]. What about 2G/GPRS?

Device-to-Device (D2D) communication is specified in NB-IoT. In forest terrain, a range of 2km would be achieved at the 164 dB path-loss limit [@Hejselbaek2018a].

NB-IoT OTDOA has been realized in an RF-SoC with sub-150m accuracy. EC-GSM also seems to be a narrow band cellular IoT standard [@Korb2018a].







> Background on how these technologies work. Basestation side? What do I know? Put into words, questions..

> What's available? How they seem/work? Jeopardy: what is the question that one is answering? Response..

## Application

### typical use cases, requirements

What are the typical use cases for wearables? Location tracking can assist in knowing where employees are at work, and to ensure the safety of lone workers.

In health, wearables can be used to monitor physiological signals in hospitals as well as during day-to-day activities.

### requirements

What are the requirements for wireless applications? Long battery life would be ideal, but the minimum would be daily charging. Wireless wearables range from bluetooth (short range) to satellite (long range).

In terms of localization:

* CSI fingerprinting
* RSSI trilateration
* TOF, AOA

## Technology

What wireless technologies can be used for wearables? An inexhaustible list can be found in the appendix, but the following will be focused on. For licensed frequencies, LTE Cat-M, LTE Cat-NB1 and EC-GSM, and for unlicensed frequencies LoRa, SigFox and Dash7.

**Cellular IoT**

EC-GSM aims to improve on the battery life limitations of 2G/GPRS. Lower power form of GSM, with extended coverage. Unfortunately 2G is in the process of being turned off in countries around the world.

eMTC or LTE Cat-M is a high-powered form of IoT communications which includes VoLTE. Designed to replace mainstream 2G/GPRS.

NB-IoT or LTE Cat-NB is the 3GPP's response to emerging unlicensed LPWANs. According to Ryan vd Bergh (April 2018) it should achieve mainstream adoption within 2 years time in South Africa. It is simpler than eMTC, and doesn't include VoLTE.

**LPWANs**

SigFox uses an ultra-narrow band using a phase modulation over carrier. This way it is highly immune to noise. Since it has such low bandwidth and data rate, it takes about two seconds to transmit a 12 byte payload. The duty cycle limitations mean one can only transmit 140 messages per day.

- Good range, but unreliable after 6kmph

Despite it's promising characteristics, LoRaWAN is seemingly a failure

- No listen-before-talk, 20% success rate
- SF12 means one cannot send data frequently, but that's where one gets ones range.
- No P2P
- Simple, incomplete networking stack

Dash7 seems to address most of it's issues.

- B.U.R.S.T.Y data
- Bidirectional, broadcasting
- P2P

## Device

*These are the devices out there and this is what they offer.*

* Quectel
* Ublox
* Sierra Wireless
* Nordic Semi
* Telit
* SimCom

# Design

## Application

Starts off as a box. Refined and revised until discrete -- goal.

## Technology

PCB prototype using multiple technologies. NB-IoT, GSM, LoRa, SigFox and Dash7. The prototype facilitates concurrent testing of multiple RATs (radio access technologies).

## Device

Multiple technologies were simplified to require only two radio modems.

* Quectel BG96
  * NB-IoT, GSM, (LTE Cat-M), GNSS/GPS
* Murata CMWX1ZZAB-078
  * LoRa, SigFox, Dash7

Quite a bit of effort was spent on the design of this PCB. It is highly configurable, and the goal is to test the different technologies near simultaneously to prove that NB-IoT and Dash7 are of the best.

Different metrics will be used, such as SNR, range, packet delivery ratio etc.

It will also require a cloud platform to gather the data via MQTT or similar lightweight protocols. Thingsboard provides a great framework, as long as it is reliable.

For processing, one can use Python - Jupyter.

# Field trials

*Matching requirements with specifications.*

Field trials can be performed mainly in Stellenbosch, since there is SigFox, LoRaWAN, GSM, and NB-IoT (MTN), coverage. Dash7 is a more local setup which can be done anywhere.

Vodacom has NB-IoT coverage in Cape Town at the CTICC and inside an office at its HQ in Century City.

# Conclusion

The end.

# References

