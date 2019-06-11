# Research design and methodology

## framework

* mini intro
  * 64 tests. 4x4x4. cost, time, power consumption, signal strength. 4 BSS. 4 UE.
* mini lit review
  * 
* methodology
  * 
* results
* discussion
* conclusion

Making use of what is available in South Africa, there are four manufacturers, and going to use four endpoints.

The documentation describes that the trace function in m-center is used to collect logs for u-blox internal technical team to analyze.

https://github.com/fgsect/scat

https://github.com/openpst/libopenpst

Most oscilloscopes cannot do seamless data logging.

At what range does class 0 require 23 dBm?

What endpoint tests can I make?

* I can measure the RSSI
  * PDR
  * Connection / disconnection
  * COPS registration time
  * Current usage
  * Ping time

Reuse dev kits. Attach RF attenuator for me only.

What tests can be performed among multiple manufacturers?

The most generic test which also takes into account

| Description                    | Current usage | Completion time |
| ------------------------------ | ------------- | --------------- |
| Manual network registration    | Yes           | Yes             |
| Automatic network registration | Yes           | Yes             |
| Search for network operators   | Yes           | Yes             |
| Minimum functionality.         | Yes           | No              |
| Full functionality             | Yes           | No              |
| Network time                   | No            | No              |
| Reboot                         | Yes           | Yes             |
| RSRP                           | Yes           | No              |
| RSSI                           | Yes           | No              |
| Transmit power                 | Yes           | No              |
| Transmit time                  | Yes           | Yes             |
| Receive time                   | Yes           | Yes             |
| Cell id                        | No            | No              |
| Extended Coverage Level        | Yes           | No              |
| SNR                            | Yes           | No              |
| EARFCN                         | No            | No              |
| PCI                            | No            | No              |
| RSRQ                           | Yes           | No              |
| Cell tower info                | No            | No              |

Table showing Ublox tests

| **ZTE** | Ublox | Quectel | Nordic | SimCom |
| ------- | ----- | ------- | ------ | ------ |
| Cost    | 1     | 2       | 3      | 3      |
| Current | 1     | 2       | 3      | 3      |
| Time    | 1     | 2       | 3      | 3      |
| RSSI    | 1     | 2       | 3      | 3      |

| **Nokia** | Ublox | Quectel | Nordic | SimCom |
| --------- | ----- | ------- | ------ | ------ |
| Cost      | 2     | 2       | 3      | 3      |
| Current   | 2     | 2       | 3      | 3      |
| Time      | 2     | 2       | 3      | 3      |
| RSSI      | 2     | 2       | 3      | 3      |

| **Ericsson** | Ublox | Quectel | Nordic | SimCom |
| ------------ | ----- | ------- | ------ | ------ |
| Cost         | 4     | 4       | 4      | 4      |
| Current      | 4     | 4       | 4      | 4      |
| Time         | 4     | 4       | 4      | 4      |
| RSSI         | 4     | 4       | 4      | 4      |

| **Huawei** | Ublox | Quectel | Nordic | SimCom |
| ---------- | ----- | ------- | ------ | ------ |
| Cost       | 4     | 4       | 4      | 4      |
| Current    | 4     | 4       | 4      | 4      |
| Time       | 4     | 4       | 4      | 4      |
| RSSI       | 4     | 4       | 4      | 4      |

| **Key** |               |
| ------- | ------------- |
| White   | Not attempted |
| Orange  | In progress   |
| Green   | Complete      |
| Red     | Not possible  |
| Grey    | Uncertain     |

## UE Monitor

!UICC && !Unknown && !LL1 && !RRC && !IND && !NAS && !REQ && !REPORT && !RLC && !MAC && !CNF && !Serving

## which tests?

There are many questions asked when it comes to the use of a wireless technology. Since there are multiple manufacturers one can expect differences in performance. When choosing a module in scalable projects, one typically looks for a balance between high performance and low cost. In high performance one expects quality, reliability, and long battery life. It must be able to connect seamlessly and from expected range. Besides the cost of the modem one also expects a low external parts count, minimal data overhead and longevity of device lifetime.

This thesis will focus on four main themes, namely cost, time, power consumption and signal strength. 

## why cost?

Cost is important to take into consideration for capital and operating expenses. Upfront costs include the modem, external parts and integration. Operating costs include the data payloads and data overhead which developers may not take into consideration. On the RRC layer, there is signaling between the UE and BSS, but only on the NAS and IP layer is data charged.

What is the effect of packet size variations on the cost of the service? And on battery life?

## which endpoint manufacturers?

The following list of manufacturers have a number of modules, SoCs and chipsets which support NB-IoT according to [@Evolution2017] and manufacturer websites.

| Manufactuer           | NB-IoT supported devices |
| --------------------- | ------------------------ |
| Quectel               | 5                        |
| Telit                 | 2                        |
| u-blox                | 6                        |
| ZTE                   | 1                        |
| Nordic                | 1                        |
| Sierra   Wireless     | 2                        |
| PyCom                 | 2                        |
| SimComm               | 1                        |
| SkyWorks              | 6                        |
| Altair Semiconductors | 1                        |
| CommSolid             | 1                        |
| Intel                 | 2                        |
| MediaTek              | 1                        |
| Neul                  | 1                        |
| Qualcomm              | 2                        |
| Sequans               | 2                        |

The following list of manufacturers have been tested to see if they are supported according to Vodacom, MTN and RF Design:.

| Manufacturers  |
| -------------- |
| Quectel        |
| u-blox         |
| Nordic         |
| SimComm        |
| Telit          |
| SierraWireless |

Since the goal of the research is to evaluate NB-IoT, a number of devices will be tested and the resulting differences investigated. Due to availability and cost limitations, the following four are chosen.



| Manufacturers |
| ------------- |
| Quectel       |
| u-blox        |
| Nordic        |
| SimComm       |

## why time?

With the UE at a certain range from the BSS, NB-IoT uses increased RACH repetitions to maintain connection. For the majority of use cases a packet makes a round trip within 130 - 250ms, but at the edge of coverage it increases drastically up to 10 seconds. This can be detrimental to battery life, especially when considering how SigFox takes roughly 6 seconds to transmit a message.

What is the effect of high / low SNR on COPS registration?

## why power consumption?

Power consumption and profiling is important to note amongst various manufacturers.

## why signal strength?

Probably one of the most useful tests is a drive by test in a generic town which has one or more base stations. The different decades of signal strength from -50 dBm to -113 dBm can be shaded on a colour-key. Points of disconnection can be analyzed, discussed and suggestions can be made.

There are two kinds, an idle mode test and a constant iperf connection test.

Lastly, an RF attenuator will be used to see the effect of changing the signal strength in a controlled manner such that the effect on time, packet size and power consumption can be consistently measured, especially considering the base station is in control of the UE.

## measuring T3324, T3412 timers

The following code converts binary strings to actual time. It is based off Table 10.5.5.32/3GPP in TS 24.008.

```python
## T3412
def extended_periodic_TAU(bin_str):
    mul = {}
    mul['000'] = [10, 'minutes']
    mul['001'] = [1, 'hours']
    mul['010'] = [10, 'hours']
    mul['011'] = [2, 'seconds']
    mul['100'] = [30, 'seconds']
    mul['101'] = [1, 'minutes']
    mul['110'] = [320, 'hours']
    mul['111'] = [0, 'deactivated']

    if bin_str[:3] in mul:
        t = mul[bin_str[:3]]
        return str(t[0] * int(bin_str[3:], base=2)) + ' ' + t[1]
    return 'failed'

## T3324
def active_time(bin_str):
    mul = {}
    mul['000'] = [2, 'seconds']
    mul['001'] = [1, 'minutes']
    mul['010'] = [1, 'deci-hours']
    mul['111'] = [0, 'deactivated']

    if bin_str[:3] in mul:
        t = mul[bin_str[:3]]
        return str(t[0] * int(bin_str[3:], base=2)) + ' ' + t[1]
    return 'failed'

def p(i):
    return extended_periodic_TAU(i)

def a(i):
    return active_time(i)

def cereg(at_str):
    arr = at_str.split(',')
    print(at_str)
    return 'Active T3324: ' + a(arr[7].split('"')[1]) \
     + ', Periodic T3412: ' + p(arr[8].split('"')[1])
```