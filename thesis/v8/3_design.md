---
title: LTE Cat-NB (Narrowband) Performance Evaluation
author: Daniel Robinson
date: Stellenbosch University, November 2019
tags: [LTE, NB-IoT]
toc: true
lot: true
lof: true
link-citations: true
csl: ieee.csl
linkcolor: blue
geometry: "left=3cm,right=3cm,top=3cm,bottom=2cm"
numbersections: true
tablenos-warning-level: 1
tablenos-number-by-section: true
---

\pagestyle{fancy}
\fancyfoot[CE,CO]{Page \thepage \hspace{1pt} of \pageref{LastPage}}

# Design and Methodology {#design}

As stated in \S\ref{resobj}, the aim of this study is to compare user equipment (UE) against mobile network operators (MNOs) with a set of tests that evaluate NB-IoT's performance according to a set of metrics which highlight striking differences due to the underlying complexities of LTE architecture.

Four mobile network operators (MNOs) are compared in South Africa according to the underlying vendor
infrastructure used, namely Nokia and ZTE in the Cape/coastal regions and Ericsson and Huawei based in Gauteng/inland regions.

More than one UE is used to improve the accuracy of the result, namely Ublox and Quectel. A unit testing framework has been carefully prepared in Python in combination with a Hewlett Packard rotary RF attenuator in 10dBm steps. The results can be applied to multiple application use cases.

## Preliminary Tests

These tests better orient the reader to the behavior of UE devices and LTE network.

### Network Info

This section looks at certain aspects of LTE networks.

#### System Information Blocks (SIB)

SIBs carry relevant information for the UE, which helps UE to access a cell, perform cell re-selection, information related to INTRA-frequency, INTER-frequency and INTER-RAT cell selections. In LTE there are 13 types of SIBs as can be seen in Table \ref{tbl:sib_descr}.

See Appendix \ref{appendix_sibs} for examples of NB-IoT SIB blocks.

* Downlink systemInformationBlockType1
* Downlink systemInformation
* Uplink rrcConnectionRequest
* Downlink rrcConnectionSetup

Table: System Information Blocks description {#tbl:sib_descr}

| SIB    | Description                                                  |
| ------ | ------------------------------------------------------------ |
| SIB-1  | Cell access related parameters and scheduling of other SIBs  |
| SIB-2  | Common and shared channel configuration, RACH related configuration are present |
| SIB-3  | Parameters required for intra-frequency, inter-frequency and I-RAT cell re-selections |
| SIB-4  | Information regarding INTRA-frequency neighboring cells (E-UTRA) |
| SIB-5  | Information regarding INTER-frequency neighboring cells (E-UTRA) |
| SIB-6  | Information for re-selection to INTER-RAT (UTRAN cells)      |
| SIB-7  | Information for re-selection to INTER-RAT (GERAN cells)      |
| SIB-8  | Information for re-selection to INTER-RAT (CDMA2000)         |
| SIB-9  | Information related to Home eNodeB (FEMTOCELL)               |
| SIB-10 | ETWS (Earthquake and Tsunami Warning System) information (Primary notification) |
| SIB-11 | ETWS (Earthquake and Tsunami Warning System) information (Secondary notification) |
| SIB-12 | Commercial Mobile Alert Service (CMAS) information.          |
| SIB-13 | Contains the information required to acquire the MBMS control information associated with one or more MBSFN areas. |

It is important to realize how intricate the underlying architecture of LTE is. For example, considering the singalling between UE and eNodeB using SIBs, we see this in action. This complexity hints that the probably cause of variation is due to the LTE network configuration.

#### Extended Coverage Level (ECL)

Extended Coverage Levels increase the amount of repetitions between UE and eNodeB to increase range. Henceforth, this should mean that a weaker signal strength increases the ECL level. There are 3 levels, with level 0 being the least repetitions, and 2 being the most.

\begin{minipage}{\linewidth}
\begin{center}
\includegraphics[width=1.0\linewidth]{../../../masters/code/tests/plotterk/Signal_power_ECL_plot.pdf}
\captionof{figure}[ECL vs RSRP.]{ECL levels shown against RSRP for Ubloxa and Quectel on ZTE-MTN and Nokia-Vodacom networks.}
\label{fig:ecl_example}
\end{center}
\end{minipage}

In this Fig. \ref{fig:ecl_example}, ECL is shown as an example against two networks and it seems apparent that it is not determined by attenuation. Further investigation is necessary.

[](../../../masters/code/tests/plotterk/Signal_power_ECL_plot.png)

[](../../../masters/code/tests/plotterk/ECL_histogram.png)

#### Cell ID, EARFCN, PCI

These identifiers are related to the specific cell towers the UE is connected to.

The Cell ID is the physical network cell ID. EARFCN uniquely identifies the LTE band and carrier frequency. PCIs, or Physical Cell Identifiers provide a psuedo-unique value for identifying eNodeBs and is a unique identifier for serving cells.

Table: PCI, Cell ID count and EARFCN after K-means cluster filtering with tuples in (Ublox, Quectel) format. {#tbl:nw_parameters}

| PCI  | Cell ID   |      | ZTE      | Nokia    |
| ---- | --------- | ---- | -------- | -------- |
| 123  | 239882509 |      | (34, 26) |          |
| 14   | 2671716   |      | (13, 29) |          |
| 11   | 2672484   |      | (1, 4)   |          |
| 2    | 484196    |      |          | (34, 32) |
|      |           |      |          |          |
|      | EARFCN    |      |          |          |
|      | 3712      |      | (48, 59) |          |
|      | 3564      |      |          | (34, 32) |

In Table \ref{tbl:nw_parameters} we see three towers on the MTN-ZTE network. More than one tower at the same frequency or EARFCN proves that Intra-Frequency Cellular Reselection works as expected.

[](../../../masters/code/tests/plotterk/Signal_power_Cell_ID_plot.png)

[](../../../masters/code/tests/plotterk/Cell_ID_histogram.png)

[](../../../masters/code/tests/plotterk/Signal_power_PCI_plot.png)

[](../../../masters/code/tests/plotterk/PCI_histogram.png)

#### C-DRX mode

On the Vodafone network in connected-DRX (C-DRX) mode, the UE is observed to show peaks spaced at regular 2.048s intervals [@Martinez2019]. On both Vodacom and MTN networks, these peaks are not visible and instead a steady stream of peaks can be seen as on the following images.

\begin{figure}[ht]
  \subfloat[C-DRX timing on MTN-ZTE-Ublox]{
	\begin{minipage}[c][1\width]{
	   0.5\textwidth}
	   \centering
	   \includegraphics[width=1.0\linewidth]{../../code/tests/logs/zte_mtn/rf_shield/ublox/scope/12_8ms.jpg}
	\label{fig:cdrx1}
	\end{minipage}}
 \hfill 	
  \subfloat[C-DRX timing on MTN-ZTE-Quectel]{
	\begin{minipage}[c][1\width]{
	   0.5\textwidth}
	   \centering
	   \includegraphics[width=1.0\linewidth]{../../code/tests/logs/zte_mtn/rf_shield/quectel/scope/12ms.jpg}
	\label{fig:cdrx2}
	\end{minipage}}
\captionof{figure}[C-DRX timing measurement]{Timing measurement of two UEs on MTN-ZTE during C-DRX. Although the duty cycles vary in C-DRX mode, it can be estimated that pulses are roughly 12ms in length with 4ms idle between. This means that ~75\% of the time the UE device is drawing current.}
\end{figure}

[](../../code/tests/logs/zte_mtn/rf_shield/ublox/scope/12_8ms.jpg)

[](../../code/tests/logs/zte_mtn/rf_shield/quectel/scope/12ms.jpg)

[](../../code/tests/logs/zte_mtn/rf_shield/ublox/scope/73.6mA.jpg_110dB_slightly_open.jpg)

[](../../code/tests/logs/zte_mtn/rf_shield/ublox/scope/cdrx73_6mA_110dB.jpg)

[](../../code/tests/logs/zte_mtn/rf_shield/quectel/scope/70.4mA_ant_0dB.jpg)

In Fig. \ref{fig:cdrx1}, the Ublox UE uses 73.6mA at 110dB attenuation with the RF shield enclosure door slightly open and in Fig. \ref{fig:cdrx2}, with the same environment the Quectel UE uses 73.6mA. Observing C-DRX on the Nokia-Vodacom network, we have slightly different results as can be seen summarized in Table \ref{tbl:cdrx_vals}. It seems that on ZTE-MTN and Nokia-Vodacom that cycles are of length 16ms and 256ms respectively.

Table: C-DRX values {#tbl:cdrx_vals}

|               | MTN-ZTE | Nokia-Vodacom |
| ------------- | ------- | ------------- |
| **Ublox**     |         |               |
| Peak current  | 73.6 mA | 72 mA         |
| Transmit time | 12.8 ms | 56 ms         |
| Idle time     | 4 ms    | 200 ms        |
|               |         |               |
| **Quectel**   |         |               |
| Peak current  | 70.4 mA | 66.4 mA       |
| Transmit time | 12 ms   | 80 ms         |
| Idle time     | 4 ms    | 180 ms        |

[](../../code/tests/logs/nokia_vodacom/centurycity/ublox/cops/scope/cops_idle_56ms.jpg)

[](../../code/tests/logs/nokia_vodacom/centurycity/ublox/cops/scope/cops_tx_200ms.jpg)

[](../../code/tests/logs/nokia_vodacom/centurycity/ublox/cops/scope/cops_72mA.jpg)

[](../../code/tests/logs/nokia_vodacom/centurycity/quectel/cops/scope/cops_80ms_idle.jpg)

[](../../code/tests/logs/nokia_vodacom/centurycity/quectel/cops/scope/cops_66.4mA.jpg)

[](../../code/tests/logs/nokia_vodacom/centurycity/quectel/cops/scope/cops_180ms_tx.jpg)

On the MTN-ZTE network the peaks indicate an on time of roughly 12ms and idle of 4 seconds. With a cycle of 16ms, it fits the LTE requirements of between 10ms and 2560ms in terms of 1ms subframes. However, NB-IoT has a minimum requirement of 256ms to 9216ms for the interval length between C-DRX transmissions and Vodacom-Nokia is using this minimum value. MTN-ZTE is utilizing vastly more time on air than permitted by the 3GPP and it is having a detrimental effect on the estimated battery life. Vodacom-Nokia is using the minimum, but it is recommended to increase this value. Lastly, this does not bode well for the scaling up of devices due to the interference, especially on the shared uplink (NPUSCH) channel.

####  E-UTRAN Node B (eNB/eNodeB)

Ericsson eNodeBs run Linux and their commands are accessible via MOShell, or the scripting language AMOS.

To get an idea of the complexity of a node (eNodeB) in a base station (BTS), running `$ get .` in the terminal of B06009-TESTPLANT returned 7037 `Managed Objects` (MOs) with 27989 parameters. See Appendix \ref{appendix_eNB} for an example code snippet of the first two `Managed Objects`. This highlights how easy it is for a BTS to produce different results in this study depending on the network configuration and environment.

### Range Field Test

This gives a good idea as to the range expected according to RSRP.

#### NB-IoT

Using a Quectel BG96, the following tests were taken on the rooftop described in Fig. \ref{fig:rooftop}.

![Rooftop outside the HF RF lab on the 5th floor of the Electrical & Electronic Engineering building. The base station it connected to is on the General Building, and is just over 150m away at the same elevation with a single building blocking line-of-sight. The base station is situated on the bottom left of the picture at an altitude of approximately 138m. \label{fig:rooftop}](C:\GIT\masters\thesis\images\rooftop_maps.JPG){width=50%}

The tests involve sending a set of 10 pings multiple times at a certain attenuation and resulting RSSI measurement using a Quectel BG96 modem.

\begin{figure}[ht]
  \subfloat[With an antenna and the attenuator set to 0dB, we find most of the values around the mean of 185.2ms, except for the tail at around 500ms which is the time of the first ping in a set of 10. ECL 0, RSRP -51 dBm.]{
	\begin{minipage}[c][1\width]{
	   0.48\textwidth}
	   \centering
	   \includegraphics[width=1.0\linewidth]{../images/rooftest1.png}
	\label{fig:ping1}
	\end{minipage}}
 \hfill 	
  \subfloat[Setting the attenuator to the max of 110dB, we see no change in the ping measurements which have a mean of 185.9ms. The tail has increased to a max of just over 600ms. ECL 0, RSRP -85 dBm.]{
	\begin{minipage}[c][1\width]{
	   0.48\textwidth}
	   \centering
	   \includegraphics[width=1.0\linewidth]{../images/rooftest2.png}
	\label{fig:ping2}
	\end{minipage}}
\captionof{figure}[Ping tests]{Ping tests on Engineering rooftop}
\end{figure}

[](C:\GIT\masters\thesis\images\rooftest1.png)

[](C:\GIT\masters\thesis\images\rooftest2.png)

\begin{figure}[ht]
  \subfloat[Removing the antenna from the attenuator, we find that the data has a slightly thicker tail, and averages around 207.1ms. ECL 0, RSRP -91 dBm.]{
	\begin{minipage}[c][1\width]{
	   0.48\textwidth}
	   \centering
	   \includegraphics[width=1.0\linewidth]{../images/rooftest3.png}
	\label{fig:ping3}
	\end{minipage}}
 \hfill 	
  \subfloat[Lastly, having no attenuator nor antenna we still have a connection at -107dBm with a mean of 190.6ms. ECL 1, RSRP -107 dBm.]{
	\begin{minipage}[c][1\width]{
	   0.48\textwidth}
	   \centering
	   \includegraphics[width=1.0\linewidth]{../images/rooftest4.png}
	\label{fig:ping4}
	\end{minipage}}
\captionof{figure}[Ping tests]{Ping tests on Engineering rooftop}
\end{figure}

[](C:\GIT\masters\thesis\images\rooftest3.png)

[](C:\GIT\masters\thesis\images\rooftest4.png)

To be able to attenuate the signal until disconnection, one must increase the range from the base station such that leakage transmission from traces, soldering and attenuator connectors do not interfere with the test. As such, there must not be a connection to the base station at all if the antenna or attenuator is disconnected or connected at maximum attenuation.

\begin{figure}[ht]
  \subfloat[A test was performed from 10pm onwards at Technopark on 14 March 2019. A connection was made at a range of 4.8 km at -93dBm and an altitude of 132m. This is a relative elevation of -6m to the base station.]{
	\begin{minipage}[c][1\width]{
	   0.48\textwidth}
	   \centering
	   \includegraphics[width=1.0\linewidth]{../images/techno_map.PNG}
	\label{fig:map_techno}
	\end{minipage}}
 \hfill 	
  \subfloat[The greatest distance measured was 5.5km from the intersection of the R44 and the turn-off to Stellenbosch Square or Jamestown at an altitude of 106m. This is a relative elevation of -32m to the base station and at an RSRP of -89dBm.]{
	\begin{minipage}[c][1\width]{
	   0.48\textwidth}
	   \centering
	   \includegraphics[width=1.0\linewidth]{../images/jamestown_map.PNG}
	\label{fig:map_jamestown}
	\end{minipage}}
\captionof{figure}[Long-range tests map]{Long-range tests map}
\end{figure}

[](C:\GIT\masters\thesis\images\techno_map4.8km.JPG){width=50%}

\begin{figure}[ht]
  \subfloat[In Technopark, at 0dB attenuation the data has a mean of 196.7ms and a tail just above 500ms in ECL 0, RSRP -93 dBm.]{
	\begin{minipage}[c][1\width]{
	   0.48\textwidth}
	   \centering
	   \includegraphics[width=1.0\linewidth]{../images/techno1.png}
	\label{fig:ping5}
	\end{minipage}}
 \hfill 	
  \subfloat[In Technopark, at 10dB the data is more spread out from 200 - 500ms with a mean of 396.4ms and a tail at just under 1000ms in ECL 1, RSRP -101 dBm.]{
	\begin{minipage}[c][1\width]{
	   0.48\textwidth}
	   \centering
	   \includegraphics[width=1.0\linewidth]{../images/techno2.png}
	\label{fig:ping6}
	\end{minipage}}
\captionof{figure}[Long-range ping tests]{Long-range ping tests}
\end{figure}



[](C:\GIT\masters\thesis\images\techno1.png)

[](C:\GIT\masters\thesis\images\techno2.png)

\begin{figure}[ht]
  \subfloat[In Technopark, at 20dB attenuation, the data is more spread across 350 - 1000ms with a mean of 793.4ms and a tail that extends to over 4500ms in ECL 2, RSRP -107 dBm. Any more attenuation and the signal is lost.]{
	\begin{minipage}[c][1\width]{
	   0.48\textwidth}
	   \centering
	   \includegraphics[width=1.0\linewidth]{../images/techno3.png}
	\label{fig:ping7}
	\end{minipage}}
 \hfill 	
  \subfloat[At the furthest point in Fig. \ref{fig:map_jamestown}, the signal strength increased to -89dBm and resumed a mean of around 209.6ms with a tail around 500ms. ECL 0]{
	\begin{minipage}[c][1\width]{
	   0.48\textwidth}
	   \centering
	   \includegraphics[width=1.0\linewidth]{../images/stelliesquare.png}
	\label{fig:ping8}
	\end{minipage}}
\captionof{figure}[Long-range ping tests]{Long-range ping tests}
\end{figure}

[](C:\GIT\masters\thesis\images\techno3.png)

[](C:\GIT\masters\thesis\images\jamestownmap.JPG)

[](C:\GIT\masters\thesis\images\stelliesquare.png)

\begin{figure}[ht]
  \subfloat[A similar pattern was seen 3.0 km away at Parmalat, although driving closer there were a few spots where connection was lost or many retries were needed such that the tail extended up to almost 3000ms for the ICMP ping time.]{
	\begin{minipage}[c][1\width]{
	   0.48\textwidth}
	   \centering
	   \includegraphics[width=1.0\linewidth]{../images/parmalat.png}
	\label{fig:ping9}
	\end{minipage}}
 \hfill 	
  \subfloat[Lastly, all the test data (including on the way to Technopark and back), we see a similar form except with a tail extending to almost 10 seconds, which is within 3GPP specifications.]{
	\begin{minipage}[c][1\width]{
	   0.48\textwidth}
	   \centering
	   \includegraphics[width=1.0\linewidth]{../images/alltests2.png}
	\label{fig:ping10}
	\end{minipage}}
\captionof{figure}[Long-range ping tests]{Long-range ping tests}
\end{figure}

[](C:\GIT\masters\thesis\images\parmalat.png)

[](C:\GIT\masters\thesis\images\alltests2.png)

![Looking at the ICMP ping response according to different RSSI values, we see high jitter of a few seconds from -80dBm or less.](C:\GIT\masters\thesis\images\jitter.png){width=50%}

This means that in an urban area, NB-IoT satisfies the 2-5 km range specification.

#### Dash7

Since Dash7 was a curiosity at the time, a Dash7 field test was performed using a Murata CMWX1ZZABZ-091, but due to 10dBm transmit power it limited range to about 300m.

![Dash7 field test reaching 300m max NLOS range](../images/1571685763894.png){width=65%}

Although Dash7 is considered a viable alternative, it fell short on range expectations.

Haystack Technologies has developed a Dash7-over-LoRa implementation that expects ranges of over a few kilometers and can be considered in future research.

### RF Spectrum Tests

Using an RTL2832 SDR dongle, we can capture RF signals. At the very least we can visualise how the signal propogates through the airspace.

![5 dB SINR NB-IoT transmissions using Sierra Wireless WP7702 at 908.2 MHz and EARFCN 3734 of length 2282ms, 1560ms and 1380ms respectively.](../images/image-20191105144302036.png)

![SigFox and LoRa RF signals \@868 MHz](../images/image-20191104223939783.png){width=30%}

Each technology has their own modulation scheme and unique features, and with that their own set of advantages and disadvantages. More can be found in \S\ref{lpwans}.

### Terrestrial Localization

Localization can be useful for asset tracking as discussed in \S\ref{asset_tracking}. Of the prominent LPWANs, SigFox is the only one that offers a simple localization service. NB-IoT will offer one when upgraded to 3GPP Release 14. Unfortunately SigFox has poor accuracy as can be seen in Fig. \ref{fig:sigfox_map}.

![With a 17.783km radius in this example, SigFox is poor when it comes to being considered as a source of localization using RSSI triangulation, and it may be better to use TOF techniques such as in OTDOA in NB-IoT \label{fig:sigfox_map}](../images/image-20191105141405835.png){width=80%}

### Power Saving Mechanisms

This section shows a brief investigation into the power saving mechanisms of NB-IoT.

With a paging time window interval of 2.54s and 4 hyper-frames making up 40.96s, the following output is obtained.

```c
AT+NPTWEDRXS=2,5,"0001","0011"
+CEREG: 5,1,"8CA7","28C464",7,,,"00011000","00101010"
```

AT+CEREG says that the T3324 active time is 48 seconds, or 2 seconds * 24 binary coded timer value. This is not the expected outcome, even according to `Table 10.5.5.32/3GPP
TS 24.008: Extended DRX parameters information` as referenced in Ublox documentation, which expects 40.96s. Besides, the paging time interval is also not working as expected.

![eDRX](C:\Users\d7rob\AppData\Roaming\Typora\typora-user-images\1555567465123.png){width=50%}

[](C:\Users\d7rob\AppData\Roaming\Typora\typora-user-images\1555570254042.png){width=50%}

The T3324 active timer value is modified to 5.12s.

```c
AT+NPTWEDRXS=2,5,"0001","0000"
```

AT+CEREG says that the timer is 32s, or 2 seconds * 16 binary coded timer value.

```c
+CEREG: 5,1,"8CA7","28C465",7,,,"00010000","00101010"
```

In the debug logs we see the timer expires after exactly 30 seconds.

```c
1400,00:07.952393,NAS_DBG_TIMER
	action=TIMER_START
	prim_id=USIM_STATUS_TIMER_EXPIRY
	duration=30
2092,00:37.952728,USIM_STATUS_TIMER_EXPIRY
	timer_handle=16871576
```

[](C:\Users\d7rob\AppData\Roaming\Typora\typora-user-images\1555568148322.png){width=50%}

![eDRX](C:\Users\d7rob\AppData\Roaming\Typora\typora-user-images\1555569320664.png){width=50%}

Increasing the T3324 active timer value to 10.24s, the following results are obtained. It is exactly the same as before.

```c
AT+NPTWEDRXS=2,5,"0001","0001"
```

AT+CEREG says that the timer is 32s, or 2 seconds * 16 binary coded timer value.

```c
+CEREG: 5,1,"8CA7","28C465",7,,,"00010000","00101010"
```

In the debug logs we see the timer expires after exactly 32 seconds.

```c
2409,+00:00.400757,NAS_DBG_TIMER
	action=TIMER_START
	prim_id=USIM_STATUS_TIMER_EXPIRY
	duration=30
5981,+00:33.283905,USIM_STATUS_TIMER_EXPIRY
	timer_handle=16871576
```

[](C:\Users\d7rob\AppData\Roaming\Typora\typora-user-images\1555569718434.png){width=50%}

![Irregular eDRX time if not properly configured. \label{fig:irregular_edrx}](../images/image-20191105162759288.png)

It is important to note that if eDRX time is not configured properly, then the outcome does not show as expected as in Fig. \ref{fig:irregular_edrx}.

![Typical eDRX current profile. \label{fig:edrx_pattern}](../images/image-20191105163855934.png){width=65%}

Finally, an eDRX event has a typical current profile as shown in Fig. \ref{fig:edrx_pattern}. This shows how for the first few microseconds there is a large current spike.

*Todo: add Debug trace of eDRX*

*Todo: add Debug trace of PTAU*

### Ultra-low Current Sleep Measurements

Using an MX 58HD DMM, one can measure the microamp sleep currents of UE devices.

Testing the accuracy, 4.501 mA is measured through a 4615 ohm resistor at 21.15V. Theoretically it should be 4.582 mA so that gives an error tolerance of 1.82% or ~2%.

*Todo: measure sleep current of UE devices*

### Mobility Tests

The Sierra Wireless 7702 has a Qualcomm 9206 modem which supports LTE Cat M1, NB1 and EC-GSM.

Using a Sierra Wireless WP7702 on Ericsson Test BTS 'L06009A3' and EARFCN 3734/3752, the UE had to periodically ping an internet-facing server and the dead time was measured before it reconnected and received a response. The RSRP was in the range -50 to -80 dBm and in ECL 0.

The tests took place within a faraday cage to isolate the test network from the live RAN, else by opening the door of the faraday cage it deregistered from the network and MME.

Table: NB-IoT and LTE Cat-M handover. {#tbl:mobility}

| Mobility test         | Time   |
| --------------------- | ------ |
| Standalone to In-band | ~ 11 s |
| In-band to Standalone | ~ 11 s |

### Throughput

NB-IoT downloading was tested on the Sierra Wireless 7702 using the following script.

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

|        | Uplink              | Downlink            |
| ------ | ------------------- | ------------------- |
| GPRS   | 158 kbps or 20 kB/s | 254 kpbs or 31 kB/s |
| NB-IoT |                     | 24 kbps or 3kB/s    |
| LTE-M1 |                     |                     |



## Example Application

An example application was built to test and understand NB-IoT. See schematic and board layout in Appendix \ref{appendix_SCH_BRD}. The board includes not just NB-IoT but also LTE Cat-M, GPRS/EDGE, SigFox, LoRa, and Dash7. Initally designed to compare LPWANs, it was decided to focus more purely on NB-IoT as there is a great deal of variance among UEs and LTE vendors already.

Notable components include:

* Quectel BG96 cellular modem
* Murata CMWX1ZZABZ-078 which includes STM32L072CZ microcontroller and SX1276 transceiver 
* Atmel SAMD21G18a microcontroller
* Microchip MIC29302WU 3A LDO Regulator @3.8V

[](../images/image-20191105153024907.png){width=75%}

 ![PCB application](../images/0_MX60dijDFSoBKpuZ.jpg){width=75%} 

By adding a DHT22 temperature and humidity sensor, button and buzzer for and example application, we see the following dashboard result in Fig. \ref{fig:dashboard_thingsboard}.

![Communication via MQTT to Thingsboard cloud with temperature, humidity, push button and downlink buzzer control \label{fig:dashboard_thingsboard}](../images/image-20191105143716571.png){width=65%}

Luckily UE manufacturers usually provide a development kit with open source schemetics and board layouts. This study will use development kits so that tests are easily reproduceable.

## Setup Procedure

Each field test will make use of various UE hardware and telemetry tests and this section outlines the steps taken to perform these field tests.

### Hardware

This section outlines some of the hardware configurations required for field test captures.

#### Attenuator

Two of these will be used in series: the HP8494B and the HP8496A. One has a range of 11dB in 1dB steps, and the other has a range of 110dB in 10dB steps, so it is possible to get a full range of 110dB in 1dB steps.

 ![The Hewlett Packard attenuators used in this study to change the RF conditions for UE devices against multiple LTE vendors](../images/SgLabs_m_HP_11716A_8496B_8494B_1.JPG)

The 1 dB attenuator is useful to attenuate the signal strength until the RSRP is on a decade multiple of 10. This way variation around the decade is more visible. 

#### Current Measurements {#current_measurements}

By measuring current, the field tests can measure the energy usage of each datagram packet.

![Block diagram of current consumption setup for SARA-N2 \ref{fig:current_setup}](../images/1555535660456.png){width=65%}



The digital multimeter in Fig. \ref{fig:current_setup} is replaced with a ZXCT1008 high-side current monitor in series with the modem. 

![ZXCT1008  high-side current monitor https://www.diodes.com/assets/Datasheets/ZXCT1008.pdf](../images/arduino86-1-1571303569557.png){width=25%}

Rs is set to a 1 ohm resistor and Rg is set as a 1k ohm resistor such that 100mA supplied to the modem makes 1V.

$$V_{out} = I_{load} [mA] * 10 [\frac{V}{mA}]$$ {#eq:iload_vout}

![ZXCT1008 in action](..\images\zxct1008.jpeg)



#### Energy Capture Device {#energy_capture_device}

The energy capture device measures the energy of each packet, and also returns the duration timings of each datagram packet for latency measurements.

`PlatformIO` compiles code for the microcontroller, and in this case it is a simple Atmel ATmega328P 8-bit microcontroller.

Code can be found on [https://github.com/daniel-leonard-robinson/masters/tree/master/code/edge/src](https://github.com/daniel-leonard-robinson/masters/tree/master/code/edge/src). It connects to the ZXCT1008 mentioned in \S\ref{current_measurements} and converts the results to energy measurements. It also returns via serial to the PyTest framework the timings of each datagram packet.

```c
void energyLoop(boolean pause) {
    uint8_t reading = analogRead(A0);
    if (reading > 60) {
        if (reading > maxReading) maxReading = reading;
        if (!readCount++) {
            tStart = millis();
            idleTime = tStart - tEnd;
        }
        tEnd = millis();
        zeroM = tEnd;
        zeroCounter = 0;
        sum += reading;
        tStepCount += micros() - tStep;
    }
    else if (pause) zeroM = millis();
    else if (millis() - zeroM < 1000);
    else if (readCount) {
        txTime = tEnd - tStart;
        tStepCount /= 1000;
        energy = sum * 500 / 1023.0 * tStepCount / 1000 / 1000;
        
        buf.flush(); tx[0] = '\0'; // energyFlush();
        buf.print(idleTime); buf.print(",");
        buf.print(txTime); buf.print(",");
        buf.print(tStepCount); buf.print(",");
        buf.print(energy); buf.print(",");
        buf.println(maxReading/2);
        Serial.print(buf); // energyPrint();
        
        sum=idleTime=txTime=readCount=maxReading=energy=tStepCount= 0; // energySetup();
    }
    tStep = micros();
}
```

### Network Registration

As mentioned in \S\ref{connectivity}, the right SIM cards are necessary. It may even be possible to use e-SIMs as in Fig. \ref{fig:hologram_esim}.

![Hologram worldwide e-SIM \label{fig:hologram_esim}](../images/image-20191105152621948.png){width=40%}

Finally, the right APNs are necessary. To use MTN's test network, the APN `rflab` is used. On Vodacom's network, the APN `nbiot.vodacom.za` is used.

### PyTest Framework

PyTest is a unit testing framework used to setup the UE for each test using AT commands and can be found on  [https://github.com/daniel-leonard-robinson/masters/tree/master/code/tests](https://github.com/daniel-leonard-robinson/masters/tree/master/code/tests). Although the testing framework is quite extensive, a few snippets of code will be discussed in this section to at least give an idea to the reader how this was developed.

![`Python PyTest` framework written in `Microsoft VS Code` and test output can be seen in bottom-left window. `PlatformIO` compiles microcontroller code and uploads via `avrdude` as can be seen in bottom-right window.](../images/image-20191106145454691.png)

Every test fixture includes the following setup and teardown code to open a serial connection to the UE. It automatically detects the COM port based on the USB vid.

```python
def serialOpen():
    # setup for each test fixture
    global serAT, serTIM, serGPS, AT_PORT, uC_PORT
    ATcount = 0
    ports = serial.tools.list_ports.comports()
    for port, desc, hwid in sorted(ports):
        vid_pid = hwid.split('=')[1].split()[0]
        if vid_pid == '2341:8036':
            uC_PORT = port
        if vid_pid == '0403:6010' and not ATcount:
            AT_PORT = port
            ATcount += 1
            pytest.vendor = 'ublox'
        if vid_pid == '04E2:1414' and ATcount < 3:
            AT_PORT = port
            ATcount += 1
            pytest.vendor = 'quectel'
        if vid_pid == '0403:6001':
            AT_PORT = port
            pytest.vendor = 'simcom'
    try:
        serAT = serial.Serial(AT_PORT, 115200, timeout=1)
        serTIM = serial.Serial(uC_PORT, 115200, timeout=1)
        serGPS = serial.Serial(GPS_PORT, 9600, timeout=1)
    except serial.serialutil.SerialException as e:
        print(e)

def serialClose():
    # tear down for each test fixture
    global serAT, serTIM, serGPS
    serAT.close()
    serTIM.close()
    serGPS.close()
```

The setup and teardown functions are defined in a global file that is imported into each file of test fixtures. The location for new data in the database depends on chosen manufacturer (LTE vendor), location, file description and connected UE. The file description is the current RF attenuation and ranges from 0 to 110.

```python
def setup_module(module):
    serialOpen()
    pytest.manufacturer = 'huawei' # 'ericsson', 'nokia', 'zte'
    pytest.loc = 'mtn/testplant_14th/'
    pytest.descr = '110'
    # pytest.lock = threading.Lock()
 
def teardown_module(module):
    serialClose()
```

See Appendix \ref{appendix_pytest} to see how a Quectel or Ublox modem is set up. Running the following commands in Table \ref{tbl:pytest_setup} will set the device up.

Table: PyTest setup commands to be run in terminal {#tbl:pytest_setup}

|                      |                             |
| -------------------- | --------------------------- |
| `pytest -svm apn`    | Runs set APN fixture        |
| `pytest -svm setup`  | Runs all the setup fixtures |
| `pytest -svm reboot` | Reboots device if necessary |

The following commands are wrappers for sending and receiving AT commands:

```python
def OK(cmd, t=0):
    reply = sendAT(cmd, t)
    assert 'OK' in reply
    return reply

def expect(cmd, reply, t=1, output=True):
    replies = reply
    if str(type(reply)) == "<class 'str'>":
        replies = [reply]
    data = sendAT(cmd, t, replies, output)
    if not len(replies[0]):
        return data
    check = False
    for r in replies:
        if len(r):
            if True in [r in i for i in data]:
                check = True
                break
    if not check:
        print(magenta + str(replies), data)
    assert check
    return data

def sendAT(cmd, t=0, expect=['OK'], output=True):
    if output:
        print(yellow + cmd)
    serAT.write(bytes(cmd + '\r', 'utf-8'))
    return receiveAT(t, expect, output)

def receiveAT(t=0, expect=['OK'], output=True):
    if str(type(expect)) == "<class 'str'>":
        expect = [expect]
    c = 0
    data = []
    exp = expect[:]
    exp.append('ERROR')
    exp.append('FAILED')
    while True:
        d = serAT.readline().decode('utf-8')
        if not len(d):
            c += 1
        d = d.strip()
        if len(d) > 0:
            if output:
                print(cyan + d)
            out = converter(d)
            if out:
                print(magenta + out)
            data.append(d)
        if t > 0:
            if c >= t:
                data.append('timeout')
                return data
        for e in exp:
            if e in d:
                return data
```

Finally, the testing framework has a `capture` command which is blocking until an energy capture event. In this event the energy is sent via serial from the energy capture device (\S\ref{energy_capture_device}) and triggers the testing framework to extract information from the `AT+NUESTATS="RADIO"` command.

```python
def receiveTIM():
    data = {}
    serTIM.flush()
    d = serTIM.readline().decode('utf-8') # d = '2300,260,2560,10.0,100,'
    if len(d):
        try:
            d = d.strip() # print(magenta + d)
            data['idleTime'] = int(d.split(',')[0])
            data['txTime'] = int(d.split(',')[1])
            data['totalTime'] = int(d.split(',')[2])
            data['energy'] = float(d.split(',')[3])
            data['maxCurrent'] = float(d.split(',')[4])
        except (ValueError, IndexError) as e:
            print(red + d)
            raise e
    return data
```

### Telemetry Tests

Telemetry tests measure various aspects of the required metrics. Running the following commands in Table \ref{tbl:pytest_run} will run through the desired telemetry test.

Table: PyTest telemetry test commands to be run in terminal {#tbl:pytest_run}

|                     |                                     |
| ------------------- | ----------------------------------- |
| pytest -svm release | UDP test for multiple payload sizes |
| pytest -svk ptau    | Run PTAU test                       |
| pytest -svk drx     | Run eDRX test                       |
| pytest -svm reg     | Run COPS test                       |
| pytest -svk echo    | Runs echo test                      |


#### UDP {#udp}

UDP is used primarily for establishing low-latency and loss-tolerating connections between applications on the internet.

To test the capability of sending to the internet for multiple UEs, a simple protocol is necessary. TCP, MQTT, CoAP and other protocols are all based on the same IP infrastructure that UDP uses, yet not all UEs have this capability. UDP will be used and other protocols can be tested against it.

This test sends a UDP packet to an internet accessible IP address. The IP is 1.1.1.1 and it belongs to Warp which claims to be the fastest DNS resolver in the world, with OpenDNS, Google and Verisign taking the next respective rankings.

As an alternative, data can be sent to the u-blox echo server at echo.u-blox.com. Because there is no DNS lookup function in the SARA-N2 module series, the server IP address that must be used is 195.34.89.241.

UDP datagrams are sent with payloads of size 1, 16, 64, 128, 256 and 512 bytes.

Here is a snippet of one of the test fixtures for Ublox sending a 16 byte UDP payload with Release Assistance flags set.

```python
@pytest.fixture(autouse=True)
def _config(request):
    pytest.test = 'release/'

...
@pytest.mark.release
def test_release_release16(request):
    pytest.subtest = request.node.name.split('_')[-1] + '/'
    if pytest.vendor == 'ublox':
        expect('at+nsocl=0', '')
        receiveAT(1)
        for i in range(5):
            OK('AT+NSOCR="DGRAM",17,14000,1')
            expect('AT+NSOSTF=0,"1.1.1.1",7,0x200,16,"FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF"',
                   '+CSCON: 0', 300)
            OK('at+nsocl=0')
            capture(1)
    ...
```

#### Periodic Tracking Area Update (PTAU)

This snippet sets up the eNodeB to schedule a PTAU event every 4 seconds (roughly ~5.5 seconds actual).

```python
...
@pytest.fixture(autouse=True)
def _config(request):
    pytest.test = 'ptau/'

def test_ptau_set(request):
    pytest.subtest = request.node.name.split('_')[-1] + '/'
    setEDRX(4, 1, 0, 0, 3, 2) # 5.5 sec ptau
    capture(1)

def test_ptau_capture(request):
    pytest.subtest = request.node.name.split('_')[-1] + '/'
    capture(10)
```

#### Extended Discrete Reception (eDRX)

This snippet sets up the eNodeB to schedule a DRX event every 2.56 seconds.

```python
...
@pytest.fixture(autouse=True)
def _config(request):
    pytest.test = 'drx/'

def test_drx_set(request):
    pytest.subtest = request.node.name.split('_')[-1] + '/'
    setEDRX(4, 1, 2, 5, 6, 2) # 2.56 continuous
    capture(1)

def test_drx_cap(request):
    pytest.subtest = request.node.name.split('_')[-1] + '/'
    capture(10000)
```

#### Cellular Operator Selection (COPS)

Network Registration is necessary when the device is not yet connected. In Figure \ref{fig:lengthy_inactive}, An initial test was performed with AT+COPS=0 network registration until T3412 timeout of 270 seconds and peak current approximately 70mA.

[](C:\GIT\masters\thesis\images\active_time.JPG)



![`AT+COPS=0` network registration on MTN-ZTE network with lengthy inactivity timer setting of 270s. \label{fig:lengthy_inactive}](C:\GIT\masters\thesis\images\activetime.jpg){width=50%}

This snippet registers the UE device on the network and as a workaround to shorten a long C-DRX inactivity timer of 10, 20 seconds or more (even up to ~265 seconds) it sends a UDP packet with a flag which tells the eNodeB that it would like to release the connection immediately, hence Release Assistance.

```python
...
@pytest.fixture(autouse=True)
def _config(request):
    pytest.test = 'cops/'

############## reg release ##############
@pytest.mark.reg
def test_cops_register2(request):
    pytest.subtest = request.node.name.split('_')[-1] + '/'
    flushTIM()
    expect('AT+CFUN=1', 'OK', 3)
    expect('AT+COPS=0', ['+CEREG: 1', '+CSCON: 0', '+CEREG:1', '+CSCON:0'], 300)

@pytest.mark.reg
def test_cops_release(request):
    pytest.subtest = request.node.name.split('_')[-1] + '/'
    fetchTIM()
    if pytest.vendor == 'ublox':
        expect('at+nsocl=0', '')
        receiveAT(1)
        OK('AT+NSOCR="DGRAM",17,14000,1')
        receiveAT(1)
        expect('AT+NSOSTF=0,"1.1.1.1",7,0x200,1,"FF"', '+CSCON: 0', 100)
        OK('at+nsocl=0')
    elif pytest.vendor == 'quectel':
        ...
        ...
    receiveAT(1)
    receiveAT(1)
    fetchTIM()
    capture(1, 3)

############## dereg release ##############
@pytest.mark.reg
def test_cops_deregister(request):
    pytest.subtest = request.node.name.split('_')[-1] + '/'
    OK('AT+COPS=2', 5)
    receiveAT(300, ['+NPSMR:'])
    flushTIM()
    capture(1, 20)
...
```

#### Echo

This test is designed to measure client and server initiated echo requests.

[](../../code/tests/logs/huawei_vodacom/quellerina/ublox/echo/3.bmp)

![Echo Test](../images/image-20191106153552851.png){width=50%}

The following snippet shows how the framework sends to a custom echo server which responds immediately and then the echo server responds again after a ten second delay.

```python
...
def test_echo_send(request):
    pytest.subtest = request.node.name.split('_')[-1] + ('512/' if big else '/')
    if pytest.vendor == 'ublox':
        expect('at+nsocl=0', '')
        receiveAT(1)
        OK('AT+NSOCR="DGRAM",17,4444')
        if big:
            expect('AT+NSOSTF=0,"34.74.25.60",5555,0x400,512,"33333333333333333333...
                   ... ... ... 3333333333333333333 ... ... ...
                   ...3333333"', '+NSONMI: 0', 300)
        else:
            expect('AT+NSOSTF=0,"34.74.25.60",5555,0x400,3,"313232"', '+NSONMI: 0', 300)
        receiveAT(1, '+CSCON: ')
        OK('AT+NSORF=0,512', 3)
    ...
    capture(1, 8)
...
```

The custom echo server has a static IP (34.74.25.60) and is open on port 5555.


```python
...
def receive_next(sock):
    "Repeatedly tries receiving on the given socket until some data comes in."
    logger.debug("Waiting to receive data...")
    while True:
        try:
            BUFFER_SIZE = 4096 # the buffer for receiving incoming messages
            return sock.recvfrom(BUFFER_SIZE)
        except socket.timeout:
            logger.debug("No data received yet: retrying.")
            pass

def receive_and_send_one(sock):
    "Waits for a single datagram over the socket and echoes it back."
    input_data, addr = receive_next(sock)
    message = input_data.decode()
    output_len = sock.sendto(input_data, addr)
    sleep(10) # 10 second delay before echoing back again
    output_len = sock.sendto(input_data, addr)

def start(args):
    "Runs the server."
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.settimeout(5) # seconds
    sock.bind((args.host, args.port))
    logger.info("Listening on %s:%s.", args.host, args.port)
    try:
        for i in itertools.count(1):
            receive_and_send_one(sock)
    ...
```



#### Ping 

The +NPING AT command can be issued to check if the module is able to send and receive data via the internet, or an internal network location.
To ping Google’s DNS server:
AT+NPING="8.8.8.8"

The information text response to the +NPING AT command will be issued after a few seconds. If the
information text response is +NPINGERR: 1, the ping has timed out (usually within 10 seconds). The first ping might fail because it can take a few seconds to connect to the base station. Use
the +CSCON URC to show when the module is connected.

Whilst the simple `Ping` command is useful to measure connectivity and latency, it unfortunately has no way to release the inactivity timer by itself, which means the modem continues to consume current in receive-mode/C-DRX. That is why the `Echo` telemetry test was designed.

## Primary Metrics

### Power Efficiency

Power efficiency is one of the main metrics focused on in this study. This section outlines a few preliminary tests and the design for the final field tests comparing UEs and MNOs.

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

* **Power consumption**: In applications where device battery life is
  a crucial factor we recommend, either LoRaWAN or Sigfox, because they are completely asynchronous. We found that the battery life of LoRaWAN SF 7 was five times that of LoRaWAN SF 12 and nearly 25 times that of Sigfox. This is mainly due to the extremely long time-on-air of LoRaWAN SF 12 and Sigfox. If NB- IoT worked with the mobile network operators to reduce its RRC- idle phase, it could develop a minimal power consumption to compare with that of LoRaWAN and Sigfox.
  * It is clear that LoRaWAN SF7 is the most power-efficient, due to the short transmission burst. NB-IoT displays the worst power-consumption, due to the extended RRC-idle state. This can be reduced using Release Assistance as in \S\ref{release_a}.

#### Energy versus SINR

![Ublox (blue) and Quectel (red) energy (J) per datagram as a function of the SINR (dB) as reported by the UE on the MTN-ZTE network limited to 1500 mJ.\label{fig:energy_sinr1400}](../images/1571781182963.png){width=65%}

With the fading colour scheme and range just as in Martinez [@Martinez2019], Fig. \ref{fig:energy_sinr1400} shows the impact of SNR on energy consumption. As observed in the figure, there is a trend of increasing energy with respect to lower SNR levels and high variability. Unfortunately, the effect of different ECLs is unclear.

![Ublox (blue) and Quectel (red) energy (mJ) per datagram as a function of the SINR (dB) as reported by the UE on the MTN-ZTE network.\label{fig:energy_sinr_log}](../images/1571781152992.png){width=65%}

Increasing the range fully and using logarithms in Fig. \ref{fig:energy_sinr_log}, one can see that there is significant overshoot on the MTN-ZTE network. The trend mentioned in Fig. \ref{fig:energy_sinr1400} continues.

[](../images/1571785381395.png)

#### Energy versus Datagram Size

[](../../code/tests/datagrams/mtn_ublox_energy.png)

[](../../code/tests/datagrams/quectel_sizes.png){width=65%}

\begin{figure}[ht]
  \subfloat[Datagram sizes of MTN-Ublox pair up to 1500 mJ. Note the steady increase in Energy consumption on the baseline, and the high variation.]{
	\begin{minipage}[c][1\width]{
	   0.48\textwidth}
	   \centering
	   \includegraphics[width=1.0\linewidth]{../../code/tests/datagrams/mtn_ublox_energy.pdf}
	\label{fig:udpsize1}
	\end{minipage}}
 \hfill 	
  \subfloat[Datagram sizes of MTN-Quectel pair up to 10 J]{
	\begin{minipage}[c][1\width]{
	   0.48\textwidth}
	   \centering
	   \includegraphics[width=1.0\linewidth]{../../code/tests/datagrams/quectel_sizes.png}
	\label{fig:udpsize2}
	\end{minipage}}
\captionof{figure}[UDP Datagram energy-sizes]{UDP Datagram energy-sizes}
\end{figure}

Fig. \ref{fig:udpsize1} shows 

#### eDRX Energy

\begin{figure}[ht]
  \subfloat[MTN-ZTE Ublox]{
	\begin{minipage}[c][1\width]{
	   0.48\textwidth}
	   \centering
	   \includegraphics[width=1.0\linewidth]{../images/1568090120083.png}
	\end{minipage}}
 \hfill 	
  \subfloat[MTN-ZTE Quectel]{
	\begin{minipage}[c][1\width]{
	   0.48\textwidth}
	   \centering
	   \includegraphics[width=1.0\linewidth]{../images/1568090147760.png}
	\end{minipage}}
\captionof{figure}[eDRX Energy]{eDRX Energy}
\end{figure}

[](../images/1568090120083.png){width=45%}

[](../images/1568090147760.png){width=50%}

\begin{figure}[ht]
  \subfloat[Vodacom-Nokia Ublox]{
	\begin{minipage}[c][1\width]{
	   0.48\textwidth}
	   \centering
	   \includegraphics[width=1.0\linewidth]{../images/1568090173885.png}
	\end{minipage}}
 \hfill 	
  \subfloat[Vodacom-Nokia Quectel]{
	\begin{minipage}[c][1\width]{
	   0.48\textwidth}
	   \centering
	   \includegraphics[width=1.0\linewidth]{../images/1568090209468.png}
	\end{minipage}}
\captionof{figure}[eDRX Energy]{eDRX Energy}
\end{figure}

[](../images/1568090173885.png){width=65%}

[](../images/1568090209468.png){width=65%}

#### PTAU Energy

\begin{figure}[ht]
  \subfloat[MTN-ZTE Ublox (mJ)]{
	\begin{minipage}[c][1\width]{
	   0.48\textwidth}
	   \centering
	   \includegraphics[width=1.0\linewidth]{../images/1568089886942.png}
	\end{minipage}}
 \hfill 	
  \subfloat[MTN-ZTE Quectel (mJ)]{
	\begin{minipage}[c][1\width]{
	   0.48\textwidth}
	   \centering
	   \includegraphics[width=1.0\linewidth]{../images/1568089931848.png}
	\end{minipage}}
\captionof{figure}[PTAU Energy]{PTAU Energy}
\end{figure}

[](../images/1568089886942.png){width=65%}

[](../images/1568089931848.png){width=65%}

\begin{figure}[ht]
  \subfloat[Vodacom-Nokia Ublox (J)]{
	\begin{minipage}[c][1\width]{
	   0.48\textwidth}
	   \centering
	   \includegraphics[width=1.0\linewidth]{../images/1568090001158.png}
	\end{minipage}}
 \hfill 	
  \subfloat[Vodacom-Nokia Quectel (J)]{
	\begin{minipage}[c][1\width]{
	   0.48\textwidth}
	   \centering
	   \includegraphics[width=1.0\linewidth]{../images/1568090070185.png}
	\end{minipage}}
\captionof{figure}[PTAU Energy]{PTAU Energy}
\end{figure}

[](../images/1568090001158.png){width=65%}

[](../images/1568090070185.png){width=65%}

#### Measured Max Current

[](../../../masters/code/tests/plotterk/Signal_power_maxCurrent_plot.png)

roughly between 70 and 120mA, and skewed towards higher consumption. It is also clamped at 128mA due to measurement limitations. 

(A) Attenuation zones evident. (B) Both MTN and Vodacom share similar distributions of max current usage. (C) Tests are varied, yet UDP packet transmission tend to use more current. (D) ECL does not affect current usage.

\begin{minipage}{\linewidth}
\begin{center}
\includegraphics[width=1.0\linewidth]{../../../masters/code/tests/plotterk/maxCurrent_histogram.pdf}
\captionof{figure}[Max current of packets histogram]{The latency-energy measurement hardware is limited to 128mA, and therefore we can see some clamping here. It shouldn't affect the energy readings much however, as maximum current occurs only during the first few microseconds of the random access preamble.}
\label{fig:}
\end{center}
\end{minipage}

[](../../../masters/code/tests/plotterk/maxCurrent_histogram.png)

### Latency and Timing

Latency and timing is also one of the main metrics focused on in this study. This section outlines a few preliminary tests and the final design of field tests.

* **Down link latency**: In applications where downlink latency is a
  critical component, only GPRS will suffice, as it is the only technology in this study that requires constant paging between the base station and the end device. 
* **Down link throughput**: Any applications requiring bi-directional communication of more than 120 bytes per 24 h, should use NB- IoT or GPRS, as Sigfox and LoRaWAN are limited by the duty- cycle limitations of the base station. 

#### TX, RX Time

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

#### Latency vs SINR

![Latency per datagram as a function of the SINR (dB) as reported by the UE on the (D) MTN-ZTE and (E) Vodacom-Nokia network respectively.\label{fig:latency_sinr_comp}](../images/1571781751620.png){width=50%}

In Fig. \ref{fig:latency_sinr_comp}, there is a poor distinction between attenuation zones as the SINR varies throughout the reported RSRP range. Grouping the data according to attenuation decade is important to see the effect of network conditions clearly.

## Secondary Metrics

![LTE RSRQ and SINR RF Conditions](../images/LTE-RF-Conditions.png)

Tests were completed in good, mid cell and cell edge RF conditions.

### Signal Strength

Signal strength can be measured using the following metrics:

* MCL
* RSRP
* RSSI
* RSRQ
* SNR
* TX Power

#### MCL

For IoT devices used in extended coverage situations,
such as deep-indoor devices or remote locations, we recommend either Sigfox or NB-IoT, as they offer a maximum MCL of more than 158 dB. IoT devices for general use would benefit from the large-scale deployment of the GPRS network, which provides excellent coverage because of its legacy infrastructure. It is clear that the extra overhead available in Sigfox, LoRaWAN, and NB-IoT allows for better indoor coverage than GPRS, which means that the LPWAN devices can be used in less than optimal operating conditions. Measured MCL correlates with theoretical values.

#### RSRP

RSRP or "Signal Power" is the power of the wanted part of the receive signal, the NB-IoT part.

![](../../../masters/code/tests/plotterk/Signal_power_histogram.png)

#### RSSI

RSSI or "Total Power" in terms of UE reports, is the radio signal strength within the receive bandwidth (both expressed in 10ths of a decibel). From this the signal to noise ratio can be calculated.

![RSSI](../images/image-20191112172439750.png){width=50%}

#### SNR

Last SNR value.

#### RSRQ

**RSRQ = N x RSRP / RSSI**

![LTE RSRQ reporting range](../images/CableFree-LTE-RSRQ-reporting-range.png)

- N is the number of Physical Resource Blocks (PRBs) over which the RSSI is measured, typically equal to system bandwidth
- RSSI is pure wide band power measurement, including intracell power, interference and noise
- The reporting range of RSRQ is defined from -3…-19.5dB

[](../../../masters/code/tests/plotterk/RSRQ_histogram.png)

![RSRQ](../images/image-20191112173112378.png)

#### Transmit power

* It is the RF power output from the module. It may be a low number if the
  received signal strength is good (and hence the module assumes that the base station is close
  by).
* Ideally the module
  should consume 230 mA for +23 dBm.

#### ECL

  It is equivalent to "PRACH coverage enhancement level" defined in 3GPP 36.321 [3] sub
  clause 5.1

  * As observed, the ECL has an impact on energy consumption, but not on the delay.

### Throughput

Data can be extracted from UDP packet transmissions using latency and data size

$THP = \frac{Datagram\ Size}{Latency}$

It also comes from RLC and MAC reporting.



**Throughput**: As throughput differs greatly between the four technologies, comparisons should rather be made in either the licensed (NB-IoT and GPRS) or unlicensed (Sigfox and LoRaWAN) spectrum categories. Applications that require huge amounts of data to be transmitted, such as real-time vehicle fleet monitoring, we recommend GPRS and NB-IoT as they are not duty cycle limited. The choice of GPRS or NB-IoT will be based on the battery life requirements of the IoT device, with NB-IoT having the advantage. In the case of extremely low-throughput applications, such as water meters, power meters, and weather stations, we recommend Sigfox, as it offers a scalable solution with no base station costs involved. Although it limits the 12 byte throughput per 24 h to 140 messages, this is more than the 20 messages offered by LoRaWAN SF12 (TTN).

* As NB-IoT operates in the licensed spectrum, there are no
  throughput restrictions, other than the data-rate restriction. We measured the uplink and downlink data rates in different signal quality environments (distances from the gateway) by querying the modem. The measured downlink rate varied from 2250 to 14,193 bps. We could find no clear correlation between the downlink data rate and the signal quality environment.

#### FOTA Upgrades

GPRS and NB-IoT are able to offer FOTA upgrades to IoT devices, as Sigfox has limited bandwidth. This feature is supported by LoRaWAN, through the fragmentation of large payloads [22].

### Data Overhead

Variation in data overhead can be measured using TX, and RX byte counters.

* The module has a limited dynamic message queue size. For IoT applications, the message size should be of the order of tens of bytes. UDP socket commands limit their payload size to 512 bytes.
* There is no indication when the UDP data has been sent.
* Downlink data from the cloud server must also be 512 bytes or less, because otherwise the messages will be lost.
* The module has an internal message buffer. If the module is unable to send the messages to the network before this buffer is full, because the application is queueing quicker than it can send them, then the UE device will return ERROR for the +NSOST/+NSOSTF commands.
* If a message cannot be sent because of communication issues between the module and eNB, the module will attempt to send the message a second time. If this fails, the message will be dropped. As +NSOST/+NSOSTF messages are UDP, there is no indication the message has been dropped.
* The UDP header is about 48-60 bytes in length, and so an application sending 100 bytes will actually send about 160 bytes. For devices in the extreme coverage class 2, this can be quite costly.
* The UE device may later resume the RRC Connected state with that context, thus avoiding the AS setup and saving considerable signaling overhead for the transmission of infrequent small data packets.

## Estimations

A few metrics are estimated in this study.

### Telemetry Interval

The recommended telemetry interval can be estimated for a subtest.

* Telemetry interval periodicity.

### Battery longevity

The battery longevity can be estimated for each subtest.

## Field Test Captures

Ublox and Quectel data has been captured for:

* Nokia networks at Vodacom head office in Century City, Cape Town
* ZTE at the MTN Mobile Intelligence Lab, Stellenbosch inside an RF enclosure with the door slightly open before being sealed.
* Ericsson at MTN headquarters on 14th Avenue, Johannesburg
* Huawei in Fairlands, JHB

### Dataset

Every UE device and MNO pair (4 total) has 7 main tests and each has its own attenuation zone (5 total). 424 files create a dataset with 1811 trace entries, 40 possible metrics and 79921 values.

Looking at the dataset as a whole this makes 140 unique outcomes (7x4x5). There are 15 subtest types which can be delved into, too.

The dataset is also heavily skewed towards lower latency entries. Tests were repeated with the intent of increasing reliability, especially when it takes a couple of seconds, but when a test took up to 300 seconds it had a much lower chance of being repeated. Also considering that dataset capture may be repeated in different locations, one does not necessarily want to spend more than a day on-site.

To solve for the skewness, each test can be normalized by taking a single mean of each of the associated trace entries and files. Now with a dataset of 140/1811 traces, it makes a minimum of 5600/79921 possible values.

Unfortunately this created problems especially where only a few discrete values are concerned, such as in ECL, as multiple means exist. To solve this, k-means clustering is applied.

### Post-processing

#### Probability estimation

Due to the large dataset and requiring a reasonable means of visualization, we can consider a histogram.

\begin{figure}[ht]
  \subfloat[Example python histogram of a univariate latency distribution showing counts]{
	\begin{minipage}[c][1\width]{
	   0.48\textwidth}
	   \centering
	   \includegraphics[width=1.0\linewidth]{../../code/tests/old/img2/histogram_counts.pdf}
	\end{minipage}}
 \hfill 	
  \subfloat[Histogram counts vary among various datasets when their sizes differ, so it would be a good idea to normalize it such that the area under the graph makes 1.0. The probability of the discrete data can also be estimated in a continuous probability density function (PDF) with the kernel density estimation.]{
	\begin{minipage}[c][1\width]{
	   0.48\textwidth}
	   \centering
	   \includegraphics[width=\linewidth]{../../code/tests/old/img2/probability_density_function_seaborn.pdf}
	\end{minipage}}
\captionof{figure}[Probability estimation on histogram latency sample]{Probability estimation on histogram latency sample}
\end{figure}

[](../../code/tests/old/img2/histogram_counts.png)

[](../../code/tests/old/img2/probability_density_function_seaborn.png)

\begin{figure}[ht]
  \subfloat[Various types of kernel density estimation (KDE)]{
	\begin{minipage}[c][1\width]{
	   0.48\textwidth}
	   \centering
	   \includegraphics[width=\linewidth]{../../code/tests/old/img2/probability_density_function.pdf}
	\end{minipage}}
 \hfill 	
  \subfloat[Various types of kernel density estimation (KDE) with histogram and KDE normalized in attempted probability mass function]{
	\begin{minipage}[c][1\width]{
	   0.48\textwidth}
	   \centering
	   \includegraphics[width=\linewidth]{../../code/tests/old/img2/probability_mass_function.pdf}
	\end{minipage}}
\captionof{figure}[Probability estimation on histogram latency sample]{Probability estimation on histogram latency sample}
\end{figure}

[](../../code/tests/old/img2/probability_density_function.png)

If the histogram bin values are normalized by dividing by the bin count, adding the values makes 1 instead of integrating along the x-axis. Similarly, multiplying the PDF by its x-axis gives the following result. Although all the plotted values are now truly under 1, the KDE is shifted and doesn't seem usable.  The integration to 1 visualization typical in statistics has to be used.

[](../../code/tests/old/img2/probability_mass_function.png)

In fact, good practice would be viewing the data as is and not trying to analyze it from what is essentially an entirely new perspective. Thus, the data will be viewed as 2D plotted points and histograms. Colour will be used to group the data according to attenuation and packet size.

#### K-Means Clustering

Instead of finding a single mean for all the entries and associated files, at least two means are specified (K=2) to take into account the outliers that some tests produce or more if discrete values are involved or isolated regions (K=3+).

\begin{minipage}{\linewidth}
\begin{center}
\includegraphics[width=0.8\linewidth]{../../../masters/code/tests/plots/dpoints.pdf}
\captionof{figure}[K-means clustering]{Trace entries per test. Absolute maximum of 1811 traces has been reduced by removing duplicates and applying thresholds. K-means clustering achieves the desired effect of reducing dimensionality and skewness induced from low latency sampling on the dataset for different tests, yet keeps most of the features of the thresholded max.}
\label{fig:}
\end{center}
\end{minipage}

[](../../../masters/code/tests/plots/dpoints.png)

#### Plot Visualization {#plots}

- what aspect is the plot trying to cover, what is it telling me on that topic, shows? observances?
- purpose
- data in the plot saying / deduce / narrative / story
  - Example, Quectel, Vodacom is worse
- 4 sentences
- 4 sentences when comparing nw, and tehn again ues
- What is the take home?



* what aspect is the plot trying to cover
* what is it telling me on that topic
* purpose
* data in the plot saying / deduce / narrative / story
* 4 sentences
* 4 sentences when comparing nw, and tehn again ues



Jupyter is a python framework which is used for post-processing, and the following code snippet shows an example of the `9-plot` format used in the results (Chapter \ref{results}):

```python
import jupyterlib as j
import plotter as p
import plotter4 as p4

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

import importlib

def plot(*args, **kwargs):
    importlib.reload(j)
    importlib.reload(p)
    importlib.reload(p4)
    testl = ['1-16 B', '64-128 B', '256-512 B', 'Echo', 'COPS', 'eDRX', 'PTAU']
    K = kwargs.pop('K') if 'K' in kwargs else None
    p4.plot(db(), *args, **kwargs, K=K if K else 3, folder='plotterk', joburg=True,
    	testl=testl)
    
...
...
    
plot('SNR', 'txTime', 'SNR (dB)', 'Latency (s)', scale=[10,1000], K=5)
plot('Signal power', 'energy', 'RSRP (dBm)', 'Power (uWh)', [10,3.6], K=6, log=True)
```

As there are numerous Jupyter files, most code resides in custom libraries which can be imported into each file to maintain consistency in case of duplication errors, and this can also be found on  [https://github.com/daniel-leonard-robinson/masters/tree/master/code/tests](https://github.com/daniel-leonard-robinson/masters/tree/master/code/tests). During development on the custom libraries, Jupyter requires `importlib` to `reload` each library when a master function such as `plot(*args, **kwargs)` is called.

Table: Custom libraries imported by Jupyter and a description of their purpose {#tbl:jupyter_libs}

| Library    | Purpose                                                     |
| ---------- | ----------------------------------------------------------- |
| jupyterlib | processing CSV files, directories, tests, thresholds        |
| plotter    | gathering data into single dictionary database for plotting |
| plotter4   | plotting data in 9-plot format, K-means clustering          |

Other plots were more specialized and code was kept within the Jupyter file it was developed in.

---

Since it appears that ECL is the ultimate factor that should influence latency and energy usage, it is the metric used for battery life estimation as well.

## Notes

> at+natspeed=115200,30,1

> disables LPM. cannot do RSSI triangulation

https://www.etsi.org/deliver/etsi_TS/125100_125199/125133/13.00.00_60/ts_125133v130000p.pdf

> In idle mode, UE shall support DRX cycles lengths 0.64, 1.28, 2.56 and 5.12 s, according to [16] and UE shall, if it
> supports eDRX_IDLE, support eDRX_IDLE cycle lengths 10.24, 20.48, 40.96, 81.92, 163.84, 327.68, 55.36,1310.72,
> 1966.08 and 2621.44 seconds, according to TS 24.008 [32]. 

It would be a good idea to use Martinez' work and complement it.