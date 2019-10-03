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



## Memory allocation

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