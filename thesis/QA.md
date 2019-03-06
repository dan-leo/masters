This is just a rough Q&A that I'm expanding on and it helps my literature survey.



# Questions

How come Dash7 can communicate more than LoRaWAN?

LoRaWAN can transmit more often than every few minutes?

Cortus?

Can we prove that NB-IoT truly is low powered?

Is RTK too short range?

NB-IoT broadcast?

NB-IoT P2P?

Am I refining asset tracking for NB-IoT?

Does moving along a circumference of RSSI change significantly with building interference involved?

Indoor tracking always uses a specific custom gateway.

Does OTDOA overcome Fresnel zone inaccuracies?

How accurate is OTDOA?

Can NB-IoT support “hot start” GPS location acquisition?

Are Vodacom's towers release 14?

Can I make my research more bottoms up?

Can I make a masters on a single sentence? Haha..

What does the Gartner IoT forecast say and is it true a few years later?

Can I do a bottoms up approach in my masters?

# Answers

Does the IoT data tsunami feed machine learning?

- Yes. So what's wrong?
- The problem is that many devices are unidirectional.

NB-IoT P2P? 

- Yes, it is included in the spec in future
- One could also re-use the RF frontend and add Dash7
- MSK downlink, OFDM uplink
- Am I going to consider it? I don't know

LoRaServer can interface with Class B and C gateways..

- Is it worth setting up? No. Time and budget constraints.

Can NB-IoT's indoor penetration be used to determine where something is?

- Apparently GSM can be used to achieve 4m horizontal accuracy and a 60% chance of determining which floor something is on.
- There is also a paper which suggests using the information from GSM towers in GPS/GNSS-denied areas, although GSM is a sunsetting technology therefore it is not considered in this paper. They even suggest that their approach can be more accurate using open databases of cell tower locations and not requiring synchronization with any towers.
- However, although can be assumed that similar approaches can be used using the NPRS (Narrowband Positioning Reference Signal), OTDOA's downlink approach using assist information from the tower should be more accurate.

Doesn't NB-IoT come with some kind of localization?

- CellID
- OTDOA

OTDOA?

- Can only be field tested this year. Out of scope of time and resource constraints.
- RSSI can be used for now.

LoRaWAN vs Dash7 is well-documented. 

- except TTN? Should be fine.

Dash7 vs NB-IoT?

- If I compared the two, I'd find that coverage, infrastructure cost is significantly different, otherwise same in bidirectionality. Both can exhibit P2P, except NB-IoT only in future.
- They are essentially similar

Haystack claims 1m indoor accuracy using Dash7. What are the challenges?

- Apparently it uses vertex data from reference nodes for RSSI & RF fingerprinting

How to fingerprint?

- Too complicated in dynamic environments

Indoor-Outdoor is the third realm?

- It is considered an IoT blindspot, because there are few solutions to cater for both short of using multiple radios.
- Usually we can consider IoT to be segmented into two realms, the indoor and outdoor realm.
  - WiFi, ZigBee, BLE are all great for indoors, while cellular networks and LPWANs compete in the outdoor sphere.
- What about use cases that require both realms?
  - A major use case is precisely locating things in real time.
  - For example, 
    - in access control one wants to locate a person inside and among multiple buildings in a secure area.
    - in the supply chain one wants to monitor critical shipments in-transit, in and around warehouses.
    - asset management
  - this is useful for critical applications and the IoMT

Although Dash7 bridges the gap between LPLAN and LPWAN, wouldn't it be better if LPWANs can handle all three realms?

- There will always be PAN/WLAN networks, and BLE and WiFi is the dominant network technology here, but it only works well within room or building sized environments respectively.
- Long range cellular networks such as GSM and LTE are optimized for low bandwidth and high battery life in the form of LTE-M and NB-IoT. There also exist LPWAN solutions such as SigFox and LoRaWAN. These work well for the outdoors
- Dash7 is hoping to bridge the gap by?
  - Encompassing both LAN coverage as well as WAN coverage in a low powered form.
- Dash7 is also a full networking stack which can reuse the PHY RF layer of other network standards, which means it is quite versatile. 
- Would it pass 3GPP / FCC standards if it reused NB-IoT's frontend?
- It's a tough question for NB-IoT because it remains to have a high cost of infrastructure (CAPEX and OPEX) required for cell tower, eNodeB, spectrum licensing etc.
  - But Release 15 does state picocell / small cell usage.
- Dash7 is good for now, NB-IoT is good for the future.
- Can Dash7 live on if it reuses NB-IoT's RF frontend? 
  - It is not likely that it would become the defacto standard as 3GPP is creating that for the cellular industry. But if it can work concurrently on a modem, then it adds useful features such as P2P. Is it worth the capital outlay to implement this if future LTE releases specify P2P communications? No.
- To answer the question, it would seem possible for NB-IoT to be the winner in future with its P2P and small cell in future releases.
- Can Dash7 have the same range as NB-IoT?
  - Dash7 can output at 27 dBm and NB-IoT at 23 dBm. This means that it only really depends on the gateways. In fact, the final answer is the MCL that the technology supports, and NB-IoT can support 164 dBm whilst Dash7 only 

Is it always good to aim for decentralization?

- Yes. The more one can do away with the man-in-the-middle, the better.

