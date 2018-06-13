# Schedule

Date today is 13 June 2018.



~~~mermaid
gantt
        dateFormat  YYYY-MM-DD
        title Masters schedule
        section Main
        NB-IoT Research           :done,    nbiot, 2018-02-01,2018-06-06
        Ublox N200 testing & registration :done,  n200, 2018-02-28, 2018-04-21
        Johannesburg              :done,    joburg, 2018-04-09, 2018-04-22
        Dash7 Research            :active,  dash7, 2018-05-25, 3w
        Build application code for P2P PoC : build_app, 2018-09-01, 90d
        
        section Critical tasks
        Literature study                    :crit, lit, 2018-06-23, 2018-06-30
        List of OFDM uplink NB-IoT modems   :crit, done, ofdm, 2018-06-06, 1w
        Source hardware                     :crit, active, after ofdm, 2018-08-01
        
        section P2P PoC
        Design, Gerbers, Sourcing           : design, 2018-06-13, 2w
        Make, populate, test                : make, after design, 3w
        Examples                            : examples, after make, 2w
        
        section Unrelated
        America                             : murica, 2018-08-10, 2018-08-25
        Sierra Wireless Legato training     : legato, 2018-06-18, 2d
~~~

