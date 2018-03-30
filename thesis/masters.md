---
title: Development of a wearable NB-IoT/LTE-M solution for critical health and safety reporting
author: Daniel Robinson
date: 31 March 2018
tags: [LTE, wearables, healthcare, safety, critical, life-threatening]
abstract: |
  This thesis aims to address current challenges in specific wireless wearable technology by using NB-IoT/LTE-M. Research and development will be geared towards senior citizens, children, hospital/clinic patients and vulnerable pedestrians. The device is intended to detect and report any of the following critical information using generic interfaces (I2C, digital IOs, UART, SPI): heart rate indicating health concerns, acceleration/jerk indicating falls or crashes, indoor localisation, body temperature, triggering of a panic button in case of emergency; whilst maintaining a discrete footprint. The solution will work in a similar way to the mobile phone app Namola, in which location info is sent to emergency responders. To conserve power, the transmission will be event-triggered, with optional infrequent polling from the server side. The idea would be to roll this out on a large scale, and for the application to choose one of the specific targets, e.g. only clinics, or only pedestrians.

toc: true
lof: false
lot: false
---

<!--pandoc '.\Literature Study.md' --filter pandoc-fignos --mathjax --number-sections --standalone --bibliography .\bibtex\library.bib -o thesis.pdf-->

# Literature Study

## Overview

### heading 3

According to this person,
$$
x=2\,\sqrt{\frac{2\,\pi\,k\,T_{e}}{m_{e}}}\,\left(\frac{\Delta E}{k\,T_{e}}\right)^{2}\,a_{0}^{2}\,e^{2}\,\Omega
$$


Cool
$$
\mathbf{V}_1 \times \mathbf{V}_2 =  \begin{vmatrix} 
\mathbf{i} & \mathbf{j} & \mathbf{k} \\
\frac{\partial X}{\partial u} &  \frac{\partial Y}{\partial u} & 0 \\
\frac{\partial X}{\partial v} &  \frac{\partial Y}{\partial v} & 0 \\
\end{vmatrix}
$$


First of all, white text on a white background is impossible too see in this form on [Sequans](http://www.sequans.com/contact).

Secondly, I'd like to enquire about AT+SQNMONI for the Sequans 3330 module. It throws a CME error "operation not supported". Is that exactly the problem?



<!--hmm this is cool-->



* item 1
* item 2

Test cite @Harikiran2016

Noice @Chavan2017a

ref [#Overview]

![Screenshot_20180108-17142 \label{fig_descr}](C:\Users\d7rob\MEng\Screenshot_20180108-171426.png "thesis description")

See figure \ref{fig_descr}



![Alt text \label{mylabel}](C:/Users/d7rob/OneDrive/Pictures/canyon.jpg){#fig:id}

See figure \ref{mylabel} or +@fig:id.



Random stuff  
cool,adddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd  

asd </br>

bethr

> block
>
> quote
>
> nice


- [ ] banana
- [ ] apple
- [x] done
- [ ] q


|  a   |   b   |  c   |
| :--: | :---: | :--: |
|  1   | $4.12 |  2   |
|  q   |   s   |  3   |

qw



You can create footnotes like this[^footnote].

[^footnote]: Here is the *text* of the **footnote**.

***

nice

---



## References
