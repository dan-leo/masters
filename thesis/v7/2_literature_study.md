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

| Numerology                                                 | 15 kHz | 3.75 kHz |
| ---------------------------------------------------------- | ------ | -------- |
| (1) Transmit power (dBm)                                   | 23.0   | 23.0     |
| (2) Thermal noise density (dBm/Hz)                         | -174   | -174     |
| (3) Receiver noise figure (dB)                             | 3      | 3        |
| (4) Occupied channel bandwidth (Hz)                        | 15000  | 3750     |
| (5) Effective noise power = (2) + (3) + 10*log ((4)) (dBm) | -129.2 | -135.3   |
| (6) Required SINR (dB)                                     | -11.8  | -5.7     |
| (7) Receiver sensitivity = (5) + (6) (dBm)                 | -141.0 | -141.0   |
| (8) Max coupling loss = (1) - (7) (dB)                     | 164.0  | 164.0    |

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