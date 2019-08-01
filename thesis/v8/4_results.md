# Objective

Application developers and cellular service providers alike are interested in implementing NB-IoT (LTE Cat-NB) as an alternative to LoRaWAN, SigFox and other LPWANs. Application developers require network coverage, and cellular service providers require consumer and enterprise demand or reasonable motivation before rolling it out nationally. Although there is a great deal of theoretical analysis and simulations in research, the lack of empirical evidence may be contributing to the impasse of growth in the network technology. This thesis aims to bridge that divide.

## Approach

The goal is to test four UE manufacturers against four network vendors with a set of RF metrics.

| NW Vendors | UE Manufacturers | RF Metrics         |
| ---------- | ---------------- | ------------------ |
| ZTE        | Ublox            | Energy Consumption |
| Nokia      | Quectel          | Latency            |
| Ericsson   | Nordic           | Behavior           |
| Huawei     | SimCom           | Cost               |

A unit testing framework has been carefully prepared in Python in combination with a Hewlett Packard rotary RF attenuator in 10dBm steps.

The UE devices are specifically the:
   * Ublox Sara N200
* Quectel BC95
* Nordic nRF9160
* SimCom SIM7020E

# Results

Ublox and Quectel data has been captured for Nokia networks at Vodacom head office in Century City, Cape Town and for ZTE at the MTN Mobile Intelligence Lab, Stellenbosch and inside an RF enclosure with the door slightly open before being sealed.

![MTN (green, black) vs Vodacom (blue, red) Latency test](C:\GIT\masters\code\tests\img\vodacom_vs_mtn_latency.png)

![MTN (green, black) vs Vodacom (blue, red) Energy test](C:\GIT\masters\code\tests\img\vodacom_vs_mtn_energy.png)

# Remaining work and plan

The current data is in the process of being processed and visualised, with results expected next week.

\begin{itemize}
    \item Addition of Nordic and SimCom to testing framework in progress
    \item Capture data from Huawei and Ericsson from Vodacom and MTN in Johannesburg end of August.
    \item Write up thesis and complete end of September
\end{itemize}