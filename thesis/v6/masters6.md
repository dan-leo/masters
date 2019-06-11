---
title: 3GPP Narrowband LTE evaluation for IoT in South Africa
author: Daniel Robinson
date: Stellenbosch University, March 2019
tags: [LTE, NB-IoT]
abstract: |
  2G/GPRS is a sun-setting technology leaving behind a void for LPWANs such as LoRaWAN and SigFox to fill. The viability of NB-IoT being such a technology for South Africa is investigated. Multiple endpoint manufacturers and base station vendors are tested to compare capabilities with respect to cost, time, power consumption and signal strength. The results proved promising.

toc: true
lot: true
lof: true
link-citations: true
csl: ieee.csl
linkcolor: blue
---

# List of Abbreviations

**3GPP** Third Generation Partnership Project

**2G, 3G, 4G, 5G** 2nd, 3rd, 4th and 5th Generation

**NB-IoT** Narrow-Band Internet of Things

**SMS** Short Message Service

**Voip** Voice over Internet Protocol

**IMS** IP Multimedia Subsystem

**LPWAN** Low Powered Wide Area Network

# Introduction

In recent years, 3GPP have developed new LPWANs for the cellular industry on the roadmap towards 5G, namely LTE Cat-M, EC-GSM-IoT and NB-IoT to supersede the sun-setting 2G/GPRS networks. GSM was first deployed in 1991 and offered calls and SMS as circuit switched data. In 2000, 2G/GPRS added internet at speeds comparable to dialup as packet switched data. Circuit switched data is ideal for real-time connections and means that links have bandwidth pre-allocated. This also increases the QoS guarantee of information transferred timeously. Packet switched data is connectionless on the other hand, with higher bandwidths possible in shared channels. GSM had been a cost-effective way to keep in touch with people around world, as well as the poorer communities in Africa. Due to the proliferation of WhatsApp, Facebook, Telegram and other social media platforms, there is a shift away from calls and sms. 

![sms_usage](../notebooks/sms_usage.png)

<!---Facebook, penetration
Africa
World Bank-->

Due to high user demand in bandwidth-hungry applications such as voice, video and file sharing, it evolved into 3G and 4G LTE which is currently in use today in the form of VoIP and IMS. Since the more affordable packet switched networks can handle more bandwidth than circuit switched networks, the transition is sensible.

![ims voip](C:\GIT\masters\thesis\images\ims voip.jpg)

That left 2G/GPRS to serve as a gateway for smart devices and sensors in the M2M sphere, but due to its high-powered nature it is not sustainable for applications which require battery longevity of up to 10 years or more. 3GPP developed dedicated LPWAN technologies to serve this purpose. In lieu of its absence, although the spectrum it held can be re-farmed for cellular LPWANs, it also opens up opportunities for market entrants of unlicensed frequencies such as LoRaWAN and SigFox. Each LPWAN technology has its own unique flaws and benefits and there is yet to be a clear winner when it comes to connecting 'things' to the internet. In South Africa, there is a push by at least two major cellular service providers to adopt a cellular LPWAN to fill the void left behind by 2G/GPRS now and in the future. NB-IoT is being investigated by MTN South Africa, and since they are also funding this research, have also provided network coverage for testing to Stellenbosch University. Ideally, the technology can be rolled out to existing base stations as a software upgrade for national coverage, but it is limited by factors such as use case demand, expensive licensing and general uncertainty about the technology. This thesis aims to highlight the challenges, advantages and disadvantages of the technology. By doing endpoint tests with multiple manufacturers and base station vendors, one can paint an accurate picture of the capabilities of the technology. The technology is robust in certain test cases and scenarios, but additional work is required from the 3GPP to enhance the technology.

<!---*According to the World Bank, there is approximately 1 cellular subscription for every person around the world. The number of cellular subscriptions range from 75% of the population in Sub-Saharan Africa to 125% in Europe and Central Asia which indicates that certain technologies, standards and protocols causes contention. One of them is NB-IoT, which is an LTE-based wireless technology which takes on the likes of LoRaWAN and SigFox.*-->

<!---Who is my target audience? Researchers, IoT enthusiasts. Myself.*-->

https://www.flickswitch.co.za/nb-iot-rollout-in-south-africa/

> NB-IoT technology is designed such that it can be used in areas beyond the radio coverage of current cellular standards and in devices which must run from battery power for many years. The devices will generally send small amounts of data infrequently; a typical usage scenario might be 100 to 200 bytes sent twice per day for battery powered devices. For mains powered devices the limit is not based on battery size, but cost and network bandwidth/resources.

> The system operation is analogous to SMS in that it is a datagram-oriented, stored-and-forward system, rather than a GPRS-like IP pipe. This is because NB-IoT devices spend most of their time asleep, making possible the required long battery life. The system implements extended DRX cycles for paging, but as this window will be limited to save battery life, the delivery of downlink messages occurs mainly when the system detects that uplink messages have been received from a device (indicating that it is awake). Here a store-and-forward system, an “IoT Platform”, is useful. [@ubloxAppNote2018]

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
  - How does NB-IoT perform?

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

## Key terminology

Channel coding

Rate Matching

Interleaving

The **PCI** value is created from two components - PSS and SSS. The PSS, Primary Synchronization Signal, has the value 0, 1, or 2. The SSS, Secondary Synchronization Signal, can have a value between 0 and 167.

The suppliers of UE will be referred to as manufacturers and of base-stations (BSS) as vendors.

NAS.

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

## framework

- ‘Paints a picture’ of what is currently known about the research question and what has been written on it by experts and scholars.

-  Is an in-depth analysis of the literature:

- - Critique, contrast, find authors who agree with each other and those who disagree and interrogate why this is so
  - Looks for weaknesses in study design, reported results, arguments, models and theoretical frameworks

- Familiarity with authors who have published extensively and/ or are subject matter experts

- Minimum use of direct quotations

- Majority of sources should be peer-reviewed journal articles

- Need to show how thinking has evolved, peaks and troughs in publications in your field over time, the history of your field

- Can also bring in other sources of literature, e.g. chapters in books, textbooks, cases, Internet sources, newspaper articles, government publications and legislation, business documentation, CDs and DVDs, radio and television broadcasts, blogs, emails, personal correspondence, theses – as long as: 

- These are relevant to your research question (the anchor)

- Need to reference correctly, as you write, otherwise you will have missing references and formatting mistakes

- Do a comprehensive literature search – make use of databases (e.g. ScienceDirect, Emerald, Heinonline, Sabinet, EBSCOhost, Pubmed, Google, Google Scholar) 

- May need to make use of Inter-Library Loans

- In writing your literature review, only include the literature that is relevant to understanding or answering your research question

- You need to read full-text articles; cannot write a literature review based on abstracts

- Read widely around your topic (so you can show linkages to other fields) and in-depth into specifics of your topic – so the lit review moves in 2 directions. Start writing a rough draft; write down the main points and find authors who agree and disagree. Divide your research question into themes (skeleton structure from before)

- Your literature review is built around your research question

- Have a short Introduction section at the beginning of the chapter (saying what will be covered in the chapter) and a short Conclusions section at the end (wrapping up the chapter and linking to the next one) – do this for other chapters too

- Need a proper filing system for sources (e.g. Mendeley)

- Examiners look at the quality of your literature review – this can make or break your thesis!

## painted picture

### how does NB-IoT work?

In the uplink, there are two physical layer channels. The random access channel connects to the base station and the uplink channel contains the data and control information. In downlink there are four channels. Synchronization is used by the endpoint to estimate symbol timing and carrier frequency and obtain the cell identity and frame boundary. The broadcast channel contains the master information block (MIB). The control channel carries downlink control information and can be repeated 2048 times, as well as the data channel which contains the payload, paging, system information and the random access response. [@Adhikary2016].

NB-IoT operation requires a minimum bandwidth of 180 kHz, which is equal to the size of the smallest LTE Physical Resource Block (PRB). Depending on the availability of spec- trum, NB-IoT can be either deployed on its own (“standalone operation”), in the guard carriers of existing LTE/UMTS spectrum (“guardband operation”) or within an existing LTE carrier by replacing one or more PRBs (“inband operation”). In order to support such flexible deployment scenarios, NB- IoT reuses the LTE design extensively, such as the OFDM (Or- thogonal Frequency Division Multiplexing) type of modulation in downlink, SC-FDMA (Single Carrier Frequency Division Multiple Access) in uplink, channel coding, rate matching and interleaving. In addition, a host of new features are added to ensure the demands of IoT based applications. Key design changes from LTE include the synchronization sequences, the random access preamble, the broadcast channel and the control channel. These changes are primarily motivated by the fact that NB-IoT is required to operate on a minimum bandwidth of 180 kHz (1 PRB), whereas many channels in LTE were designed to span multiple PRBs occupying greater bandwidth compared to 180 kHz. These design changes achieve the IoT requirements while ensuring best co-existence performance with the existing LTE system [@Adhikary2016].



### basestations?

When only a fraction of the existing LTE cell sites support NB-IoT, devices cannot attach to the best cell if that cell does not support NB-IoT. As a result, the path loss can be very high. In addition, they also suffer from high interference from non-NB-IoT cells [@Mangalvedhe2016a].

## evaluations

**List**

* periodic link reporting
  * energy consumption
  * delay performance
* 

## cellular connections

According to the [World Bank in 2016](https://www.google.com/publicdata/explore?ds=d5bncppjof8f9_&ctype=l&strail=false&bcs=d&nselm=h&met_y=it_cel_sets_p2&scale_y=lin&ind_y=false&rdim=region&idim=region:SSF:MEA:ECS:EAS:LCN:NAC:SAS&ifdim=region&tdim=true&ind=false&icfg&iconSize=0.5), mobile cellular subscriptions around the world started growing in the early 90s until approximately 100 subscriptions per 100 people at that time. Europe & Central Asia leads with 125 and Sub-Saharan Africa follows with 72 subscriptions per 100.

## basestation stats

![basestation stats](https://infographic.statista.com/normal/chartoftheday_17097_voip_worldwide_revenue_n.jpg)



Huawei, the Chinese telecommunications company, has cornered about a quarter of global revenue from VoIP and IMS equipment, according to estimates from IHS Markit. Ericsson, the Swedish telecommunications company, holds about 21 percent of the VoIP and IMS global revenue, followed by Nokia and ZTE. 

Voice over Internet Protocol (VoIP) allows users to make voice calls using broadband internet connection instead of a standard phone line. Overall the VoIP revenue dropped by 12 percent year over year between 2017 and 2018. The dip is fueled by the sluggish voice over LTE (VoLTE) network advancements and flatlined spending. VoLTE was the main driver of VoIP and IMS growth, so roadblocks for the broadband network stymie VoIP market expansion.

### Adhikary

In terms of coverage performance, Adhikary [@Adhikary2016] takes into account the doppler spread which denotes the speed of the endpoint, but does not take into account inter-cell interference. Endpoints typically transmit at 23 dBm in an urban environment, with base stations transmitting at 43 or 46 dBm.

|   Numerology   |   15 kHz   |   3.75 kHz   |
| ---- | ---- | ---- |
|   (1) Transmit power (dBm)   |   23.0   |   23.0   |
|   (2) Thermal noise density (dBm/Hz)   |   -174   |   -174   |
|   (3) Receiver noise figure (dB)   |   3   |   3   |
|(4) Occupied channel bandwidth (Hz)| 15000| 3750|
|(5) Effective noise power = (2) + (3) + 10*log ((4)) (dBm)| -129.2 |-135.3|
|(6) Required SINR (dB) | -11.8 | -5.7|
|(7) Receiver sensitivity = (5) + (6) (dBm) | -141.0 | -141.0|
|(8) Max coupling loss = (1) - (7) (dB) | 164.0 | 164.0|

### Bello

Bello [@Bello2018a] evaluates PSM.

periodic link reporting

- energy consumption
- delay performance

### Yeoh

Experimental assessment of battery lifetime for commercial off-the-shelf NB-IoT module [@Yeoh2018d]

### Lauridsen

An Empirical NB-IoT Power Consumption Model for Battery Lifetime Estimation [@Lauridsen2018]

### Feltrin

NB-IoT: Performance Estimation and Optimal Configuration [@Feltrin2018].

System model.

### Thomas

[@Thomas2018] Evaluation of next-generation low-power communication technologies to replace GSM in IoT-applications

### Kasbah

[@Kasbah2005] GSM RF equipment testing and performance analysis

## in-depth

![nb-iot current profile](https://www.mathworks.com/content/dam/mathworks/videos/n/nb-iot-functionality-in-lte-toolbox.mp4/jcr:content/renditions/nb-iot-functionality-in-lte-toolbox-thumbnnail.jpg)

## 3GPP

https://www.3gpp.org/technologies/keywords-acronyms/96-nas

![JPEG - 33.6Â kb](http://www.3gpp.org/local/cache-vignettes/L400xH152/eps-control-plane-for-e-utran-2-0586e.jpg)

<!---TR 36.888
foil-backed insulation
metalized windows
concrete thick-walled buildings
UL regular reporting traffic characteristics for low-cost MTC-->

| Use cases            | UL interval                            | Packet (bits)        | Mobility                                                     |
| -------------------- | -------------------------------------- | -------------------- | ------------------------------------------------------------ |
| **No mobility**      | 1min (optional)   5min, 30min,   1hour | 1000, optional 10000 | Static,   Pedestrian (optional, no seamless   handover requirement) |
| **Limited mobility** | 5s (optional)   10s,30s                | 1000                 | Vehicular (no seamless   handover requirement)               |



**Power class**

Table 6.2.2F-1: UE Power Class from 3GPP TS 36.101 defines the mean power of output power measurement.

| EUTRA band | Class 3 (dBm) | Tolerance (dB) | Class 5 (dBm) | Tolerance (dB) | Class 6 (dBm) | Tolerance (dB) |
| ---------- | ------------- | -------------- | ------------- | -------------- | ------------- | -------------- |
| 8          | 23            | ±2             | 20            | ±2             | 14            | ±2.5           |



## mtn



**Cellular IoT Trials FIRST INFO pA1.pptx**

Shielded box

CCN - Air interface simulator for handovers

**NB-iOT system Architecture.pdf**

Really useful stuff. MCL

**Examining the real differences.docx**

idle mode reselection

Both CAT-M1 and NB-IoT are being pursued aggressively to become the de-facto connectivity solution for IoT products. While both standards fare well in different scenarios, it is critical not to take market perceptions at face value but rather compare both solutions evenly, all things being equal, in order to make the right technology decisions.

We analysed three key KPIs including coverage, cost and power consumption. While the market perception is that NB-IoT has a clear advantage over CAT-M1 for these KPIs, we conclude that CAT-M1 actually offers advantages for coverage and power, and only a minimal cost disadvantage when compared to NB-IoT.

Future platforms that support both CAT-M1 and NB-IoT may ultimately allow providers to hedge their bets, but until then it is crucial to understand the technical data and consider the real added-value before choosing.

**MTN SA ENM-NBIOT PROJECT HIGH LEVEL TIMEPLAN V0.1.pptx**

Ericsson's NB-IoT integration time is 20 weeks. Four phases.

NB-IoT 20 weeks

URAN 10 weeks

WRAN 20 weeks

GRAN 18 weeks

**MTN SA EPC NB-IoT Introduction Statement of Work.docx**

The Internet of Things (IoT) is quickly becoming a reality and its impact on both industry and society is going to be profound. Ericsson forecasts that the number of IoT connected devices globally
will surpass mobile phones in 2018. 

MTN South Africa can be viewed as an early supporter of the standards that are now part of 3GPP Release 13. MTN South Africa would like to fast track their NBiOT deployment, with a C-level commitment to be ready for commercial services no later than September 2017. MTN currently has 3 RAN vendors, each responsible for enabling NBiOT in their respective regions.

MTN has indicated that the core architecture will comprise of a ‘roaming’ type scenario interconnecting via pre-existing IoT infrastructure supplied by ZTE.

Statement of work and responsibility matrix.

**MTN SA EPC NBIoT Solution Design and Impact Analysis.pdf**

**MTN SA EPC NBIoT Solution Design and Impact Analysis ver 2.pdf**

**MTN SA EPC NBIoT Solution Design and Impact Analysis.docx**

The objective of this document is to describe the architecture, features and impact
that NBiOT introduction will cause to the MTN network and beyond – this
document should enable a service integrator to be able to configure the Core
network for NBiOT. The plan was to prove the concept in MTN’s test EPC
environment by reusing the existing EPC network and activating, configuring, and
testing IoT functions in the SGSN-MME, EPG and DNS servers. However the
idea now is to go directly to the end to end verification and consult with MTN on
various NBiOT issues from a core perspective.

eDRX

PSM

Ericsson, Huawei and ZTE node elements

Besides the optimizations that fall on the generic IoT capabilities such as low UE
complexity and power saving – there are NBiOT functions and features that have
major impact on the SGSN-MME.

**MTNSA NB-IoT Trials - Ericsson's Industria North Drive Test - Results 2017-08-28.pdf**

Three tests in

* idle mode
* 60s call 10s idle sequence
* continuous call

BCCH plot

RxLevFull

RxLevSub DRX

RxQualFull

RxQualSub

Call failed locations

Handover failed locations

**MTNSA NB-IoT Trials - S1 Traffic Split Test Report.pdf**

MTN’s proposed solution for the NB-IoT field trials is to use live eNodeBs
connected simultaneously to MTN’s test plant MME for NB-IoT testing, and to
the Randburg MME, a live MME, for carrying legacy LTE traffic from the same
eNodeBs. The proposed setup will keep the live traffic undisturbed on the live
core while directing all NB-IoT traffic to the test plant core which has already
been set up and tested for NB-IoT. This allows for traces and other verifications
to be carried out on the NB-IoT core (test plant) without any interference to the
live traffic.
To achieve this, a cell TAC split will be done on the eNodeB by defining one
Tracking Area that will only allow legacy LTE traffic, which will be advertised to
the Live MME, and a second Tracking Area that will only allow NB-IoT traffic,
which will be advertised to the test plant MME.

Successful.

**N07789_NBIoT_RAN_LLD_Parameter_Set.xlsx**

**N09021_NBIoT_RAN_LLD_Parameter_Set.xlsx**

**N14701_NBIoT_RAN_LLD_Parameter_Set.xlsx**



* attachWithoutPDNConnectivityList false
* ceLevelNumber 1
* cmcIndex 0
  * Cell
    Maximum Coverage (CMC). Index 0 represents low coverage
    with few required repetitions to reach UEs on cell edge. Index 2
    represents deep coverage.
* coverageEnhancementLevel 0
* eDrxAllowed true
* mappinginfonb
  * 1, 2, 4 not mapped
  * 3, 5 mapped to SI message 1
* nbIotCellType 3
  * standalone
* pMax 1000
  * Limits UE uplink transmission power in the serving cell and calculates the parameter Pcompensation for cell selection.
* pZeroNominalNPusch -103
* qRxLevMin -140
  * The required minimum received Reference Symbol Received Power (RSRP) level in the E-UTRA frequency for cell reselection. Can recommend in field trial
* sInterSearchThreshold 0
  * Cell Reselection Threshold (inter-frequency measurements).
* sIntraSearchThreshold 60
  * Cell Reselection Threshold (intra-frequency measurements).
* siPeriodicity 512
* siPeriodicity 4
* siWindowLength 160

**NBIoT and CATM_1.pptx**

››› Amount of radio resources allowed for use by NB-IoT users upper limited in MI17A

–Maximum one NB-IoT cell (1 PRBs) for transmission of NPDCCH and NPDSCH

–Maximum one NB-IoT cell (1 PRBs) for transmission of NPUSCH

–Assumed to be enough for low load of connected NB-IoT users

››› Amount of radio resources allowed for use by Cat-M1 users upper limited in MI17A

–Maximum one narrowband (6 PRBs) for transmission of MPDCCH and PDSCH

–Maximum one narrowband (6 PRBs) for transmission of PUSCH

–Assumed to be enough for low load of connected Cat-M1 users

››› New BB5216 digital unit will also support mixed mode between GSM and LTE/NB-IoT

–Processing resources are not pooled between GSM and LTE/NB-IoT

EC-GSM-IoT

**NB-IoT Spectrum Strategy.pptx**

Refarm 2 GSM channels to make 400 kHz. 100 kHz guard band.

**NBiOT_CELL_INFORMATION_Field_Trial_MTN_SA.xlsx**

* Azimuth
  * 0, 120, 240
* Sector 1, 2, 3
* height
* mech tilt
* elec tilt

naming convention

**NBIoT_RAN_LLD_Parameter_Set.xlsx**

**NBIoT_RAN_LLD_Parameter_Set Rev 2.0.xlsx**

paging

RRC

**NBIoT_Test Cases.xlsx**

Cell selection on powerup. Verify NB-IoT Cell Selection while Power Up.

S-GW Network name and time to UE

Attach Initiated by a UE Using IMSI.

Attach Initiated by a NB-IoT UE Using IMEI.

Network Initiated PDP Deactivation: Verify NB-IoT UE can process PDP Context Deactivation procedure initiated by network.

Detach Initiated by a NB-IoT UE.

PDP Context Deactivation Initiated by a NB-IoT UE.

Capabilities: Verify UE capabilities.

Security: Verify integrity and ciphering.

Pass/Fail Criteria Verify ping response on NB IoT UE

![ericsson_ping](C:\GIT\masters\thesis\images\ericsson_ping.png)

PDP Context Activation without APN Initiated by a NB-IoT UE

Boosting, deboosting.

Verify the +9 dB Power Boost for NRS delivered with NB-IOT.

![iperf](C:\GIT\masters\thesis\images\iperf.png)



iperf











# Research design and methodology

## framework

* mini intro
  * 64 tests. 4x4x4. cost, time, power consumption, signal strength. 4 BSS. 4 UE.
* mini lit review
  * 
* methodology
  * 
* results
* discussion
* conclusion

Making use of what is available in South Africa, there are four manufacturers, and going to use four endpoints.

The documentation describes that the trace function in m-center is used to collect logs for u-blox internal technical team to analyze.

https://github.com/fgsect/scat

https://github.com/openpst/libopenpst

Most oscilloscopes cannot do seamless data logging.

At what range does class 0 require 23 dBm?

What endpoint tests can I make?

* I can measure the RSSI
  * PDR
  * Connection / disconnection
  * COPS registration time
  * Current usage
  * Ping time

Reuse dev kits. Attach RF attenuator for me only.

What tests can be performed among multiple manufacturers?

The most generic test which also takes into account

| Description                    | Current usage | Completion time |
| ------------------------------ | ------------- | --------------- |
| Manual network registration    | Yes           | Yes             |
| Automatic network registration | Yes           | Yes             |
| Search for network operators   | Yes           | Yes             |
| Minimum functionality.         | Yes           | No              |
| Full functionality             | Yes           | No              |
| Network time                   | No            | No              |
| Reboot                         | Yes           | Yes             |
| RSRP                           | Yes           | No              |
| RSSI                           | Yes           | No              |
| Transmit power                 | Yes           | No              |
| Transmit time                  | Yes           | Yes             |
| Receive time                   | Yes           | Yes             |
| Cell id                        | No            | No              |
| Extended Coverage Level        | Yes           | No              |
| SNR                            | Yes           | No              |
| EARFCN                         | No            | No              |
| PCI                            | No            | No              |
| RSRQ                           | Yes           | No              |
| Cell tower info                | No            | No              |

Table showing Ublox tests

| **ZTE**      | Ublox | Quectel | Nordic | SimCom |
| ------------ | ----- | ------- | ------ | ------ |
| Cost         | 1     | 2       | 3      | 3      |
| Current      | 1     | 2       | 3      | 3      |
| Time         | 1     | 2       | 3      | 3      |
| RSSI         | 1     | 2       | 3      | 3      |

| **Nokia**    | Ublox | Quectel | Nordic | SimCom |
| ------------ | ----- | ------- | ------ | ------ |
| Cost         | 2     | 2       | 3      | 3      |
| Current      | 2     | 2       | 3      | 3      |
| Time         | 2     | 2       | 3      | 3      |
| RSSI         | 2     | 2       | 3      | 3      |

| **Ericsson** | Ublox | Quectel | Nordic | SimCom |
| ------------ | ----- | ------- | ------ | ------ |
| Cost         | 4     | 4       | 4      | 4      |
| Current      | 4     | 4       | 4      | 4      |
| Time         | 4     | 4       | 4      | 4      |
| RSSI         | 4     | 4       | 4      | 4      |

| **Huawei**   | Ublox | Quectel | Nordic | SimCom |
| ------------ | ----- | ------- | ------ | ------ |
| Cost         | 4     | 4       | 4      | 4      |
| Current      | 4     | 4       | 4      | 4      |
| Time         | 4     | 4       | 4      | 4      |
| RSSI         | 4     | 4       | 4      | 4      |

| **Key** |               |
| ------- | ------------- |
| White   | Not attempted |
| Orange  | In progress   |
| Green   | Complete      |
| Red     | Not possible  |
| Grey    | Uncertain     |

## UE Monitor

!UICC && !Unknown && !LL1 && !RRC && !IND && !NAS && !REQ && !REPORT && !RLC && !MAC && !CNF && !Serving

## which tests?

There are many questions asked when it comes to the use of a wireless technology. Since there are multiple manufacturers one can expect differences in performance. When choosing a module in scalable projects, one typically looks for a balance between high performance and low cost. In high performance one expects quality, reliability, and long battery life. It must be able to connect seamlessly and from expected range. Besides the cost of the modem one also expects a low external parts count, minimal data overhead and longevity of device lifetime.

This thesis will focus on four main themes, namely cost, time, power consumption and signal strength. 

## why cost?

Cost is important to take into consideration for capital and operating expenses. Upfront costs include the modem, external parts and integration. Operating costs include the data payloads and data overhead which developers may not take into consideration. On the RRC layer, there is signaling between the UE and BSS, but only on the NAS and IP layer is data charged.

What is the effect of packet size variations on the cost of the service? And on battery life?

## which endpoint manufacturers?

The following list of manufacturers have a number of modules, SoCs and chipsets which support NB-IoT according to [@Evolution2017] and manufacturer websites.

| Manufactuer           | NB-IoT supported devices |
| --------------------- | ------------------------ |
| Quectel               | 5                        |
| Telit                 | 2                        |
| u-blox                | 6                        |
| ZTE                   | 1                        |
| Nordic                | 1                        |
| Sierra   Wireless     | 2                        |
| PyCom                 | 2                        |
| SimComm               | 1                        |
| SkyWorks              | 6                        |
| Altair Semiconductors | 1                        |
| CommSolid             | 1                        |
| Intel                 | 2                        |
| MediaTek              | 1                        |
| Neul                  | 1                        |
| Qualcomm              | 2                        |
| Sequans               | 2                        |

The following list of manufacturers have been tested to see if they are supported according to Vodacom, MTN and RF Design:.

| Manufacturers  |
| -------------- |
| Quectel        |
| u-blox         |
| Nordic         |
| SimComm        |
| Telit          |
| SierraWireless |

Since the goal of the research is to evaluate NB-IoT, a number of devices will be tested and the resulting differences investigated. Due to availability and cost limitations, the following four are chosen.



| Manufacturers |
| ------------- |
| Quectel       |
| u-blox        |
| Nordic        |
| SimComm       |

## why time?

With the UE at a certain range from the BSS, NB-IoT uses increased RACH repetitions to maintain connection. For the majority of use cases a packet makes a round trip within 130 - 250ms, but at the edge of coverage it increases drastically up to 10 seconds. This can be detrimental to battery life, especially when considering how SigFox takes roughly 6 seconds to transmit a message.

What is the effect of high / low SNR on COPS registration?

## why power consumption?

Power consumption and profiling is important to note amongst various manufacturers.

## why signal strength?

Probably one of the most useful tests is a drive by test in a generic town which has one or more base stations. The different decades of signal strength from -50 dBm to -113 dBm can be shaded on a colour-key. Points of disconnection can be analyzed, discussed and suggestions can be made.

There are two kinds, an idle mode test and a constant iperf connection test.

Lastly, an RF attenuator will be used to see the effect of changing the signal strength in a controlled manner such that the effect on time, packet size and power consumption can be consistently measured, especially considering the base station is in control of the UE.

## measuring T3324, T3412 timers

The following code converts binary strings to actual time. It is based off Table 10.5.5.32/3GPP in TS 24.008.

```python
## T3412
def extended_periodic_TAU(bin_str):
    mul = {}
    mul['000'] = [10, 'minutes']
    mul['001'] = [1, 'hours']
    mul['010'] = [10, 'hours']
    mul['011'] = [2, 'seconds']
    mul['100'] = [30, 'seconds']
    mul['101'] = [1, 'minutes']
    mul['110'] = [320, 'hours']
    mul['111'] = [0, 'deactivated']

    if bin_str[:3] in mul:
        t = mul[bin_str[:3]]
        return str(t[0] * int(bin_str[3:], base=2)) + ' ' + t[1]
    return 'failed'

## T3324
def active_time(bin_str):
    mul = {}
    mul['000'] = [2, 'seconds']
    mul['001'] = [1, 'minutes']
    mul['010'] = [1, 'deci-hours']
    mul['111'] = [0, 'deactivated']

    if bin_str[:3] in mul:
        t = mul[bin_str[:3]]
        return str(t[0] * int(bin_str[3:], base=2)) + ' ' + t[1]
    return 'failed'

def p(i):
    return extended_periodic_TAU(i)

def a(i):
    return active_time(i)

def cereg(at_str):
    arr = at_str.split(',')
    print(at_str)
    return 'Active T3324: ' + a(arr[7].split('"')[1]) \
     + ', Periodic T3412: ' + p(arr[8].split('"')[1])
```



\newpage

# Results

## Power Profiling

### Ublox + ZTE

The following tests measure current for a Ublox SARA N200 connected to a ZTE base station.

![Block diagram of current consumption setup for SARA-N2](C:\Users\d7rob\AppData\Roaming\Typora\typora-user-images\1555535660456.png)

The digital multimeter in the figure is replaced with a ZXCT1008 high-side current monitor in series with the modem. 

![ZXCT1008  high-side current monitor https://www.diodes.com/assets/Datasheets/ZXCT1008.pdf](http://cxem.net/arduino/images/arduino86-1.png)

Rs is set to a 1 ohm resistor and Rg is set as a 1k ohm resistor such that 100mA supplied to the modem makes 1V.

$V_{out} = I_{load} [mA] * 10 [\frac{V}{mA}]​$

![zxct1008](C:\GIT\masters\thesis\images\zxct1008.jpeg)

An initial test was performed with AT+COPS=0 network registration until T3412 timeout of 270 seconds.

![active_time](C:\GIT\masters\thesis\images\active_time.JPG)

Peak current is approximately 70mA.



![activetime](C:\GIT\masters\thesis\images\activetime.jpg)

Extended Discontinuous Reception (eDRX) mode means that paging windows can be scheduled such that the modem can be contacted by the server.

![eDRX mode](C:\Users\d7rob\AppData\Roaming\Typora\typora-user-images\1555540836196.png)

With a paging time window interval of 2.54s and 4 hyper-frames making up 40.96s, the following output is obtained.

```c
AT+NPTWEDRXS=2,5,"0001","0011"
+CEREG: 5,1,"8CA7","28C464",7,,,"00011000","00101010"
```

AT+CEREG says that the T3324 active time is 48 seconds, or 2 seconds * 24 binary coded timer value. This is not the expected outcome, even according to Table 10.5.5.32/3GPP
TS 24.008: Extended DRX parameters information as referenced in Ublox documentation, which expects 40.96s. Besides, the paging time interval is also not working as expected.

![eDRX](C:\Users\d7rob\AppData\Roaming\Typora\typora-user-images\1555567465123.png)

![eDRX](C:\Users\d7rob\AppData\Roaming\Typora\typora-user-images\1555570254042.png)

The T3324 active timer value is modified to 5.12s.

```c
AT+NPTWEDRXS=2,5,"0001","0000"
```

AT+CEREG says that the timer is 32s, or 2 seconds * 16 binary coded timer value.

```c
+CEREG: 5,1,"8CA7","28C465",7,,,"00010000","00101010"
```

In the debug logs we see the timer expires after exactly 30 seconds.

```c
1400,00:07.952393,NAS_DBG_TIMER
	action=TIMER_START
	prim_id=USIM_STATUS_TIMER_EXPIRY
	duration=30
2092,00:37.952728,USIM_STATUS_TIMER_EXPIRY
	timer_handle=16871576
```



![eDRX](C:\Users\d7rob\AppData\Roaming\Typora\typora-user-images\1555568148322.png)

![eDRX](C:\Users\d7rob\AppData\Roaming\Typora\typora-user-images\1555569320664.png)

Increasing the T3324 active timer value to 10.24s, the following results are obtained. It is exactly the same as before.

```c
AT+NPTWEDRXS=2,5,"0001","0001"
```

AT+CEREG says that the timer is 32s, or 2 seconds * 16 binary coded timer value.

```c
+CEREG: 5,1,"8CA7","28C465",7,,,"00010000","00101010"
```

In the debug logs we see the timer expires after exactly 32 seconds.

```c
2409,+00:00.400757,NAS_DBG_TIMER
	action=TIMER_START
	prim_id=USIM_STATUS_TIMER_EXPIRY
	duration=30
5981,+00:33.283905,USIM_STATUS_TIMER_EXPIRY
	timer_handle=16871576
```

![eDRX](C:\Users\d7rob\AppData\Roaming\Typora\typora-user-images\1555569718434.png)

(These tests should continue until an eDRX value of 2621,44s, or 43.69 minutes and repeated for Quectel, Nordic, SimCom and on Nokia, Ericsson and Huawei basestations)

Also, what is the current usage of running a specific command? Is it negligible or is, for example, polling AT+CSQ constantly detrimental on battery life?

## ping

### Quectel + ZTE

The following tests were taken on the roof outside the HF RF lab on the 5th floor of the Electrical & Electronic Engineering building. The base station it connected to is on the General Building, and is just over 150m away at the same elevation with a single building blocking line-of-sight. The base station is situated on the bottom left if the picture at an altitude of approximately 138m.

![rooftop_maps](C:\GIT\masters\thesis\images\rooftop_maps.JPG)

The tests involve sending a set of 10 pings multiple times at a certain attenuation and resulting RSSI measurement.

With an antenna and the attenuator set to 0dB, we find most of the values around the mean of 185.2ms, except for the tail at around 500ms which is the time of the first ping in a set of 10.

![rooftest1](C:\GIT\masters\thesis\images\rooftest1.png)

Setting the attenuator to the max of 110dB, we see no change in the ping measurements which have a mean of 185.9ms. The tail has increased to a max of just over 600ms.

![rooftest2](C:\GIT\masters\thesis\images\rooftest2.png)

Removing the antenna from the attenuator, we find that the data has a slightly thicker tail, and averages around 207.1ms.

![rooftest3](C:\GIT\masters\thesis\images\rooftest3.png)

Lastly, having no attenuator nor antenna we still have a connection at -107dBm with a mean of 190.6ms.



![rooftest4](C:\GIT\masters\thesis\images\rooftest4.png)

To be able to attenuate the signal until disconnection, one must increase the range from the base station such that leakage transmission from traces, soldering and attenuator connectors do not interfere with the test.

There must not be a connection to the base station at all if the antenna or attenuator is disconnected or connected at maximum attenuation.

A test was performed from 10pm onwards at Technopark on 14 March 2019. A connection was made at a range of 4.8 km at -93dBm and an altitude of 132m. This is a relative elevation of -6m. At a point just below technopark and slightly closer, the altitude is -13m relative to the base station.

![techno_map4.8km](C:\GIT\masters\thesis\images\techno_map4.8km.JPG)

At 0dB attenuation the data has a mean of 196.7ms and a tail just above 500ms.

![techno1](C:\GIT\masters\thesis\images\techno1.png)

At 10dB the data is more spread out from 200 - 500ms with a mean of 396.4ms and a tail at just under 1000ms.

![techno2](C:\GIT\masters\thesis\images\techno2.png)

At 20dB attenuation, the data is more spread across 350 - 1000ms with a mean of 793.4ms and a tail that extends to over 4500ms.

![techno3](C:\GIT\masters\thesis\images\techno3.png)

Any more attenuation and the signal is lost.

The greatest distance measured was 5.5km from the intersection of the R44 and the turn-off to Stellenbosch Square at an altitude of 106m. This is a relative elevation of -32m to the base station.

![jamestownmap](C:\GIT\masters\thesis\images\jamestownmap.JPG)

At this point, the signal strength increased to -89dBm and resumed a mean of around 209.6ms with a tail around 500ms.

![stelliesquare](C:\GIT\masters\thesis\images\stelliesquare.png)

A similar pattern was seen at Parmalat, but driving closer there were a few spots where connection was lost or many retries were needed such that the tail extended up to almost 3000ms for the ICMP ping time.

![parmalat](C:\GIT\masters\thesis\images\parmalat.png)



Adding the previous test data together we see the following shape and form.

![alltests1](C:\GIT\masters\thesis\images\alltests1.png)

Lastly, all the test data including raw data on the way to Technopark, we see a similar form.

![alltests2](C:\GIT\masters\thesis\images\alltests2.png)



Looking at the ICMP ping response according to different RSSI values, we see high jitter of a few seconds from -80dBm or less.

![jitter](C:\GIT\masters\thesis\images\jitter.png)



# Discussion

Paging the base station?

Initial ping takes longer than the rest? Should one rebuild the ping test to make it more generic? What does a ping test look like?

When R14 is released, does it have backwards compatibility with R13?

There is a a certain range from the base station where the dev kit disconnects from the base station with attenuator and without antenna.

It seems that signal does poorly when passing through hills?



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

# Questions

* time, cost, energy analysis
* 

# List of references