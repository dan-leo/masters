% 
% TikZpicture alone 
\begin{tikzpicture} 
\draw (0,0) node[minimum height=2cm,minimum width=3cm,draw] {$2 \times 3$}; 
\end{tikzpicture} No attempt to centre box 

% Try it with the \centering command 
{\centering% 
\begin{tikzpicture} 
\draw (0,0) node[minimum height=2cm,minimum width=3cm,draw] {$2 \times 3$}; 
\end{tikzpicture} 
} With \verb+\centering+ command 

% Try it with the \par\centering command 
{\par\centering% 
\begin{tikzpicture} 
\draw (0,0) node[minimum height=2cm,minimum width=3cm,draw] {$2 \times 3$}; 
\end{tikzpicture} 
} With \verb+\par\centering+ command 

% Try it with the \centering \par command pair 
{\centering% 
\begin{tikzpicture} 
\draw (0,0) node[minimum height=2cm,minimum width=3cm,draw] {$2 \times 3$}; 
\end{tikzpicture} 
\par} With \verb+\centering+ and \verb+\par+ command pair 

% Try it with the \par\centering and \par command pair 
{\par\centering% 
\begin{tikzpicture} [mindmap, grow cyclic, every node/.style=concept, concept color=blue!40,
    level 1/.append style={level distance=1cm,sibling angle=60},
    level 2/.append style={level distance=1cm,sibling angle=30},]
\draw (0,0) node[minimum height=2cm,minimum width=3cm,draw] {$2 \times 3$}
    child { node {Healthcare}
        child { node {Sleep Apnea Monitoring}}
        child { node {Glucose Monitoring}}
    }
    child { node {Automotive}
        child { node {TCU}}
        child { node {Head Unit}}
    }
    child { node {Transport}
        child { node {UBI}}
        child { node {Stolen Vehicle Tracking}}
        child { node {Toll Collection}}
    }
    child { node {Public Safety}
        child { node {Police}}
        child { node {Fire}}
        child { node {Ambulance}}
    }
    child { node {Energy}
        child { node {Smart Meter - Electricity}}
        child { node {Smart Meter - Gas}}
    }
    child { node {Home \& Security}
        child { node {Alarm}}
        child { node {Gateway}}
    };
\end{tikzpicture} 
\par} 

With \verb+\par\centering+ and \verb+\par+ command pair 


% Finally with \begin{center}\end{center} 
\begin{center} 
\begin{tikzpicture}[mindmap, grow cyclic, every node/.style=concept, concept color=orange!40]
\draw (0,0) node[minimum height=2cm,minimum width=3cm,draw] {$2 \times 3$}; 
\end{tikzpicture} 
\end{center} With \verb+\begin{center}\end{center}+ pair 
% 

\begin{center} 
\begin{tikzpicture}[mindmap, grow cyclic, every node/.style=concept, concept color=orange!40, 
    level 1/.append style={level distance=5cm,sibling angle=60},
    level 2/.append style={level distance=3cm,sibling angle=30},]
\draw (0,0) node[draw] {Primary Applications}
   child { node {Healthcare}
        child { node {Sleep Apnea Monitoring}}
        child { node {Glucose Monitoring}}
        child { node {AED Monitoring}}
        child { node {Patient Monitoring}}
        child { node {PERS/mPERS}}
        child { node {Sport \& Fitness}}
    }
    child { node {Automotive}
        child { node {TCU}}
        child { node {Head Unit}}
        child { node {Smart Antenna}}
        child { node {Connected Gateway}}
        child { node {Commercial Vehicle TCU}}
    }
    child { node {Transport}
        child { node {UBI}}
        child { node {Stolen Vehicle Tracking}}
        child { node {Toll Collection}}
        child { node {Fleet Management}}
        child { node {Railway}}
        child { node {Transit}}
        child { node {Container Tracking}}
        child { node {Aviation}}
    }
    child { node {Public Safety}
        child { node {Police}}
        child { node {Fire}}
        child { node {Ambulance}}
    }
    child { node {Energy}
        child { node {Smart Meter - Electricity}}
        child { node {Smart Meter - Gas}}
        child { node {Smart Meter - Water}}
        child { node {Smart Grid  - Generation}}
        child { node {Smart Grid  - Transformer}}
        child { node {Smart Grid  - IED (Cap, Bank, etc)}}
    }
    child { node {Home \& Security}
        child { node {Alarm}}
        child { node {Gateway}}
        child { node {Home Automation}}
        child { node {Set-box}}
    };

\end{tikzpicture}
\end{center}

\centering
\begin{tikzpicture}[mindmap, grow cyclic, every node/.style=concept, concept color=orange!40, 
    level 1/.append style={level distance=5cm,sibling angle=60},
    level 2/.append style={level distance=3cm,sibling angle=30},]

\node{Secondary Applications}
    child { node {Industrial \& Infrastructure}
        child { node {Industrial Heavy Equipment}}
        child { node {Industrial Gateway}}
        child { node {Tank Monitoring}}
        child { node {Drones/UAV/UAS/Robot}}
        child { node {Factory Automation}}
        child { node {Industrial Equipment - Other}}
        child { node {Infra - EV Charging Station}}
        child { node {Infra - Traffic Light}}
        child { node {Infra - Waste Management}}
        child { node {Infra - Pipeline Management}}
        child { node {Infra - Public Lighting}}
        child { node {Infra - Video Surveillance}}
        child { node {Infra - Parking Management}}
        child { node {Building HVAC}}
        child { node {Building Elevator Monitoring}}
        child { node {Building Automation}}
        child { node {Agriculture - Precision Planting}}
        child { node {Agriculture - Soil Monitoring}}
        child { node {Agriculture - Animal Tracking}}
    }
    child { node {Mobile Computing}
        child { node {Laptop}}
        child { node {Tablet}}
        child { node {Rugged Laptop or Tablet}}
    }
    child { node {Field Service \& Logistics}
        child { node {Handheld - Bar Code Scanner}}
        child { node {Handheld - Public Safety}}
        child { node {Personel Tracking / Monitoring}}
        child { node {Offender Tracking}}
        child { node {Goods tracking}}
        child { node {Tracking \& Logistics - Other}}
    }
    child { node {Sales \& Payment}
        child { node {POS}}
        child { node {Cashier}}
        child { node {Vending / Kiosks / Ticketing}}
        child { node {ATM}}
        child { node {Footfall Measurement}}
        child { node {Digital Signage}}
        child { node {Retail}}
    }
    child { node {Networking}
        child { node {Network Failover}}
        child { node {Routers}}
        child { node {Enterprise Gateway}}
    }
    child { node {Consumer}
        child { node {Camera}}
        child { node {Kid / Pet Tracker}}
        child { node {Wearables}}
        child { node {Appliances}}
    };
\end{tikzpicture}
\par