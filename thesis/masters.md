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
---

# Literature Study

NB-IoT is on par with SigFox in terms of coverage, except that it has higher indoor penetration and bandwidth [@Lauridsen2017]. Because it is a licensed frequency, it significantly exceeds LoRa's population coverage when it comes to rural and deep indoor areas [@Persia2017]. Current NB-IoT modules do not meet the battery lifetime target[^longevity_target] although several optimizations are recommended by [@Yeoh2018a]. 

## Localization

In the case of LoRaWAN, current hardware and software implementations limit timestamp resolution of time-of-flight (ToF) and time-difference-of-arrival (TDoA) schemes to 1 µsec, which limits localization accuracy to worse than 300 m [@Dongare2017].





ref [Literature Study]

aefaed

[^longevity_target]: 10 years

---

## References
