---
title: Development of a wearable NB-IoT/LTE-M solution for critical health and safety reporting
author: Daniel Robinson
date: 31 March 2018
tags: [LTE, wearables, healthcare, safety, critical, life-threatening]
abstract: |
  This thesis aims to address current challenges in specific wireless wearable technology by using NB-IoT/LTE-M. Research and development will be geared towards senior citizens, children, hospital/clinic patients and vulnerable pedestrians. The device is intended to detect and report any of the following critical information using generic interfaces (I2C, digital IOs, UART, SPI): heart rate indicating health concerns, acceleration/jerk indicating falls or crashes, indoor localisation, body temperature, triggering of a panic button in case of emergency; whilst maintaining a discrete footprint. The solution will work in a similar way to the mobile phone app Namola, in which location info is sent to emergency responders. To conserve power, the transmission will be event-triggered, with optional infrequent polling from the server side. The idea would be to roll this out on a large scale, and for the application to choose one of the specific targets, e.g. only clinics, or only pedestrians.

toc: true
lof: false
lot: false
link-citations: true
csl: ieee.csl
---

Dedicated especially to the women who fear being out there in the wild streets alone.

# Literature Study

LTE Cat M1 and NB-IoT are two similar new technologies geared for the internet-of-things sector in the world. They occupy licensed spectrum in the cellular bands, which does mean that they're not free. However, one has the benefits of avoiding interference and a higher power throughput. There appears to be many applications which use networks such as GSM, Wifi, Bluetooth, ZigBee, etc, but not as many when it comes to LTE Cat M1/NB-IoT. In fact, quite often GSM is used for connectivity, and GPS for localization. In this paper, the plan is to improve on the commonly used GSM. The goal is to investigate the optimum feasibility/usage of LTE Cat M1/NB-IoT, and a single application will be developed as a case study. There is no merit to adding GPS to 'yet another project', unless it can be proved that it has great symbiosis with the proposed technologies. What is more interesting is what kind of localization one can achieve. There are basically two categories of indoor localization: model-based and fingerprinting-based. Model based uses geometrics relative to several known anchors, like RSSI, OTDoA and AOA which are more suitable in the line-of-sight (LOS). Of the fingerprinting approach, two algorithms emerge namely predictive and deterministic, which are more suited to multipath propagation in non line-of-sight (NLOS) environments. CSI fingerprinting is a pre-processing technique, but much better than the easiest and most common form -- RSSI trilateration. 

(insert (spider) diagram comparing network technologies weighted by coverage, throughput etc.)

NB-IoT is on par with SigFox in terms of coverage (no outage at 20 dBm indoor penetration loss), except that it has higher indoor penetration (8% outage at 30 dBm indoor penetration loss vs 13% and 20% for SigFox and LoRa respectively) and bandwidth [@Lauridsen2017]. It has a maximum-coupling-loss (MCL) of 164 dBm. Because it is a licensed frequency, it significantly exceeds LoRa's population coverage when it comes to rural and deep indoor areas [@Persia2017]. Current NB-IoT modules do not meet the battery lifetime target[^longevity_target] although several optimizations are recommended by [@Yeoh2018a].

It can be a rather utopian idea that there will be worldwide coverage of a LPWAN. 

[^longevity_target]: 10 years

## Localization

In the case of LoRaWAN, current hardware and software implementations limit timestamp resolution of time-of-flight (ToF) and time-difference-of-arrival (TDoA) schemes to 1 µsec, which limits localization accuracy to worse than 300 m [@Dongare2017].

There are a number of localized applications beneficial to health and safety. A GPS solar powered GSM wearable which monitors autism in children is proposed in [@Ahmed2017c], but lacks details on extending battery life, coverage etc. A thorough investigation in elderly assistance, including fall detection (also in @Chavan2017a), heartrate and movement activity, is proposed in [@Bizjak2017a].

PPG sensor to detect heart attacks as in [@Valliappan2017], also uses GSM. ZigBee to base station monitors chronic diseases for elderly patients [@Jian2010]. Vital signs are monitored and sent via bluetooth in [@Wu2008a], [@Kale2017a], [@Rathi2017] and in the form of jewellery in [@Patel2018].

Kalman filters in [@Wu2016]. Sarsat 406 MHz life jacket in [@Serra2011]. GSM and GPS Telemedicine in [@Suganthi.2012a] and [@Tewary2016b]. 

Autonomous emergency bracelet for women proposed in [@Harikiran2016]. 

NB-FI seems like an interesting UNB alternative to SigFox as it's bi-directional. There's a nice range calculator on http://waviot.com/technology/what-is-nb-fi. The main market of NB-Fi is the US and Russia where duty-cycle doesn't apply as in https://www.thethingsnetwork.org/forum/t/waviot-nb-fi-protocol-and-the-radio-transciever/5151.

## Table

| Paper           | Objective                                                    | Method                                                       | Result                                       | Challenges                                                   |
| --------------- | ------------------------------------------------------------ | ------------------------------------------------------------ | -------------------------------------------- | ------------------------------------------------------------ |
| @Ahmed2017c     | Localization and monitoring of children with **autism**.     | **Hat / cap.** Threshold alerts. GSM / GPS                   | None / unclear                               | Solar                                                        |
| @Bizjak2017a    | Elderly assistance                                           | **Smartwatch.** Survey. GSM. Wifi. GPS.                      | Of risks, fear falls and accidents the most. | Waterproofing                                                |
| @Valliappan2017 | Elderly heart patient monitoring                             | **Headset.** Cheap arduino parts. 433 MHz. GPS. SMS (GSM)    | Not 100% accurate.                           | Accuracy. Measuring all cardiovascular diseases.             |
| @Jian2010       |                                                              | Zigbee.                                                      |                                              |                                                              |
| @Sierra2017     | Follow up on January tests amongst industry players. Point out deep coverage conditions at 164 MCL with at least 160 bps. | Device waking up from Power Saving Mode (PSM) using the Radio Resource Control (RRC) Resume procedure to resume a suspended RRC connection.Message sequence |                                              | Congestion on network delaying response to protocol control messages from the device. Often 50 ms for commercially deployed networks.Time for modem to boot up (hundreds of milliseconds) |
| @LinkLabs2016   | Comprehensive look at LPWAN technologies                     | LPWAN use cases, 9 fundamental concepts, 5 main technologies. | Pros and Cons.                               | Revolutionary -- monitor and control devices more economically than before. More investment in future. |
| @Ratasuk2016    | Targets and preliminary system design                        | Coverage, capacity, latency, battery life analysis           |                                              |                                                              |
| @Doherty2018    | Digital Doherty power amplifier proposed                     | Parallel-combining-transformer for dual-band coverage        |                                              | PA to be efficient not only at peak power but also at power back-off (PBO) to extend battery life. |
|                 |                                                              |                                                              |                                              |                                                              |
|                 |                                                              |                                                              |                                              |                                                              |

When measuring differential temperature variations, if spikes in temperature variation were suppressed, one could use a rolling average instead.



# System Overview


# Testing

NB-IoT downloading was tested  on the Sierra Wireless 7702 using the following script.

```bash
while [ 1 ]; do	
    # wget --retry-connrefused --waitretry=1 
    # 	--read-timeout=20 --timeout=15 -t 0 --continue
    wget -t 0 -c http://speedtest.ftp.otenet.gr/files/test100k.db
    # check return value, break if not successful (0)
    if [ $? != 0 ]; then break; fi;
    sleep 1s;
done;
```

A 100 kb file is downloaded at a rate of around 3kB/s. The script continues download if stalled or other errors occur. Since it is a `Yocto` installation[^yocto], the other `wget` arguments were not available.

[^yocto]: It's not an embedded solution. Rather, it creates a custom one for you, regardless of hardware architecture [@yocto1]. 

After many failed attempts with the Ublox N200 version 01B and 02B on the ZTE eNodeB in Stellenbosch, not a single log was reported by Tektronix' NSA (Network & Service Analyzer / Network Spectrum Analyzer / Non-Standalone) Protocol Analyzer when attempting to register manually with the eNodeB's standalone NB-IoT cell.

There is an interesting problem where only one of the two sims provisioned for the B06009 eNodeB / Test Plant will register to MTN (65510). According to Michael, the one sim is probably out of the IMSI range. (NSA shows `network registration failed`)

The Sierra Wireless 7702 has a Qualcomm 9206 modem which supports LTE Cat M1, NB1 and EC-GSM.

Whenever any node in the network like UE/SGW/PGW fails to respond back for any of the request messages sent by MME, then MME will be rejecting the attach procedure with cause "network failure" after maximum retries of the request message.

When Mubanga Nsofu (from Qualcomm, sent by Arun Handoo and Hardik Shah) came in this morning, he connected the DM Port of the Sierra Wireless 7702 which has a Qualcomm 9206 modem to QPST which acts as an intermediary for QXDM. We were able to decode all RF logs. Strangely, the modem didn't want to connect to in-band NB-IoT this morning, but we could tell through the logs that it registers 5 times before being rejected by the MME (rejection cause 17: “Network failure” [(Causes related to PLMN specific network failures and congestion / Authentication Failures) This cause is sent to the MS if the MSC cannot service an MS generated request because of PLMN failures, e.g. problems in MAP](https://stupidcaterpillar.wordpress.com/2011/07/20/cause-codes-from-network/)), and thus attempting via GSM as a fallback (which did still work).

His time was limited, so we left it at that, but he will be in Phase 1 tomorrow, and we can now do the tests properly. For example, attach latency under different conditions, cell-selection vs **re**selection etc.  NB-IoT (standalone, in-band), Cat M1 and GSM all still work again, since Michael and I reset the cells on the eNodeB.

Anyway, it would be nice to get cell-**re**selection working between NB1, M1 and GSM by adding `pr relationships` between neighbouring cells. Michael is trying to get some info from Ericsson, because he didn't find what he was looking for in the docs.

So far, cell-selection seems to work between NB1 in-band @953.36MHz and stand-alone @953.41MHz. It only takes about 10 seconds to switch between cells. There is also a little bit of interference there, which is noticeable when the ping tests stop at around -63dBm. I do struggle to get even just cell-selection to work between NB1 (in either mode), Cat M1 and GSM. According to Phillip New from Sierra Wireless, it does work. But I still think it's UE side problems. Furthermore, cell-**re**selection would be awesome on the live network, considering the dynamic localization use-case for my masters.

The eNodeB can read RF logs, but as Michael says, it crashes the server whenever they try to get it working (and this for the last few months). So yes, I will meet with Mubanga again tomorrow, and do some more tests, as well as seeing what is the problem when it comes to at least cell-selection.

P3 Communications https://mybroadband.co.za/news/broadband/250759-confirmed-mtn-has-the-best-network-in-south-africa.html

Nice https://mybroadband.co.za/news/cellular/255991-how-mtn-became-the-best-network-in-south-africa.html

ICASA is crap https://mybroadband.co.za/news/broadcasting/256005-icasa-looking-to-move-digital-radio-forward-in-south-africa.html

end-2016, Vodacom was best. http://www.vodacom.com/news-article.php?articleID=4338

The QXDM Professional software is also known as the Qualcomm eXtensible Diagnostic Monitor. It is a utility for those who have devices using Qualcomm ASICs and trial hardware, and allows them to test, evaluate and potentially diagnose issues in the RF performance of their mobile devices. It is often used in order to facilitate product development of these devices.

Using the software, users can see all the signaling messages made by their mobile devices, as the software generates a log of them. These logs can be annotated through the software as well. Any mix of network and phone parameters can be added to the screens, and users are allowed to use complex formulae when working with their parameters. Myriad statistical data is also generated by the program in real-time so that users can better identify potential performance issues. Users can access Markov statistics, Mux statistics, RLP statistics, the block error rate, mobility management data, paging and access statistics, forward and reverse link statistics, and more. The program also gives users a graphic display of the portable device’s signals. The program is compatible with Windows operating systems.





![3gpp-standards-for-the-internetofthings-6-1024](C:\Users\d7rob\MEng\3gpp-standards-for-the-internetofthings-6-1024.jpg)

# Internal doc

## Ideas

Ryan spoke to me. We had a great discussion. I need to paint my mind on a whiteboard, but for now I'll type here. NB-IoT not so good for emergency response. Better for monitoring. There are so many other things I can do, though. But in the end it's all about just passing the masters hey. So I do have a bunch of inside information, which could potentially be to my advantage. I'm stuck at a crossroads 3 months early says Ryan. He's looking at virtualization / SDN of MTN and 5G etc by 2022.

80 references.



## Title ideas

* Investigation into the effectiveness of NB-IoT as an emergency response wearable
  * Localization
  * Battery life
  * Global reach
  * Base station complexities
  * rel13 vs rel14
  * This is basically very much based on just NB-IoT and **all** it's features and limitations. How interesting is that really? Not unless I can extract something very useful out of it. Right?

*  Energy-efficiency optimization of LTE NB-IoT.
  * Current usage
  * Simulations
  * On-chip development
  * SDR
  * proprietary
  * fokkit

* Investigating the development of a life-saving wearable.
* Cat-M truck tyre.
* NB-IoT pedestrian safety device. fuckin' yeah. 

## Papers (to be processed)

## Secondary Research formation

### Bigger picture
~~~mermaid
graph LR
IoT --> Wireless-Networks
IoT --> Applications
Wireless-Networks --> LPWAN
Wireless-Networks --> Wifi
Wireless-Networks --> Bluetooth
Wireless-Networks --> ZigBee
Applications --> Monitoring
Monitoring --> Localization
Monitoring --> Physiological-signals
Monitoring --> Dead-reckoning
LPWAN --> GSM
GSM -- GSM Discontinued--> EC-GSM
LPWAN --> UNB
UNB --> SigFox
UNB --> NB-Fi
LPWAN --> LoRa
LPWAN --> Satellite
LPWAN --> Comparisons/survey
LPWAN --> LTE
LTE --> Cat-M
LTE --> NB-IoT
M2M-system --> NB-IoT
SDR --> NB-IoT
LPWAN --> Localization
Fields --> IoT
Fields --> Medical
Fields --> Industrial
Fields --> Educational
Fields --> g
IoT --> Smart-Grid/Cities
Smart-Grid/Cities --> Vehicle/Parking
Applications --> Vehicle/Parking
Localization -- Inter-cell-reselection --> Mobility
Localization --> CSI-fingerprinting
Localization --> RSSI-trilateration
Localization --> GPS/GNSS
Primary-Research --> Secondary-Research
~~~

~~~mermaid
graph LR

Everybody --> GV
GV --> Twilio
Twilio --> South_Africa
GVCallback --> GV
GV --> Everybody
South_Africa --> GVCallback
~~~



### NB-IoT

~~~mermaid
graph LR
NB-IoT --> Group-comms
NB-IoT --> Evaluation/analysis/overview/simulation
NB-IoT --> Performance
NB-IoT --> Optimization
NB-IoT --> Present
NB-IoT --> Future
NB-IoT --> Localization
Localization --> Mobility
Localization --> NPRS
Performance --> Energy-efficiency
Performance --> RF
RF --> Co-existence
RF --> Band
Performance --> Throughput
Performance --> Coverage
Performance --> Capacity
Performance --> Deployment
Performance --> Power
Optimization --> Data
Optimization --> Battery
Present -- 3GPP --> Rel13
Future -- 3GPP --> Rel14
Rel14 --> Rel15
Rel14 --> NPRS
Rel15 --> 5G
Rel14 --> Mobility
~~~

## Thoughts 

I'm still not sure what topic I'd like to investigate regarding NB-IoT. I like embedded development. My idea at the moment is to research and develop a localized wearable for emergency response purposes using LTE-NB2 or LTE-Cat-M2. It could potentially measure physiological signals such as heartrate and respiration, and/or dead reckoning using 9-axis measurements etc. But it feels more like an application that people out in business / in the field can do i.e. it doesn't feel very academic? I'd like something within Secondary research, not Primary, and not an application as it seems that I'm leaning towards. There is NB-IoT coverage in the area, and release 14 (NB2/M2) will be tested soon within a month or two. Release 13 (NB1/M1) is currently in place, which doesn't really allow for mobility / cell reselection.



# Appendix

## Applications

~~~mermaid
graph LR

Healthcare --> Sleep-Apnea-Monitoring
Healthcare --> Glucose-Monitoring
Healthcare --> AED-Monitoring
Healthcare --> Patient-Monitoring
Healthcare --> PERS/mPERS
Healthcare --> Sport-&-Fitness

Automotive --> TCU
Automotive --> Head-Unit
Automotive --> Smart-Antenna
Automotive --> Connected-Gateway
Automotive --> Commercial-Vehicle-TCU

Transport --> UBI
Transport --> Stolen-Vehicle-Tracking
Transport --> Toll-Collection
Transport --> Fleet-Management
Transport --> Railway
Transport --> Transit
Transport --> Container-Tracking
Transport --> Aviation

Public-Safety --> Police
Public-Safety --> Fire
Public-Safety --> Ambulance

Energy --> Smart-Meter
Smart-Meter --> Electricity
Smart-Meter --> Gas
Smart-Meter --> Water
Energy --> Smart-Grid
Smart-Grid --> Generation
Smart-Grid  --> Transformer
Smart-Grid  --> IED:Cap,Bank,etc

Industrial-&-Infrastructure --> Industrial-Heavy-Equipment
Industrial-&-Infrastructure --> Industrial-Gateway
Industrial-&-Infrastructure --> Tank-Monitoring
Industrial-&-Infrastructure --> Drones/UAV/UAS/Robot
Industrial-&-Infrastructure --> Factory-Automation
Industrial-&-Infrastructure --> Industrial-Equipment
Industrial-&-Infrastructure --> Infra
Infra --> EV-Charging-station
Infra --> Traffic-light
Infra --> Waste-Management
Infra --> Pipeline-Management
Infra --> Public-Lighting
Infra --> Video-Surveillance
Infra --> Parking-Management
Infra --> Infrastructure

Field-service-&-Logistics --> Personel-Tracking/Monitoring
Field-service-&-Logistics --> Offender-Tracking
Field-service-&-Logistics --> Goods-Tracking
Field-service-&-Logistics --> Tracking-&-Logistics

Mobile-Computing --> Laptop
Mobile-Computing --> Tablet
Mobile-Computing --> Rugged-Laptop/Tablet

Networking-Gateways-and-Routers --> Network-failover
Networking-Gateways-and-Routers --> Routers
Networking-Gateways-and-Routers --> Enterprise-Gateway

Sales-&-Payment --> POS
Sales-&-Payment --> Cashier
Sales-&-Payment --> Vending/Kiosks/Ticketing
Sales-&-Payment --> ATM
Sales-&-Payment --> Footfall-measurement
Sales-&-Payment --> Digital-Signage
Sales-&-Payment --> Retail

Wearables --> Camera
Wearables --> Kid/Pet-tracker
Wearables --> Appliances
Wearables --> Consumer

Home-&-Security --> Alarm
Home-&-Security --> Gateway
Home-&-Security --> Home-Automation
Home-&-Security --> Set-box
Home-&-Security --> Home

~~~

```mermaid
graph LR
A[Square Rect] -- Link text --> B((Circle))
A --> C(Round Rect)
B --> D{Rhombus}
C --> D
```


\newpage

---

# References
