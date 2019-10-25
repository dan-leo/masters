LTE Cat-NB (Narrowband) characterization of user equipment (UE) and mobile network operators (MNOs)



|      |      |      |
| ---- | ---- | ---- |
| Total free memory    | 11929.1 | 11947.7 |
| Max free memory      | 10985.3 | 10984.9 |
| Num Allocs memory    | 1910.4  | 1292.8  |
| Num Frees memory     | 1770.3  | 1147.1  |



|      |      |      |      |      |
| ---- | ---- | ---- | ---- | ---- |
| Currently allocated   | 26195.4   | 16282.4     | 26157.7       | 16282.8         |
| Total free memory    | 17140.6   | 6717.6    | 17178.3       | 6717.2         |
| Max free memory      | 15264     | 6706.7    | 15264         | 6705.7         |
| Num Allocs memory    | 1930      | 1891.3     | 936.3       | 1649.7        |
| Num Frees memory     | 1715.3   | 1825.1    | 723.1      | 1583.6        |



# Memory allocation

Memory can be considered a reasonable UE health metric in terms of monitoring code stability.

\begin{minipage}{1.0\linewidth}
\begin{center}
\includegraphics[width=1.0\linewidth]{../../../masters/code/tests/plotterk/Current_Allocated_histogram.pdf}
\captionof{figure}[Currently allocated memory.]{Currently allocated memory. Equal distribution of attenuation zones and tests. Quectel uses about 16kB of memory and Ublox about 26kB.}
\label{fig:}
\end{center}
\end{minipage}

![](../../../masters/code/tests/plotterk/Current_Allocated_histogram.png)

\begin{minipage}{1.0\linewidth}
\begin{center}
\includegraphics[width=1.0\linewidth]{../../../masters/code/tests/plotterk/Total_Free_histogram.pdf}
\captionof{figure}[Free memory available.]{Free memory available. Equal distribution of attenuation zones and tests. Quectel has about 7kB of memory free and Ublox about 17kB.}
\label{fig:}
\end{center}
\end{minipage}

![](../../../masters/code/tests/plotterk/Total_Free_histogram.png)

\begin{minipage}{1.0\linewidth}
\begin{center}
\includegraphics[width=1.0\linewidth]{../../../masters/code/tests/plotterk/Signal_power_Num_Allocs_plot.pdf}
\captionof{figure}[Accumulated memory allocations per packet (390/1619) up to 4000.]{Accumulated memory allocations per packet (390/1619) up to 4000. (ABCD) Attenuation zones evident per decade, Quectel has slightly more allocations per MNO, tests show majority linear increases and ECL does not have a notable effect on the number of allocations.}
\label{fig:}
\end{center}
\end{minipage}

![](../../../masters/code/tests/plotterk/Signal_power_Num_Allocs_plot.png)

![](../../../masters/code/tests/plotterk/Num_Allocs_histogram.png)

![](../../../masters/code/tests/plotterk/Signal_power_Num_Frees_plot.png)

![](../../../masters/code/tests/plotterk/Num_Frees_histogram.png)

The number of allocations and frees are very similar, hence the latter is not shown here as well. The code can be considered running stable for both Ublox and Quectel, with memory usages of 60% and 70%, respectively.

# tables

<!--\begin{tabular}{l|lll|lll|l|l|l|l|l}-->

\begin{table}[]
\begin{tabular}{l|lll|lll|l|l|l|l|l}
    \\ \hline
​        & \multicolumn{3}{c|}{16} & \multicolumn{3}{c|}{128} & 512 & COPS & Echo & PTAU & eDRX \\ \hline
​        & 5      & M     & 95     & 5      & M      & 95     &     &      &      &      &      \\ \hline
Quectel &        &       &        &        &        &        &     &      &      &      &      \\
Ublox   &        &       &        &        &        &        &     &      &      &      &      \\
MTN     &        &       &        &        &        &        &     &      &      &      &      \\
Vodacom &        &       &        &        &        &        &     &      &      &      &     

\end{tabular}
\end{table}



\begin{table}[]
\begin{tabular}{cccccccccccccccccccccc}
        & \multicolumn{3}{c}{\textbf{16}} & \multicolumn{3}{c}{128} & \multicolumn{3}{c}{512} & \multicolumn{3}{c}{COPS} & \multicolumn{3}{c}{Echo} & \multicolumn{3}{c}{PTAU} & \multicolumn{3}{c}{eDRX} \\
        & 5        & M        & 95        & 5      & M     & 95     & 5      & M     & 95     & 5      & M      & 95     & 5      & M      & 95     & 5      & M      & 95     & 5      & M      & 95     \\
Quectel &          &          &           &        &       &        &        &       &        &        &        &        &        &        &        &        &        &        &        &        &        \\
Ublox   &          &          &           &        &       &        &        &       &        &        &        &        &        &        &        &        &        &        &        &        &        \\
MTN     &          &          &           &        &       &        &        &       &        &        &        &        &        &        &        &        &        &        &        &        &        \\
Vodacom &          &          &           &        &       &        &        &       &        &        &        &        &        &        &        &        &        &        &        &        &       
\end{tabular}
\end{table}



# UE-MNO Comparison

Table: Comparing means of UE-MNO pairs

|                      | Ublox-MTN | Quectel-MTN | Ublox-Vodacom | Quectel-Vodacom |
| -------------------- | --------- | ----------- | ------------- | --------------- |
| **Metrics**          |           |             |               |                 |
| Latency (s)          | 5.52      | 10.73       | 12.5608       | 27.7113         |
| Transmit time (s)    | 0.52      | 1.34        | 14.4993       | 4.19134         |
| Receive time (s)     | 1.28      | 3.31        | 60.4745       | 10.5279         |
| Energy (J)           | 11.4      | 21.9        | 21.9968       | 57.7098         |
| Max current (mA)     | 102.7     | 104.1       | 106.4         | 108.7           |
| Transmit power (dBm) | 16.96     | 14.80       | 16.16         | 18.64           |
| RSSI (dBm)           | -93.31    | -89.50      | -83.30        | -82.28          |
| TX Bytes (B)         | 345.8     | 852.7       | 3113          | 446.5           |
| RX Bytes (B)         | 109.2     | 386.7       | 769.3         | 147.7           |
| ACK/NACK RX Packet   | 20.1      | 7.5         | 13.2          | 12.3            |
| RLC UL (B)           | 468.8     | 336.9       | 343.8         | 201.3           |
| RLC DL (B)           | 240.2     | 144.2       | 77.1          | 43.3            |
| MAC UL (B)           | 568.2     | 554.0       | 357.3         | 292.3           |
| MAC UL (B)           | 321.1     | 181.2       | 87.1          | 55.2            |
|                      |           |             |               |                 |
| **Estimates**        |           |             |               |                 |
| Battery Lifetime     |           |             |               |                 |
|                      |           |             |               |                 |

Table: Comparing means of MNOs

|                               | MTN     | Vodacom |
| ----------------------------- | ------- | ------- |
| Latency (s)                   | 8.14    | 20.1    |
| Transmit Latency (s)          | 0.93    | 9.35    |
| Receive Latency (s)           | 2.30    | 35.5    |
| Energy (J)                    | 16.7    | 39.9    |
| Max current (mA)              | 103.5   | 107.6   |
| Transmit power (dBm)          | 15.9    | 17.4    |
| RSSI (dBm)                    | -91.4   | -82.8   |
| SINR (dB)                     | 3.43    | 3.36    |
| RSRQ (dB)                     | -13.0   | -13.1   |
| TX Bytes (B)                  | 599.2   | 1779.7  |
| RX Bytes (B)                  | 247.9   | 458.5   |
| ACK/NACK RX Packet            | 13.8    | 12.7    |
| Currently allocated           | 21238.9 | 21220.3 |
| RLC UL (B)                    | 402.9   | 273.2   |
| RLC DL (B)                    | 192.2   | 60.2    |
| MAC UL (B)                    | 561.2   | 324.8   |
| MAC UL (B)                    | 251.2   | 71.3    |
|                               |         |         |
| **Estimates**                 |         |         |
| Battery Lifetime              | 1500    | 800     |
| Data Billing (how many 512 B) | 5000    | 2000    |



# SINR

![Vodacom Energy (J) vs SINR (dB)](../images/1568089425196.png)



\begin{minipage}{1.0\linewidth}
\begin{center}
\includegraphics[width=1.0\linewidth]{../../../masters/code/tests/plotterk/SNR_txTime_plot.pdf}
\captionof{figure}[Measured latency points (526/1558) under 25 seconds against SINR.]{Measured latency points (526/1558) under 25 seconds in comparison (AB) of UE, (C) MNOs, (DE) attenuation zones, (F) UE-MNO boxplots, (GH) test types, (I) and ECLs against SINR.}
\label{fig:sinr_latency}
\end{center}
\end{minipage}

![](../../../masters/code/tests/plotterk/SNR_txTime_plot.png)

In Figure \ref{fig:sinr_latency}, (ABCF) UE devices share similar characteristics and differ according to MNO vendor. UE has a mean of 2 seconds on MTN-ZTE, and 6-7 seconds on Vodacom-Nokia. (DE) Attenuation per decade is not evident according to SNR. It can be suggested that using SNR as a metric for other tests is not beneficial if the attenuation zones cannot be distinguished. This also suggests that transmit power is a result of RSRP/RSSI variation instead. (GH) Tests are varied across SNR. eDRX paging cycles and COPS maintain similar latencies, however the rest increase three-fold or more. (H) Echo tests have outlier registrations and deregistrations at Vodacom-Nokia. UDP packet byte size does not seem to have an effect on latency. (I) Most of Vodacom-Nokia's dataset is on ECL 1. Increased ECL levels do not seem correlated with latency. (Note) The tail at 200 dB is cleared up as a single K-means cluster point due to excess repetition of one of the tests. At K=5, K-means points are a third of the maximum filtered values, which therefore minimizes the low latency kurtosis and retains the unique features.

Extended Coverage Levels (ECL) are determined by the network. The eNB (base station) sets the number of transmission repetitions (ECL) according to received signal strength reported by the UE.

\begin{minipage}{1.0\linewidth}
\begin{center}
\includegraphics[width=1.0\linewidth]{../../../masters/code/tests/plotterk/SNR_txTime_outliers.pdf}
\captionof{figure}[Measured latency outliers (51/61) up to 300 seconds against SINR.]{Measured latency outliers (51/61) up to 300 seconds in comparison (AB) of UE-Vendors, (C) MNO-Vendors, (DE) attenuation zones, (F) UE-MNO boxplots, (GH) test types, (I) and ECLs against SINR.}
\label{fig:sinr_latency_otl}
\end{center}
\end{minipage}

![](../../../masters/code/tests/plotterk/SNR_txTime_outliers.png)

Furthermore, in Figure \label{fig:sinr_latency_otl} latency outliers are (ABC) mostly as a result of Vodacom-Nokia. Both MNOs have outliers up to 300 seconds, but that is for cases where the inactivity timer is active. Since the inactivity timer cannot be controlled by the UE, the next step is to deregister from the network with `AT+COPS=2`. On MTN-ZTE, this is a quick action taking at most a few seconds, however on the Vodacom-Nokia network it can take 40 seconds or more. This is the real latency caveat which makes the Vodacom-Nokia network unusable.