## Intro

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

## Lit study

- ‘Paints a picture’ of what is currently known about the research question and what has been written on it by experts and scholars.
- Is an in-depth analysis of the literature:
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