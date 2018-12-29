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

# Literature Study

LTE Cat M1 and NB-IoT are two similar new technologies geared for the internet-of-things sector in the world. They occupy licensed spectrum in the cellular bands, which does mean that they're not free. However, one has the benefits of avoiding interference and a higher power throughput. There appears to be many applications which use networks such as GSM, Wifi, Bluetooth, ZigBee, etc, but not as many when it comes to LTE Cat M1/NB-IoT. In fact, quite often GSM is used for connectivity, and GPS for localization. In this paper, the plan is to improve on the commonly used GSM. The goal is to investigate the optimum feasibility/usage of LTE Cat M1/NB-IoT, and a single application will be developed as a case study. There is no merit to adding GPS to 'yet another project', unless it can be proved that it has great symbiosis with the proposed technologies. What is more interesting is what kind of localization one can achieve. There are basically two categories of indoor localization: model-based and fingerprinting-based. Model based uses geometrics relative to several known anchors, like RSSI, OTDoA and AOA which are more suitable in the line-of-sight (LOS). Of the fingerprinting approach, two algorithms emerge namely predictive and deterministic, which are more suited to multipath propagation in non line-of-sight (NLOS) environments. CSI fingerprinting is a pre-processing technique, but much better than the easiest and most common form -- RSSI trilateration. 

(insert (spider) diagram comparing network technologies weighted by coverage, throughput etc.)

NB-IoT is on par with SigFox in terms of coverage (no outage at 20 dBm indoor penetration loss), except that it has higher indoor penetration (8% outage at 30 dBm indoor penetration loss vs 13% and 20% for SigFox and LoRa respectively) and bandwidth [@Lauridsen2017]. It has a maximum-coupling-loss (MCL) of 164 dBm. Because it is a licensed frequency, it significantly exceeds LoRa's population coverage when it comes to rural and deep indoor areas [@Persia2017]. Current NB-IoT modules do not meet the battery lifetime target[^longevity_target] although several optimizations are recommended by [@Yeoh2018a].

[^longevity_target]: 10 years

## Localization

In the case of LoRaWAN, current hardware and software implementations limit timestamp resolution of time-of-flight (ToF) and time-difference-of-arrival (TDoA) schemes to 1 µsec, which limits localization accuracy to worse than 300 m [@Dongare2017].

There are a number of localized applications beneficial to health and safety. A GPS solar powered GSM wearable which monitors autism in children is proposed in [@Ahmed2017c], but lacks details on extending battery life, coverage etc. A thorough investigation in elderly assistance, including fall detection (also in @Chavan2017a), heartrate and movement activity, is proposed in [@Bizjak2017a].

PPG sensor to detect heart attacks as in [@Valliappan2017], also uses GSM. ZigBee to base station monitors chronic diseases for elderly patients [@Jian2010]. Vital signs are monitored and sent via bluetooth in [@Wu2008a], [@Kale2017a], [@Rathi2017] and in the form of jewellery in [@Patel2018].

Kalman filters in [@Wu2016]. Sarsat 406 MHz life jacket in [@Serra2011]. GSM and GPS Telemedicine in [@Suganthi.2012a] and [@Tewary2016b]. 

Autonomous emergency bracelet for women proposed in [@Harikiran2016]. 



| Paper           | Objective                                                | Method                                                    | Result                                       | Challenges                                       |
| --------------- | -------------------------------------------------------- | --------------------------------------------------------- | -------------------------------------------- | ------------------------------------------------ |
| @Ahmed2017c     | Localization and monitoring of children with **autism**. | **Hat / cap.** Threshold alerts. GSM / GPS                | None / unclear                               | Solar                                            |
| @Bizjak2017a    | Elderly assistance                                       | **Smartwatch.** Survey. GSM. Wifi. GPS.                   | Of risks, fear falls and accidents the most. | Waterproofing                                    |
| @Valliappan2017 | Elderly heart patient monitoring                         | **Headset.** Cheap arduino parts. 433 MHz. GPS. SMS (GSM) | Not 100% accurate.                           | Accuracy. Measuring all cardiovascular diseases. |
| @Jian2010       |                                                          | Zigbee.                                                   |                                              |                                                  |
|                 |                                                          |                                                           |                                              |                                                  |
|                 |                                                          |                                                           |                                              |                                                  |

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

![3gpp-standards-for-the-internetofthings-6-1024](C:\Users\d7rob\MEng\3gpp-standards-for-the-internetofthings-6-1024.jpg)

# Appendix

## Applications

\noindent\hspace*{\fill} 
\begin{tikzpicture}[mindmap, grow cyclic, every node/.style=concept, concept color=orange!40, 
​    level 1/.append style={level distance=5cm,sibling angle=60},
​    level 2/.append style={level distance=3cm,sibling angle=30},]
\node{Primary Applications}
   child { node {Healthcare}
​        child { node {Sleep Apnea Monitoring}}
​        child { node {Glucose Monitoring}}
​        child { node {AED Monitoring}}
​        child { node {Patient Monitoring}}
​        child { node {PERS/mPERS}}
​        child { node {Sport \& Fitness}}
​    }
​    child { node {Automotive}
​        child { node {TCU}}
​        child { node {Head Unit}}
​        child { node {Smart Antenna}}
​        child { node {Connected Gateway}}
​        child { node {Commercial Vehicle TCU}}
​    }
​    child { node {Transport}
​        child { node {UBI}}
​        child { node {Stolen Vehicle Tracking}}
​        child { node {Toll Collection}}
​        child { node {Fleet Management}}
​        child { node {Railway}}
​        child { node {Transit}}
​        child { node {Container Tracking}}
​        child { node {Aviation}}
​    }
​    child { node {Public Safety}
​        child { node {Police}}
​        child { node {Fire}}
​        child { node {Ambulance}}
​    }
​    child { node {Energy}
​        child { node {Smart Meter - Electricity}}
​        child { node {Smart Meter - Gas}}
​        child { node {Smart Meter - Water}}
​        child { node {Smart Grid  - Generation}}
​        child { node {Smart Grid  - Transformer}}
​        child { node {Smart Grid  - IED (Cap, Bank, etc)}}
​    }
​    child { node {Home \& Security}
​        child { node {Alarm}}
​        child { node {Gateway}}
​        child { node {Home Automation}}
​        child { node {Set-box}}
​    };

\end{tikzpicture}
\hspace{\fill}

\centering
\begin{tikzpicture}[mindmap, grow cyclic, every node/.style=concept, concept color=orange!40, 
​    level 1/.append style={level distance=5cm,sibling angle=60},
​    level 2/.append style={level distance=3cm,sibling angle=30},]

\node{Secondary Applications}
​    child { node {Industrial \& Infrastructure}
​        child { node {Industrial Heavy Equipment}}
​        child { node {Industrial Gateway}}
​        child { node {Tank Monitoring}}
​        child { node {Drones/UAV/UAS/Robot}}
​        child { node {Factory Automation}}
​        child { node {Industrial Equipment - Other}}
​        child { node {Infra - EV Charging Station}}
​        child { node {Infra - Traffic Light}}
​        child { node {Infra - Waste Management}}
​        child { node {Infra - Pipeline Management}}
​        child { node {Infra - Public Lighting}}
​        child { node {Infra - Video Surveillance}}
​        child { node {Infra - Parking Management}}
​        child { node {Building HVAC}}
​        child { node {Building Elevator Monitoring}}
​        child { node {Building Automation}}
​        child { node {Agriculture - Precision Planting}}
​        child { node {Agriculture - Soil Monitoring}}
​        child { node {Agriculture - Animal Tracking}}
​    }
​    child { node {Mobile Computing}
​        child { node {Laptop}}
​        child { node {Tablet}}
​        child { node {Rugged Laptop or Tablet}}
​    }
​    child { node {Field Service \& Logistics}
​        child { node {Handheld - Bar Code Scanner}}
​        child { node {Handheld - Public Safety}}
​        child { node {Personel Tracking / Monitoring}}
​        child { node {Offender Tracking}}
​        child { node {Goods tracking}}
​        child { node {Tracking \& Logistics - Other}}
​    }
​    child { node {Sales \& Payment}
​        child { node {POS}}
​        child { node {Cashier}}
​        child { node {Vending / Kiosks / Ticketing}}
​        child { node {ATM}}
​        child { node {Footfall Measurement}}
​        child { node {Digital Signage}}
​        child { node {Retail}}
​    }
​    child { node {Networking}
​        child { node {Network Failover}}
​        child { node {Routers}}
​        child { node {Enterprise Gateway}}
​    }
​    child { node {Consumer}
​        child { node {Camera}}
​        child { node {Kid / Pet Tracker}}
​        child { node {Wearables}}
​        child { node {Appliances}}
​    };
\end{tikzpicture}
\par


\newpage

---

# References

