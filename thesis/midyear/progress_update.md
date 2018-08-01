---
title: Progress Report
author:
- Daniel Robinson
- Prof MJ Booysen
date: July 2018
tags: [LTE, wearables, healthcare, safety, critical, life-threatening, SDR, NB-IoT, Dash7, localization]

toc: true
lof: false
lot: false
link-citations: true
csl: ieee.csl
linkcolor: blue
---

\vspace{10 mm}

# Overview

## Title

**Hybrid P2P NB-IoT::LoRa::Dash7 WAGL Emergency Response wearable.**

## Objectives

A Peer-to-peer, Narrow-band Internet-of-Things, Long-Range Radio, Dash7 alliance, Wide-Area-Guided-Location Emergency Response wearable is being designed.

Upon the quest of finding the ultimate IoT solution for emergency response, an idea was borne which uses peer-to-peer networking and a suitable long-range LPWAN. Fast localization is key, along with the capability of sending critical physiological signals. A final practical PoC will be worn and tested in the form of either a LoRa or NB-IoT based system, both with Dash7 wireless P2P networking, land-based localization and A-GPS. The two comparable systems also aid the licensed vs unlicensed LPWAN debate. The P2P network is most useful in WAGL mode which guides a responder directly to the wearer, besides the ability to operate independently from gateways in constrained cases.

## Introduction

Since efforts in localization typically use GPS/GNSS, weak or no satellite signal creates a compelling case for guiding a responder to the distressed user.

Adding P2P capabilities adds decentralization to the centralized nature of the system, bringing the best of both worlds into a hybrid.

Decentralized networks can reach centralized ones by multi-hops. Using a self-healing system of updating nodes that haven't reached a centralized gateway, one can make sure that messages get through as soon as possible.

There are efforts in industry to combine these technologies into SoCs. Having a hybrid system ready like this can be ideal to harness the power of these future SoCs.

This solution if taken up seriously (funding) can add peace of mind and alleviate crime starting in small towns.

## Scope

Ideally, the more features, the better. For the purposes of clarity, the scope of the project will remain mostly in the region of LPWAN technologies. Nevertheless, it is interesting to note that piezoelectric and thermal energy harvesting can be used, besides solar. There are existing GSM + GNSS solutions in the market today which provide satisfactory performance, but the techniques can be considered archaic and not future-proof.

# Work Completed

I've done some preliminary testing on GNSS, NB-IoT, LTE Cat-M, EC-GSM, LoRa, SigFox and Dash7 of which all work successfully.

![GNSS testing](C:\GIT\trucker\images\j_mapoutput.JPG)

IMU data proves promising in the use of dead reckoning.

# Remaining Work

## Prototype

An experimental prototype is currently under development, and needs to work robustly. It has all these technologies in one, making it ideal to evaluate in field tests.

## Localization

Besides the use of GNSS, a hand-held directional finder needs to be developed which pinpoints the location of users in decentralized circumstances.

## Field Trials and Data processing

Rigorous testing and analysis needs to be done.

## Final devices

The final devices need the ability to be worn by users, and to prove that the concept works successfully.
