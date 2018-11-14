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
autoSectionLabels: true
---

\vspace{10 mm}

> *Dedicated especially to the women who fear the unknown out there in the wild streets.*



# Intro

Thomas Durand has made efforts to evaluate the feasibility of next generation LPWANs to replace GSM in a generic way. This research aims to further that progress in such a way as to test a use case scenario in a more specific way. The outcomes hope to prove the viability of these next-gen communication technologies, especially considering the unique topography of Stellenbosch, and the availability of these technologies at the University creates a great opportunity for the research community to learn more about them.

To be specific, there is IoT coverage available for:

* GSM
* NB-IoT
* SigFox
* LoRa
* Dash7

MTN mostly funds this research, and since they are always looking to expand their borders, they would appreciate this research for future advancement.

The reality is that new technologies may beat what exists currently on the market (in this case, GSM), but there needs to be incentive for large service providers like MTN and Vodacom to roll out these new technologies.

## Cellular IoT

### Jargon explained

* 2G, 3G, 4G, 5G?
* 4G vs 4G LTE vs LTE?
* 2G vs GSM?
* GSM vs EC-GSM-IoT vs eGPRS?
* eGPRS vs GPRS?
* LTE Cat-M vs eMTC vs LTE Cat-NB2 vs LTE Cat-M2?

### 5G

5G is the fifth generation of cellular mobile communications. It succeeds the 4G, 3G and 2G systems. 5G performance targets include high data rate, reduced latency, energy saving, cost reduction, higher system capacity and massive device connectivity. -- Wikipedia

It does include the higher releases of NB-IoT, LTE Cat-M, EC-GSM etc, too.

### NB-IoT {#intro_nbiot}

NB-IoT is an LTE technology with 20dBm more coverage than GSM. The protocol stack has been stripped of most LTE functionality, leaving a simplicity ideal for long battery-life applications.

Vodacom is currently trialing 3GPP release 13 (14 soon) NB-IoT in Gauteng with 1200 Huawei base stations, and apparently 100 Nokia base stations in the Western Cape. Unfortunately, attempts to find a sim card to test in the Western Cape has been unsuccessful.

MTN has been kind enough to set up 3 ZTE base stations in Stellenbosch in partnership with the University, besides the Ericsson field test sites and faraday cage setup they have in Johannesburg.

I have taken it upon myself to do research in a way that incentivizes these large service providers to invest in the infrastructure needed to transition to new technologies.

The other issue is the politics surrounding the whole situation. Internally, the different departments need to reach consensus and have a successful business model where they know they will eventually create a profit. Externally, there is ICASA and the analog television whitespace which uses up most of the RF spectrum. There are plans to transition to digital television. Alas, political change is slow, and subject to law proceedings as well.

### LTE Cat-M / eMTC

LTE Cat-M uses more power than NB-IoT, and has the possibility of VoLTE (Voice over LTE). It is more similar to the LTE we know today in our smartphones, routers and dongles except it uses a much lower bandwidth and half-duplex communications.

MTN would actually like to be the provider of LTE Cat-M coverage in South Africa, but they have connectivity problems with some vendors.

### NB-IoT and LTE Cat-M coverage

The world is undecided whether to implement NB-IoT, LTE Cat-M or both. 

![There are many labs around the world](C:\GIT\masters\thesis\metrics\images\labs.JPG)

There is LTE Cat-M connectivity in Canada and Mexico. Both technologies in the USA, Australia and Turkey. NB-IoT in some countries in Europe, China and South Africa.

![Worldwide coverage deployed or in progress](C:\GIT\masters\thesis\metrics\images\world_coverage.JPG)

As mentioned in @sec:intro_nbiot, there is only working NB-IoT coverage in Gauteng and Stellenbosch in the Western Cape.

### EC-GSM-IoT

This is a form of GSM / 2G based on eGPRS.

## GSM and LTE

There is GSM coverage everywhere in South Africa. At least reaching 99% of people in urban areas. Almost as much LTE, too.

GSM is considered a sunsetting technology, as some countries are turning them off, but it is still a major income source for service providers in South Africa, as there is a large majority of people who have GSM/2G-only cellphones, and use it for SMS and voice calls.

## LPWAN

### SigFox

Sigfox uses an ultra narrowband 100Hz carrier and phase modulation to achieve its great range of up to 50km. The bitrate is incredibly low, at 100bps. Bi-directionality of data is very poor at 4 downlink messages, and 140 uplink messages per day.

![SigFox world coverage](C:\GIT\masters\thesis\metrics\images\sigfox_coverage_world.JPG)



![SigFox coverage in South Africa](C:\GIT\masters\thesis\metrics\images\sigfox_coverage_SA.JPG)

### LoRa / LoRaWAN

TTN coverage in Stellenbosch.

![TTN LoRaWAN coverage in the Western Cape](C:\GIT\masters\thesis\metrics\images\lora_WC_coverage.JPG)

### Dash7

Dash7 can reuse LoRa's PHY RF layer.

Dash7 coverage in medialab via Wizzilab kit, and 2km medium range coverage. Useful for P2P connectivity.

# Scenarios

Since an emergency response wearable is being developed, it has to be compared in different scenarios according to a set of metrics

* Emergency
  * This uses the most power and aims to get a signal out there as fast as possible. Once it acknowledges that the control centre has received its distress signal, it will periodically send it's location as a beacon until a response unit as arrived and taken control of the situation.
* Normal
  * It would beacon it's location at a periodic interval like every 10 minutes.
  * Post-emergency event it would stay in a heightened alert mode until it times out or the control center deems it safe to lower it's alertness.
  * It would continue to monitor physiological signals for any critical conditions.
* What would it be doing in the background?
  * In both cases it would listen for RF traffic, in case the control center or loved one would like to poll the device for it's location
  * It requires some GPS assist data for faster signal acquisition.
* How does it handle good / bad coverage?
  * buildings and indoor
    * homes
    * shopping centres
    * basements
    * inside vehicles
  * outdoor
    * parks and trees
    * mountains
    * streets and pavements
    * long range?

# Metrics

Metrics to test in each scenario.

* SNR (Signal to Noise Ratio)
  * Changes according to indoor, outdoor environments
* PDR (Packet Delivery Ratio)
  * Reliability
  * Time to server
* Range / coverage
  * Overlapping areas?
  * Short, medium, long range field tests
* Battery life
  * Measure battery consumption in each case

# Literature Study

# System Overview

# Field Trials

# Analysis and results

# Conclusion

# Appendix

# References