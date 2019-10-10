---
title: LTE Cat-NB (Narrowband) Performance Evaluation
author: Daniel Robinson
date: Stellenbosch University, Sept 2019
tags: [LTE, NB-IoT]
abstract: |
  2G/GPRS is a sun-setting technology leaving behind a void for LPWANs such as LoRaWAN and SigFox to fill. The viability of NB-IoT being such a technology for South Africa is investigated. Multiple endpoint manufacturers and base station vendors are tested to compare capabilities with respect to power efficiency, latency, signal strength and other metrics. The results proved promising.

toc: true
lot: true
lof: true
link-citations: true
csl: ieee.csl
linkcolor: blue
geometry: "left=3cm,right=3cm,top=2cm,bottom=2cm"
numbersections: true
tablenos-warning-level: 1
tablenos-number-by-section: true
---

![](../images/whitespace.png)

# Declaration {-#declaration}

# Abstract {-#abstract}

# Uittreksel {-#uittreksel}

# Acknowledgements {-#acknowledgements}

* **Prof Thinus Booysen** - for his unrelenting care, innovative passion and inspiring belief in people.
* **Family** - for their love and dedication.
* **Friends** - for their wisdoms, experiencing the journey together and sharing moments in highs and lows.
* **MTN Mobile Intelligence Lab** - for providing funding, expertise and a decent laboratory environment.

# Acronyms {-#acronyms}

|      |      |
| ---- | ---- |
| **3GPP** |    Third Generation Partnership Project |
| **AMQP** |    Advanced Message Queue Protocol |
| **AT** |      Attention |
| **BPSK** | Binary Phase-Shift Keying |
| **BTS** | Base Transceiver Station |
| **CDP** | Connected Device Platform |
| **COPS** | Cellular Operator Selection |
| **CoAP** | Constrained Application Protocol |
| **D2D** | Device to Device |
| **DCE** | Data Communications Equipment |
| **DL** | Downlink |
| **DTE** | Data Terminal Equipment |
| **E-UTRAN** | Evolved-UMTS Terrestrial Radio Access Network) |
| **EARFCN** | E-UTRA Absolute Radio Frequency Channel Number |
| **EARFCN** | Extended Absolute Radio-Frequency Channel Number |
| **ECL** | Enhanced Coverage Level |
| **eDRX** | Extended Discontinuous Receive X |
| **eNB - eNodeB** | E-UTRAN Node B |
| **GPRS** | General Packet Radio Service |
| **IMEI** | International Mobile Equipment Identity |
| **IMSI** | International Mobile Station Identity |
| **IP** | Internet Protocol |
| **LPWAN** | Low-Power Wide-Area-Network |
| **LTE Cat-NB1/2** | Long Term Evolution Narrow-Band Category 1/2 |
| **MCL** | Maximum Coupling Link |
| **MCS** | Message Coding Scheme |
| **MNO** | Mobile Network Operator |
| **MO** | Mobile Originated |
| **MQTT** | Message Queuing Telemetry Transport |
| **MT** | Mobile Terminated |
| **MTN** | Mobile Telephone Network |
| **NW** | Network |
| **OTDOA** | Observed Time Difference Of Arrival |
| **PCI** | Physical Channel ID |
| **PDR** | Packet Delivery Ratio |
| **PS** | Packet Switched |
| **PTAU** | Periodic Tracking Area Update |
| **PTAU** | Periodic Tracking Area Update |
| **QXDM** | QUALCOMM eXtensible Diagnostic Monitor |
| **RRC** | Radio Resource Control |
| **SIM** | Subscriber Identity Module |
| **SMS** | Short Message Service |
| **SNR** | Signal to Noise Ratio |
| **TCP** | Transmission Control Protocol |
| **TE** | Terminal Equipment |
| **UDP** | User Datagram Protocol |
| **UE** | User Equipment |
| **UL** | Uplink |
| **UMTS** | Universal Mobile Telecommunications System |
| **URC** | Unsolicited Result Code |
| **USSD** | Unstructured Supplementary Service Data |
| **UUID** | Unique User Identification |
| **WAP** | Wireless Application Protocol |



## SI Units {-#siunits}

- **kB, MB** - kilobyte, megabyte
- **kbps** - kilobits per second
- **mJ or J** - millijoules or joules
- **s, ms, us** - second, millisecond, microsecond

\newpage

# Introduction {#intro}

This study evaluates the performance of NB-IoT.

A number of tests have been developed, performed and analyzed for multiple UEs (Ublox and Quectel) and MNOs (MTN and Vodacom) via ZTE and Nokia vendors. Power saving, latency, RF, packet and network metrics are evaluated using UDP, Echo, COPS (network registration), eDRX and PTAU tests.

---

NB-IoT is a promising contender to fill the role that 2G/GPRS leaves behind as countries around the world schedule its retirement. There are many alternative LPWANs, however.

## Why NB-IoT?

NB-IoT shows performance benefits over alternatives in terms of up and downlink throughput, range and longevity.

According to 3GPP specifications and manufacturer claims, highlights include:

* ~ 10 year battery-lifetime.
* Under 10 second transmission acknowledgement for latency-tolerant applications
* \+ 20 dB improvement over 2G/GPRS via enhanced coverage levels (ECL).

## Problem Statement {#probstat}

NB-IoT (LTE Cat-NB) is a competitive alternative to LoRaWAN, SigFox and other LPWANs. Application developers require network coverage, and cellular service providers require consumer and enterprise demand or a business case before rolling it out nationally. Although there is a great deal of theoretical analysis and simulations in research, the lack of empirical evidence may be contributing to a general uncertainty in the standing of the technology with respect to alternatives and a thus a slower adoption. This thesis aims to bridge that divide by evaluating NB-IoT's performance empirically using a set of metrics and estimate optimal use.

Whilst theoretical models provide value in showing how factors affect an approximation, it is no match for the variability induced by unpredictable network conditions and the underlying complexities of LTE architecture. Thus, an empirical approach is proposed. To emphasize the point, the energy efficiency of a single network is already questionable in Durand [@Durand2019] and Martinez [@Martinez2019].

## Research Objectives {#resobj}

The aim of this study is to evaluate latency and power efficiency of NB-IoT with a set of metric tests comparing user equipment (UE) devices against multiple mobile network operator (MNO) vendors exposing the change in variability due to proprietary LTE complexities.

Battery longevity and recommended telemetry intervals are to be estimated, and secondary metrics such as signal strength, throughput and data overhead are to be investigated.

This in turn evaluates robustness, stability, capabilities, sources of variability and claimed versus actual core features.

## Scope of Work {#scopework}

The study will be limited to the following in Table \ref{tbl:metric_summary}.

Table: UE devices, MNO vendors, metric comparisons and estimations {#tbl:metric_summary}

| MNO Vendors | UE Manufacturers | Main Metrics     | Secondary Metrics | Estimations        |
| ----------- | ---------------- | ---------------- | ----------------- | ------------------ |
| ZTE         | Ublox            | Power Efficiency | Signal Strength   | Battery Longevity  |
| Nokia       | Quectel          | Latency          | Throughput        | Telemetry Interval |
| Ericsson    | Nordic           |                  | Data Overhead     |                    |
| Huawei      | SimCom           |                  |                   |                    |

A more comprehensive study on throughput, packet delivery ratio (PDR), maximum coupling link (MCL) and scalability has been performed by Durand [@Durand2019]. Martinez has investigated the performance boundaries of NB-IoT for a Vodafone network in Barcelona, Spain [@Martinez2019].

Huawei, Ericsson, Nokia and ZTE are among the top 5 LTE vendors in the world. Ublox, Quectel, Nordic and SimCom are among the more popular NB-IoT module manufacturers, besides Telit, Gemalto, akorIoT and so on. Power efficiency and and latency is affected by variability important considerations have to be made in application development.

Telemetry tests will be limited to LTE protocols and UDP packets, which is the simplest layer and used by CoAP. Unlike UDP, MQTT uses TCP which is not a connectionless protocol. TCP streams data orderly, reliably, and at a cost to data overhead.

QXDM is a diagnostic program built for UE devices with Qualcomm chipsets, yet it costs in excess of a few thousand USD. On the other hand, UEMonitor is free and can capture debug traces from both Ublox and Quectel. An opensource decoder by LanternD offers further analytical leverage, yet it is still in beta and unstable. There is no support or alternative for Nordic or SimCom devices, however. The capture method should be easily repeatable and expandable for new UE devices. On the basis that the AT command API is familiar to all UE devices, a framework will be built to extract data via this method.

Whilst this research is funded by MTN and being aware of internal documentation, this is an independent study which should aid any potential adopters of the technology.

## Terminology {#terminology}

This section briefly introduces various IoT, LPWAN, LTE and metric related topics and is expanded upon in Section \ref{background}.

The Internet of Things (IoT in Section \ref{iot}) is a blanket term for smart devices that connect to the internet. These devices are typically found in remote or urban areas where it would be more efficient for a device to control and monitor the status of the surrounding environment than human intervention. 

Wired devices usually connect using ethernet, although it is not uncommon to use industry grade protocols such as RS232, CAN, ModBus, ProffiBus, and so on before data reaches a network hub and the internet. On the other hand, wireless connections have the benefit of easy installation and really shine in inaccessible areas. It is quite effective to connect Bluetooth and WiFi for short range applications, or using Low Powered Wide Area Networks (LPWANs in Section \ref{lpwans}) such as LoRaWAN, SigFox and NB-IoT for ranges exceeding a few kilometers and especially for limited sources of power.

Long-Range Radio (LoRa or LoRaWAN in Section \ref{lorawan}) uses chirp-spread-spectrum (CSS) modulation to make it quite immune to doppler effect motion and SigFox (Section \ref{sigfox}) uses binary phase-shift keying (BPSK) which increases noise immunity.

LPWANs enable many use cases (Section \ref{usecases}) in sensors, actuator control and location tracking to name a few.

GSM and GPRS fall under 2G and 2.5G which started development in the early 90s. Data transmission (such as USSD, SMS, WAP, IP) is circuit-switched over GSM, and packet-switched over GPRS. Circuit switched data is billed per time interval such as seconds or minutes, and packet-switched is charged per number of bytes (kB, MB, etcetra). It evolved into 3G in Release 99 at the turn of the millenium and LTE in Release 8 (Q4 2008).

Long Term Evolution (LTE) is a cellular architecture which is a subset of an even more complex 3GPP body that guides its development. In LTE, the narrowband category is known as LTE Cat-NB or NB-IoT. For their M2M applications, LTE Cat-M is similar, yet it features VoIP, faster throughput and is more similar to the LTE protocol. There are two different versions of NB-IoT, with LTE Cat-NB1 being release 13 and LTE Cat-NB2 being release 14. Their specifications have been frozen in Q1 2016 and mid-2017, respectively.

## Background {#background}

Uncertainty about NB-IoT.

If NB-IoT worked with the mobile network operators to reduce its RRC-idle phase, it could develop a minimal power consumption to compare with that of LoRaWAN and Sigfox.

---

Although NB-IoT joined LPWANs circa 2016-2017, demand uptake among consumer and industry in South Africa is still slow as well as national coverage rollout. Worldwide it has 30% (rough estimate?) population coverage with most in Europe, China and lately America (mid-2019).

In South Africa, NB-IoT has most of its coverage in the Gauteng province as well as a few sites in other towns and cities. Although Gauteng only covers 1.49% of the land mass in South Africa, it holds ~22% of its ~57 million people so it is great as a live trial run before pushing for national coverage.

It is based off of LTE, making integration and upgrading of existing infrastructure more seamless than an entirely separate technology, although it also brings with the drawbacks of legacy LTE. This includes the benefit of low power, and the low bandwidth trade off which is suitable for smart devices and IoT.

An application developer in IoT is interested in a hands-on approach with the technology they will use, with the aim of scaling up production such that volumes of 1000 devices or more can be reached. Thus an empirical evaluation of the technology is focused on in this thesis, especially when considering that much of the research is analytical or simulation bound.

Martinez [@Martinez2019] has explored NB-IoT from the perspective of the application developer. It is well thought out, and follows a similar path to this thesis. When evaluating performance, it would do well to find the limits of the technology as well as find the optimum 'sweet spot' or range for efficient operation.

A user would consider critical characteristics such as energy consumption, coverage, cost, network latency and behavior. Martinez looks at these except for cost, which is better looked at by Ali [@Ali2015]. A set of tests were devised and results showed that in some cases its energy consumption performed better than an LPWAN referenced technology such as LoRa, with the added benefit of guaranteeing delivery. However, the high variability in energy consumption and network latency call into question its reliability especially for mission-critical applications.

Network operators are looking to enter the LPWAN sphere. 3GPP have made this possible by adapting LTE into Cat-M and NB-IoT.

Application developers are always on the lookout for viable technologies, and tend to use the most prolific ones

## Internet of Things{#iot}

In 2014, Gartner estimated that Internet of Things (IoT) had reached the height of inflated expectations, and the hype it generated has resulted in a rich ecosystem of technologies.

![Gartner's IoT hype 2014](../images/hype-cycle-2014-100371840-large.idge.jpeg)

![Gartner's Hype Cycle for Emerging Technologies, 2019](../images/CTMKT_741609_CTMKT_for_Emerging_Tech_Hype_Cycle_LargerText-1.png)

![[Gartner's 2018 Hype Cycle for ICT in Africa](http://www.gartner.com/newsroom/id/3884512)](../images/42881085945_739bbdc8e9_c.jpg)

IoT hype becomes many other emerging technologies. https://blogs.sas.com/content/hiddeninsights/2016/07/06/long-live-the-iot-hype/

Hype yields investment, regardless whether the underlying innovation holds value. IoT holds value in connecting things to the internet, as in its namesake. This can be seen in the venture capital injection into companies and start-ups and the number of connected devices over time.

![Number of connected devices [@Ali2015]](../images/Expected-number-of-connected-devices-to-the-Internet-This-chart-is-obtained-from-recent.png)



IoT shows great potential for exponential growth, and unless a technology disruption occurs which means we do not require connections or our devices, then there is undoubtedly an [uptrend](https://amarketresearchgazette.com/global-narrowband-iot-nb-iot-market-2019-2025-vodafone-china-unicom-china-telecom-att-etisalat-telstra-orange-telefonica-sk-telecom-deutsche-telekom/). As Gartner predicts, we should be in the plateau of productivity now, and this can be observed by looking at the current news regarding the technology.

A few months before publishing, [AT&T announces](https://blog.nordicsemi.com/getconnected/att-launches-nb-iot-network-in-usa) nation-wide coverage of NB-IoT in the USA, alongside its existing LTE Cat-M coverage. Deutsche Telekom and Vodafone cover Europe (news?) and China enables millions more IoT devices [@china2019].

* Matching emerging applications with existing technologies has become one of the
  main challenges for IoT initiatives, especially when a new technology appears in the landscape and the map must be redrawn.

Although there are many ways to connect IoT to the internet, NB-IoT is an LPWAN which is the focus of this study.

## Low-Powered Wide-Area Networks {#lpwans}

There are many wireless technologies out there, with some standardized (including Bluetooth, 6LowPan, RPMA, Weightless, IETF 6TiSCH, SigFox, LoRaWAN, Dash7 amongst others). Many are proprietary to retain company value and they try to meet application specific requirements also limited by technological constraints. Matching custom applications with a wireless technology is non-trivial as there is no silver bullet that matches all use-cases. On the contrary, many technologies overlap in their capabilities.

Table: Brief comparison of wireless LPWANs {#tbl:lpwan_comparison}

|                       |             | LoRaWAN           | SigFox   |      |      |
| --------------------- | ----------- | ----------------- | -------- | ---- | ---- |
| Frequency             |             | 433, 868, 915 MHz | ~868 MHz |      |      |
| Bandwidth             |             |                   | 200 kHz  |      |      |
| Throughput            | 56–114 kbps | 27 kbps           | 0.1 kbps |      |      |
| Duty cycle limitation |             | 1-10%             | 1%       |      |      |
| Messages per day      |             |                   | 140      |      |      |
| Bytes per message     |             |                   | 12       |      |      |

Table: Brief comparison of cellular technologies {#tbl:cellular_comparison}

|                   | 2G/GSM/GPRS | EC-GSM-IoT | LTE Cat-M | NB-IoT     |
| ----------------- | ----------- | ---------- | --------- | ---------- |
| Frequencies       |             |            |           | 0.8-2.6GHz |
| Bandwidth         |             |            |           | 200kHz     |
| Throughput        |             |            |           | 250 kbps   |
| Bytes per message |             |            |           | 512        |

LPWANs enable a vast array of use cases.

|              | MCL    | Scalability | Battery life | Throughput |
| ------------ | ------ | ----------- | ------------ | ---------- |
| NB-IoT       | 164dBm | >50k        |              |            |
| GPRS         | 148dBm |             |              |            |
| LoRaWAN SF12 | 157dBm |             |              |            |
| SigFox       | `dBm   | >50k        |              |            |

| Technology   | MCL  | Scalability | Battery life | Throughput |
| ------------ | ---- | ----------- | ------------ | ---------- |
| NB-IoT       | X    | X           |              | X          |
| GPRS         |      | X           |              | X          |
| LoRaWAN SF7  |      |             | X            |            |
| LoRaWAN SF12 | X    |             |              |            |
| SigFox       | X    | X           |              |            |

* Competition in the LPWAN space and regional momentum will ensure that the various technologies will continue to develop and improve to support more features and expand the network coverage. 
* We expect selected uptake of each technology in specific application areas and our results show that each technology is better suited to specific applications and their concomitant requirements. Sigfox, NB-IoT, and LoraWAN SF12 performed equally well for applications where MCL (range) is paramount, with LoraWAN SF7 doing slightly worse. In applcitions where the main consideration is scalability, Sigfox, and NB-IoT substantially outperformed the LoraWAN varieties. However, if battery life is the most important consideration, LoraWAN SF7 seems to have the edge, with NB-IoT (the default setup we tested) performing worse. NB-IoT performed the best for uplink throughput, with LoraWAN SF7 coming in second. For all the other two-related metrics evaluated, namely downlink throughput and firmware upgradability, NB-IoT performs substantially better than the other technologies.
* Poor for asset tracking and utility metering.
* Average for smart bicyles, parking, garbage bins, agriculture and intelligent buildings.
* Good for pet tracking, POS, healthcare.
* NB-IoT outperforms SigFox and LoRaWAN in UL/DL throughput, scalability, MCL range and FoTA updates. It is superseded by LoRaWAN in battery life for SF7.

## Metrics {#metrics_intro}

* **MCL**: For IoT devices used in extended coverage situations,
  such as deep-indoor devices or remote locations, we recommend either Sigfox or NB-IoT, as they offer a maximum MCL of more than 158 dB. IoT devices for general use would benefit from the large-scale deployment of the GPRS network, which provides excellent coverage because of its legacy infrastructure. It is clear that the extra overhead available in Sigfox, LoRaWAN, and NB-IoT allows for better indoor coverage than GPRS, which means that the LPWAN devices can be used in less than optimal operating conditions. Measured MCL correlates with theoretical values.
* **Power consumption**: In applications where device battery life is
  a crucial factor we recommend, either LoRaWAN or Sigfox, because they are completely asynchronous. We found that the battery life of LoRaWAN SF 7 was five times that of LoRaWAN SF 12 and nearly 25 times that of Sigfox. This is mainly due to the extremely long time-on-air of LoRaWAN SF 12 and Sigfox. If NB- IoT worked with the mobile network operators to reduce its RRC- idle phase, it could develop a minimal power consumption to compare with that of LoRaWAN and Sigfox.
  * It is clear that LoRaWAN SF7 is the most power-efficient, due to the short transmission burst. NB-IoT displays the worst power-consumption, due to the extended RRC-idle state. This can be reduced using Release Assistance as in Section \ref{release_a}.
* **Throughput**: As throughput differs greatly between the four technologies, comparisons should rather be made in either the licensed (NB-IoT and GPRS) or unlicensed (Sigfox and LoRaWAN) spectrum categories. Applications that require huge amounts of data to be transmitted, such as real-time vehicle fleet monitoring, we recommend GPRS and NB-IoT as they are not duty cycle limited. The choice of GPRS or NB-IoT will be based on the battery life requirements of the IoT device, with NB-IoT having the advantage. In the case of extremely low-throughput applications, such as water meters, power meters, and weather stations, we recommend Sigfox, as it offers a scalable solution with no base station costs involved. Although it limits the 12 byte throughput per 24 h to 140 messages, this is more than the 20 messages offered by LoRaWAN SF12 (TTN).
  * As NB-IoT operates in the licensed spectrum, there are no
    throughput restrictions, other than the data-rate restriction. We measured the uplink and downlink data rates in different signal quality environments (distances from the gateway) by querying the modem. The measured downlink rate varied from 2250 to 14,193 bps. We could find no clear correlation between the downlink data rate and the signal quality environment.
* **Scalability**: 
  * Lower (sub-500 devices per gateway) scalability of LoRaWAN per base station compared to NB-IoT and GPRS. This low scalability is due to the limited number of channels and the lack of any scheduling between devices. To compensate for the low scalability, an increase in spatially diverse base stations would allow packets to be received by multiple base stations at varying received power levels.
  * This simulation showed that with 55,000 devices transmitting the base station would reach the 270 simultaneously transmitting devices that Sigfox claims is possible while still ensuring a 99.9% PDR.
* **Down link latency**: In applications where downlink latency is a
  critical component, only GPRS will suffice, as it is the only technology in this study that requires constant paging between the base station and the end device. 
* **Down link throughput**: Any applications requiring bi-directional communication of more than 120 bytes per 24 h, should use NB- IoT or GPRS, as Sigfox and LoRaWAN are limited by the duty- cycle limitations of the base station. 
* **FoTa**: GPRS and NB-IoT are able to offer FOTA upgrades to IoT devices, as Sigfox ha s limited bandwidth. This feature is supported by LoRaWAN, through the fragmentation of large payloads [22].

## Use Cases {#usecases_intro}

- Public Safety
- Agriculture
- Smart Metering
- Actuator Control
- Real-time Monitoring
- Asset Tracking

IoT has use case requirements in UL/DL throughput, battery longevity and scalability.

The most popular use case in IoT is smart metering.

## Smart Metering {#smartmetering}

One of the simplest use cases in IoT is smart metering. Periodically sending uplink data at regular intervals from a static location has the advantage of remote monitoring and reducing the need for physical readings. It also opened up new features for users (such as dynamic pricing and usage pattern analysis) and operators (such as load balancing a large number of clients). The clear value proposition and success is partially due to the belief that IoT should be low powered and low data transmissions which still exists today.

**Smart metering can be considered as defeating the purpose of NB-IoT when considering its downlink capabilities.**

Smart metering can be considered the traditional IoT model.

## Push-Pull Model

Traditionally, IoT devices push data to the internet at regular intervals. This push model can be considered quite energy inefficient, especially when the data is only occasionally actionable. For example, in asset tracking or remote monitoring.

A pull model is ideal for dynamic rule engines, pulling data only when necessary and ultimately edge computing, where building an application around this idea can greatly enhance battery life.

## Edge Computing

Edge computing is the practice of offloading cloud processes to the endpoint. It saves on data overhead, especially when there are data charges involved and battery longevity is desired.

Since NB-IoT is optimized for downlink communications, it can be the ideal candidate.

## NB-IoT {#nbiot}

Formed by the 3GPP from LTE, NB-IoT was developed within that framework and its capabilities are particularly well suited to smart metering.

![IoT Market representation [@Martinez2019]](../images/1559246290186.png)

Taking it one step further, the 3GPP defined two device categories, namely Cat NB1 and NB2, with the latter adding support for:

- Support of Positioning of Device using OTDOA
  - seamless cell re-selection
- Push to talk voice messaging
- New Device Power Class (14 dBm)
- Multicast transmission

 OTDOA positioning, 

Compared to LTE

- devices are stationary

- intermittent burst transmissions

- low data bandwidth

- delay-tolerant applications

- support for huge number of devices

- deals with poor coverage (indoor penetration)

- battery lifetime of a few years

  

* eDRX and PSM
* Debugging
  * QXDM, UEMonitor etc
  * [@ubloxAppNote2018]



* NB-IoT devices are seen as stationary, only small chunks of data are intermittently transmitted and applications are envisaged as delay-tolerant.
* NB-IoT technology is designed such that it can be used in areas beyond the radio coverage of current
  cellular standards and in devices which must run from battery power for many years. The devices
  will generally send small amounts of data infrequently; a typical usage scenario might be 100 to
  200 bytes sent twice per day for battery powered devices. For mains powered devices the limit is not
  based on battery size, but cost and network bandwidth/resources.
* The system operation is analogous to SMS in that it is a datagram-oriented, stored-and-forward
  system, rather than a GPRS-like IP pipe. This is because NB-IoT devices spend most of their time
  asleep, making possible the required long battery life. The system implements extended DRX cycles
  for paging, but as this window will be limited to save battery life, the delivery of downlink messages
  occurs mainly when the system detects that uplink messages have been received from a device
  (indicating that it is awake). Here a store-and-forward system, an “IoT Platform”, is useful.



Although most users interact only with the UE device which runs its own proprietary firmware stack, NB-IoT also has a complex backend architecture.

## LTE Architecture

![LTE_classic_architecture](../images/LTE_classic_architecture.png)

The complexities of LTE architecture further increases the chance of performance degradation with respect to 3GPP specifications due to the vast array of setup parameters. It would be beneficial to analyze the performance of multiple UE devices against various MNO vendors. It is important to note that MNOs may use various vendors in their architecture, and thus this study is mainly focused on the eNodeB vendor which is also UE device facing and has the greatest chance of performance degradation due network quality, RF interference and so forth.

* Both UDP socket commands and datagram commands use the IP data transport through the SGi.

## Performance Evaluation

It would be useful for the application developer to know the boundaries resulting from this approach. Drawbacks and optimizations targeting IoT can be discussed. The application developer is a potential adopter of the technology and focuses on parameters that fall within end-user control.

Cellular operators would also benefit by knowing where they can improve upon their configurations and equipment.

To this end it would be beneficial to:

- Analyze critical metrics at the core of NB-IoT, such as energy consumption, coverage, cost and latency.
- Create a testing framework to characterize NB-IoT devices in actual operation and using various networks.
- Set optimal operating boundaries based on the obtained results. This should also re-evaluate suitability in certain use cases.

There are over 50 MNOs in the world that are using NB-IoT, yet most draw from a subset of the [top 5 LTE vendors](https://www.rcrwireless.com/20160531/network-infrastructure/top-5-wireless-infrastructure-makers-tag4-tag99):

1. Huawei
2. Ericsson
3. Nokia
4. ZTE
5. Samsung

## MNO Vendors

In South Africa, there are two mobile network operators trialing NB-IoT and combined they use four of the top LTE vendors. Samsung has started using NB-IoT only as recently as May 2019, [announcing a partnership with KT to create a Public Safety (PS-LTE) network](https://enterpriseiotinsights.com/20190506/nb-iot/samsung-kt-launch-nbiot-service-through-ps-lte-network-korea). They're also implementing device-to-device (D2D) communications to increase connectivity in unfavourable conditions.

Table: MNOs and their BTS Vendors {#tbl:mno_bts}

| BTS Vendors | Cellular operator (MNO) |
| ----------- | ----------------------- |
| Nokia       | Vodacom                 |
| ZTE         | MTN                     |
| Huawei      | Vodacom                 |
| Ericsson    | MTN                     |

Theoretically, one can assume that these manufacturers meet 3GPP's specifications and that they have set up an optimal environment.

With a testing framework, one can evaluate these capabilities in a transparent manner for both developers and cellular operators alike and work towards improving the quality thereof.

Cellular operators are in control of some things, and users of others.

Table: Cellular control {#tbl:cellular_control}

|                             | Cellular operators | Users       |
| --------------------------- | ------------------ | ----------- |
| NB-IoT Base stations (BTS)  | **X**              |             |
| NB-IoT User Equipment (UE)  |                    | **X**       |
| LoRaWAN Gateways            |                    | **X**       |
| LoRaWAN Devices             |                    | **X**       |
| NB-IoT licensed spectrum    |                    | billed      |
| LoRaWAN unlicensed spectrum |                    | duty-cycled |
|                             |                    |             |
|                             |                    |             |

MNO/BTS Vendors are open to all UE manufacturers.

## UE Manufacturers

UE devices specifically used:

- Ublox Sara N200
- Quectel BC95

and the following recommended in future:

- Nordic nRF9160
- SimCom SIM7020E

### Ublox

### Quectel

### Nordic

### SimCom

These UEs all share AT commands as the API to control their capabilities.

## AT Commands {#atcommands}

This section outlines the capabilities of the UEs.

Table: Summary AT Command set for Ublox {tbl:atcommands}

|                      | Command    | Description                                                  |
| -------------------- | ---------- | ------------------------------------------------------------ |
| Set configuration    | AT+NCONFIG | Change configuration for SI_AVOID, Scrambling etc.           |
| Network Registration | AT+COPS    | This command initiates search for cell towers to connect to depending on MNO-related SIM-card and registers/deregisters accordingly. |
| Set APN              | AT+CGDCONT | Sets the relevant APN for the MNO.                           |
|                      |            |                                                              |

* SARA-N2 series modules implement a FOTA solution based on CoAP. It is possible to configure the
  module’s poll timer for when the module checks the FOTA CoAP server for new firmware. When the
  feature is enabled and a new package is available, the module will automatically download the FOTA
  update and provide URCs about its progress. The module’s firmware is not updated automatically
  when the download has completed and so the application must start the upgrade process step.
* The +UTEST AT command allows the user to set the module in non-signaling (or test) mode, or
  returns to the signaling (or normal) mode. In test/non-signaling mode, the module switches off the
  protocol stack for performing single tests which could not be performed during the signaling mode.
* MO Datagrams sent and received by IoT platform has these commands wrapped internally in a Constrained Application Protocol (CoAP) message and sent over UDP sockets. Once the module accepted a datagram it cannot be removed and will be transmitted to the network as soon as radio conditions permit. The only way to clear the module’s transmit queue is to reboot it. In good radio conditions, the transmission might take a few seconds. In bad radio conditions a transmission opportunity may not occur for minutes, days or weeks but the datagram will be transmitted once radio conditions are good enough. When a MO message is queued, the module will try to send the message to the base station. It will only send the next message once the previous message has been sent. If there is a radio link failure (RLF), the device will re-scan the channel ranges and try to reconnect to a base station. There may be a back off time where the device goes into deep-sleep mode before trying again.
* An unsolicited result code (URC) is a string message (provided by the DCE) that is not a response to
  a previous AT command. It can be output, when enabled, at any time to inform the DTE of a specific
  event or status change.

When it comes to base stations, the user does not have control over the inactivity timer. Release assistance can request the eNB/network to disconnect the modem from Radio Resource Control (RRC) connected mode.

## Thesis structure {#thesis-struct}

NB-IoT is introduced to the reader in Chapter \ref{intro}. A literature study reviews the current empirical research in Chapter \ref{litstudy}. Design and methodology shows the steps taken to capture different metrics and process the resulting dataset in Chapter \ref{design}. Results are analyzed in Chapter \ref{results} and discussed with recommendations in Chapter \ref{#discussion}. Lastly, a conclusion is made in Chapter \ref{conclusion}.

# Literature Study {#litstudy}

Several studies provide theoretical models not only for the energy consumption of NB-IoT networks [@Andres-Maldonado2017], but also for their latency and delay bounds [@Feltrin2019], impact of coverage extensions [@Andres-Maldonado2018b], coverage performance [@Adhikary2016], battery lifetimes [@Yeoh2018d],[@Lauridsen2018], (theoretically) optimal configuration strategies [@Feltrin2018] and overall performance for particular verticals [@Soussi2018],[@Beyene2017b].

Only Martinez [@Martinez2019] focuses effort on the adopter and presents an operational and empirical analysis of the technology when it is deployed in a real network (such as Vodafone in the Metropolitan area of Barcelona). Durand [@Thomas2018] compares different LPWANs empirically including NB-IoT.

Despite the unquestionable value of the theoretical models (for example, to understand orders of magnitude or to guess the theoretical upper and lower bounds), an empirical approach provides real insights into the variability that a UE device experiences when deployed in real conditions. This work therefore complements Martinez and related works, and it further provides empirical measurements for UEs that are deployed using a real-world NB-IoT network always while taking the perspective of an application developer.

* GSM RF equipment testing and performance analysis [@Kasbah2005]
* Analysis of NB-IoT Deployment in LTE Guard-Band [@Ratasuk2017c]

The empirical results of NB-IoT depend on the device used (UE) and underlying vendor architecture of the MNO providing coverage. Thus, 

## LoRaWAN {#lorawan}

LoRaWAN is a contender for NB-IoT. It lacks bidirectionality and datarate.

* LoRaWAN performs better for short messages, but it is subjected to a very high penalty when
  more than one message per data block is required.
* Second, the LoRaWAN reliability mechanism must be ensured at the
  upper layers, and thus may incur higher energy costs.
* 

## SigFox {#sigfox}

SigFox is a contender for NB-IoT. It lacks bidirectionality and datarate.

## NB-IoT {#nbiot_lit}

- This section describes NB-IoT in more detail and the setup procedures involved.
- 3GPP
- the UE device is to a large extent/entirely controlled by the network/eNodeB.
  - UE devices must follow NW settings broadcast inside the SIB and allocations for UL/DL data.
- 

## Standing/Positioning

[@Martinez2019]

NB-IoT has proven to be competitive in terms of energy consumption,

* Decent study on the operational trade-offs of NB-IoT over LTE.

Complexities

- signalling, dynamic adjustments triggered by network conditions, timing
- competitive in terms of NB-IoT consumption due to 3GPP efforts to be similar to LPWANs

Proprietary spectrum vs ISM bands?

- ISM external interference and share
- otherwise high unpredictability in device behavior

Reliability?

- Delivery guarantee

Delay Tolerance

- high variability in delivery time. Deal-breaker for some applications.

Data rate

- sporadic high bandwidth

Ownership model

- connectivity service, contract, charged per byte
- coverage depends on deployed infrastructure

## Hardware

* Modem
* Antenna
* RX/TX lines

## Setup

* AT+NCONFIG
  * AUTOCONNECT
  * CR_0859_SI_AVOID
  * CR_0354_0338_SCRAMBLING
* URCs
* APN

## Network Registration

- By default the SARA-N2 series modules will automatically try and connect to the network. This
  feature will read the SIM for the PLMN and attempt to register with the network. The device will use
  the default APN from the network. The auto-connect feature can be enabled by the +NCONFIG AT
  command. Reset the module to save these settings to the non-volatile memory.
- If the application requires more control over the registration process set the SARA-N2 series
  modules into the manual registration mode. With the auto-connect feature turned off the module is
  able to manually connect to a specific PLMN and specify an APN.
- After a RRC connection is made to the base station the module will try and register with the
  network. If the module IMEI or IMSI is not allowed on the network, the module will disconnect from
  that base station and continue scanning for other base stations. This can be seen if the <mode>
  parameter of the +CSCON AT command shows the “1” and then “0” response without +CEREG
  changing to 1 or 5 means that the module was not able to register on that network.
  In case the module is registered to the network, the <status> parameter of the +CEREG AT
  command will be 1 (registered) or 5 (registered & roaming).
- See [@ubloxAppNote2018]] for a connection status compatibility matrix.

## RRC Connection and Inactivity Timer

After network registration or transmitting a data packet, the device usually enters RRC connected (C-DRX) mode for a specified inactivity timeout specified by the network.

- When the module is in RRC connected mode it will be receiving all the base station signaling. The
  average power consumed in this mode is about 48 mA. If the RRC connection is left for 20 s of
  inactivity before the RRC is released, then this will consume about 1 mWh @ 3.6V.
- 48 mA in this mode
- 20 seconds is about 1mWh @ 3.6V
- AT+CSCON
- After a short period, if no messages are being sent from the module, the +CSCON response will be
  “0” to show the RRC connection has been released by the eNodeB.
- At the first registration or when the module wakes from the power save mode (PSM), it performs a
  Random Access CHannel (RACH) procedure to attach to the base station. This establishes a Radio
  Resource Control (RRC) connection to the base station. Once established only the base station can
  release this connection. The module cannot drop the RRC connection other than turning off the
  radio using the AT+CFUN=0 command.
- The base station has an “inactivity” timer for each module and if there is no activity the base station
  will send a RRC release message to the module. The module should respond back to the base station
  with an acknowledgment. The inactivity timer is nominally 20 s.
- The module will be able to receive and send messages immediately when in connected mode.
- During a RRC connection, the +CSCON AT command provide the signalling connection status. It is
  also possible to enable the +CSCON URC.
- When a MO message is sent from the module, the module must first create a RRC connection if
  there is not already established with the base station. This status can be checked using the
  AT+CSCON command.
  To check the signalling connection status issue the +CSCON read command. The second parameter
  of the information text response (+CSCON: <n>,<state>) provides the interested information:
  * 0: idle mode (no RRC connection)
  * 1: connected mode (RRC connection)
- To configure a URC for this command, issue the AT+CSCON=1 command. A URC will be issued at
  each RRC connection status change. 

## Release Assistance {#release_a}

Release assistance requests the eNodeB to release the RRC connection immediately. By avoiding 20 seconds of idle RRC in C-DRX mode, there is a 93% improvement in power consumption for a 200 byte transmission in ECL 1.

[@ubloxAppNote2018]

An example of sending a 200 byte message in ECL 2 with good SNR can include 5 RACH transmission bursts, a Transmission Block Size ~43 bytes, one repetition and taking just over 1 second, consuming 200uWh.

For the same example in bad SNR, the TBS allocated 32 bytes per chunk, with a repetition of 8 and 4. It took 5.5 seconds and consumed 1.07mWh -- fives times as much as before.

- Some applications may not want to wait for the base station’s inactivity timer to expire after 20 s as
  this wastes power from the battery. In Release-13 the “Release Assistance” feature allows the
  module to request for the RRC connection to be dropped as soon as the message has been received
  by the network.
- The flag is noticed by the MME on the network and sends a message back to the eNodeB base
  station to drop the RRC connection. The network must support Release Assistance for this feature.
- After the RRC connection has been released the module then goes in to a period where it could be
  paging the base station. The timer for this period is called T3324. After T3324 has expired the
  module goes into Power Save Mode (PSM). See section 11 for further information



## Power Saving Mechanisms

The NB-IoT protocol allows for power save mode (PSM), and the SARA-N2 series modules also
support a Deep Sleep mode where the module is running at very low current, ~3 $uA$. The module
automatically enters various states depending on the device activity. Here below are listed the
common activities and the various states it will be in after registration.

* T3324 / T3412 timer values

### T3412 PTAU Timer

* (GPRS timer 3)
*  3GPP TS 24.008 [4], figure 10.5.147a and table 10.5.163a.

* Bits 5 to 1 represent the binary coded timer value. Bits 6 to 8 define the timer value unit for the GPRS
  timer as follows
* 8 7 6
  0 0 0 value is incremented in multiples of 10 minutes
  0 0 1 value is incremented in multiples of 1 hour
  0 1 0 value is incremented in multiples of 10 hours
  0 1 1 value is incremented in multiples of 2 seconds
  1 0 0 value is incremented in multiples of 30 seconds
  1 0 1 value is incremented in multiples of 1 minute
  1 1 0 value is incremented in multiples of 320 hours (Note 1)
  1 1 1 value indicates that the timer is deactivated (Note 2)
* Example: "01000111" = 7 x10 hours = 70 hours
* NOTE 1: This timer value unit is only applicable to the T3312 extended value IE and the T3412
  extended value IE (see 3GPP TS 24.301 [5]). If it is received in an integrity protected message, the
  value shall be interpreted as multiples of 320 hours. Otherwise the value shall be interpreted as
  multiples of 1 hour.
* NOTE 2: This timer value unit is not applicable to the T3412 extended value IE. If this timer value
  is received, the T3412 extended value IE shall be considered as not included in the message (see
  3GPP TS 24.301 [5]).

### T3324 Active Timer

* The T3324 Timer is reset after a downlink message is received. The negative impact on energy savings should be taken into account if downlink data is fragmented.
* the Active Timer (T3324) controls the time lapse during which the UE device is reachable by the network in RRC Idle, i.e., the number of eDRX cycles.

* Bits 5 to 1 represent the binary coded timer value. Bits 6 to 8 define the timer value unit for the GPRS
  timer as follows
* 8 7 6
  0 0 0 value is incremented in multiples of 2 seconds
  0 0 1 value is incremented in multiples of 1 minute
  0 1 0 value is incremented in multiples of deci-hours
  1 1 1 value indicates that the timer is deactivated
* Example: "00100100" = 4 x1 minute = 4 minutes

### eDRX Cycle

* An eDRX cycle is composed of an active phase, controlled by a Paging Time Window (PTW) timer, which ranges from 2.56 s to 40.96 s followed by a sleep phase until the end of the eDRX cycle. Within the PTW, the standard LTE paging is observed.

### PTW

## System Information Blocks (SIB) {#sib}

The SIB describes the method of attachment and what repetitions the UE device must use to first transmit
to the base station. Once a RRC connection is made, the base station then uses the perceived SNR
to configure the uplink allocations the UE device will use to transmit the messages.
Because allocations for each uplink/downlink are dynamically set by the base station it is difficult to
calculate the power consumption of a single message deployed in the field.

* example SIB

## Repetitions (ECL)

* ECL
* Module interference increases the number of repetitions
* Minimize ECL 2.
* Network operators should provide enough coverage to allow devices to be mostly in coverage class 0
  or 1. Depending on the NB-IoT deployment, the network could have large areas, or devices located in
  deep locations which unfortunately mean they operate in Coverage Class 2.
* Coverage Class 2 uses high repetitions for the RACH process and also higher coding schemes when
  transmitting data and therefore fundamentally consumes more power than it would in the other
  coverage classes.

* 

## Behavior

* The application can monitor the status of the module’s connection, registration and PSM state by
  polling or configuring URCs. By monitoring the module status the application can behave more
  efficiently, depending on the application type. For example, the application may want to know when
  the module goes into Power Save Mode (PSM).

Register the module to the NB-IoT network before to send or receive any messages. Without being
registered the module will not be able to send or receive any messages.
To check the network registration status issue the +CEREG read command. The second parameter
of the information text response (+CEREG: <mode>,<state>) provides the interested information
* 0: not registered, not registering
* 1: registered
* 2: not registered, but currently in the process to
* 3: registration denied. The application should have a re-try mechanism which does not simply try registration immediately, but has some back-off process
* 4: unknown
* 5: registered, roaming

When the module has started the network search process, poll the +NUESTATS AT command and
view the Rx and Tx Time:

* If Rx Time is increasing then the module is trying to scan for a base station.
* If Tx Time is increasing then the module has found a base station and is trying to communicate
  with it.
* If the Total Power and Signal Power values are different than -32767 (invalid) then the module has
  read the MIB and SIB signals from the base station.
* Once an RRC connection is made, the +CSCON read command will return 1. Turn on the +CSCON
  URC which will be output at each RRC connection change.



If the SIM used is an international SIM (roaming SIM) then the registration process can take many
minutes for the first time. Once the module is registered on that network the PLMN should be
stored in the SIM so that registration is quicker next time. The application can tell if it is using
roaming SIM by the state being “5”.

* The +CEREG URC can be enabled to provide the network registration status. Depending on the
  <mode> parameter it is possible to configure the interested URC parameters (i.e. <mode>=4 or 5 to
  see the provided network timers). See SARA-N2 AT Commands Manual [2] for more details.
* Properly setting the +CEREG AT command (<modem>=3, 4 or 5) it is possible to see the
  registration EMM cause value. These values are described in the 3GPP TS 24.008 [4]. Typical
  causes:
  * #5 IMEI not accepted
  * #11 PLMN not allowed
  * #12 Location Area not allowed
  * #13 Roaming not allowed in this location area
  * #22 Congestion

## Data transmission

The SARA-N2 series modules are able to send raw data through UDP sockets to an IP address. The
data sent over the socket AT commands is not wrapped in any other layer, and the data provided is
the data that is sent.

The Constrained Application Protocol (CoAP) is a datagram-based client/server application protocol
for devices on the constrained network (e.g. low overhead, low-power), designed to easily translate
to HTTP for simplified integration with the web. CoAP clients can use the GET, PUT, POST and
DELETE methods using requests and responses with a CoAP server.

The usage of the Non-IP method during the sending or receiving of messages saves the overhead of
needing to send a UDP IP header.

See [@ubloxAppNote2018] for an Application example.

### Ping

Issue the +NPING AT command to check if the module is able to send and receive data.
Check to see if the network can communicate to the internet, or it is needed another accessible
server’s IP address to ping.
To ping Google’s DNS server:
AT+NPING="8.8.8.8"
To ping OpenDNS DNS server:
AT+NPING="208.67.222.222"
The information text response to the +NPING AT command will be issued after a few seconds. If the
information text response is +NPINGERR: 1, the ping has timed out.

* The first ping might fail because it can take a few seconds to connect to the base station. Use
  the +CSCON URC to show when the module is connected.

### Echo

For a more advanced check on sending data to an external server, send data to the u-blox echo
server at echo.u-blox.com.
* Because there is no DNS lookup function in the SARA-N2 module series, use the IP address
server which is 195.34.89.241.

Command Response Description
AT+NSOCR="DGRAM",17,10000 0
OK
Create a UDP socket.
AT+NSOST=0,"195.34.89.241",7,5,"0102
030405"
0,5
OK
Send data on socket 0.
+NSONMI: 0,5
Receive data on socket 0.
AT+NSORF=0,5 +NSORF: 0,"195.34.89.241",7,5
,"0102030405",0
OK
Request data from socket 0.
Echo’d data received

## Available Metrics

When the module is synchronized to the base station and is receiving the signaling the +NUESTATS AT command is able to describe the radio, cell, BLER and throughput statistics.
The most useful statistic is the "RADIO" type.

### RSRP

It is the power of the wanted part of the receive signal, the NB-IoT part.

### Total power

It is the radio signal strength within the receive bandwidth (both expressed in 10ths
of a decibel). From this the signal to noise ratio can be calculated.

### Transmit power

* It is the RF power output from the module. It may be a low number if the
  received signal strength is good (and hence the module assumes that the base station is close
  by).

*  Ideally the module
  should consume 230 mA for +23 dBm.

### TX, RX Time

TX Time is the duration for which the module’s transmitter has been switched on.

RX Time is the duration for which the module’s receiver has been monitored for downlink
activity (both expressed in milliseconds since the last reboot). Together these can be used to
assess the time the module spends in each state and hence estimate the power consumed by
the module.

When the module first tries to register with the network, the Tx time will be zero as it will not have
instantly found a base station. The Rx time will increase to show it is scanning for a base station.
Once a base station is found it is possible to see that it is attempting to transmit to the base station
as the Tx time will start to increase. If the base station does not respond to the module’s Tx, then
the +CSCON: 1 URC will not be issued.

### ECL 

It is equivalent to "PRACH coverage enhancement level" defined in 3GPP 36.321 [3] sub
clause 5.1

* As observed, the ECL has an impact on energy consumption, but not on the delay.

### SNR

Last SNR value.

## Latency {#latency}

* < 10 seconds
* 

## Power Consumption {#power}

* ~ 10 years battery life

Low power consumption is vital for battery longevity.

* PCB layout, antenna matching and location will have an effect to the overall interference received by the module.
* PSM and eDRX
* On the other hand, although the average power is comparable, peaks in transmission of LoRaWAN’s radio are around 40 mA, while in NB-IoT they reach 220 mA. This causes additional stress on the battery, which has to be managed with care.
* As can be observed, mean values for NB-IoT are similar to the energy that a LoRaWAN device requires to transmit while using the SF12 configuration. The 5th percentile results for NB-IoT (best observed performance) are comparable to the best case performance of LoRaWAN when operating at SF8. This is in our opinion a relevant result, as NB-IoT guarantees packet delivery with similar power consumption.
* The expected achievable lifespan (on average) for a NB-IoT is on the order 2-3 years, depending on the datagram size.
* However, adopters may take into consideration some differences. First, sending larger messages (up to 512 bytes) has almost no impact on NB-IoT.
* In a simple periodic-reporting application with very limited computing requirements5, the average power can be modeled approximately by Eq. \ref{eq:avgpower}, as detailed in [21]:

$$P = \frac{E_{msg}}{T_{msg}}$$ {#eq:avgpower}

* 

## Data Usage

* The module has a limited dynamic message queue size. For IoT applications, the message size should be of the order of tens of bytes. UDP socket commands limit their payload size to 512 bytes.
* There is no indication when the UDP data has been sent.
* Downlink data from the cloud server must also be 512 bytes or less, because otherwise the messages will be lost.
* The module has an internal message buffer. If the module is unable to send the messages to the network before this buffer is full, because the application is queueing quicker than it can send them, then the UE device will return ERROR for the +NSOST/+NSOSTF commands.
* If a message cannot be sent because of communication issues between the module and eNB, the module will attempt to send the message a second time. If this fails, the message will be dropped. As +NSOST/+NSOSTF messages are UDP, there is no indication the message has been dropped.
* The UDP header is about 48-60 bytes in length, and so an application sending 100 bytes will actually send about 160 bytes. For devices in the extreme coverage class 2, this can be quite costly.
* The UE device may later resume the RRC Connected state with that context, thus avoiding the AS setup and saving considerable signaling overhead for the transmission of infrequent small data packets.

## Application Architecture

* ![1569744612309](../images/1569744612309.png)
* At the far left the customer’s device contains a u-blox NB-IoT module that communicates over the radio network with a cell tower that supports the NB-IoT network. The cellular network links the cell tower with an IoT platform. This IoT platform stores uplink datagrams from the NB-IoT module. The customer server communicates with the IoT platform to retrieve uplink datagrams and to send downlink datagrams to the NB-IoT. The IoT platform holds downlink datagrams until the NB-IoT module is awake to receive them.
* The SARA-N2 series modules implement basic UDP socket commands for directly communicating with an external service. With these commands the customer can build a simple IoT platform. With an external processor other IoT layers could be implemented to aid this system design. SARA-N2 series modules support AT commands for general CoAP messaging. This allows the customer to not require CoAP in their external processor.
* Many developers coming from a GPRS type background may expect an always on type connection, normally using TCP. NB-IoT is not session oriented, latencies are much higher and the device will enter a power save mode. This is very different to always-on modems with “chatty” protocols like TCP.
* UDP sockets do not create connections to servers; UDP is a connection-less datagram protocol. Because of this MO messages may not be received by the server and lost. The application should take this in to consideration and provide its own acknowledgements between the UE device and server. CoAP is one protocol which can be used on top of UDP to provide this.
* For resolving the issue of sending MT messages to a very sleepy module, when a MO message is sent to the cloud server, the cloud server will know the module is active and connected to the network. As seen in section 7 the connection is alive until the RRC connection is released by the network and then still contactable when paging inside the T3324 period. If there are MT messages to be sent to the module, the cloud server should send this message in this time.

## Use cases

Use cases suitable for NB-IoT

## Martinez

Martinez et al. [@Martinez2019] did empirical tests within the Vodafone Network in Barcelona. They observed UE device and NW behavior, measured current traces, and did various tests in different modes.

Table: NW Config {#tbl:nw_config}

| Mode       | NW Configuration                                             |
| ---------- | ------------------------------------------------------------ |
| **Mode 1** | Inactivity timer = 20s (network default)<br/>T3324 = 0s (disabled)<br/>C-DRX = 2.048s (network default) |
| **Mode 2** | Inactivity timer = Immediate Release<br/>T3324 = 8s<br/>I-DRX = 2.56s<br/>eDRX/PTW = Disabled |
| **Mode 3** | Inactivity timer = Immediate Release<br/>T3324 = 0s (disabled) |

* performance bounds
* empirical

## Notes

**MTN Lab / 14th Ave Phase 3: Test Plant**

NB-IoT PoC MTN South Africa (Ericsson RAN Connectivity Tests only) [@Ssengonzi2017]

Industrial north Drive Test Requirements [@NorthDrive2017]

**Stellenbosch**

Evaluation of next-generation low-power communication technologies to replace GSM in IoT-applications [@Thomas2018]

**Manufacturers**

Ublox has an NB-IoT Application Development Guide [@ubloxAppNote2018] which details many of the capabilities of the UE.


