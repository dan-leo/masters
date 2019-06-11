## Intro edit

![sms_usage](../notebooks/sms_usage.png)

<!---Facebook, penetration
Africa
World Bank-->

Due to high user demand in bandwidth-hungry applications such as voice, video and file sharing, it evolved into 3G and 4G LTE which is currently in use today in the form of VoIP and IMS. Since the more affordable packet switched networks can handle more bandwidth than circuit switched networks, the transition is sensible.

![ims voip](C:\GIT\masters\thesis\images\ims voip.jpg)

That left 2G/GPRS to serve as a gateway for smart devices and sensors in the M2M sphere, but due to its high-powered nature it is not sustainable for applications which require battery longevity of up to 10 years or more. 3GPP developed dedicated LPWAN technologies to serve this purpose. In lieu of its absence, although the spectrum it held can be re-farmed for cellular LPWANs, it also opens up opportunities for market entrants of unlicensed frequencies such as LoRaWAN and SigFox. Each LPWAN technology has its own unique flaws and benefits and there is yet to be a clear winner when it comes to connecting 'things' to the internet. In South Africa, there is a push by at least two major cellular service providers to adopt a cellular LPWAN to fill the void left behind by 2G/GPRS now and in the future. NB-IoT is being investigated by MTN South Africa, and since they are also funding this research, have also provided network coverage for testing to Stellenbosch University. Ideally, the technology can be rolled out to existing base stations as a software upgrade for national coverage, but it is limited by factors such as use case demand, expensive licensing and general uncertainty about the technology. This thesis aims to highlight the challenges, advantages and disadvantages of the technology. By doing endpoint tests with multiple manufacturers and base station vendors, one can paint an accurate picture of the capabilities of the technology. The technology is robust in certain test cases and scenarios, but additional work is required from the 3GPP to enhance the technology.

<!---*According to the World Bank, there is approximately 1 cellular subscription for every person around the world. The number of cellular subscriptions range from 75% of the population in Sub-Saharan Africa to 125% in Europe and Central Asia which indicates that certain technologies, standards and protocols causes contention. One of them is NB-IoT, which is an LTE-based wireless technology which takes on the likes of LoRaWAN and SigFox.*-->

<!---Who is my target audience? Researchers, IoT enthusiasts. Myself.*-->

## Perspectives in SA

[https://www.flickswitch.co.za/nb-iot-rollout-in-south-africa/](https://www.flickswitch.co.za/nb-iot-rollout-in-south-africa/)

## Ublox perspective

> NB-IoT technology is designed such that it can be used in areas beyond the radio coverage of current cellular standards and in devices which must run from battery power for many years. The devices will generally send small amounts of data infrequently; a typical usage scenario might be 100 to 200 bytes sent twice per day for battery powered devices. For mains powered devices the limit is not based on battery size, but cost and network bandwidth/resources.

> The system operation is analogous to SMS in that it is a datagram-oriented, stored-and-forward system, rather than a GPRS-like IP pipe. This is because NB-IoT devices spend most of their time asleep, making possible the required long battery life. The system implements extended DRX cycles for paging, but as this window will be limited to save battery life, the delivery of downlink messages occurs mainly when the system detects that uplink messages have been received from a device (indicating that it is awake). Here a store-and-forward system, an “IoT Platform”, is useful. [@ubloxAppNote2018]

## News

NB-IoT Release 14 modems have been released this 2019.

<https://blog.nordicsemi.com/getconnected/att-launches-nb-iot-network-in-usa>

## NB-IoT new release overview

In LTE Release 14, NB-IoT has new features which include positioning, multicast, and a new UE output power class, whereas the system and UE throughput, non-anchor carrier operation, mobility, and service continuity are further enhanced [@Hoglund2017].

Furthermore, currently the work for LTE Release 15 NB-IoT is ongoing, and new features are introduced to further improve the NB-IoT battery life and latency and improve performance in more use cases [10].

## LPWAN comparison

**What LPWANs exist out there, and which ones are bi-directional?**

| LPWAN      | Bi-directionality |
| ---------- | ----------------- |
| NB-IoT     | Yes               |
| Dash7      | Yes               |
| SigFox     | No                |
| LoRaWAN    | No                |
| EC-GSM-IoT | Yes               |
|            |                   |
|            |                   |

