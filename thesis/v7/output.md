# Keywords

- IoMT
- Localization
- Bidirectionality
- Cellular IoT
- NB-IoT
- LPWANs
- Dash7
- LoRa vs LoRaWAN
- Network stacks
- OSI model
- Geofencing
- Terrestrial vs satellite location
- Unidirectionality
- SigFox low data rate
- Indoor-Outdoor
- Vodacom, MTN
- South Africa
- Industry, Enterprise, Governments, Military, Consumers
- Nordic, Ublox, Quectel, Sierra Wireless, SimCom, Pycom
- Wizzilab, HayStack
- Stealth
- 5G
- Criticism
- P2P
- Real-time
- Security
- IoT data tsunami
- Push vs pull model



# Introduction

In terms of connectivity, smartphones fit well indoors and outdoors due to WiFi and LTE. Although LTE can has coverage in both, it is more suited for mobile use cases, and WiFi for more static ones. This can be attributed to our personal lifestyles. In smart / IoT devices we may require something similar, especially in localization. What if we had LTE NB-IoT and Dash?

Most of these devices are unidirectional and send data periodically or are event driven. But this can be quite taxing on battery life to periodically grab a GPS location. Arguably, end users only want to see where devices are on-demand, or when a device exits a boundary. Using bidirectional networks, one can tell the device that one wants to know where it is, and the device can listen for changes in signal strength to know that its position has changed sufficiently in relation to its gateway(s), thereby acquiring a GPS location.

There are many benefits to network bidirectionality, such as the ability to update parameters over the air, change geofence boundaries and pull data on-demand from end points.

This thesis aims to outline the benefits of network bidirectionality in localization for the IoT.

We live in an increasingly populated world driven by consumerism, with a huge shipping industry and a greater chance of things being misplaced, going missing, damaged or more.

A common saying in today's world is "there's an app for that". This implies that cellphones, which constitute a major part of augmenting our daily lives by us becoming instantly accessible in the form of calls, SMS, emails and instant messaging applications such as WhatsApp and Telegram, can do almost anything for us. Unfortunately, there are some limitations that are unavoidable, such as:

- size and weight due to high-powered cellular networks such as LTE.
- app incompatibilities and bugs
- daily battery life
- WiFi is low powered but short range

That's where the internet-of-things (IoT) and wearables come in. 



Typical wearable applications use Bluetooth paired with a cellphone. Fitness tracking ones by Garmin, Fitbit etcetera use it to synchronize data with the cloud and apps to show progress. Insurance companies have taken this a step further (such as Discovery Health in South Africa) to use this data to incentivize an active exercising lifestyle (in the form of vitality rewards[^vitality]), which lowers premiums and ultimately lowers risk for life insurance / medical aid claims. Virgin Active, for example, offers gym facilities to enable this active lifestyle. Bluetooth also offers convenience by not having wires in other accessories such as headphones, car radios, speakers, keyboards and mice.

[^vitality]: Vitality rewards offer a plethora of discounts in flight, hotel, car rental, fuel, food, entertainment and other lifestyle choices. 

Bluetooth had teething problems in the beginning, and although incompatibilities have been smoothed out over the years, one should still factor in the technological literacy of the general population. What seems intuitive to developers may not seem to others, and striving for a plug-and-play nature of a device is always the best ideal.

For this, one desires a truly standalone solution. In a city, Wifi or Bluetooth is too short range and does not have the seamless cell reselection capabilities as cellular networks have. Consider the LTE variant of the Apple watch for $500-800. It only has 18 hours of battery life, so it is essentially a cellphone on your wrist.

IoT typically uses GSM or LPWAN networks to connect endpoints to the internet. GSM is great for bi-directionality, especially in real-time applications as it is 'always-on' with constant synchronization on the physical RF layer between tower and endpoint. In battery-powered use cases, it is considered power hungry and takes approximately a minute to complete the network registration steps, packet switched context and tcp socket setup from modem boot. This is useful for data sent or received periodically. Unfortunately, it is also a sunsetting technology being switched off in certain countries around the world. Although, in SA it is still a great source of revenue for cellular service providers as many of the general population still use 'cheap' cellphones that can only call or SMS. LPWAN networks such as SigFox or LoRaWAN have great low battery usage, however are restricted by RF duty cycle limitations on the unlicensed frequency bands such as ISM that restrict the number of messages that can be sent per day. They can request a reply from the server, but most of the time the data transmission is unidirectional -- from endpoint to gateway. They can request a reply, but not passively listen for one from a gateway on demand. LoRaWAN also has low setup costs via the ability to install inexpensive public gateways with TTN (The Things Network). And SigFox has high range due to its ultra-narrow (carrier-phase) bandwidth.

![LTE variant of the Apple Watch Series 4](C:\GIT\masters\thesis\images\applewatch.JPG)

NB-IoT is the cellular-IoT response to LPWAN networks. It benefits from licensed frequencies which don't have restrictions on data throughput, except in monetary terms. Being bidirectional, it wins in localized and actuator control use cases. In localization, this is especially true in the case of assisted GPS/GNSS where sending ephemeral and almanac data from the internet via multi-cast to end points will enable a hot start of a few seconds as opposed to a few minutes. It saves precious battery life since GPS/GNSS broadcasts are sent from satellites at a rate of 50 bits per second. GPS/GNSS is becoming cheaper as time progresses, lowering the need for expensive TOF, TDoA, AoA (terrestrial localization) needs. NB-IoT is unique that it gains TDoA and AoA from a mere software upgrade of existing cellphone towers and eNodeBs, yet there are still licensing costs which can exceed a few million ZAR a year. With nationwide adoption from a demand in use cases, it becomes more viable for cellphone service providers to roll out coverage. NB-IoT touts that it is an easy software upgrade, but the current situation in South Africa with ICASA and licensing costs still make this expensive. Luckily it only requires one 200kHz channel out of many, and GSM/GPRS can be re-farmed to use it. Certainly less than the 1.4 MHz required by LTE-M. LTE-M does seem useful as well, yet it doesn't have as much range or power-saving capability as NB-IoT.

Another mysterious contender is Dash7. It has its origins in the ISO 18000-7 standard for active RFID, intended by the US Department of Defense for container inventory and grew to become a medium range bidirectional wireless network system [@Weyn2015] useful in the indoor-outdoor realm.

Proposed is also an idea to reuse the RF PHY layer of NB-IoT for Dash7's OSI stack, resulting in a compressed tracking solution that works well both indoors and outdoors. NB-IoT and satellite tracking for outdoors, and Dash7 with beacons for indoors.

## Problem statement

ToF, AoA, TDoA is becoming more expensive than satellite localization due to gateway costs, whilst the latter  is becoming cheaper. GPS/GNSS is the way to go, however current tracking devices are power inefficient due to the wireless network limitations that are disregarded. Requesting an ephemeral / almanac update periodically drains battery faster than having the data multi-casted to the endpoints.

NB-IoT and Dash7 seem most promising due to their directionality and medium to long range capabilities.

Thomas has done some general tests in LPWAN and NB-IoT. But the NB-IoT investigation is not deep enough to make a conclusive argument. According to him, the battery life is poor due to network-determined power saving factors. However, it is left up to the user.

How do we segment the kind of IoT that listens for messages from the internet? It's all very good to have one way transmissions, and LoRaWAN and SigFox seem sufficient.

NB-IoT seems to be an all-rounder for IoT.

What are the requirements for localized wearables and assets?

* Accuracy < 10m
* Cell reselection
* Mobility
* Indoor-outdoor coverage

Title ideas:

* NB-IoT in standalone bidirectional IoT and wearable applications
* NB-IoT and Dash7 for localized wearables

# Lit Study

## Patrick Burns

### Powerful statements

Dash7 bridges the gap between LPLAN and LPWAN.

OTA parameterization is underestimated.

IoMT is overlooked.

LoRaWAN is bad, even though Haystack supports a concurrent stack.

Wireless IoT technology deployments:

* Commercial and Industrial Networks
* Private Personal Networks
* Public Networks

### Snippets

https://medium.com/@patburns/announcing-haystacks-lorawan-replacement-program-1a72cb4cf201

LPWAN technologies operating in unlicensed radio spectrum will eventually dominate the enterprise and industrial IoT arena. Semtech is running at the front of the pack with LoRa. SigFox?

LoRaWAN is basically a one-way, barebones networking stack that enables tags to upload small bits of data to the cloud. It’s not secure, it doesn’t work in real-time, it’s expensive to maintain, and you can’t really send commands to a LoRa endpoint with it. Still, a few companies you’ve heard of appear to be trying it despite the risks.

- **Compatibility and co-existence with LoRaWAN**
- **Complete bi-directional communications vs. LoRaWAN one-way**
- **Real-time indoor location with up to one meter precision**
- **Over-the-air firmware updates for easier maintenance and better security**
- **Real-time endpoint queries and commands**
- **50% greater range vs. LoRaWAN**
- **200% greater system density vs. LoRaWAN**

So to sum things up, with Haystack your LoRa solution has much better range, costs less, is more secure, can do high-precision indoor location, and can still work with “legacy” LoRaWAN gateways.

Listen-before-talk operations

Anyone contemplating a LoRaWAN implementation is exposed to serious security risks.[http://bit.ly/2Lorasec](http://bit.ly/2Lorasec)

indoor location example, using node-to-node multilateration

LoRaWAN is not a serious IoT protocol.

Dash7 networking already supports all the requirements of the NB-IoT draft spec, and it is capable of providing LPWAN and LPLAN features to NB-IoT.

Supports real-time indoor location to 1 meter precision.



https://medium.com/@patburns/5-reasons-the-iphone-6-will-save-the-internet-of-things-7ac8b96fbd5

* NFC means Dash7 can communicate over it

https://medium.com/iotforall/why-you-can-t-google-the-internet-of-things-1f1207212a75

* Gartner's hype cycle 2014
* Today’s wireless IoT technologies spew too much data, can’t be queried in real-time, burn too much energy, and if left unchecked, will cause a [data tsunami](https://www.cloudsherpas.com/partner-salesforce/data-tsunami-big-data-security-internet-things/) will make the slope of Gartner’s hype curve seem quite real.
* nearly all are oriented around pushing data (remember [Pointcast](http://askville.amazon.com/happened-Pointcast-push-technology-general/AnswerViewer.do?requestId=7037556)?) — to the network rather than endpoints standing by for intelligent queries to pull data, a la Google Search.
* Searching in real-time for objects in the Internet of Things using simple or complex queries — and thereby pushing the maximum amount of data cleansing and analysis to the edge of the network — didn’t make anyone’s priority list 10–20 years ago?
* In many cases, these technologies are programmed to beacon their status every few milliseconds as a way to fake a real-time query capability, which [wreaks havoc](http://www.gartner.com/newsroom/id/2684915) on the downstream network.
* To their credit, cellular carriers have made good strides in re-using their LTE networks for IoT applications, but LTE’s high cost and short battery life limit its potential to mains-powered applications like vending machines, so their role in the tsunami is relatively limited.
* **“We clearly see data and content being created**[ **at the edge of the network**](http://www.eweek.com/networking/fog-computing-aims-to-reduce-processing-burden-of-cloud-systems.html) **… this content won’t be sent over the network to be processed by the ‘enterprise-based’ cloud infrastructure. Rather, you will need cloud computing-like processing at the edge.”— Vernon Turner, SVP @ IDC**
* There are only two essential jobs of a low power wireless IoT technology:
  1. Immediately send a message when an important event occurs.
  2. Immediately and accurately answer queries, simple or complex, from an authorized user.

![Gartner](https://www.mediabuzz.com.sg/images/stories/asian_e_marketing/2015_01/Gartner.png)

Today's endpoints:

* ![img](https://cdn-images-1.medium.com/max/800/1*C74trB-B7fP3FSnGiYrI9g.png)
* Pull model
  * Enables higher quality, real-time data queries
  * Pushes computing and analysis to the extreme edge of the network, reducing network congestion and latency
  * Improves network capacity, reducing hardware, storage, power, and labor costs
  * Reduces power consumption at the endpoint, router, and data center.
  * Improves privacy and security
* Note that many IoT vendors will continue to advocate for the current “dumb endpoint” approach, claiming that a router or gateway that connects to the endpoint can do the parsing, filtering, and storing of data — a sort of “near-edge” computing paradigm. But their argument is rooted in the inherent weaknesses of incumbent wireless technologies and does nothing to improve wireless radio spectrum capacity, endpoint battery life, endpoint privacy and security, or storage costs. It’s a little like saying that Google should be indexing content delivery networks like Akamai instead of individual websites themselves.
* ![img](https://cdn-images-1.medium.com/max/800/1*Hx4y9k1Ok0krKDV9udhRJg.png)
* Just as some of today’s biggest web-based phenomenon like YouTube or Facebook would likely not exist had Google not perfected the indexing of the web, some of the biggest innovations in the IoT await the ability to spider and search wireless endpoints.

https://medium.com/the-startup-magazine-collection/a-simple-proposal-to-improve-security-for-the-internet-of-things-4fcc0663f70e

* **Remaining quiet is not the most important principle of IoT security and privacy, but it’s a pretty basic one.**
* Avoiding or minimizing the chances of unauthorized discovery is not technically difficult. But today’s IoT technologies like Bluetooth, 6lowpan, [Sigfox, LoRaWAN](http://www.rethinkresearch.biz/articles/on-lpwans-why-sigfox-and-lora-are-rather-different-and-the-importance-of-the-business-model/), and others make unauthorized discovery **very easy** and it creates the worst kind of [angst](http://www.bizjournals.com/sanjose/news/2015/04/17/data-breaches-and-internet-of-things-risksare.html) in IT departments.
* “Properly implemented strong crypto systems are one of the few things that you can rely on. Unfortunately, endpoint security is so terrifically weak that NSA can frequently find ways around it.” — Edward Snowden
* **dollar-for-dollar, stealth is the simplest, cheapest, and most effective form of IoT security protection available.**
  * **Cloaking**
  * **Googling the IoT.**
  * **Minimize interference.**
  * **Maximize wireless network capacity.**
  * **Power.**
  * **Access control.**
  * **Storage**
* **Chatterboxes and Cuckoos are out, Snipers are in.** 
* **Listen-Before-Talk (“LBT”).**
* **Event-driven messages.**
* **All layers of the firmware stack must work in concert to successfully achieve stealth.**
* **Data caching.**
* **Better Low-Level Cryptography.**
* **Firmware updates.**
* **Open Source.**
* **Rethink roadmaps.**
* **New ventures may already have the answer.** Such as Haystack.
* Government regulation of the IoT.

https://medium.com/@patburns/why-the-internet-of-things-is-going-nowhere-112540e79ae

*  today’s wireless IoT technologies are the [cassette tapes](http://bit.ly/1Kt5WX3) of the IoT and won’t scale in any kind of secure or practical way. **But today’s wireless IoT pain looks like pleasure compared to the ugly reality of the mobile IoT, or what I like to call the “Internet of Moving Things”.**
*  **Battery life.** Movement can be an important power saving tool for managing sleep/wake cycles battery-powered devices. A mobile device that doesn’t move might sleep more than one constantly on the move.
*  **Movement changes risk.**
*  **Absence**
*  **Cause and Effect.**
*  **Location**
*  **Movement = news**
*  **Things move!**
*  *Note to cellular people reading this: you can drive a drone from afar using cellular, but expecting the rest of the IoT to deploy high-cost and high-powered cellular at the endpoint is fantasy apart from some niche use cases where cost and battery life are not important.*
*  Things. For niche devices or mobile IoT gateways (like a smartphone) that customers are already resigned to recharging every day or two (cellular technology is notoriously high power), this requirement does not apply. For 99% of other IoT endpoints, multi-year battery life is non-negotiable.
*  The same way that “unforeseen” companies like Uber took advantage of foundational breakthroughs like smartphones, Google Maps, and low cost GPS chipsets, similar companies will be built around an IoT that properly addresses movement.

## Indoors

Looking at the technologies which work well indoors is a great way to visualize the problem from this perspective, and the same when looking outdoors.

Indoors we have WiFi, Bluetooth, ZigBee and other short-range wireless networks

## Outdoors

Outdoors we have GSM/GPRS, NB-IoT, SigFox, LoRaWAN

**Terrestrial vs satellite localization**

## The indoor-outdoor realm

This is considered to be a third realm which is hard to get a wireless technology / localization to work well in both.

## RSSI triangulation

RSSI triangulation is too hard.

## AoA



## Questions?

What is the power dbm of Dash7? Max? In the Wizzikit?

What metrics are typically useful to determine the viability of a wireless network in iot and wearables? Probably range, coverage, battery usage, SNR, PDR, power saving modes.

NB-IoT has power saving modes such as eDRX, PSM.

Cannot get in touch with Haystack?

Vodacom, MTN roll out NB-IoT in SA somewhat.

# Design

The design section answers what problem this thesis will solve with tangible evidence. Although localization is an overlooked problem in the IoT, 3GPP is addressing this issue in future releases of NB-IoT with OTDoA. There could be a simpler way to keep track of assets and wearable users when optimizing when geofencing events trigger.

Pat Burns has written a great deal about Dash7, LoRa and how it seems to be the better LPWAN option over others. Bidirectionality is obviously a great plus.

It seems that cellular carriers have been touting their own LPWAN solution, and although a bit rushed, in the long-term 3GPP will optimize it well enough that it could become the network standard.

There's been a lot of criticism of NB-IoT's power usage. I believe it's only fair to test current devices in different modes.

Pat has given great ideas for Dash7 and localization which I wish to apply to NB-IoT. He's only offered criticism to cellular LPWANs but I'm not yet convinced. I have the equipment so I might as well test them. I wonder if he is biased in any way to promote his own company Haystack which primarily uses Dash7. Lately he has developed equipment which uses Dash7 over LoRa which is quite probably the best thing I've heard. What can also be done is do add the Dash7 stack to NB-IoT which I think will be amazing. Imagine P2P connectivity using cellular devices. And I'm not talking cellphones using bluetooth or wifi-direct, because those are short range transmission devices. Dash7 is medium range, anything from 200m to 2km. It can essentially bridge the gap between LPLAN and LPWANs. A good way to picture this is the short range WiFi, Bluetooth, ZigBee devices on the left, and long range LPWANs such as LoRaWAN, SigFox, NB-IoT on the right, with Dash7 being the bridge in the middle. I haven't found a comparable stack as uniquely powerful as Dash7. Although it is well documented and patented, it is still unfortunately complicated for the end user. This could be a limiting factor for technology uptake.

MTN has graciously set up towers here in Stellenbosch, and they expect interesting results. I'm the last and only one working on them, so I better make them proud.

Vodacom have towers around Cape Town, however they're usually reluctant to set up unless they get requests from the community.

Looking at these problems on a micro level, I'm sure one can apply it to a macro level around the world.

LoRa is a great radio technology. Unfortunately, the major firmware stack being used is LoRaWAN in the public community. For example, TTN uses this. I think it's the greatest model with the most power by having a gateway cost 250 euros and can be set up by anyone.

I'm banking on the fact that licensed spectrum means much more data can be sent.

How come Dash7 can communicate so often?

So what do I have?

A Dash7 Wizzikit which contains a gateway and two endpoints. What can I do with it? I can probably have one endpoint do two hops before it reaches the gateway. I can test the range and power usage? I don't actually know these values and couldn't find it in the specifications. At the moment it can send sensor data successfully.

Haystack offer a tag product which can interface with a gateway which does Dash7 over LoRa and simultaneously LoRaWAN. Although, I've read enough about LoRaWAN to believe it is really crap.

I also have a multitude of NB-IoT devices which work successfully so far. I have yet to test e-DRX and PSM sucessfully, but I believe there's great potential there.

NB-IoT seems suited for static cases, but that's at the moment. Mobility is coming in future releases, and that includes inter and intra cell-reselection.

Ideally, one should only have to register once, which would average about 5 seconds, and then stick in the mode of one's choosing.

To apply Pat's ideas to NB-IoT, there should be a sufficient radius that the device is comfortable in before it wants to check how much it has moved and still be able to communicate with the tower. What is comfort?

I wonder if there are any other Class B or C LoRa networks or devices? It seems too hard to obtain. Anyway, suggestions can be made but it's outside the time and budget scope of this thesis.

SigFox? Hmm. Nope. It's unidirectional.

LoRaWAN? Nope, already decided it's crap. Great idea, though, but please add bidirectionality / class b or c.

What is SA interested in? Hey SA. Is NB-IoT really viable?

How effective is assisted-GNSS/GPS in NB-IoT localization when multicast/broadcast is used?

It seems to be useful in Dash7 already, but what are the specs for it? Since Dash7 seems to be lower range, can we use it indoors?

In a cellphone we have LTE and WiFi. Using that analogy, for smart devices we can have a similar configuration by using NB-IoT and Dash7.

What about considering the fact that RSSI trilateration works well close by? Could that be used indoors? Unfortunately cell tower sites cannot just be placed anywhere so we won't be able to use this to our advantage.

This is why Dash7 gateways would be better to use in buildings.

I want this thesis to be published and Pat Burns and JP Norair read this. Of course, they'll offer their own criticism, as I believe they would, but I'd really like to see both NB-IoT and Dash7 adopted more mainstream in the IoT field. This is currently not my problem to solve, but I'll certainly keep it in mind through the project.

I wonder if the Wizzikit I have is the same dBm as WiFi? Because I could pick up the Naspers WiFi signal from the medialab also 4 floors down. Hmm.

Dash7 needs to be more powerful indoors. Using sub-gigahertz frequencies does help.

Both technologies can listen to the strength of gateways or towers and determine when sufficient movement occurs to tell the cloud.

This combination can be useful for another idea I've had, which is emergency response. Long range networks such as NB-IoT can let a control centre know that the device / user is in trouble and a dispatched responder can communicate directly with the device using P2P communication via Dash7. I actually had a board designed which could handle a few of the long range wireless networks which included LoRaWAN, SigFox, NB-IoT and GSM and Dash7 for medium range.

Thinus, the only way that I've really made progress was to fill up the design chapter. Can you believe it? I've struggled so much on the literature study, because I never fully believe what people say, and then it has to link to my design, but I can't just look at anything unless I have a design, and I need to look at stuff to make a design, so that was my catch 22.

What GPS/GNSS modem am I going to use?

If I can reset the modem's hot start data, then I can play around with what kind of ephemeral and almanac data I send from the network at different positions around the cell tower.

But that doesn't make a difference where it is if it's outside. Or does it?

Well, when am I going to trigger a listen to a satellite.

cellular rssi change -> satellite localization

dash7 rssi change -> nothing..

Apparently NB-IoT is only left with the consumer market, which is a tough nut to crack. Rather aim for enterprise, industry, military and goverment. If convinced, those are the ones that can really take the technology forward.



## Localization

GPS/GNSS.



## NB-IoT

Since NB-IoT and Dash7 seem curiously interesting in the wearable and IoT world, a series of metrics will be tested to investigate their viability. The research seems promising. Because LPWAN networks such as LoRaWAN and SigFox are unidirectional, they will not be investigated.

First, the technologies must be connected to the internet.

End-2017, MTN set up a ZTE NB-IoT basestation in Stellenbosch for the use of research and testing. Unfortunately due to technical difficulties, a connection was unable to be made until July 2018. Nevertheless, a few tests were done at MTN's testplant in Johannesburg for two weeks during April. One of four faraday cages were made available, and also included LTE-M and GSM to test.

Vodacom have coverage in Gauteng with 1200 Huawei basestations, however Cape Town is quite limited, with currently only two working at Century city and the CTICC.

Build a HayTag. Build an NB-IoT tag.

## NB-IoT modems

A suitable end-point is also required to test NB-IoT. The following boards and feedback is stated:

For a start, Pycom's FiPy was tested since it had multiple wireless technologies such as SigFox, LoRa, LTE-M and NB-IoT of which potential comparisons could be made. Unfortunately efforts were unsuccessful. During April 2018, the FiPy NB-IoT bootloader had just been released. It was loaded on the Sequans Monarch modem. The developers stated that at that point in time it only worked on Ericsson basestations. The 8th band was manually set but unfortunately it just couldn't connect. Noting the power usage of the ESP32 and combined modem it was actually quite hot to the touch.

Ublox's SARA N200 was tested, with a sample modem from RFDesign populated on a PCB designed by Thomas Durand and assembled by Barracuda Holdings. Efforts were unsuccessful until  visiting Vodacom World Campus in Midrand on the last day. They had a very specific setup procedure which unfortunately RFdesign failed to indicate in their support. Luckily it could also be tested later in the day in Randburg again at MTN's testplant. The problem was an SI_AVOID and SCRAMBLING parameter which had to be properly set.

The testplant also had one of two Sierra Wireless WP7702 development kits in South Africa provided for by Philip Nel of sierra Wireless. This board was used to test NB-IoT, LTE-M and GPRS.

The Quectel BG96 was tested on MTN's basestation in Stellenbosch and on Vodacom's towers in Cape Town.

Nordic nrf91 has yet to be tested.

## Dash7 modems

* MuRata CRWXM1ABZZ1
* Wizzikit

## Metrics

* SNR
* PDR
* Bandwidth, throughput
* Range, coverage



## PCB

Design a PCB to take these multiple wireless technologies. Do network tests.

It will be on a two layer board.

![latest_PCB2](C:\GIT\masters\thesis\images\latest_PCB2.JPG)



## Current usage

Eevblog current monitor.

## Cloud

GCP. Thingsboard.

## Communication

Ethernet, wifi..

MQTT

# Measurements

Dash7 has only 250m range NLOS at 10dBm. What about at the 27dBm limit?

NB-IoT has 5km range.

# Simulations and Analysis

Let's simulate an endpoint using NB-IoT and Dash7 in an indoor-outdoor scenario.

How can peer-to-peer work in our favour? What if we have a bunch of static endpoints in a packing warehouse?

What information can we use to resolve spatial awareness without the help of a satellite signal. Unless, we have anchor points.

There is great power in merely listening. Both NB-IoT and Dash7 can be designed to do this and use very little power.

If one knows where a satellite is and it's not immediately there, then one doesn't have to check for very long, saving more battery life.

One can listen to an NB-IoT base station for satellite updates, and Dash7 gateways for room changes.

# Conclusion

Seeing NB-IoT and Dash7 as viable in IoT and wearables will fuel use cases for them. Use case demand is directly proportional to coverage, and vice versa. At the moment, current research seems promising but having tangible evidence such as this proves the viability of the technology for other use cases as well, and for cellular service providers to roll out coverage.

The proposal in this paper suggests an ultra-low power consumption configuration to allow a device 



# Summary

LoRaWAN, SigFox bad.

Pull model, not push.

Hi Thinus.. I've been delving into the lit a bit.

GPS.. find module that I can reset.

Tests, what kind? 

* range
* 

# Thinus feedback

![Thinus Booysen (thinusbooysen@gmail.com)](https://lh3.googleusercontent.com/a-/AAuE7mCc6ScDT93ghh-Ez83q5GCvHnfmHQQ6NRppMZLzTQ=s32-c-k-no) So, it is about comparing the technologies for outdoor&indoor localisation and about proposing a new method of doing localisation using them? (please help me right if any part of that is wrong)

Yes.. that is essentially the essence of it

NB-IoT has the ability for multicast in release 14 I believe, and to reuse it to send periodic GPS/GNSS data save much preprocessing time for end units

If I can prove that it works now for at least 1 or a few devices then it is entirely scalable

Same for Dash7.. I can work on doing exactly that, although the range is considered medium and not long like NB-IoT, SigFox etc. On the other, there's something else one can do with it indoors

Still toying a little with the idea, but being in range of beacons indoors could be useful for malls, warehouses etc..

The beacons have enough power to transmit advertising packets, but the endpoints only have to listen every now and then, which saves power. Instead of transmitting a tx request.

Otherwise, what if endpoints can communicate P2P with each other? Although they'd still need some kind of anchorage, at least one peer to say "I'm exactly here, because I got a satellite lock"..

It's all to solve, "where is it? I want to know now" without waiting for the next periodic transmission in the case of unidirectional LPWANs such as SigFox and LoRaWAN

So in that sense, it can also be crucial to critical IoT when having bidirectionality

What's the next steps, you may ask?

Well, luckily I already have a PCB with NB-IoT and Dash7 built-in. The NB-IoT should not require too much work to get a working PoC. The Dash7 might require more effort, though

![Thinus Booysen (thinusbooysen@gmail.com)](https://lh3.googleusercontent.com/a-/AAuE7mCc6ScDT93ghh-Ez83q5GCvHnfmHQQ6NRppMZLzTQ=s32-c-k-no)Yes. I am very happy with this direction, especially if it gets you excited, and it obviously has driven you to type something up. So if you believe it could work, by all means go ahead. 

I can also do simulations for the future features such as multicast in scalable situations.. estimate the average latency, responsiveness, reliability, positional accuracy..

So yes, it is quite interesting

And it took me a while to notice this gap in what is currently the norm

So I'll keep at it :)

![Thinus Booysen (thinusbooysen@gmail.com)](https://lh3.googleusercontent.com/a-/AAuE7mCc6ScDT93ghh-Ez83q5GCvHnfmHQQ6NRppMZLzTQ=s32-c-k-no)Great. Now, hunt it down and finish it off. 