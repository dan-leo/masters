# MTN Yearly Presentations

Good morning everyone. My name is Daniel Robinson. Am currently studying for a masters degree at Stellenbosch University.

## Background

South Africa has vulnerable people subject to crimes, theft and accidents. There's great potential to solve problems in that sector.

*Tell brief story about Hannah Cornelius who was kidnapped, raped, murdered. Also about the safety app Namola which sends your location immediately and gets you in touch with a control centre in seconds.* This is great, but in the case of cellphone theft, or a stressful situation, there may not even be time to do that. Imagine a discrete wearable which can sense the heightened heart rate and is trained for these situations. It's inspiring, but I'm not sure if I'll reach that point yet. At least there are a myriad of things wearables can do for us in future, and that I can look into.

## Objectives

I'm specifically looking at heart rate, respiration and fall-sensing. Each of these can generate a critical event which is crucial to reach an emergency response centre. The data will help determine if a dispatch is necessary.

We'd need a wireless technology to send / receive signals. There are a couple in the licensed and unlicensed frequency bands. And they usually have many use cases.

### Use Cases

- Smart city devices and meters
- Asset tracking
- Agriculture
- Health care
- Safety & security
- Automotive & logistics
- Manufacturing
- Smart city
- Energy & Utilities
- Smart home & Retail

Essentially, I'll make a wearable that assists vulnerable people in SA. Fall-sensing, pedestrians in trouble.

Thomas Durand has done some great research for MTN and Stellenbosch University on different LPWAN technologies in South Africa, incl NB-IoT.

I hope to further that research by successfully proving the use case for NB-IoT in wearable devices. It is also a fulfilling field, as one makes a direct difference in people's lives.

Wearables have strict metrics that are not easy to satisfy, as all components have to be discrete. The greatest losses result from small antenna and battery size.

This use case overlaps with asset tracking, healthcare and safety & security. If successful, it can provide yet another incentive for cellular carriers in SA to roll out this technology, and/or commercialization.

Nevertheless a generic point of view that considers the other use cases will help to customize the technology for many of the 455 public enterprises in SA.

### Requirements

Doesn't need FOTA updates, but downlink packets are useful for orbital information like ephemerides and the almanac for satellite tracking.

Doesn't have to be cheaper than currently on the market, but prove that it can be. For example, the Apple Watch uses LTE and costs $300.

The scope of the project is within South Africa. Consider commercialization. 

Measure and analyze metrics. 

Look for alternative land-based forms of tracking including TOF, AOA, RSSI trilateration especially when inside buildings or places without satellite line-of-sight.

### Prototype

Proof of concept. First version will test wireless technologies and various sensors.

## Method

### Wireless technologies

I am looking at a few of the main wireless technologies out there.

2G/GSM is a sunsetting technology with great coverage and market penetration in SA. It certainly gathers a large share of revenue by calls and SMS.

When looking at SigFox, we see a technology with far range, but data rates that could be considered too low for our application. LoRa has higher data rates, but is still subject to duty cycle limitations. Dash7 is a full-stack medium range wireless technology that overcomes many of the limitations, including the duty cycle by having listen-before-talk and adaptive data rates.

NB-IoT is a very promising technology. It can coexist with 2G/GSM and LTE networks. When comparing to 2G it has 7 times greater range, and in power saving modes time to transmission is a few seconds, compared to about a minute for 2G. There are a few successful use cases for NB-IoT in South Africa, such as smart metering, asset tracking etc.

There are also a couple of hurdles in the way. Although lauded as a mere software upgrade, it does require the latest basestations and licensing fees. There needs to be a substantial revenue model which ties in with demand.

## Progress

I've build a hardware prototype that tests the various wireless technologies. It is designed in a way that it is highly configurable.

I've looked at the current research in NB-IoT. There are only about a hundred IEEE papers, compared to thousands which make use of 2G/GSM. I think what I'm doing will benefit the research community.

## Demo

I have here a demo. As you can see on this dashboard, I am sending sensor data in real time via different wireless technologies.

## Plan remaining steps

Next step would be to add sensors, location tracking, metric measurement.

Battery-life optimization.

Specifically heartrate, respiration and fall-sensing.

## Final destination


Main focus is on NB-IoT. Nevertheless, I've been very interested in other technologies to compare.

I've build a prototype that includes various licensed and unlicensed wireless technologies. NB-IoT, LTE Cat-M, GPRS/EDGE, SigFox, LoRa, Dash7.

I envision a smaller scale device which will be thoroughly tested. It will answer many of the questions that industry is wondering about, as well.

(I'm still trying to figure out why there is not enough demand, but at least one of the reasons is because it is not mainstream enough yet. Hardware costs are not yet cheaper than 2G. It is projected to be half the price of 2G modems within a few years.)