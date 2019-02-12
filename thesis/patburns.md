# Pat burns

This is a summary of all that Pat Burns is saying on medium and about Haystack. Each heading is a different topic.

# 5G + IoT

**A Match Made In Hell: 5G and IoT**

I was at MWC last week here in SF and got to hear some talking points from some cellular folks about how that even if NB-IoT and LTE CatM1 aren’t really going to solve for low power IoT use cases, what “everybody” is waiting for is 5G, which I am told supposed to be in stores sometime between 2020 and 2025.

But now we learn there are problems deploying 5G indoors, via Dan Jones @ [Lightreading](http://ubm.io/2w9211F):

> Low-emissivity glass used in modern homes and apartments could become an impediment to delivering 5G connectivity to users indoors, Light Reading hears.

> US carriers are currently testing “millimeter wave” radios for use in fixed and mobile 5G services. Light Reading has now been told that the 28GHz radios have trouble penetrating low-emissivity (low-e) glass, which is designed to insulate the home while cutting UV rays from the sun.

> Low-e glass works by using an extremely thin metal-oxide coating on the window. Other window designs also use gas fillings and reflective coatings for better energy efficiency.

> Multiple people have confirmed to Light Reading that low-e glass nearly completely blocks mmWave 5G signals. The lower-band cellular signals used today — from 800MHz to 2.5GHz in the US — are much better at penetrating common building materials, albeit by no means perfect.

In case any of you IoT folks were hoping for a low-power LPWAN miracle from 5G, here’s one attempt — that demonstrates that the high-powered cellular leopard doesn’t change its spots — to deal with the current dilemma:

> Some trials have apparently boosted the mmWave signal to try and improve test performance, but the FCC has strict limits written into radio test licenses.

So … the carriers have given us LTE CatM1, which as discussed previously is not even remotely low power. [And NB-IoT](https://medium.com/@patburns/how-to-solve-the-cellular-iot-prisoners-dilemma-546326d18c79), which is proving to be both pricey and very unlikely to deliver endpoints with multiyear battery life. And this is before either have rolled out in volume where … who-knows-what-additional-surprises-await-us.

At this point, to gauge a carrier’s seriousness about the low power IoT — and [some like Orange](https://hackernoon.com/want-to-know-what-oranges-new-lpwan-strategy-is-5ea46209fb97) are doing the rational thing and embracing non-LTE alternatives — you just have to look for their non-LTE offerings. Those that cling to LTE are signaling that their focus will be on mains-powered meter reading (a good market opportunity, BTW) and other applications (automotive) where a large power supply is handy. For the billions of of things in the IoT that need sensing, measuring, controlling, or tracking but don’t have access to such power supplies, those carriers are opting out. Analysts take note.

# Blueborne

**The Billion Dollar IoT Device Discovery Opportunity**

A few thoughts on last week’s Blueborne exploit, which should raise eyebrows for anyone deploying Bluetooth in the IoT.

1. Blueborne looks like a nightmare for anyone deploying Bluetooth in the IoT. Here’s the description from the [firm](https://www.armis.com/blueborne/) that uncovered the exploit:

> “BlueBorne is an attack vector by which hackers can leverage Bluetooth connections to penetrate and take complete control over targeted devices. BlueBorne affects ordinary computers, mobile phones, and the expanding realm of IoT devices. The attack does not require the targeted device to be paired to the attacker’s device, or even to be set on discoverable mode. Armis Labs has identified eight zero-day vulnerabilities so far, which indicate the existence and potential of the attack vector.

But then there’s this:

> Armis believes many more vulnerabilities await discovery in the various platforms using Bluetooth. These vulnerabilities are fully operational, and can be successfully exploited, as demonstrated in our research. The BlueBorne attack vector can be used to conduct a large range of offenses, including remote code execution as well as Man-in-The-Middle attacks.”

For the full shock value of this exploit, here’s a short video by the firm that made the discovery that explains the risk:



<iframe data-width="854" data-height="480" width="700" height="393" data-src="/media/2ee94c8c09c764242f1344c82d6ac63a?postId=8615893e6df8" data-media-id="2ee94c8c09c764242f1344c82d6ac63a" data-thumbnail="https://i.embed.ly/1/image?url=https%3A%2F%2Fi.ytimg.com%2Fvi%2FLLNtZKpL0P8%2Fhqdefault.jpg&amp;key=a19fcc184b9711e1b4764040d3dc5c07" class="progressiveMedia-iframe js-progressiveMedia-iframe" allowfullscreen="" frameborder="0" src="https://medium.com/media/2ee94c8c09c764242f1344c82d6ac63a?postId=8615893e6df8" style="display: block; position: absolute; margin: auto; max-width: 100%; box-sizing: border-box; transform: translateZ(0px); top: 0px; left: 0px; width: 700px; height: 393.391px;"></iframe>

\2. Bluetooth radios are notoriously easy to discover and a large part of Blueborne appears based on [this fact](https://security.stackexchange.com/questions/169527/what-is-blueborne-and-how-to-protect-myself):

> The BlueBorne attack vector has several stages. First, the attacker locates active Bluetooth connections around him or her. Devices can be identified even if they are not set to “discoverable” mode. Next, the attacker obtains the device’s MAC address, which is a unique identifier of that specific device. By probing the device, the attacker can determine which operating system his victim is using, and adjust his exploit accordingly. The attacker will then exploit a vulnerability in the implementation of the Bluetooth protocol in the relevant platform.

\3. Many Bluetooth devices are — and you are not going to believe this — [not patchable](http://www.crn.com/news/internet-of-things/300091991/armis-bluetooth-vulnerability-leaves-5-billion-iot-devices-open-to-blueborne-malware-attack.htm).

> *However, Parker said that up to 40 percent of the 5.3 billion impacted devices probably would not be patchable — mainly because they are IoT devices, like smart refrigerators, that cannot be easily updated.*

> *Right now, Armis said that users could disable Bluetooth to protect their connected devices while waiting for the patch.*

\4. If there is any good news for Bluetooth developers, it is small, embeded devices do not appear — for now — to be a primary target for Blueborn, but rather higher-powered [gateways](https://www.armis.com/blueborne/) running Linux, Android, Windows, or iOS which in turn connect to low power devices.

> The vulnerabilities disclosed by Armis affect all devices running on Android, Linux, Windows, and pre-version 10 of iOS operating systems, regardless of the Bluetooth version in use. This means almost every computer, mobile device, smart TV or other IoT device running on one of these operating systems is endangered by at least one of the eight vulnerabilities.

\5. I’ve written about device discovery [before](https://medium.com/the-startup-magazine-collection/a-simple-proposal-to-improve-security-for-the-internet-of-things-4fcc0663f70e) and the principles still apply: **low power IoT endpoints should operate in a “stealthy” mode unless there is a reason to make noise.** It saves power, reduces network congestion, and makes discovering your IoT device much, much harder. I didn’t say “impossible to discover”, but like prey in the jungle wanting to avoid alerting a predator, part of minimizing your chances of being discovered is just to keep quiet. Older protocols — including Bluetooth take an opposite tack: they never stop talking and are always discoverable. Even when you tell your Bluetooth radio to go into [non-discovery mode](https://www.phonearena.com/news/Did-you-know--enabling-Bluetooth-in-non-discovery-mode-doesnt-prevent-access-to-your-smartphone_id82327).

Bluetooth is not alone in this ease of discovery. WiFi and IEEE 802.15.4xx are just two examples of stacks (or semi-stacks) that weren’t conceived with the modern IoT in mind. Even more recent attempts like LoRaWAN were architected without thinking this through.

In the world of IoT wireless protocol development, device discovery seems to (usually) be the job given the guys who weren’t smart enough to work on documentation. But if we are just seeing the beginning of hacks like Blueborne — as the author of the vulnerabilty suggests — the solution to limiting IoT device discovery is a billion dollar opportunity.

# NB-IoT criticism

**Here’s Something Entertaining In The IoT**

In a chapter out of IoT news-of-the-weird, here’s a pro-LoRaWAN writer [politely destroying](http://bit.ly/2mgXcQq) whatever threads of low power legitimacy NB-IoT might still be holding onto. Like one drunk yelling that another drunk should not be allowed to drive, here’s a LoRaWAN person getting a chance to claim another “LPWAN” firmware stack is less capable than LoRaWAN. And he’s sort of right.

Hard to believe that after millions in marketing dollars, NB-IoT has stuck it’s neck out so far as to make itself a worthy target for … LoRaWAN. But the numbers, as I’ve written [here](http://bit.ly/2AsmtRs) and [here](http://bit.ly/2xuqQWv), are bad for NB-IoT. And they are pretty [bad](http://bit.ly/2pBcYqp) for [LoRaWAN](http://bit.ly/lorawan), too.

For fixed meter reading applications where a message or two per day is all that is required, NB-IoT *might* work in a limited capacity. But as soon as the endpoint begins moving, requires more frequent communications, or needs to support real-time location, NB-IoT nukes your battery and becomes effectively useless.

And LoRa is a good LPWAN radio (and getting [better](http://bit.ly/2EsTWsq), it seems), but LoRa*WAN*is comically bad freeware and a disaster for non-fixed endpoints. [Far better alternatives](http://bit.ly/2haytech) are, of course, available.

Just remember: friends don’t let friends use NB-IoT, but real friends don’t let friends use LoRaWAN, either.

**Verizon And AT&T Are Taking A Pass On NB-IoT**

In a move that should shock no-one who follows movements in LPWAN technologies, Verizon announced they are [deploying LoRa](http://ubm.io/2B9i9WE) and apparently have no plan to deploy NB-IoT:

> [Verizon Communications Inc.](http://www.lightreading.com/complink_redirect.asp?vl_id=5926) (NYSE: VZ), which launched the country’s first national LTE-M service in March, said it’s embracing LoRaWAN unlicensed technology for building overall solutions for some customers. That surprised attendees at the show, given Verizon’s emphasis on LTE-M as a system that uses cellular infrastructure with its security quality-of-service mechanisms.

And just confirming what we already knew, AT&T is sticking with high-power LTE CAT M1 while it gently gives NB-IoT the tap-tap to the back of the head:

> “Though it is testing NB-IoT, AT&T hasn’t found a differentiator that would justify offering it alongside LTE-M, Allen said. Advantages to LTE-M include a higher data rate and the ability to carry voice calls.”

If it worked as originally promised, there would be plenty to differentiate NB-IoT from CAT M1, which remains very high power and high priced.

So, this leaves #4 carrier T-Mobile as the only carrier claiming to be actively pursuing NB-IoT in the US.

Combining these carrier defections wtih the [weak performance of NB-IoT](http://bit.ly/2xuqQWv) in mobile environments and it’s safe to say end users should be getting comfortable with crossing NB-IoT off their list of prospective LPWAN technologies in the U.S. market. It is worth continuing to watch the technology for fixed meter reading applications in markets like China where Huawei is aggressively pushing the technology. But the Verizon/AT&T news amounts to a big win for Semtech and with recent news from [SigFox](http://ubm.io/2AKKNuN), the LPWAN field may be clearing faster than expected.

This is also critical information for “un-carrier” types like [Comcast](http://comca.st/2B4a8T9) and a few startups building out LoRa-based public networks. For them, differentiation just became a matter of do-or-die.

A huge swath of the LPWAN market opportunity — mobile use cases — remains almost entirely unsolved (and unsolvable) by LoRaWAN. If you are being pitched by a sales guy from a telco or other LPWAN network provider, ask how they are solving for low power mobile applications. The network that can provide you with high precision, real-time location and sensing in combination with multi-year battery life is the one to pay most attention. For more thoughts, look [here](http://bit.ly/2pBcYqp).

UPDATE 05 Feb 2018: Verizon is now planning both a LoRaWAN offering *and* an NB-IoT offering for 2018 , according to this article: <http://www.verizon.com/about/news/verizon-carries-successful-data-session-new-nb-iot-guard-band-network>.

**The Really Hard Thing About GPS and the IoT**

> “All things excellent are as difficult as they are rare.”

> \- Baruch Spinoza

**TL;DR:**

1. **The mobile IoT needs GPS**
2. **GPS is traditionally not low power**
3. **Getting GPS right with low power requires a tricky confluence of technologies**

This month, I witnessed a “coming out” party of sorts for a new LTE NB-IoT [product from Samsung](http://zd.net/2yrMDB9). It’s a “tracker” that you can put on dogs, bikes, kids, or whatever moves.

At first blush, it is an exciting product:

- It is IP68 water- and dust-proof, has a horizontal/vertical of 4.21cm, and is 1.19cm thick.
- It is optimal for indoor and outdoor use, including pet and children tracking, protecting personal items, and attaching to luggage.
- An attachable ring will enable it to be hung on bags and key chains.
- It also has an on-demand feature, where it will show its location and set times; while its geo-fence feature alerts users when it has left a set virtual zone
- It can also be synced with smart home appliances to turn on the light, TV, or the robot cleaner when close to home.

Small, versatile, feature rich … what’s not to like, right?

Except this:

- Connect Tag consumes little energy and data, and **a full charge will last seven days.**

NB-IoT, as most readers of this website probably know, is the cellular industry’s response to Sigfox and LoRa. Another cellular response, LTE CAT M1, has outed itself as a “high power” WAN technology. So, NB-IoT is supposed to be the cellular industry low power savior: long range plus low power and, of course, low cost.

Now, it’s possible that this is just a bad implementation of GPS over NB-IoT, but let’s just assume Samsung knows a thing or two about wireless and location services. So what happened?

1. There’s something inherent in the NB-IoT stack that isn’t very “low power”, after all, which seems unlikely given what we hear about the uptake of NB-IoT for fixed meter reading; or
2. NB-IoT can’t easily support “hot start” GPS location acquisition.

GPS, as I’ve written [before](http://bit.ly/2pBcYqp), can be a very power hungry component of a mobile IoT endpoint. Historically, we’ve seen mobile GPS endpoints married with cellular, which (usually) promised around 30 days of battery life and often delivered far less. LPWAN’s were supposed to change all that, but in the Samsung case above, battery life, it would appear, got *worse*.

A GPS receiver needs to locate at least four satellites in the sky in order to compute its location, and the time required to do so can range from a few seconds to many minutes. A “cold start” can force your mobile endpoint into searching for satellites for many minutes … with predictable battery life results. A “hot” start, on the other hand, can enable the endpoint to acquire GPS coordinates in a few seconds.

So to avoid battery meltdown on your GPS-enabled mobile IoT device, hot starts are extremely helpful. Enabling a GPS hot start requires the network to broadcast a kind of “cheat sheet” to the GPS receiver to allow it to acquire location more quickly. For many [Assisted GPS](http://bit.ly/2p1E6hh) or “A-GPS” is the mechanism for doing this.

Low Power Wide Area Networking technologies are about battery powered devices that can communicate over long distances and deliver long — as in multi-year — battery life. Today, lots of LPWAN technologies are being deployed in fixed use cases — meter reading, for example — and simply send a message once a day back to a host reporting on the day’s usage. Water meters, for example.

But deploying LPWAN’s for real-time outdoor location is another matter. While there are multiple techniques for deriving location without GPS, most LPWAN protocols at best offer a high-latency, low accuracy form of location that would be hard to characterize as real-time. Adding GPS to these requires the GPS receiver to be active and, in most cases, in a perpetual state of looking for satellite signals. Even invoking GPS based on an event (e.g. movement) is full of risks like false positives that will also deplete a battery. A-GPS mitigates this power draw problem but … supporting it correctly remains elusive for many (but not all) LPWAN protocols. It is unclear whether this is the driver behind the Samsung NB-IoT battery life issue, but I look forward to hearing more detail from those closer to that product.

# Final thoughts

- In addition to its capabilities for geolocating low power mobile devices, we believe DASH7 has a foundational role to play in authenticating location for this next wave of network computing. One or more unlicensed band LPWAN technologies are likely to dominate this function and DASH7 was purpose built for location-based LPWAN duties.
- Beyond blockchains and smart contracts, the vulnerability of GNSS is something worth pondering further and whether DASH7 has an additional role to play as part of an encrypted, terrestrial backup to GNSS.
- As blockchain-based IoT apps generate ever-larger tsunamis of data, companies seeking to profit from the of that data will want to consider authenticating the location provenance of that data, as incentives to sell fraudulent data via a smart contract will be high.
- As blockchain-based IoT apps begin substituting for cloud services IoT apps, it inadvertently brings us closer to a vision of driving more IoT processing to the true edge of the network — the endpoint — something I’ve [touched on](http://bit.ly/1knol10) before.
- A decentralized IoT, focused on short bursty messaging, is not too different from a decentralized internet that only processes SMTP messages.
- In lieu of meshing, expect “repeaters” to play a larger role in decentralized LPWAN deployments.
- The importance of peer-to-peer messaging, especially by battery powered endpoints, in a decentralized IoT is difficult to overstate.

# Theft

**How To Predict If Your IoT Device Will Steal From You**

Sometimes making your wide area IoT device truly “wide area” isn’t as easy or as safe as it looks. One blind spot for many IoT technologies: roaming. Here’s a story about a non-profit group that tracks the migratory patterns of birds and found itself victim of a costly mobile [IoT device theft](https://bbc.in/2KXDM16):

> According to official broadcaster [**Radio Poland**](http://www.thenews.pl/1/11/Artykul/370157,Stork-incurs-hefty-phone-bill), the environmental EcoLogic Group placed a tracker on the back of a white stork last year to track the bird’s migratory habits.

> It travelled some 3,700 miles (6,000kms), and was traced to the Blue Nile Valley in eastern Sudan before the charity lost contact.

> EcoLogic told the [**Super Express**](https://www.se.pl/wiadomosci/polska/bocian-narobil-dlugow-aa-YXmy-sAtc-CQ66.html) newspaper that somebody found the tracker in Sudan, removed the sim card and put it in their own phone, where they then racked up 20 hours’ worth of phone calls.

> Radio Poland says that the organisation has received a phone bill of over 10,000 Polish zloty ($2,700; £2,064), which it will have to pay.

# Animal tracking

As mobile IoT use cases go, animal tracking in most cases is compelling both in terms of its financial return as well as its environmental benefits. From altrustic examples like tracking storks in order to better understand the spread of West Nile virus to tracking the location of billions of farm animals around the world to improve productivity, the business opportunity is attractive to IoT hardware developers and the data that can be collected is coveted by ranchers, buyers, regulators, investors, law enforcement, and others.

Until recently, animal tracking over wide area wireless area networks has remained effectively unsolved due to the high cost of cellular service, large device form factors, and poor battery life. Some short range RFID solutions provide a type of chokepoint visibility, but longer range/lower power/lower cost wireless networking technologies, as I’ve discussed [here](http://bit.ly/lorawan) and [here](http://bit.ly/2xuqQWv), are in the early stages of breathing new life into wide area animal tracking.

But as those things being tracked/monitored begin moving over wider and wider areas, the issue of network coverage becomes more serious: if my device strays outside of its “home” network — whether private network or public network — what is the best way to borrow connectivity from other networks?

# Asset tracking

**Maybe We Need A Lost and Found For Nukes**

As asset tracking use cases go, they don’t get much scarier than [this](https://www.mysanantonio.com/news/local/article/Plutonium-went-missing-in-San-Antonio-but-the-13071072.php):

> Two security experts from the Department of Energy’s Idaho National Laboratory drove to San Antonio, Texas, in March 2017 with a sensitive mission: to retrieve dangerous nuclear materials from a nonprofit research lab there.

> Their task, according to documents and interviews, was to ensure that the radioactive materials did not fall into the wrong hands on the way back to Idaho, where the government maintains a stockpile of nuclear explosive materials for the military and others.

> To ensure they got the right items, the specialists from Idaho brought radiation detectors and small samples of dangerous materials to calibrate them: specifically, a plastic-covered disk of plutonium, a material that can be used to fuel nuclear weapons, and another of cesium, a highly radioactive isotope that could potentially be used in a so-called “dirty” radioactive bomb.

> But when they stopped at a Marriott hotel just off Highway 410, in a high-crime neighborhood filled with temp agencies and ranch homes, they left those sensors on the back seat of their rented Ford Expedition. When they awoke the next morning, the window had been smashed and the special valises holding these sensors and nuclear materials had vanished.

Now I don’t know what mechanisms might have been in place for tracking these materials, but we can more or less assume there was no LPWAN involved:

> **More than a year later, state and federal officials don’t know where the plutonium — one of the most valuable and dangerous substances on earth — is. Nor has the cesium been recovered.**

> No public announcement of the March 21 incident has been made by either the San Antonio police or by the FBI, which the police consulted by telephone. When asked, officials at the lab and in San Antonio declined to say exactly how much plutonium and cesium were missing. But Idaho lab spokeswoman Sarah Neumann said the plutonium in particular wasn’t enough to be fashioned into a nuclear bomb.

Not enough plutonium to make a bomb, but … no word on how much cesium was there and … it’s radioactive and bad for your [health](https://www.atsdr.cdc.gov/phs/phs.asp?id=575&tid=107):

> If you were to breathe, eat, drink, touch, or come close to large amounts of radioactive cesium, cells in your body could become damaged from the radiation that might penetrate your entire body, much like x-rays, even if you did not touch the radioactive cesium. You would probably experience similar effects if you were exposed to any other substance with similar radioactivity. **You might also experience acute radiation syndrome, which includes such effects as nausea, vomiting, diarrhea, bleeding, coma, and even death.** A number of people in Brazil, who handled radioactive cesium that was scavenged from a medical machine used for radiation therapy, became sick from exposure to the radiation; a few of them died.

But back to the Department of Energy’s asset tracking capabilities:

> It is nonetheless now part of a much larger amount of plutonium that over the years has gone quietly missing from stockpiles owned by the U.S. military, often without any public notice.

> Unlike civilian stocks, which are closely monitored by the Nuclear Regulatory Commission and openly regulated — with reports of thefts or disappearances sent to an international agency in Vienna — the handling of military stocks tended by the Department of Energy is much less transparent.

I know that lost nuclear materials are a serious concern at DoE — the team at [Argonne](https://www.rfidjournal.com/purchase-access?type=Article&id=4786&r=%2Farticles%2Fview%3F4786%2F4) Labs has worked on this using Savi active RFID technology almost a decade ago. (There may be more recent activity than this — please feel free to comment). Here’s the DoE’s response to today’s story:

> The Energy Department, which declined comment for this story, doesn’t talk about instances of lost and stolen nuclear material produced for the military. It also has been less willing than the commission to punish its contractors when they lose track of such material, several incidents suggest.

> That nontransparent approach doesn’t match the government’s rhetoric.

> Protecting bomb-usable materials, like the plutonium that went missing in San Antonio, “is an overriding national priority,” President Obama’s press office said in a [fact sheet](http://www.nss2016.org/document-center-docs/2016/3/31/fact-sheet-united-states-military-nuclear-material-security) distributed during the fourth and final Nuclear Security Summit that he hosted in late March 2016, a Washington event attended by more than 50 heads of state.

In addition to losing nuclear materials while in transit, there is the challenge of keeping tabs on inventory stored in “warehouse” facilities like Savannah River where cylinders of nuclear materials can be misplaced without actually leaving the facility.

Perhaps DoE is already at work with better rules and technologies for how their mobile workers safeguard nuclear materials during transit, but especially for “small nukes” like the ones described above, a lightweight, low power, LPWAN [solution](http://bit.ly/2haytech) would have been inexpensive and probably helped recover something that in the wrong hands could be used as a WMD.

# P2P + LPWAN

- Decentralized IoT, focused on short bursty messaging, is not too different from a decentralized internet that only processes SMTP messages.
- In lieu of meshing, expect “repeaters” to play a larger role in decentralized LPWAN deployments.
- The importance of peer-to-peer messaging, especially by battery powered endpoints, in a decentralized IoT is difficult to overstate.

 **Adding P2P + LPWAN connectivity to Cheeseburger Compass**

The [Cheeseburger Compass](https://blog.hackster.io/cheeseburger-compass-directs-you-to-the-nearest-burger-joint-no-internet-required-78306b497c24) (CC) is a simple example of a piece of geolocation-enabled gadgetry that operates without the internet, more or less. And in its own simple way shows us another path towards a decentralized IoT: it just tells you the closest place to get a burger.

Hypothetically, we could add a low power, wide area network radio like LoRa to the CC. And in doing so, every CC user can communicate with other CC users over ranges of .25 miles to 10 miles. All are mobile, and using the right networking protocol, even with GNSS/GPS on the mobile client, the battery can last years.

And still no internet.

Five Guys, In-N-Out, and White Castle could interact with these CC users offering promotions, internet free. Using a networking protocol like DASH7, promotions could be broadcasted to CC users or routed individually.

Using a networking protocol like DASH7 that supports P2P communication, CC clients could send messages to one another.

As long as the message size remains small — a text message, email message, GPS location coordinates, sensor data, etc. — a LPWAN-based system can operate without the need to connect to the broader internet.

**What About DNS?**

A LPWAN based, decentralized messaging system could route messages via one or more application layer protocols and using a networking protocol like DASH7 that supports multi hop, a decentralized equivalent of a Domain Name Service could exist either on “master nodes” or in a blockchain environment.

You say: but isn’t blockchain using the internet? Perhaps, but not necessarily. A truly decentralized blockchain network could (theoretically) operate on a purely wireless basis. Some companies like [Blockstream](http://bit.ly/2Evnc5b) are taking this to extremes using satellites but this is only one example.

# P2P

**A New Way To Think About The P2P IoT**

A few end-of-year thoughts on P2P and LPWAN’s:

- At Haystack we’ve seen an uptick in the number of solutions/concepts that are looking for a decentralized approach to implementing a low power, wide area network. This is driven in large part by blockchain, which I’ve started to talk about [here](http://bit.ly/2PsSJHL) and [here](http://bit.ly/2wJDLrJ).
- Blockchains are driving discussions about decentralization, but those conversations are surfacing some other realities about the nature of decentralized IoT networks.
- Centralization, as applied to the IoT, can describe the physical network topology of an IoT network, or it can describe the governance (application layer) of the network. A “hub-and-spoke” physical topology as is common in cellular networks is one example of a centralized physical network with a centralized governance model.
- Semi-decentralized networks might include decentralized blockchain-based applications — let’s take a supply-chain app like [VeChain](http://bit.ly/2CmmghU) — that operate over internet links run by hub-and-spoke telco’s with a centralized physical and governance model.
- A truly decentralized IoT network therefore describes a non-hub-and-spoke (e.g. non-cellular) physical topology as well as a decentralized governance model.
- Putting aside governance for purposes of this post, what constitutes a decentralized physical topology in an IoT network? For starters, it means eliminating a “hub” or central server and implies some version of peer-to-peer networking. In theory, you and I could have a decentralized IoT network with just two endpoints — one for you and one for me — communicating on a peer-to-peer basis.
- If we add a third endpoint, our options may expand from simple peer-to-peer messaging, to multi-hop messaging. In other words, if A, B, and C are arranged in a straight line where A is out of range of C, A could send message X to B, who in turn passes X over to C. We can even add a fourth endpoint (“D”) and extend the process further. At Haystack, we refer to this as multihop networking.
- A decentralized physical network topology eliminates the “hub” and instead relies on endpoints to communicate on a peer-to-peer basis and in some cases “hopping” or “meshing” a message from its origin to its destination.
- While “meshing” was at least theoretically implemented with certain IEEE 802.15.4 protocols like ZigBee, we have yet to see meshing with longer range, low power LPWAN radios like LoRa. Nor are we likely to see it given the overhead it requires and the strength of signal propagation seen by LPWAN radios. In reality, meshing for 2.4GHz protocols was more a marketing gimmick driven by poor signal propagation than an actual need for “meshing” — that is to say, if 2.4GHz could have done the job in getting messages directly from an endpoint to the gateway via better signal propagation, there would have been little need for meshing.


# Trilateration

**Confirming the RSSI Alert Without GNSS/GPS**

While GPS implemented on a LPWAN using Haystack is very low power, for some applications the added cost of the GPS receiver may drive developers to look for alternatives. A non-GPS alternative is also necessary for indoor location use cases as well as a means for a “back up” to GPS or for use cases requiring [both indoor and outdoor](http://bit.ly/2b65gRQ) geofencing (e.g. certain warehouse/supply chain use cases).

**Trilateration Using Fixed Gateways**



![img](https://cdn-images-1.medium.com/max/800/1*IIE6LfhG6OW5xVt-8ZxFNA.png)

Trilateration via multiple fixed gateways. Better than single gateway, but not as granular as GPS.

The use of trilateration is one method where while not as accurate as GPS, we have still observed relatively high levels of accuracy. The location granularity is highly correlated with the number of gateways within range of a given endpoint: a single fixed gateway receiving a message from an endpoint will help us infer location in a far less precise manner than five fixed gateways doing the same thing.

The use of trilateration requires the use of a location engine at the gateway or potentially in the cloud, as well as a site survey to help calibrate RSSI values with the

**Trilateration Using Mobile Gateways or Mobile Endpoints**

Also, a moving gateway or moving endpoint will result in measurements that are comparable to multiple gateways, providing another potential path with superior location granularity to a single fixed gateway and single non-moving endpoint.

We have observed high levels of accuracy (not as accurate as GPS, however) using both this method as well as using a single, fixed gateway measuring a moving endpoint. Both have the effect of generating multiple vectors between gateway(s) and endpoint to provide a higher resolution location than with a single fixed gateway and single non-moving endpoint. Still, these approaches may be less reliable and more costly to implement and still vulnerable to false positives as illustrated above.

This method of trilateration also applies to moving gateways locating a fixed endpoint.

One more thought on mobile gateways: developers considering “lost and found” use cases may be considering mobile gateways for scenarios where fixed gateway infrastructure is limited and endpoints have the potential to travel over long distances.

**Time Difference of Arrival (TDOA)**

TDOA is an additional approach to non-GPS-based location that we explored in some detail in a [recent post](http://bit.ly/2PsSJHL). For LoRa, we find RSSI to be a more convenient and reliable method of performing relative location, but as new permission-less use cases utilizing blockchain emerge, the need for a more secure (non-spoofable) terrestrial alternative to GPS is a hot topic on Telegram now. Exciting new territory.

We are not actively supporting TDOA commercially (yet) but expect to do so later this year in conjunction with these efforts around blockchain.

**Other Considerations**

Using the DASH7 Advertising Protocol is not the only path to implementing a real-time geofence with DASH7. For example, environmental sensor triggers may initiate a geolocation process or heuristics about the underlying asset may cause intelligent interrogation of the endpoint which, in combination with a geofence, creates additional paths

# Geolocation

**One IoT Technology Responds To A Geolocation Dilemma**



# Geofencing

One feature that is under-discussed when discussing mobile asset tracking is the ability to generate an alert when an asset moves into or out of a pre-defined geographic area, commonly referred to as **geofencing**. In the low power/LPWAN space, geofencing is rarely discussed because … it’s just hard to do for most LPWAN technologies. Some LPWAN vendors may talk of *geolocation*, but references to **geofencing** may be scarce or non-existent for reasons I’ll touch on below.

Defining Geofencing

First and before getting into the low power IoT part of this post, maybe it’s worth clarifying what we are talking about:



![img](https://cdn-images-1.medium.com/max/800/1*vtZDJHmyougW1DVRAmE2gQ.png)

So, it’s a **virtual geographic boundary**. Graphically, it is usually configured using a map, perhaps like this:



![img](https://cdn-images-1.medium.com/max/800/1*HH1UzPL6umgRNVOusNxUxA.png)

Or a more complex shape like this:



![img](https://cdn-images-1.medium.com/max/800/1*EU3lpOK7b5gkvYol9X1eew.png)

Then, as an endpoint enters or leaves the geofence, it triggers an alert and sent to someone who cares. Like this:



![img](https://cdn-images-1.medium.com/max/800/1*9_Ke1ecuX8XVmE7Wl5DgXQ.png)

You probably have your own experiences with geofences as a consumer — certain [location-based advertising](https://www.adweek.com/digital/heres-how-digital-advertisers-are-using-waze-to-connect-with-people-behind-the-wheel/) is effectively implementing a geofence when a cellular or in-store wireless network “detects” you entering a certain geography and enables an advertiser to put an offer in front of you. (I drove with Waze over the holidays to visit relatives and experienced the annoyance firsthand …)

For the IoT, however, geofencing experiences are different. Primarily, **geofencing is about managing mobile assets: tracking them, securing them, and monetizing them.** In my experience, geofencing is something we talk about **for IoT use cases that are based outdoors**. Indoor location and geofences are another topic and but first I am focusing on outdoor.

In the annals of mobile asset tracking history, the “dominant” wireless technologies have been cellular and satcom. True, their tracking products are becoming less expensive and smaller, [but short battery life and high cost](http://bit.ly/2p1LeMh)remain as significant barriers to penetrating the mobile asset tracking market. Here’s a look at how AT&T does it with cellular:



![img](https://cdn-images-1.medium.com/max/800/1*qTCvC60v0qYy3SMk-FYz0g.png)

Cellular-based Geofencing

**Conclusion**

Geofencing is an exciting opportunity for mobile asset tracking over LPWAN systems, but the importance of the [right](http://bit.ly/2haytech) networking stack cannot be overstated. A unidirectional protocol is a poor choice for most LPWAN implementations but in particular those seeking to implement geofencing. A bi-directional protocol that supports multicasting/broadcasting as well as low power wakeup is, for the LPWAN world, essential.

# LoRaWAN geolocation / tracking

In a book I’ve read aloud at least 500 times called the [Pig’s Picnic](http://amzn.to/2HWqgGA), a pig (Mr. Pig) wants to look his best when he asks Miss Pig to join him for a picnic. So after obsessing about which bow tie to wear, he takes advice from his friends Lion, Fox, and Zebra and borrows something special from each of them. A foxy tail from Fox. A beautiful head of hair from Lion. And stripes from Zebra. Newly outfitted with delusions of hotness, Mr. Pig shows up at Miss Pig’s doorstep for their date. When she sees the unrecognizable creature in her doorway she squeals, threatens to call her friend Mr. Pig, and slams the door. Mr. Pig runs home, strips off his borrowed finery, and hurries back to Miss Pig’s house with open arms. To children (and those adults out there who identify as children), the moral of this story is “you’re OK just the way you are.”

So I noticed a new LPWAN geolocation project called [Collos](http://bit.ly/2F3Dtjg) which attempts to mimic the story of Mr. Pig. In this case, an unattractive LPWAN stack called LoRaWAN is prepping for a big date with a huge slice of the mobile IoT marketplace called geolocation. But LoRaWAN for battery powered devices is unidirectional, poorly architected throughout, won’t support GNSS/GPS, and was never meant for this kind of action. Reminds me of:



![img](https://cdn-images-1.medium.com/max/800/1*eN4amBaALc_Cekn8fbhs-Q.png)

But the mobile LPWAN market is big, so last year we saw LoRaWANers pushing a time-based trilateration technique to fake geolocation and geofencing. And [as I’ve written](http://bit.ly/2sWkq0w) before, this by itself is a lot like Mr. Pig pretending to be someone he’s not.

So this year we apparently get Collos which doubles down on LoRaWAN and recommends adding multiple *additional* radios to “build on” LoRaWAN’s geolocation prowess. Yes, additional radios. In 2018. Welcome to the future.

Here’s a peek at the craziness:



![img](https://cdn-images-1.medium.com/max/800/1*E4HxIyDvrC3HLzQbJqpN5A.png)

In this case Collos recommends developers use LoRaWAN for pet tracking — a dicey proposition by itself since battery-powered LoRaWAN is a [really bad](http://bit.ly/2pBcYqp)pick for mobile use cases. But to compensate for its weaknesses, Collos recommends *adding WiFi and Bluetooth radios*, which raise device costs and accelerate battery drain, particularly in the case of WiFi. And neither of these is exactly long range.

For example, there this sequence for finding your lost pet:



![img](https://cdn-images-1.medium.com/max/800/1*rcAPDtoBN3QvBjb-0gjGWg.png)

First, GPS on a unidirectional LPWAN device with no ability to receive A-GPS ephemeris data means a cold start *of several minutes* for *each* acquisition of GPS coordinates. I’ve already discussed this, but basically GPS should never appear in the same paragraph as battery powered LoRaWAN unless you think of battery life in terms of days. Then, we’re asked to lean on WiFi — yes, *WiFi* — to solve for LoRaWAN’s lack of bi-directionality. If there are no WiFi access points near or accessible to your lost dog, this feature is useless. But do not despair! Collos recommends adding the renown industry standard for wide area geolocation better known as Bluetooth. If you haven’t heard, Bluetooth is [making headlines](http://bit.ly/2t1RML3) in the world of wide area geolocation.

So here’s what Collos is pitching us, I think: *this unidirectional IoT stack called LoRaWAN is an unattractive option for battery powered geolocation, so to help us put a bit of lipstick on LoRaWAN, please add two additional short range radios so we can appear marginally less unattractive.*

Clearly the LoRaWAN community is struggling to provide a sound response to the demand for geolocation for mobile, battery powered endpoints. GNSS/GPS is j[ust really hard to do](http://bit.ly/2xuqQWv) on battery powered LPWAN’s if your stack wasn’t designed from the ground up to support bi-directional communications and multicast messaging to endpoints. Better, really, for the LoRaWAN community, which seems committed to LoRaWAN for god-knows-what-reason, to have the courage to say that it is “just OK the way it is” for simple fixed use cases like water meters rather than continue to contort itself to be something it was never meant to be. That is to say, geolocation for mobile LPWAN’s will be handled by another stack (or stacks), but it won’t be LoRaWAN.

Two notes:

1. Collos is sponsored by Semtech, the makers of the LoRa LPWAN radio my company, [Haystack](http://bit.ly/2aSPRzX), currently endorses.
2. In fairness, Collos provides this disclaimer:



![img](https://cdn-images-1.medium.com/max/800/1*8JYW59QZ1TtuKjNlnn9LZg.png)



- [I](https://medium.com/tag/internet-of-things?source=post)

# Bluetooth geofencing / trackers

Despite efforts by Bluetooth tracking companies to [pretend](http://bit.ly/2t1RML3) their devices can be found over large geographic areas, Bluetooth is too short range for most commercial or industrial asset tracking, so the subject of geofences there is moot. And passive RFID (EPC Gen 2) is not typically used for mobile asset tracking, either.

But with newer LPWAN technologies and better networking software, mobile asset tracking is about to become much more interesting and geofences will play an important role.

# Generic "dumb" geofencing

**Implement LPWAN Geofences Without Haystack/DASH7?**

If you want to implement an LPWAN geofence using a unidirectional protocol, you might as well call it a “dumb geofence,” since your endpoint is effectively clueless about its location and will likely either “under-transmit” to the gateway — making the geofence useless — or, if the regulatory authorities will allow it, to over-transmit, which in an attempt to emulate a real-time geofence, will burn precious battery life.



![img](https://cdn-images-1.medium.com/max/800/1*FCdLgs4Yo0yJXW_G6pSkSA.jpeg)

How unidirectional endpoints do geofencing

One or two companies are pursuing the “dumb” LPWAN geofence route using a hack of [LoRaWAN](http://bit.ly/lorawan)’s [one-way only capabilitie](http://bit.ly/2xUiokU)s to provide some level of location visibility for battery powered LoRaWAN devices. But since these utilize a unidirectional, uplink-only protocol, their mentions of geofencing are usually scarce or non-existent.

**Drawbacks of “Dumb” Geofences**

The drawbacks of attempting a geofence with a unidirectional protocol should be obvious:

- An endpoint programmed to transmit or “beacon” at some regular interval — say, every 30 minutes — loses any claim to being “real-time” and really should be part of no serious geofencing architecture as your mobile asset may be long gone by the time you receive your first geofence-driven alert.
- An endpoint that uses movement, via an accelerometer, as a trigger for a message from an endpoint is basically of little value for assets that move frequently or in environments where vibration or other environmental factors trigger a false positive. An endpoint that moves constantly — let’s say an animal — would be transmitting continually throughout the day, whether inside a geofence or outside, since there is no way to command the endpoint to stop transmitting or “stay quiet” when it is inside the geofence.
- An uplink-only endpoint that has traveled out of range of fixed gateway infrastructure, has no way to “know” when or how to beacon its existence or respond to a wakeup call from a mobile gateway. An uplink-only endpoint, programmed to beacon every 30 minutes, and has traveled out of range at a rate of 60 mph for 29 minutes could be nearly 30 miles away from the gateway before it is potentially flagged as missing. And given the high rate of packet loss and lack of error correction in battery powered LoRaWAN, there is a strong chance that the missing endpoint will be mistaken for a false negative. Moreover, the antenna array requirements to implement a LoRaWAN uplink-only TDOA system are a non-trivial systems integration effort.
- The lack of error correction in a unidirectional protocol does not provide the gateway with an opportunity to request that the endpoint re-transmit the last message in order to confirm the RSSI value it just received. For example, assume a gateway receives Packet A with RSSI value = 1.0 and then receives Packet B with RSSI value = 0.75 just ten seconds later and then … nothing. If it were your gateway you want to a) confirm that Packet B is legitimate and b) tell the endpoint to send some more packets. But with unidirectional protocol this isn’t possible.

Note: I have seen one company that claims to deploy GPS on LoRaWAN though the battery life — four days! — obviates the need for a LPWAN in the first place and the lack of real-time alerts for a geofence perimeter breach render these useless for geofencing applications.

# Dash7 + Geofencing

**Implementing LPWAN Geofences Using the DASH7 Advertising Protocol**

At Haystack we are implementing the [DASH7](http://bit.ly/2haytech) networking stack over one LPWAN — Semtech’s LoRa — with good results. (More on this [here](http://bit.ly/lorawan) and [here](http://bit.ly/2OQMzkh).) DASH7 provides a fully bi-directional and feature rich firmware stack that overcomes the many limitations of LoRaWAN while exploiting the strengths of the LoRa radio.

To execute geofencing on a LoRa-based LPWAN network, DASH7 contributes at least two unique and essential features.

1. **High-precision location** using DASH7’s multicast feature, as outlined [here](http://bit.ly/2xuqQWv). Without high-precision location, a geofence is just hard to reliably execute and subject to false-positive events. Haystack’s innovative approach to implementing GNSS/GPS over low power radios — using multicasted A-GPS datagrams to shorten the GPS location acquisition sequence to just seconds — while preserving multi-year battery life solves for this.
2. **Real-time geofence alerts** via the **DASH7 advertising protocol.**

In our case, an endpoint briefly samples a channel for activity, checks for signs that there is a background frame within the activity, and if true, receives the background frame. Again, there is more on this in the DASH7 specification but basically the DASH7 Advertising Protocol is the foundation for many features in DASH7 including real-time queries, group synchronization, and more. But in the case of geofencing, it has a more intriguing use: **measuring signal strength.**

**Step 1: Signal Strength As A Proxy For Location**

A conventional approach to the use of signal strength in implementing geofencing would be a simple received signal strength indicator (RSSI) that, when it breaches a given value, triggers an alert. For example, suppose you configure the perimeter of your geofence to correspond with some RSSI value received from a gateway, e.g. a 200 meter radius from the gateway = an RSSI value of *X.* RSSI values above *X* are assumed to indicate an endpoint that is within the 200 meter radius, values below *X* are assumed to indicate an endpoint beyond 200 meters.

Here is a picture showing a circular geofence perimeter:



![img](https://cdn-images-1.medium.com/max/1000/1*5Si6tPEvm1HsdJneaHlTMQ.png)

Mobile asset sitting inside a RSSI-derived geofence …

And here’s another showing the mobile asset that moved outside the geofence:



![img](https://cdn-images-1.medium.com/max/800/1*XuKUnnTMxxR0OhKsUG9Bzw.png)

The mobile asset moves outside the RSSI-derived geofence perimeter. This should trigger an alert.

One issue (among others) with this type of geofencing approach is: what happens if either the gateway or the endpoint are measuring an RSSI value that is corrupted or otherwise “false?” All things being equal, this will trigger an alert to the business user, also known as a false positive. For example, a 40-foot intermodal shipping container parked temporarily between a gateway and an endpoint will — due to the sturdy steel construction of the container and the stubbornness of wireless signals that won’t propagate very easily through or around steel — result in a weak (or non-existent) RSSI value that is *<*X, triggering a false-positive geofence alert.



![img](https://cdn-images-1.medium.com/max/800/1*L-hgl0oWxxEScp7rba077Q.png)

RSSI is not a perfect solution for geofencing. A large metal object placed between a gateway and endpoint may result in false positives.

Or think of a construction site with large metal vehicles, metal girders, and other RF-unfriendly objects:



![img](https://cdn-images-1.medium.com/max/600/0*ntyFYPcMvFuC9ATt)

Google “multipath” for more info

So to avoid false positives in our LPWAN geofencing application, we need a method to confirm — with high precision — the actual location of the endpoint. But before we trigger the logic that would derive high precision location, **it’s better from the standpoint of preserving battery life if we don’t needlessly trigger it.** How?

One answer is to utilize signal strength not as a final determinant of location, but as a *proxy* for location that may trigger an additional process for establishing more precise location. And what better way to implement that proxy than using messaging/packets that are already being transmitted between devices — DASH7 advertising packets!

In other words, a gateway already transmitting DASH7 advertising packets can embed a signal strength indicator into any packet allowing an endpoint to not only “wake up”, but also know whether there is a need to invoke GPS. It’s as if the gateway is continually transmitting “You still there?” and the endpoint only responds when the strength of that transmission decreases past a pre-determined threshold.



![img](https://cdn-images-1.medium.com/max/800/0*5FxIg-0p88FGzwKD)

If RSSI > X, there is usually no need for endpoint on this bicycle to invoke GPS or even reply to a gateway located behind that window …

For example, a bicycle parked in the garage just 20 meters from a residential gateway receives a strong RSSI value embedded in DASH7 advertising packets sent from the gateway and the endpoint may be programmed to do … nothing. But an endpoint receiving advertising packets with decreasing RSSI values can be assumed to be moving away from the gateway and could be programmed to invoke GPS.

In case it isn’t clear, the reason this use of DASH7 and RSSI is so important is that it massively reduces power consumption compared to other high powered/always-on protocols. If you want the “LP” in LPWAN and want a real-time geofence without false positives, this is the best approach available today.

There are alternative versions of this approach, e.g. the *endpoint* transmits advertising packets to the gateway, effecting the same outcome after a gateway responds with a command to invoke GPS. Similarly, environmental sensors may trigger the endpoint to transmit advertising packets to the gateway, i.e. accelerometer. Diving even deeper, it’s even possible to utilize other endpoints as a means for establishing a signal strength proxy, i.e. an endpoint peer with exact (GPS) knowledge of its location can help another endpoint learn its relative location using DASH7’s peer-to-peer and multi-hop messaging capability. (More on that [here](http://bit.ly/2ByPE31).)

In sum, there are many ways that DASH7 helps skin the RSSI cat in support of geofencing, and the fact that a geofence can be implemented without heavy ongoing messaging traffic (and battery drain) is again, especially relative to cellular, a really big deal.

**Step 2: Confirming Location**

OK so we’ve established how to execute a proxy for location using RSSI and DASH7 advertising packets. Now: let’s explore happens when an RSSI measurement falls below a pre-determined level and triggers a sequence to acquire more precise GPS location.

**Confirming the RSSI Alert via GNSS/GPS**

An endpoint that measures an RSSI value that is less than *X* may invoke high-precision GPS (or other GNSS satellite constellation) using the DASH7 multicast feature. This sends a GPS “cheat sheet” or Assisted GPS datagram from the gateway to the endpoint, enabling the endpoint to acquire its GPS coordinates via a “warm start” that takes only seconds. More on this [here](http://bit.ly/2pBcYqp), but **if you are serious about implementing geofencing over LPWAN’s, I recommend GPS** as the way to go given its ease of implementation and, if you really want to avoid false positives, for ease of use. GPS allows for more precise measurements of the location of the mobile asset and avoids potentially large errors possible with RSSI. Over the next 24–36 months, **I expect the pricing of GNSS/GPS receivers for low power devices to decrease significantly.**

GPS allows for greater flexibility in the shape of the geofence. For example, a single gateway implementing an RSSI-based geofence would most likely default to a simple circular geofence like this:



![img](https://cdn-images-1.medium.com/max/800/1*CJC2u8VYkfIZ_TLPrGPfKQ.png)

Black dot = gateway

With GPS, the high precision allows us the flexibility to create geofences that match the contours of a physical boundary like this:



![img](https://cdn-images-1.medium.com/max/800/1*ktT2J_y1VhY8AKc2H_nkhw.png)

Geofenced yard of construction equipment rental company

Or this:



![img](https://cdn-images-1.medium.com/max/800/1*pZbya-wyo97aElGiudWXWg.png)

A series of fenced sections in a depot, all managed with a single gateway and multiple GPS-defined geofences

A side note on GPS: the normalization of “GPS” is also something that many in the IoT overlook: buyers in both enterprise and consumer markets are familiar with the paradigm of GPS and expect GPS-like levels of precision in their mobile asset tracking deployments. It is certainly possible to utilize non-GPS approaches to outdoor location, but give the falling costs of GPS components, the availability of networking stacks like Haystack’s DASH7, combined with the additional costs of implementing a non-GPS location solution, the list of reasons to withhold GPS from end users is growing shorter. Adding GPS/GNSS to your LPWAN feature set is something your customers can relate to way, way better than some of the other nerd-speak in your product specification sheet.

# Cloud

Anchor gateways.

# IoMT

Why Movement is Important to the IoT

An Internet of Moving Things is at its core a network of physical objects that are mobile or moveable and can be wirelessly measured or controlled. Amazingly, the designers of today’s IoT gave little or no thought to connecting things that move and today we are stuck with wireless IoT technologies that require a lengthy pairing ritual that renders them nearly useless for connecting with a moving thing. **Yet solving for moving things is of critical importance to the future of the IoT because:**

1. **Things move!** An IoT that cannot measure or control things that move or things that are moving is an IoT that … is an Internet of Only Some Of The Things. It’s like the internet without SMTP email.
2. **Movement = news.** When a thing moves, it is often an important or “newsworthy” event. For example, sensing movement on your parked bicycle might be an indication that it is being stolen.
3. **Location.** Moving things often change geographic location. The question “Where is it?” is asked every day by billions of people about everything from car keys to shovels to humvees. DoD spends millions of hours every year just [looking](https://www.washingtonpost.com/world/national-security/pentagon-loses-sight-of-500-million-in-counterterrorism-aid-given-to-yemen/2015/03/17/f4ca25ce-cbf9-11e4-8a46-b1dc9be5a8ff_story.html) for stuff like humvees, fyi.
4. **Cause and Effect.** When things move, it’s often caused by or associated with someone or something else. “Movers”, as Aristotle might say, are highly relevant to the big data questions being asked every day. “Who was the last guy to use this broken chainsaw?” or “Which truck carried these frozen vials of flu vaccine?”
5. **Absence.** Conversely, an absence of movement can itself be meaningful. A cow on a ranch or a stay-at-home senior that does not move for 24 hours might be injured or sick.
6. **Battery life.** Movement can be an important power saving tool for managing sleep/wake cycles battery-powered devices. A mobile device that doesn’t move might sleep more than one constantly on the move.
7. **Movement changes risk.** A moving thing may set in motion other events — or at least the potential for other events to occur. A moving car or bicycle or fighter jet is far more likely to crash or experience mechanical failure than one that is parked.

Moving Things Are Already Making Today’s IoT Obsolete

While the mobile internet is expected to be [10x the size](http://techcrunch.com/gallery/mary-meeker-internet-trends/slide/7/) of the desktop internet, the forecasts seem not to have affected most of the folks working on the IoT.



![img](https://cdn-images-1.medium.com/max/600/1*0U4B0cIC6AZeLcZ9rQxb2A.jpeg)

For example, drones are forecasted to be a [multi-billion dollar](http://for.tn/1FoMw8S) industry unto themselves and are already showing their potential as “IoT gateways in the sky” for everything from monitoring [oil pipelines](http://www.fastcompany.com/3031725/fast-feed/oil-giant-bp-is-first-company-approved-to-use-commercial-drones) to moisture content on [farmland](http://ww2.kqed.org/science/2014/04/21/drones-the-newest-water-saving-tool-for-parched-farms/). But the go-to wireless technologies for today’s drones are … wait for it … WiFi and Bluetooth, which can’t communicate with terrestrial-based sensors while moving because they were designed 20+ years ago when CompuServe was still hot.

Along with Bluetooth, ZigBee, Thread, and others, WiFi radios perform an elaborate mating ritual when they connect to a new endpoint. If you’ve ever logged onto a new WiFi access point and it took many seconds or even minutes, it’s because there’s an outdated and obsolete sequence of discovery, handshaking, authentication, payload delivery, and more. As a result, **to connect with any of these, you must remain still — completely still, usually — in order to establish a connection.**

For local area networks like your house where endpoints and access points are mostly fixed, this is probably not an issue. **But for things that move at speeds of 5 mph or more, requiring endpoints to stop whatever they are doing and remain still while a wireless technology “locks on” is simply a non-starter.**

*Note to cellular people reading this: you can drive a drone from afar using cellular, but expecting the rest of the IoT to deploy high-cost and high-powered cellular at the endpoint is fantasy apart from some niche use cases where cost and battery life are not important.*

A Fast Moving World Needs an IoT That Can Keep Up

Drones are just one example of a world of moving things challenging the capabilities of today’s IoT. Here are roughly four categories of things to solve for:

**1. Mobile Vehicles: Next-Gen IoT Gateways**

Mobile vehicles have important roles to play as messaging and sensor data gateways that stand between endpoints and cloud-based applications. Most have onboard power supplies (e.g. a car battery) and most will have high speed cellular connections that facilitate this gateway role. **The ability for a fast moving mobile IoT gateway to reliably communicate with fixed (“vehicle-to-infrastructure”) endpoints is a significant gap in the capabilities of today’s IoT.**



![img](https://cdn-images-1.medium.com/max/400/1*SPRmtIEZ-Go5a0tYr-d8oQ.jpeg)



![img](https://cdn-images-1.medium.com/max/400/1*JIxD50o4TJYsEuNqTJcUEw.jpeg)



![img](https://cdn-images-1.medium.com/max/400/1*E5g8qNqxH9ls7Yu6Y0O7Rg.jpeg)



![img](https://cdn-images-1.medium.com/max/600/1*lj_kXHG5GjvPgTMWjzv_Jg.jpeg)



![img](https://cdn-images-1.medium.com/max/600/1*UOOmr_WRTQMiQM2UsgaY7g.jpeg)



![img](https://cdn-images-1.medium.com/max/800/1*MIfD2daep6bxiHHgz8-kEg.jpeg)



![img](https://cdn-images-1.medium.com/max/400/1*gr2niNfLcj5SajMSJ875VA.jpeg)

Mobile IoT gateways will also communicate with other mobile IoT gateways. For example, there is already work underway around vehicle-to-vehicle or “V2V” wireless using variations on short-range WiFi to support collision avoidance, but this solves (in a very non-secure way) for only part of the vehicle-based opportunity which includes not only other vehicles, but also mobile and fixed IoT endpoints placed along highways, bridges, city streets, or parking garages.

2. IoT Endpoints That Move

These are the millions or billions of endpoints that move, spanning a array of industrial, commercial, government, and consumer applications. When solving for moving IoT endpoints, understanding the **speed** (or distance traveled per second) of an object is important to arriving at the right connectivity solution. For example, there are things that move pretty slowly:



![img](https://cdn-images-1.medium.com/max/400/1*4HN8WEFyK7b3o2TVGH5YBg.jpeg)



![img](https://cdn-images-1.medium.com/max/400/1*SDtpL5MkhjbWXK8WTBrTyA.jpeg)



![img](https://cdn-images-1.medium.com/max/400/1*0bGAVtbL76ffX2iBQguT2w.jpeg)

And there are the things that can move fast:



![img](https://cdn-images-1.medium.com/max/400/1*mqLo2btQTKzQ_Rd_Qir06Q.jpeg)



![img](https://cdn-images-1.medium.com/max/400/1*0vWIZ0lFGEsxDK1Pz-v9-g.jpeg)



![img](https://cdn-images-1.medium.com/max/400/1*bxStbGK3AT-GbN6pTYBV6g.jpeg)

There are things that don’t move on their own but get moved around:



![img](https://cdn-images-1.medium.com/max/400/1*_ggKfkE7NYRAijokqZePKw.png)



![img](https://cdn-images-1.medium.com/max/400/1*8L2qnrzeYBZUzTkqdETU4Q.png)



![img](https://cdn-images-1.medium.com/max/400/1*OLWUJ5NVk4i92gu01BZc4A.jpeg)

3. IoT Endpoints That Don’t Move

A large part of an Internet of Moving Things is just using mobile IoT gateways to measure fixed things. These cover a diverse array of applications and industries and many will be without mains power and require a battery, which in turn means the endpoint can’t use a power-thirsty wireless technology lest it require frequent battery changes or recharges — the near-universal achilles heel of IoT endpoints.

Four Killer Apps for the Internet Of Moving Things

I meet many developers with cool IoT ideas and here are a few that I consider to be killer apps for an Internet of Moving Things:



![img](https://cdn-images-1.medium.com/max/600/1*JIxD50o4TJYsEuNqTJcUEw.jpeg)

**Driverless cars.** To be successful, driverless cars are going to need help from wireless IoT technologies to solve some [big, unsolved vehicle-to-infrastructure problems](http://www.technologyreview.com/news/530276/hidden-obstacles-for-googles-self-driving-cars/)including detecting icy bridges, pedestrians, potholes, uncovered manholes, operating in snow and rain, or maneuvering around construction road crews. Interfacing securely and in real-time with other moving or parked cars more than a few feet away is an unsolved problem as well as communicating with “smart city” and other battery-powered fixed infrastructure like smart street signs or bridge stress sensors. Solving for V2I (and vehicle-to-pedestrian, “V2P”) is fundamentally a low power IoT problem (most V2I situations will not include access to mains power sources) and while the auto industry’s current dalliance with WiFi may make for some nice demos, it won’t solve for V2I or V2P in any secure, private, safe, or scalable way.



![img](https://cdn-images-1.medium.com/max/600/1*yaGi1DD_bwFSAKMHJOkYNA.jpeg)

**Agriculture Drones.** Some of the most exciting drone apps focus on the agricultural sector where drones not only provide high-resolution imagery and infrared sensing, but also an “IoT gateway in the sky” capturing data from animals, water troughs, tools and equipment in the field, and more. The opportunity extends just as easily to other industries where drones are becoming popular like oil and gas, mining, construction, and defense.



![img](https://cdn-images-1.medium.com/max/600/1*E5g8qNqxH9ls7Yu6Y0O7Rg.jpeg)

**Search and Rescue.** Locating missing firefighters or hikers in a forest, shipwreck survivors, lost dogs, and more via moving vehicles like drones or cars. The “eyeball” method for these use cases is now officially obsolete and fast moving vehicles need a wireless technology that can locate things in hard to reach, hard to see places.



![img](https://cdn-images-1.medium.com/max/600/1*kZ50ELsU1KXsoqy1tuAtBA.jpeg)

**E-commerce.** A killer mobile IoT opportunity — perhaps with a longer time horizon? — is in the area of e-commerce, where everything from the handbag carried by a woman walking her dog to passing buses will effectively become a query-able, wireless IoT endpoint. Soon, we will be able to learn the make and model of a cool mountain bike as it passes by or capture a promo code as we pass a billboard on a highway.

How To Get The IoT Moving



<iframe data-width="800" data-height="332" width="700" height="291" src="https://medium.com/media/49d321333588777abf222dde7deb2ddd?postId=112540e79ae" data-media-id="49d321333588777abf222dde7deb2ddd" allowfullscreen="" frameborder="0" style="display: block; position: absolute; margin: auto; max-width: 100%; box-sizing: border-box; transform: translateZ(0px); top: 0px; left: 0px; width: 700px; height: 290.5px;"></iframe>

The big question to explore: what is the best wireless connectivity option to address the internet of moving things? Here are the must-have requirements based on everything we’ve learned so far:

1. **Instant-on.** Solving for the Internet of Moving Things absolutely requires the ability to have “instant on” connectivity. A basic scenario of a fixed endpoint connecting with a car or truck moving at 60 mph means there might be 1–2 seconds of time available to send and receive a message before the vehicle is out of range. This is closely related to the concept of real-time queries at the endpoint which is explored in more detail [here](http://bit.ly/1hExgtG).
2. **Cross-Application Data Interoperability.** On our PCs, we know about the difference of file formats, but we take for granted the fact that there is a common concept of a file, containing a name, modified date, and other useful information along with the data. **There is no such standardization with IoT platforms.** The disconnect, here, occurs because most standards bodies are too compartmentalized: teams work on the wireless standardization, others the networking, others the applications. In an IoT of moving things, it is excessively important for data exchange to be transactable between devices owned by different owners, managed by different networks, and sending different kinds of data. The concept of the file must be clear, and it must be fundamental to the technology stack.
3. **P2P.** Similar to instant-on, capturing data from a fixed or moving object — like a driverless car — should not require a time-consuming cloud lookup and/or cellular network connection and should instead provide the option of pure point-to-point connectivity. Bluetooth Low Energy, for example, operates on the principle of one-way “beacons” that provide a unique endpoint identifier that can only be resolved via a cloud lookup. As hacks go, Bluetooth has done about the best it can do but the IoT cannot be built around a hack. P2P is also important from the perspective of associating an event with other nearby endpoints. E.g., “The door to the refrigerator containing the possible cancer cure was left open by Roger at 2:13 a.m. last night.”
4. **Plays Well with Thousands of Endpoints.** Crowded environments like smart cities and dense industrial settings will be overflowing with fixed and mobile IoT endpoints. Using non-stop beaconing for these is a non-starter, lest we run out of available radio spectrum, drain endpoint batteries, and violate basic principles of privacy. It must be possible to quickly perform queries from among thousands or even millions of endpoints in a given area and with no degradation of latency.
5. **Good signal range.** The farther your wireless IoT technology can communicate, the better its chances of connecting with a moving object, especially one moving at 60+ mph. For example, the short range of technologies like Bluetooth (30 feet max, often less) make connecting with moving objects next to impossible. In 2015 there is no reason not to demand maximum range measured in miles.
6. **Stealth.** It’s one thing for your home thermostat to be hacked but it’s quite another thing for your car’s accelerator or your child’s location to be hacked. “Stealthy” endpoints that listen before they talk (explored in greater detail [here](http://bit.ly/1WQYcXC)) with better low level (MAC layer) encryption are minimally required versus the comically bad privacy and security found in Bluetooth, [WiFi](http://www.securitynewsdesk.com/research-shows-growing-concern-over-public-wifi-security/), [ZigBee](http://thehackernews.com/2015/08/hacking-internet-of-things-drone.html), and other technologies derived from Ethernet. The non-stop [beaconing hack](https://en.wikipedia.org/wiki/IEEE_802.11p) used in some V2I demos is one example of security comedy that could end tragically, but anyone thinking of using variants of a notoriously insecure protocol like WiFi for should remember what happens to automakers who [cut corners](http://www.wsj.com/articles/volkswagen-ceo-winterkorn-resigns-1443007423).
7. **Low Power.** Since most IoT endpoints, either fixed or mobile, are battery powered, low power remains a must-have for nearly all devices in the Internet of Moving Things. For niche devices or mobile IoT gateways (like a smartphone) that customers are already resigned to recharging every day or two (cellular technology is notoriously high power), this requirement does not apply. For 99% of other IoT endpoints, multi-year battery life is non-negotiable.
8. **Low Cost.** Like low power, the non-ascendancy of cellular as a mass market IoT technology is also attributed to the high costs of cellular chipsets and the recurring monthly fees from cellular carriers working to amortize the high capital costs of running a cellular network. Suggested retail price for battery powered IoT modules should be less than $10 based on my own discussions with hundreds of developers and customers, many of whom have a target price point well below $10.

Preparing Your Company For The Internet of Moving Things

If your company is throwing elbows and punches inside the mosh pit of home automation, perhaps the Internet of Moving Things is not your biggest priority. However if your company is investing in smart cities, driverless cars, drones, wearables, or any of the other industries mentioned above, you should be taking note of the shortcomings of the most common wireless IoT technologies in the marketplace as it relates to movement. In some cases it may be possible to demand incumbents update their technologies to better support movement, in other cases the right decision will be to start afresh. My company, [Haystack](http://www.haystacktechnologies.com/), is one of the few in the IoT marketplace that designed its IoT networking stack (based on [DASH7](http://haystacktechnologies.com/products-and-services/what-is-dash7-2/)) with the Internet of Moving Things in mind from the beginning.

But one thing is certain: a failure to address movement will bode poorly not ony for the IoT, but for many new innovations, including many we haven’t even imagined, that will depend on an IoT that can adequately communicate with things that move. The same way that “unforeseen” companies like Uber took advantage of foundational breakthroughs like smartphones, Google Maps, and low cost GPS chipsets, similar companies will be built around an IoT that properly addresses movement.


# Security

A Simple Proposal To Improve Security for the Internet of Things.

A small change can help stop big hackers.

Almost every IoT security breach in [recent news](http://securityaffairs.co/wordpress/39143/security/drone-internet-of-things.html) can be traced to the poor architecture of the [wireless protocol](http://www.iotevolutionworld.com/smart-transport/articles/408425-the-jeep-car-hack-target-moment-the-internet.htm) used by the device. But unlike fighter pilots who maintain radio silence in order to avoid detection by the enemy, it is surprising how few IoT technologies were designed with even a minimum level of stealth in mind.

> **Remaining quiet is not the most important principle of IoT security and privacy, but it’s a pretty basic one.**

Avoiding or minimizing the chances of unauthorized discovery is not technically difficult. But today’s IoT technologies like Bluetooth, 6lowpan, [Sigfox, LoRaWAN](http://www.rethinkresearch.biz/articles/on-lpwans-why-sigfox-and-lora-are-rather-different-and-the-importance-of-the-business-model/), and others make unauthorized discovery **very easy** and it creates the worst kind of [angst](http://www.bizjournals.com/sanjose/news/2015/04/17/data-breaches-and-internet-of-things-risksare.html) in IT departments.

“[Some security measures are often](http://www.esecurityplanet.com/network-security/internet-of-things-a-potential-security-disaster.html) not thought of originally and embedded in the system, so they have to be put in later … A lack of attention and planning is always a source of security problems that inevitably come up when new technology is deployed.” — [Ruggero Contu](https://it.linkedin.com/pub/ruggero-contu/0/60a/a71), analyst @ Gartner

Most wireless IoT technologies were originally conceived as ways to stream large files (Bluetooth, WiFi) while some were designed to be “lighter” versions of WiFi (e.g., ZigBee). Today they are being re-positioned as “IoT” technologies and security, to put it nicely, is an [afterthought](http://rethinkresearch.biz/articles/findings-from-iot-intelligence-survey-raise-more-questions-than-answers/?utm_source=The+Rethink+IoT+List&utm_campaign=f173d12d71-RIoT_68_Friday_Edition_7_3_2015&utm_medium=email&utm_term=0_7db7a5a5fa-f173d12d71-163973785). Oh yes — some have tried to “layer on” security and may profess to support encryption, but hacks for all of these technologies are quite public yet fundamentally traceable to one original sin:

**these wireless IoT technologies don’t know how to keep quiet.**

Most wireless IoT technologies need to make themselves known in order to make it easy for users or networks to “discover” them. If you connect to WiFi in public or even around your home or office, you know what I mean.

More recently, [drones are being used](https://www.praetorian.com/iotmap/#17/30.27066/-97.74213) to hunt for ZigBee-based endpoints, giving bad actors an easy way to discover, map, and [hack ZigBee](http://www.networkworld.com/article/2969402/microsoft-subnet/researchers-exploit-zigbee-security-flaws-that-compromise-security-of-smart-homes.html) endpoints:

this type of hack provides all sorts of information about each endpoint, including manufacturer ID.

Oh and drones are being used to discover WiFi, too. Hacking devices called “[pineapples](http://bit.ly/1Jf2oqI)” enable ridiculously easy [man-in-the-middle](https://en.wikipedia.org/wiki/Man-in-the-middle_attack) WiFi surveillance:

And of course when you hunt for a new Bluetooth device to pair you often discover plenty of Bluetooth devices advertising themselves around you:

This need to be “discoverable” — and this is not limited to ZigBee, Bluetooth or WiFi but to most wireless IoT technologies — requires a near-constant advertising of a device’s presence, leading to any number of “[disaster scenarios](http://www.esecurityplanet.com/network-security/internet-of-things-a-potential-security-disaster.html)” that others have extensively written about.

# Stealth

In my experience, few people who understand IoT customer requirements will object to the principle of quiet or “stealthy” IoT endpoints, *at least in principle*. In technical practice, however, it means upgrading or replacing legacy technologies, of which there are roughly three classes as it relates to stealth:

1. **Chatterboxes.** These devices talk non-stop, sending data to the network every few milliseconds whether they have something important to say or they just want to repeat what they said 200 milliseconds ago. They usually share things in the clear (not encrypted) and are easy to spot in the wild. And hack.
2. **Cuckoos.** Like a [cuckoo clock](https://en.wikipedia.org/wiki/Cuckoo_clock), these devices don’t necessarily talk non-stop but they periodically blurt out their presence — usually every few seconds — in order to sync with a network and aid discovery. They are usually capable of sending a message when they have news of an event to share — like a change in temperature, for example.
3. **Snipers.** These devices speak only when an authorized device queries them or, like Cuckoos, when they have something important to share with the network. They don’t “fire” their weapon unless absolutely required.

Most wireless IoT endpoints in the marketplace today fall into the chatterbox or cuckoo class, which violate what should be a first principle of IoT device security:

**Be stealthy.**

Why Stealthy IoT Endpoint Design Matters

> “Properly implemented strong crypto systems are one of the few things that you can rely on. Unfortunately, endpoint security is so terrifically weak that NSA can frequently find ways around it.” — Edward Snowden

The natural state of most things in the world is … quiet. Think about it. Thousands of years of trial and error prove that being quiet (perhaps in combination with hiding) helps to avoid alerting predators to your location, enables prey to hear an approaching predator, provides an ambient environment that gives others the ability to be heard, and conserves energy. In the world of wireless, [radio silence](https://en.wikipedia.org/wiki/Radio_silence) has been a basic tenet of military communications security that remains in place today.

Silence is almost always inexpensive, easy to do, and effective and is probably the most popular security behavior practiced by humans since … Neanderthal man.

There is no technical reason that the Internet of Things cannot embrace silence, or *stealth* as I prefer to call it, as a first principle of endpoint security. Stealth is not a silver bullet for IoT security ([there is no silver bullet](http://www.windriver.com/whitepapers/security-in-the-internet-of-things/wr_security-in-the-internet-of-things.pdf)) and stealth alone won’t protect a network from intrusions, but **dollar-for-dollar, stealth is the simplest, cheapest, and most effective form of IoT security protection available.**

> **The simplest and least expensive security requirement for next generation wireless IoT technology design is stealth.**

**Why?**

1. **Cloaking.** It is harder to discover, hack, spoof, and/or “stalk” an endpoint if a hacker cannot locate the endpoint.
2. **Googling the IoT.** Stealth enables [real-time queries of endpoints, a la Google](http://bit.ly/1N3MSmv) search that non-stealthy endpoints can’t support. Stealth also enables fast queries (<2 seconds) in environments with thousands of endpoints, in turn enabling big data analytics at the true edge of the network.
3. **Minimize interference.** Less data being transmitted minimizes the opportunities for interference and failed message transmissions. Contrast this with the [tragedy of the commons](http://bit.ly/1hjJZBV) at 2.45 GHz, where WiFi, ZigBee, microwave ovens, and other countless other technologies engage in wireless gladiatorial combat and cause too many customers to return their IoT gadgets because they “don’t work”.
4. **Maximize wireless network capacity.** Stealthy endpoints send and receive less data and make it possible to operate in radio spectrum where spectrum is “narrow”. This is particularly important with newer [LPWAN technologies](http://bit.ly/haystackiot) that appear poised for success in the IoT.
5. **Power.** Less data being transmitted reduces power consumption both at the endpoint and in the downstream network. If your IoT endpoint is battery powered (most are), then stealth is important unless your customers enjoy changing or recharging batteries.
6. **Access control.** Stealthy endpoints make it easier to control access to the endpoint by limiting who can query the endpoint.
7. **Storage.** Less data being transmitted reduces storage costs. [Storage vendors](http://searchstorage.techtarget.com/opinion/Internet-of-Things-data-will-boost-storage), on the other hand, love the non-stealthy IoT status quo.

> **Put simply, IoT wireless endpoint design that does not embrace stealth is inherently less secure and less private.**

Principles of Stealthy IoT Endpoint Design

There is no global consensus on how best to implement wireless IoT endpoint security. Competing vendors claim to solve for slices of what amounts to a [massive challenge](http://www.securityweek.com/massive-challenge-securing-internet-things), but reasonable people should be able to agree on first principles of next-gen IoT endpoint design in order to achieve stealth:



![img](https://cdn-images-1.medium.com/max/600/1*tdsYAsIvxmDIzsjF6GAAyg.jpeg)

- **Chatterboxes and Cuckoos are out, Snipers are in.** Wireless protocols that constantly advertise their presence or otherwise spew too much data are obsolete or obsolescent. Their inherent security and privacy flaws stem from design that took place in a different era with a different vision of IoT use cases and different silicon.
- **Listen-Before-Talk (“LBT”).** Listen-before-talk implies an endpoint that “listens” for an authorized interrogator before transmitting anything to the network. Its means of network synchronization, the way it checks for new messages, the way it masks its address, and other factors encompass the way a LBT endpoint behaves. **LBT is essential to stealthy IoT endpoint design.**
- **Event-driven messages.** “Event-driven” implies an endpoint that transmits a message about an event — for example, a change in temperature or the detection of movement — when the event occurs. Like LBT, event-driven messages are essential to stealthy IoT endpoint design as data is only transmitted in connection with important events rather than at some arbitrary interval or for purposes of synchronizing with the network.



![img](https://cdn-images-1.medium.com/max/600/1*DKmcyxOxBvhNi0YFddk1rA.png)

- **Full-stack stealth.**Implementation of listen-before-talk and event-driven architecture in the endpoint cannot be limited to a single layer (e.g. Layer 2) in the [OSI stack](https://en.wikipedia.org/wiki/OSI_model), but rather must implemented **throughout** the endpoint’s firmware/software stack — from layers 2 through 7. For example, the principle of stealth is defeated if the low level operating mode of the endpoint is “quiet” but the means of network syncronization or the application running on the endpoint forces unnecessary chatter with the network. **All layers of the firmware stack must work in concert to successfully achieve stealth.**
- **Data caching.** Rather than transmit data as it is created, stealthy endpoints [cache](https://en.wikipedia.org/wiki/Cache_%28computing%29) data in the endpoint until the endpoint is queried by an authorized user or an event triggers the sharing of the data. By caching, we enable [real-time endpoint queries](https://medium.com/@patburns/why-you-can-t-google-the-internet-of-things-1f1207212a75) and reduce the strain on wireline network infrastructure and storage.
- **Better Low-Level Cryptography.** Stealthy endpoint design must define methods for managing a network of [multiple keys](https://en.wikipedia.org/wiki/Key_management), as well as new ciphers suited to small data payloads. WiFi hackers, for example, take advantage of the fact that WiFi devices talk too much, and common traffic from different devices can be analyzed against each other. This works because all the devices on the network use the same key. During WWII, British code breakers used this same basic strategy to break German codes.
- **Firmware updates.** Stealthy endpoint design must not preclude the secure execution of over-the-air (OTA) firmware updates and patches. As devices age, they require maintenance including security patches, and the operating mode of a wireless protocol should not preclude OTA software updates.
- **Open Source.** Many security vulnerabilities are simply bugs or oversights which would have been quickly detected and fixed if there had been an open source community working on the project. A famous example is the security firmware for the smart card payment platform [MiFare](https://en.wikipedia.org/wiki/MIFARE).

It is worth mentioning that almost by definition achieving stealth results in an endpoint consuming less power. Similarly, stealthy endpoints that speak when queried are better stewards of scarce radio spectrum. So while stealth is an important next step in IoT security, it simultaneously solves for other IoT usability and scalability goals.

How We Can Bring Stealth to the IoT … Now

If security is such a big deal for the IoT — and there are [more than a few](http://www.networkworld.com/article/2921004/internet-of-things/beware-the-ticking-internet-of-things-security-time-bomb.html)[experts](http://www.zdnet.com/article/internet-of-things-you-have-even-worse-security-problems/) who think it is — then we should be taking steps now towards implementing stealthier endpoints.

- **Rethink roadmaps.** First, and most importantly, established vendors should re-think wireless protocol design roadmaps and incorporate full stack stealth at least as a matter of corporate responsibility, if not for revenue opportunities. The kind of shareholder and brand fallout experienced in recent [payment card](http://www.bloomberg.com/bw/articles/2014-03-13/target-missed-alarms-in-epic-hack-of-credit-card-data) and [email](http://www.thewrap.com/11-revelations-from-wikileaks-sony-hack-emails-amy-pascals-travel-expenses-david-fincher-complains-of-leak/) hacks is sure to reach the Internet of Things soon, so responsible CXO’s and boards are asking whether IoT roadmaps include full stack stealth. There is also little reason why standards bodies like the ZigBee Alliance, the [Thread](http://threadgroup.org/) Group, and others who profess to care about IoT security cannot add stealth as a requirement for their next iterations of their stacks.
- **New ventures may already have the answer.** The huge number of new IoT ventures being created every month reflects the scale and scope of the opportunity. Companies like the one I co-founded, [Haystack](http://www.haystacktechnologies.com/), are bringing new stealth-based IoT technologies like [DASH7](http://haystacktechnologies.com/products-and-services/what-is-dash7/) to the marketplace and others may follow, but LBT and event-driven messaging is at the core of what we designed at Haystack.
- **Borrow & Mix.** A combination of the first two may provide the industry with an interim solution. Melding new technologies and standards [on top of existing standards](https://medium.com/@patburns/5-reasons-the-iphone-6-will-save-the-internet-of-things-7ac8b96fbd5) may provide a way of staunching some of the bleeding.



![img](https://cdn-images-1.medium.com/max/600/1*haw2_8dv6Eszb2SXIEOVfA.jpeg)

“We believe that by adopting the best practices we’ve laid out, businesses will be better able to provide consumers the protections they want and allow the benefits of the Internet of Things to be fully realized.” — FTC’s Edith Ramirez

- **Regulatory pressure.** Short of industry moving to stealthier connectivity for business reasons, we will likely see external drivers of stealth, too. The prospect of [government regulation](http://www.usatoday.com/story/news/politics/2015/02/09/internet-of-things-house-caucus-senate-hearing/22927075/) of the IoT is a [growing threat](http://www.rt.com/usa/227111-ftc-internet-things-risks/) now in Washington as the IoT is seen as rife with risks to consumer privacy and [homeland security](http://www.nextgov.com/cybersecurity/2014/11/report-government-has-only-5-years-secure-internet-things/99446/).

# Real-time

Real-Time Is A Must-Have for the IoT

Today’s internet is mostly [real-time](https://en.wikipedia.org/wiki/Real-time_computing) (for a good time waster, [check this out](http://pennystocks.la/internet-in-real-time/)) and the Internet of Things needs to be real-time, too. If you disagree with this statement you are either invested in non-real-time technologies or you still watch the CBS Evening News at 6 p.m. on Channel 2 with your black and white television. **The importance of real-time data — with a real-time query capability that is transacted at the edge of the network — should be obvious** to anyone familiar with the scalability and operating challenges of future IT networks. Just in terms of time, consider industrial, commercial, and public safety applications where minutes or seconds of latency can render data non-actionable and often worthless.

> **“We clearly see data and content being created**[ **at the edge of the network**](http://www.eweek.com/networking/fog-computing-aims-to-reduce-processing-burden-of-cloud-systems.html) **… this content won’t be sent over the network to be processed by the ‘enterprise-based’ cloud infrastructure. Rather, you will need cloud computing-like processing at the edge.”— Vernon Turner, SVP @ IDC**

There are only two essential jobs of a low power wireless IoT technology:

1. Immediately send a message when an important event occurs.
2. Immediately and accurately answer queries, simple or complex, from an authorized user.

The first job is something that many IoT technologies don’t do that well. A few do it on an as-it-happens basis (e.g. IF the temperature in this storage facility falls below 40 degrees, THEN send an alert message to router). Those who can’t do this usually overcompensate by sending *everything* every few milliseconds so that nothing gets missed and someone else cleans up the data aftermath. Still others send a regular update every 10 minutes or **10** **hours** *(!)*since their network design or choice of wireless frequency prohibits anything more frequent.

The second job is one nearly every one of today’s technologies fails to do. Here’s an example of a simple real time query request:

*Query: “I need the location and pressure statistics for the past five hours on any fire extinguisher in the metropolitan area that was touched by XYZ Corp this month.”*

But the response to this request using today’s IoT connectivity options would go something like:

*Result: “Will do, sir, but we have 50,000 endpoints in the area so we should be able to get the data to you by Friday around lunchtime.”*

Beyond Real-Time Networking

The practical benefits of a real-time IoT at the network’s edge mentioned so far are really just the start and the ability to query endpoints directly — with or without the cloud — gives rise to entirely new opportunities. For endpoints in public networks, we will see **public API’s and paywalls for individual IoT endpoints**. **Advertising or e-commerce in association with specific endpoints.** **Endpoints that behave in unique ways when queried by or in the physical presence of another unique endpoint or person.** For private networks, business intelligence applications can now bypass the latency of today’s wireless IoT technologies and see faster (in a few seconds, in most cases) and more meaningful reporting. Just as some of today’s biggest web-based phenomenon like YouTube or Facebook would likely not exist had Google not perfected the indexing of the web, some of the biggest innovations in the IoT await the ability to spider and search wireless endpoints.

# Network types

We can usually categorize wireless IoT technology deployments into about three network models:

**Commercial and Industrial Networks.** These make up the majority of IoT connections in the world, yet a potpourri of wireless IoT technologies is deployed here with most designed long before the realities of [Hadoop](https://en.wikipedia.org/wiki/Apache_Hadoop), [ARM-based](https://en.wikipedia.org/wiki/ARM_architecture) silicon, smartphones, and other innovations that — combined — make extraordinary IoT forecasts more believable. Well-meaning technologies like ZigBee or 6lowPAN hog bandwidth in dense environments, drain endpoint batteries too quickly, and don’t offer the real-time query capability at the edge of the network that the IoT needs. In many cases, these technologies are programmed to beacon their status every few milliseconds as a way to fake a real-time query capability, which [wreaks havoc](http://www.gartner.com/newsroom/id/2684915) on the downstream network. To their credit, cellular carriers have made good strides in re-using their LTE networks for IoT applications, but LTE’s high cost and short battery life limit its potential to mains-powered applications like vending machines, so their role in the tsunami is relatively limited. Newer technologies like [LPWAN’s](http://www.computerworld.com/article/2867331/these-iot-networks-are-unapologetically-slow.html)(you might have heard of [SigFox or LoRa](http://www.rethinkresearch.biz/articles/on-lpwans-why-sigfox-and-lora-are-rather-different-and-the-importance-of-the-business-model/)) seem likely to prevail due to range that is often comparable to LTE while utilizing less costly hardware and consuming power consumption at a fraction of LTE’s rate. LPWAN’s at the moment suffer from a one-way beaconing syndrome where data can only be sent every few minutes, though [help is on the way](http://haystacktechnologies.com/haystack-lpwan-presentation/).

> **“IoT deployments will generate large quantities of data that need to be processed and analyzed in real time … leaving providers facing new security, capacity and analytics challenges.” —** [**Fabrizio Biscotti**](http://www.gartner.com/newsroom/id/2684616)**, research director @ Gartner.**

**Private Personal Networks.** Your [FitBit](http://bit.ly/1INBr0y) uses Bluetooth beacons that send accelerometer data to your smartphone (or anything nearby) every few milliseconds. FitBit is a major success, but non-stop beaconing is a dumb way to send data to your smartphone or usually anything else. [Far better to batch the data](http://www.pcworld.com/article/2946039/can-your-wearables-sucky-battery-life-be-saved-maybe-by-streaming-to-a-smartphone.html) and transmit less frequently — ideally when an authorized user queries it — resulting in major battery life gains for your FitBit and your smartphone. And since Bluetooth beacons are unencrypted, batching data makes it harder for [stalkers and NSA types](http://www.wired.com/2015/08/hackers-can-seize-control-of-electric-skateboards-and-toss-riders-boosted-revo/) to do their spy work. Oh, and this wearables market is [projected to be at $53 billion](http://www.juniperresearch.com/press/press-releases/smart-wearables-market-to-generate-$53bn-hardware) in four years, which combined with oodles of other Bluetooth gadgets, is its own data tsunami.

**Public Networks.** Exciting but mostly in the pilot or planning phases, these include smart cities that make real-time parking data available to anyone who asks. Public or semi-public lost-and-found networks for everything from stolen bicycles to lost [Alzheimer’s patients](https://en.wikipedia.org/wiki/Silver_Alert). Roadways equipped with environmental and other sensors to be shared with vehicles to ease congestion, reduce fuel consumption, and improve safety. For public networks using licensed spectrum (e.g. cellular carriers), the data tsunami is capped by the practical limits of the technology. For public networks using unlicensed spectrum (like LPWAN’s, which I expect to prevail in public networks), a [tragedy of the commons](http://bit.ly/1hjJZBV) problem puts them in a similar tsunamic position as private commercial networks.

# Big data / IoT data tsunami

**“With this massive influx of data many companies will have no idea what hit them.” —** [**Bill Briggs**](http://techcrunch.com/2015/05/19/the-internet-of-some-things/?ncid=rss&cps=gravity_1730_-6534947085658919463#.elat5p:accn)**, CTO, Deloitte Consulting**

Just how serious is the risk of an IoT data tsunami?

- By 2017 [half of IT networks](http://www.zdnet.com/article/iot-boom-signals-possible-network-capacity-overload-idc/) will go from having a network capacity surplus to being network constrained, and 10 percent of sites will be overwhelmed. Storage vendors, on the other hand, [love the IoT status quo](http://searchstorage.techtarget.com/opinion/Internet-of-Things-data-will-boost-storage).
- [86% of manufacturers](http://www.economistinsights.com/technology-innovation/analysis/manufacturing-and-data-conundrum) in US and Europe already report major increases in shop-floor data collection over the past two years; 62% are not sure if they have been able to keep up with larger data volumes.
- Working overtime to feed the tsunami, battery-powered endpoints lose [battery life](http://www.electronics-eetimes.com/en/iot-wireless-sensors-and-the-problem-of-short-battery-life.html?cmp_id=7&news_id=222925594&page=0) prematurely, resulting in higher maintenance and replacement costs, something that catches IoT newbies by surprise. Data overload also causes data centers to work harder and [burn more electricity](http://www.computerworld.com/article/2598562/data-center/data-centers-are-the-new-polluters.html) in the process.
- Security and privacy [weaknesses abound in IoT](http://www.wired.com/2014/01/theres-no-good-way-to-patch-the-internet-of-things-and-thats-a-huge-problem/) networks but wireless connectivity is a notorious hacker’s hangout. About 90 percent of all IT networks will have an [IoT-based security breach](http://www.zdnet.com/article/iot-boom-signals-possible-network-capacity-overload-idc/) within two years.

**“We live in a real world where bandwidth is neither infinite nor free. There’s a lot of data being generated. We talk about 50 billion sensors by 2020. If you look today at all the sensors that are out there, they’re generating 2 exabytes of data. It’s too much data to send to the cloud. There’s not enough bandwidth, and it costs too much money.” —** [**Todd Baker**](http://www.biztechmagazine.com/article/2014/08/fog-computing-keeps-data-right-where-internet-things-needs-it)**, OIX product management head @ Cisco**

Today’s Wireless Is Killing the IoT

To pinpoint the origins of the data tsunami, go to the source: the wireless IoT endpoint. Wireless endpoints are essentially a computer chip, a **radio**, an antenna, one or more sensors, some memory, and a power supply. Endpoints can be very tiny or quite large and can be standalone or integrated with other devices, but all share these basic attributes. **The purpose of an endpoint is simple: to sense its environment and report to the network as programmed.**

The radio in an endpoint can employ one of a number of low power wireless communications protocols yet most protocols were created to be a sort of WiFi-lite. As a result, nearly all are oriented around pushing data (remember [Pointcast](http://askville.amazon.com/happened-Pointcast-push-technology-general/AnswerViewer.do?requestId=7037556)?) — to the network rather than endpoints standing by for intelligent queries to pull data, a la Google Search.

> **“Not only has the demand for capacity on our wireless networks been accelerating significantly, but it’s been accelerating in a non-scalable way,” says Charles Golvin, analyst @** [**Forrester Research**](http://www.forrester.com/rb/research/)**.**

Unfortunately, as the data tsunami is upon us, technologies like [Bluetooth](https://en.wikipedia.org/wiki/Bluetooth), [6lowPAN](https://en.wikipedia.org/wiki/6LoWPAN), [ZigBee](https://en.wikipedia.org/wiki/ZigBee) and others are utterly unfit to the task of the next phase of the IoT.

Where The Tsunami Is Happening

![img](https://cdn-images-1.medium.com/max/800/1*xjB7g0GluWNb7i2tR8-71Q.jpeg)

**“IoT threatens to generate massive amounts of input data from sources that are globally distributed. Transferring the entirety of that data to a single location for processing will not be technically and economically viable.” — Joe Skorupa, VP Distinguished Analyst @ Gartner**

# Google-like IoT search

That none of today’s protocols seriously contemplated a Google-like future for the IoT is astonishing. Searching in real-time for objects in the Internet of Things using simple or complex queries — and thereby pushing the maximum amount of data cleansing and analysis to the edge of the network — didn’t make anyone’s priority list 10–20 years ago?

The IoT Needs A Google

The data tsunami is a complex business and technical problem, and Occam’s Razor says to use the simplest approach to solve complex problems. The simplest approach to solving the IoT data tsunami is to **fundamentally rethink the role of IoT endpoints**. Today’s endpoints can often be (simply) abstracted into something like this:



![img](https://cdn-images-1.medium.com/max/800/1*C74trB-B7fP3FSnGiYrI9g.png)

This approach is not only not addressing the data tsunami of today, it provides almost no room growth from future developers who want to exploit the data on an endpoint any number of creative and innovative ways no one has even countenanced.

Google is the most popular way of searching the world wide web due to its simplicity, speed, and effectiveness. **It’s time to think of IoT endpoints more like web servers with an integrated database/filesystem that can be queried on demand or set to generate alerts. In other words, the Google model.**

Note that many IoT vendors will continue to advocate for the current “dumb endpoint” approach, claiming that a router or gateway that connects to the endpoint can do the parsing, filtering, and storing of data — a sort of “near-edge” computing paradigm. But their argument is rooted in the inherent weaknesses of incumbent wireless technologies and does nothing to improve wireless radio spectrum capacity, endpoint battery life, endpoint privacy and security, or storage costs. It’s a little like saying that Google should be indexing content delivery networks like Akamai instead of individual websites themselves.

# Pull model

Like a web server, the ideal default for an IoT endpoint is to require that it remain silent until an authorized user queries it with a specific question or command. Keeping IoT devices in quiet mode forces them to batch data and “speaking only when spoken to” solves for many problems simultaneously:

1. Enables higher quality, real-time data queries
2. Pushes computing and analysis to the extreme edge of the network, reducing network congestion and latency
3. Improves network capacity, reducing hardware, storage, power, and labor costs
4. Reduces power consumption at the endpoint, router, and data center.
5. Improves privacy and security

But what if a sensor is tripped without a query? This is important as well and IoT endpoints need the flexibility to transmit to the network when a specific event occurs, like, say, a sensor threshold is breached or a motion sensor detects a cat walking by.

The IoT endpoint architecture of the future would ideally be (again simply) abstracted like this:



![img](https://cdn-images-1.medium.com/max/800/1*V2esJMLNcL13QOhS1scRaQ.png)



# Haystack performance

How much range is possible? **We recently tested a beta version of our upcoming product,** [**HayTag**](http://www.haytagstore.com/)**, at a range of** **more than two miles (3.2 km)**in San Mateo, California using 433 MHz under strict (less than 1 miliwatt) FCC power limits and using an antenna contained in a tag that is about the size of a poker chip. Its indoor performance—the ability to maneuver through walls, HVAC ducts, metal plumbing fixtures, and even human flesh — shows great promise.

How To Add A Google To the IoT

Querying an IoT network Google-style may seem obvious or easy, but it’s also possible that it wasn’t built (until now) because it is hard to do. At a company I co-founded, [Haystack](http://www.haystacktechnologies.com/), **we designed an endpoint device filesystem and low latency, query-based device architecture to enable exactly this kind of real time data retrieval.** The technology, called [**DASH7**](https://en.wikipedia.org/wiki/DASH7), does this (and more) uniquely in the marketplace:



![img](https://cdn-images-1.medium.com/max/800/1*Hx4y9k1Ok0krKDV9udhRJg.png)

[Haystack](http://www.haystacktechnologies.com/) is still a young company, but [getting good reviews](http://www.rethinkresearch.biz/articles/dash7-offers-alternative-lpwan-open-standard/) and we submit that our approach as a step in the right direction to help avert the IoT data tsunami.

# Cellular

*I am omitting cellular, which is expensive, power hungry, requires a monthly subscription, and is not a serious option for most IoT applications.*

**Lessons From Cellular**

In the mobile handset business as well as other mobile data businesses, this borrowing of connectivity is known as “roaming”. Carriers make roaming agreements with your carrier and charge your carrier for the right to connect on their network. When roaming, your phone’s right to roam in another’s territory is authenticated using a private key embedded in a SIM card inserted into your phone. Billing matters are pre-arranged between your home network and the partner network. Basically, SIM’s are/were a necessary evil for mobile phones for a range of reasons including but not limited to roaming, but the constant with mobile phones is they are tied to human users who will (usually) detect a missing handset within minutes or hours, report it lost/stolen, and generally mitigate the kind of fraud charges we see in the Hijacked Stork incident above.

**But wide area mobile IoT devices are different.** By definition, they (frequently) operate remotely and away from the beneficial owner or user. Detecting a stolen mobile IoT device may not be obvious and using the Hijacked Stork as an example, the GPS location of the fraudster making phone calls might appear on a map the same as it would for the stork.

For owners or operators with multiple (even thousands) of devices, the risk of a stolen SIM is compounded by orders of magnitude.

But as the Lesson of the Hijacked Stork illustrates, this is risky business for LPWAN vendors. If your mobile LPWAN device supports fully bi-directional communications and public key cryptography, the risks of the theft of a SIM card can be mitigated or eliminated via SIM-less roaming. But for those of you out there experimenting with SIM-based mobile LPWAN devices like [this one](https://www.zdnet.com/article/samsung-launches-nb-iot-gps-smart-tag/), it’s probably worth asking your engineering team if they are *really* going to deploy a SIM card with it and if so, if they are fully aware of the risks.

**Maybe The SIM Is Not Such A Great Idea for the Mobile IoT**



![img](https://cdn-images-1.medium.com/max/800/1*1Ncyhx42qyyOCI6dsPxhNw.jpeg)

Adding a SIM to a mobile IoT device is a bad idea for many reasons, but here’s a really basic one: **adding a SIM to an IoT device increases deployment**[**costs:**](http://www.nickhunn.com/lora-vs-lte-m-vs-sigfox/)

> “Today almost every M2M device includes a SIM card. **The cost of procuring the SIM card for an M2M application, getting someone to physically put it in the SIM card slot and then verify the network connection usually costs upwards of $25**. As the same engineer is probably also physically installing the device, which takes 30 minutes or more, that’s lost in the overall installation costs, so no-one really appreciates it. But the prospect of tens of millions of SIMs being fitted into devices every day to get to our tens of billions is a non-starter. The IoT needs products which are taken out of a box, turned on and just connect and work. For LTE-M that means eSIMs, which are still only supported by a few networks. Both cellular and LPWAN networks need ways to register devices automatically, so manufacturers can buy services for multiple units which they pre-provision.”

So before we even get to the security risks of a SIM in a LPWAN device, the simple addition to total cost of ownership should be enough to shake your head.

SIM cards are de rigeur for wireless carriers, so you shouldn’t be surprised to hear that NB-IoT and LTE CAT-M devices are using them. Here is [AT&T’s](https://marketplace.att.com/products/att-iot-starter-kit-lte-m) LTE-M “starter kit” and here’s [Vodafone’s](https://www.vodafone.cz/en/about-vodafone/press-releases/message-detail/technologie-nb-iot-vodafonu-zvysi-efektivitu-dodav/) NB-IoT version of the same. The state of carrier IT and billing systems leads me to predict that carriers will not be quick to abandon SIM cards for IoT devices, mobile or fixed.

If you want to predict whether your IoT device will “steal” from you, you can raise the probability by a huge margin if the device includes a SIM card. The theft could be overt, a la the Hijacked Stork, or more subtle, as in the hit to TCO. The SIM has its uses in mobile telephony but its use in IoT devices, particularly mobile IoT devices, is a stopgap whose time has passed. Bring on the SIM-less IoT devices.

*Next post: Options for SIM-less wide area IoT systems.*



# Today's developers

As a result, today’s developers have to compromise with “What is the best I can do using Bluetooth or WiFi?” when they should be asking, “What sort of world-changing IoT product could I build if range, battery power, or device cost were not an issue?”

# Streaming

**WiFi and Bluetooth are comically weak IoT connectivity options.** Both were designed as streaming technologies and if they were truly compelling IoT options, one or both would already be widely deployed among the millions of commercial, industrial, or military embedded sensor networks scattered throughout the world today. But alas, this did not and never will happen. Bluetooth, after 25 years, still has woeful interoperability problems. WiFi is insecure for roaming connections, is difficult to configure, and requires a hard-coded internet server address in order to get around any of these problems—all fatal for an IoT technology. **The real reason Bluetooth and WiFi reside in your smartphone is to replace headset cables and enable you to cheaply stream large amounts of data from the internet!**

**protocols like Bluetooth or WiFi that were designed to pipe audio to wireless headsets or wirelessly stream Netflix!**

# Fixed Hub

A hub is a fixed piece of hardware (like the Cisco router in your home or office) that is of little use to mobile users who need to monitor the body temperature of 10,000 head of cattle on a ranch, control a flying drone, or locate a missing Alzheimer’s patient. A hub also forces developers to interact with IoT hardware (like a [home security system](http://www.control4.com/products/system-overview)) via an intermediary (a hub) acting as a gateway to one or more other outdated wireless technologies like [ZigBee](http://en.wikipedia.org/wiki/ZigBee) or [Insteon](http://en.wikipedia.org/wiki/Insteon). As a result, developers are locked into that proprietary hub with no way of ever directly connecting to an IoT node, not unlike the days when AOL tried to convince developers that they should develop apps that access the World Wide Web via the AOL Developer Network.

# History

The more sensational IoT success stories of the last decade like [RFID tags at Wal-Mart](http://online.wsj.com/news/article_email/at-zara-fast-fashion-meets-smarter-inventory-1410884519-lMyQjAxMTA0MDEwNzExNDcyWj?tesla=y) were built around plus-sized enterprise software, short range wireless connections, and ugly and overpriced hardware.

How The IoT Was Blindsided

Once upon a time, some people in the Defense Department created the [internet](https://en.wikipedia.org/wiki/ARPANET). Then when that turned out pretty well, some other people decided to try to create a wireless version of the internet and invented technologies like WiFi. Still others invented more ways of connecting gadgets to this internet thing and built technologies like Bluetooth and ZigBee. All of this happened a long time ago before [MIT](https://en.wikipedia.org/wiki/Internet_of_Things#Early_history) even coined the term “internet of things”.

But a funny thing happened on the way to the internet of things: newer and more exciting technologies. [ARM](https://en.wikipedia.org/wiki/ARM_architecture)-based processors, [MEMS](https://en.wikipedia.org/wiki/Microelectromechanical_systems) sensors and actuators, the iPhone, and more. It all happened so fast … and as I’ve outlined [here](http://bit.ly/1N3MSmv) and [here](http://bit.ly/1WQYcXC) and [here](http://bit.ly/haystackiot), today’s wireless IoT technologies are the [cassette tapes](http://bit.ly/1Kt5WX3) of the IoT and won’t scale in any kind of secure or practical way. **But today’s wireless IoT pain looks like pleasure compared to the ugly reality of the mobile IoT, or what I like to call the “Internet of Moving Things”.**

# 433 MHz

There is more than one option for a second frequency to 13.56 MHz, but the company I co-founded, [Haystack Technologies](http://www.haytagstore.com/), is deploying one that is well-tested: 433 MHz. Long the domain of garage door openers, tire pressure monitoring, keyless entry systems, and shipping container tracking tags, 433 MHz is an underutilized, license-free, and globally-available slice of spectrum that can deliver both long range and help deliver low power. It will not interfere with other radios in today’s smartphones — unlike radios operating around 900MHz or 2.45GHz — and its low power emissions ensure little or no health risk from electromagnetic radiation.

# Smartphones

Construction workers, doctors, field service techs, soldiers, cops, retailers, students, and basically [most human beings](http://www.emarketer.com/Article/Smartphone-Users-Worldwide-Will-Total-175-Billion-2014/1010536) in the industrialized world rely on their smartphone as the [device they rely on](http://allthingsd.com/20110808/people-willing-to-go-without-sex-shoes-and-caffeine-rather-than-give-up-their-cell-phone/) more [than any other](http://www.psychologytoday.com/blog/artificial-maturity/201409/nomophobia-rising-trend-in-students).

One conclusion is inescapable: **smartphones are becoming the universal remote control for the Internet of Things.**

But the [consumerization of IT](http://www.forbes.com/sites/louiscolumbus/2014/03/24/how-enterprises-are-capitalizing-on-the-consumerization-of-it/), low cost smartphones, and low barriers to entry for developing both smartphone apps and IoT hardware are changing the way developers think about building for the IoT.

**Yet despite all this progress, smartphones today are restraining the growth of the IoT by forcing developers to use wireless connections never intended as IoT technologies.**

Outfitted with connectivity options that were originally invented 20–30 years ago, smartphones interact with IoT hardware nodes either via a WiFi-enabled [**hub**](http://www.smartthings.com/get-started/kits/?gclid=Cj0KEQjw4uSgBRDZveXz9M-E1aoBEiQA2RMP6oYaFF6mWALKrId6LOwAi9wn35Wuw-8fEXO7uGnszDYaAiHE8P8HAQ) or directly via **Bluetooth and WiFi.** There are two fundamental flaws with either approach:

* **Hubs lock developers into fixed, proprietary servers.**
* **WiFi and Bluetooth are comically weak IoT connectivity options.**

# Smartphone + 433 MHz

The Future Of The IoT Is (Practically) Already Inside Your Smartphone

1. **Re-use The Antenna.** Re-using the NFC antenna is a matter of geometry that relates to electromagnetic wavelength. In other words, we can generate wireless communications with the same 13.56 MHz NFC antenna on certain frequencies, but not on others. Both frequencies must be a sufficient distance from each other in the radio spectrum that cross-interference is negligible, but close enough that the antenna will still work properly. So for a second frequency to be “eligible” it must first clear this hurdle.
2. **Re-use The Silicon.** But an additional hurdle — re-using the same NFC radio silicon — also requires that the second frequency must also be supportable with the same semiconductor materials used in the NFC silicon radio. If the frequency is too far from 13.56 MHz, it won’t work. So in addition to antenna compatibility, silicon compatibility further limits choices of a second frequency.
3. **Re-Use NFC API’s.** Similar to the way developers can access WiFi resources on a device regardless of the WiFi standard, IoT developers should be able to access next-gen IoT connectivity using the same or similar API’s used with NFC.

But best of all, by re-using NFC hardware and enabling a second frequency, the **bill of materials cost to enable a smartphone to be truly IoT-ready is close to zero.**

For companies who design, build, sell, or rely on smartphones, the opportunities provided by a truly IoT-ready smartphone are too lucrative to ignore. Use cases that were simply off the table due to the constraints of WiFi or Bluetooth are back on the table, along with the revenue and subscriber benefits that are already manifest. To name a few:

- **Smart Cities**
- **Driverless Cars**
- **Smart Lost and Found**
- **Drones**
- **Mobile Advertising**
- **Social Discovery**
- **Environmental Control Systems**
- **Industrial Automation Systems**

The importance of Apple’s NFC announcement to the future of the IoT is difficult to overstate. As an analogy, imagine the state of smartphone apps today without the ability to stream rich images or video via WiFi. The IoT is at a similar inflection point, where without better IoT connectivity in smartphones, the IoT will muddle through with underperforming hardware, underwhelming apps, a Tower of Babel of proprietary enterprise connectivity, and more of the cute-but-ultimately-optional consumer gadgetry that passes for “IoT” today.

4. Smartphone Gateways and Endpoints

The smartphone represents an exciting opportunity for mobile IoT data acquisition as I’ve outlined [here](http://bit.ly/1NifkBs) and clearly smartphones are their own class of mobile endpoint. Smartphones should be center stage in the IoT but without better wireless IoT connectivity, we’ll just have to enjoy our crummy IoT options via WiFi and Bluetooth until you-know-who decides to take the lead.

# Forecasting

The Internet of Things is an industry that after several decades of trial-and-error, hit the top of Gartner’s [hype cycle](http://www.mediabuzz.com.sg/asian-emarketing-latest-issue/210-asian-e-marketing/digital-marketing-trends-a-predictions-week-1/2504-gartner-hype-in-2015-around-the-internet-of-things-iot-and-wearables) curve just this year. If you believe in this kind of forecasting, then the IoT is set to start a rapid dive on the negative slope of this curve before — hopefully — one day pulling out of the nosedive and into a smooth upward glide path.

If there is an actual IoT nosedive — in hype or reality — the autopsy will likely say it was caused by wireless. Today’s wireless IoT technologies spew too much data, can’t be queried in real-time, burn too much energy, and if left unchecked, will cause a [data tsunami](https://www.cloudsherpas.com/partner-salesforce/data-tsunami-big-data-security-internet-things/) will make the slope of Gartner’s hype curve seem quite real.

Put bluntly, if we keep doing what we are doing now, much of the IoT we are all anxiously awaiting is going to suck.

# Present

Today’s IoT Is Pretty Damn Noisy

# Future

If we look ahead to the things smartphones will do for us in the future but can’t do today, the IoT figures prominently in the discussion.

**For IoT unit sales to even approach analyst** [**forecasts**](http://www.idc.com/getdoc.jsp?containerId=prUS24903114) **requires a next generation IoT connectivity option that resides in a smartphone, is not named Bluetooth nor WiFi, and can connect to IoT hardware nodes directly via a smartphone without a hub.**

What does this next generation option look like? For starters:

- It should be **effortless to set-up and use**
- It should consume **minuscule amounts of power**
- It offers much **longer communications range**
- It is **very low cost**

If you agree that to ship the next 10 billion IoT devices there has to be a better way to connect IoT hardware endpoints, then keep reading.

Why The Internet of Things Is Going Nowhere

The next phase of the IoT is stuck unless we replace crummy outdated technology

# NFC

Hiding In Plain Sight: Game-Changing Plumbing for the IoT

Apple’s decision to finally implement a mobile payments technology called [Near-Field Communication](http://en.wikipedia.org/wiki/Near_field_communication) (NFC) for both the [iPhone](http://www.engadget.com/2014/09/16/iphone-6-and-6-plus-review/) 6 *and* the [Apple Watch](http://www.apple.com/watch/?cid=wwa-us-kwg-watch-com)is a major event in the history of e-commerce and computing. Companies in the retail, telecom, banking, transportation, security, and gaming industries— to name a few — are all re-calibrating strategies in light of the news. Future iPads, Macs, and even Beats headphones will likely be NFC-enabled with better “pairing” between Apple products, but potentially mobile payments and wireless charging as well. Developers —and basically the entire computing industry— must now ask how future products will take advantage of NFC. 

**With Apple’s endorsement, NFC has been transformed into the most important wireless technology in the world today and will become more ubiquitous than WiFi and Bluetooth combined.**

What may not be obvious to many is that Apple added more than just “NFC” and actually added a new piece of hardware — a *radio—* and new radios are difficult things to squeeze into a smartphone. They cost money, suitable printed circuit board and antenna real estate is scarce, interference with other radios and antennas is common, and they can further reduce battery life. While WiFi, Bluetooth, and cellular radios have been part of the smartphone for years, NFC is the first new radio in the iPhone in *seven years* and this news by itself is of great significance.

A quick explanation:

[NFC](http://en.wikipedia.org/wiki/Near_field_communication) is a radio frequency identification (RFID) technology, with an extremely short transmission range of 1–4 centimeters. Such short range is ideal for payments but it also means NFC is not a serious connectivity option for the IoT, which requires longer range, among other attributes.

NFC chips are popular and inexpensive (less than 10 cents each in high volumes) due to their use in *billions* of devices around the world including payment and transport cards. NFC-enabled products consume zero or minuscule amounts of power and the technology has been in use for many years. But a critical attribute of NFC as it relates to the IoT, in addition to its low cost, is the radio frequency where it operates: 13.56 megahertz. This slice of the radio spectrum is license-free and it’s already used around the world on thousands of different products.


# Dash7 + NFC

Apple have brought out NFC in iPhone which can be a game changer with minimal effort. If one can reuse the 433 MHz aspect then it can interface directly with the IoT.

**Less obvious is the enormity of what Apple has (unwittingly?) enabled with NFC: a better wireless connectivity option for the IoT.**

Yet despite its very short range, NFC is an historic opportunity for the IoT: **by making a tiny modification to next-generation NFC chips, smartphones are able to connect concurrently with thousands of low power IoT devices from hundreds or even thousands of meters away.**

The hidden value of NFC to the IoT lies in the ability of the current NFC antenna along with next generation of NFC silicon radios to support a second frequency, similar to the way WiFi radios support multiple frequencies for different versions of WiFi.

# Generic communications protocol

Still, picking a second frequency is only half the battle: we still need a 21st century data communications protocol to run on top of our newfound IoT plumbing.

All of this long range and low cost goodness requires a **communications protocol** that runs on top of this second frequency. For those readers who might not understand what a communications protocol is, just think of it as a way to send and receive packets of wireless data in ways that makes the most sense for the applications they support. WiFi sends packets one way to support your Skype call; Bluetooth sends packets a different way to emulate your headset cable. Same thing goes for our next-gen IoT protocol, which requires (at least) the following purpose-driven ingredients:

- **NFC- and Frequency-Optimized.** The protocol must be designed to work using one or more frequency bands that can co-exist with 13.56 MHz, but ideally also be designed to, like WiFi, re-use the data elements and API’s of NFC in order to minimize developer learning curves.
- **Instant Connections.** This protocol cannot engage in unnecessary handshaking, beaconing, Klingon language translations, or any other superfluous traits of wireline protocols like Ethernet. Connections must be made with IoT hardware in 1–2 seconds, especially with moving objects like drones, cars, or people on the move.
- **P2P Discovery.** Communicate directly with IoT nodes via a two-way peer-to-peer mode without requiring a cloud lookup. Nodes can “advertise” themselves or make themselves “discoverable” to other users. Think CPC ads for the internet of things.
- **Ready For What Developers Bring To The Party.** Our experience at Haystack has shown that with the right protocol, Android and iOS developer communities are ready to bring hundreds of new and even world-changing ideas for the IoT. The right protocol provides maximum flexibility for them almost regardless of use case, while still allowing for industrial-grade performance that supports hundreds of thousands or even millions of users. A protocol cannot be everything to everyone, but designed correctly, the right protocol can cover a vast amount of the IoT landscape.
- **Ultra-low Power.** Not only should the protocol not impact a smartphone battery much at all, it also needs to provide for 10+ year battery life on standalone IoT hardware nodes. I have met with hundreds of IoT developers and end users in the past 10+ years and one thing is clear: convenience is king and customers just want to set up their IoT nodes, forget about them, and let them do their job. Frequent battery recharges or replacements are the malignant tumors of many now-dead wireless solutions.
- **Easy To Set Up, Easy To Use.** In addition to the convenience of a low power device with long lasting batteries, the protocol must enable easy setup and connections between devices. The hair-pulling chore of pairing two previously unknown Bluetooth devices, to cite one example, is just so 1980's.
- **Standardization.** Like WiFi and Bluetooth, this technology will need standardization to enable cross-vendor interoperability and standardization. Ideally, the protocol will also be open source.

# Dash7 protocol

DASH7 Advertising Protocol Basics

A defining feature of DASH7 — and the path to solving for high-precision LPWAN location and real-time geofence alerts — is its low power wakeup, also referred to as “instant-on.” Instant-on allows DASH7 endpoints to remain in a low power “listen” mode and avoid the kind of power-intensive synchronization and other overhead that is standard in more high-powered wireless protocols.

You can download the DASH7 specification [here](http://bit.ly/2TxGhYz), but the following is an illustration of how a host (let’s say, a LoRa gateway) sends “background frames” to an endpoint causing the endpoint to “wake up” and prepare for a location query or other data transmission like an Assisted GPS datagram:



![img](https://cdn-images-1.medium.com/max/800/1*0tASFIJYqULKKYbO_ywLIg.png)

# Haystack

When we designed the protocol stack for HayTag, [DASH7](http://www.indigresso.com/wiki/doku.php?id=dash7_mode_2:main), **we started with the premise that the IoT needs a wireless protocol that was madespecifically for the IoT**

Here are a few examples of our IoT-centricity (among many) that I believe you will be hard pressed to find occurring with other wireless IoT technologies:

**Example 1: Listen Before Talk.** Our hardware nodes typically stay “silent” until awakened by another authorized device. This saves huge amounts of power and is distinct from technologies like Bluetooth, which often rely on perpetual “beacons” that drain batteries and pose privacy risks by emitting a unique ID to anyone within range. Combined with our support of AES 128 private- or public-key cryptography, our approach has a superior IoT security and privacy profile to either WiFi or Bluetooth.

**Example 2: Real-time Queries.** In a peer-to-peer transaction between two of our devices, we enable a developer to embed a **query** into the very first outgoing packet sent to a second device*.* Why? Imagine needing to immediately know the presence or condition of a single IoT hardware node operating among 50,000 other nodes. With WiFi or Bluetooth, there is a loooong handshaking and lookup process that can clog airwaves and burn battery life, not to mention the hours it could take to interrogate 50,000 devices using those technologies. Our approach results in a response from a target IoT node in **2 seconds or less** and without a cloud lookup. This is also great for connecting between one or more moving endpoints — **the Internet of Moving Things**— that is next to impossible for WiFi or Bluetooth.

But in addition to designing a protocol with the IoT in mind, we also designed our firmware stack for HayTag with NFC in mind, betting one day that NFC would be, you know, the hottest wireless technology on the planet. Here’s another example:

**Example 3: Writing Programs for NFC is Like Writing Programs For Our Stuff.** Today, an API designed to work with NFC can be extended to also work with our technology with minimal added effort as Both NFC and DASH7 use a similar language, [NDEF](http://developer.android.com/reference/android/nfc/NdefMessage.html), for accessing data stored on devices. Both also use similar foundational methods for storing raw data and database records on their chips and both have a similar interface to the “secure element” on the smartphone. Finally, there is no need the “application profiles” found in some wireless protocols: the file system and data methodology in our technology.

We are excited to be bringing [HayTag](http://www.haytagstore.com/) to market later this year and announcing other products for IoT developers in 2015, but like many in the NFC community who waited so long for Apple’s NFC endorsement, we know the world is ready for the next wave of smartphone IoT connectivity and look forward to playing a role in its future.

# Blockchain

**The Blockchain Moment for LPWAN’s**

For now, I will skip thoughts on implementing high power, short range radios like WiFi for PoL and leave it to others. For smartphones today, WiFi may have a role to play in PoL.

But the more lively space in the IoT today is with LPWAN technologies like Semtech’s [LoRa](http://bit.ly/2EsTWsq) (and new entrants due to appear later this year) that operate in unlicensed spectrum and whose architecture is more aligned with the way smart contracts work. *Note: NB-IoT and LTE Cat M-1, by virtue of being centralized,* [*among other reasons*](http://bit.ly/2xuqQWv)*, can be omitted from this discussion.*

LPWAN’s are interesting for PoL because the long range (up to several miles) means the number of participating gateways required to authenticate an endpoint can be far fewer than, say, that required to cover an entire city with participating WiFi access points. LPWAN’s are also interesting due to the scalability of the technology to small, mobile devices with a limited power supply, unlike WiFi. You can envision wristbands or keyfobs that utilize PoL with this profile in mind. And lastly, LPWAN’s like LoRa are designed primarily for use in unlicensed bands which aligns nicely with the “permissionless” architecture of blockchain apps.

*Note: An LPWAN -based PoL will, like Ethereum, Bitcoin, and other blockchains themselves, implement* [*Byzantine Fault Tolerance*](http://bit.ly/2IeIve8) *to withstand attempts by bad actors to undermine the PoL system. This is accomplished primarily at the application layer but we also see opportunities to implement BFT in the wireless networking layers themselves.*

But implementing LPWAN’s for PoL is not just about the choice of radio but more importantly, the networking stack that rides atop the radio. If you follow [DASH7](http://bit.ly/2haytech), you’ll know it is being deployed on LPWAN radios like LoRa and others and is uniquely suited to the requirements for PoL mentioned above. I will share more in a future post on how we are implementing PoL over DASH7 and I will be looking forward to hearing how other entrants in the PoL space plan to solve for the requirements mentioned earlier in this post.

# Smart contracts + PoL

**How To Make Better Smart Contracts With DASH7 and PoL**

*Note: this is the first in a series on implementing Proof of Location using DASH7*

Recently our team began taking a look at how DASH7 will help blockchain applications with a hard-to-solve problem: authenticating the physical location of one or more parties in a [**smart contract**](http://bit.ly/2jFerK0).

Smart contracts are computerized transaction protocols that execute the terms of an agreement without the need for a central authentication or organizing authority. Authenticating execution of some smart contracts can be straightforward— e.g. “Party A will pay you $0.10 every time Party B posts a tweet that includes the hashtag #DASH7” — via a simple script. However, a smart contract that includes terms that require one party’s physical presence or location in a given geographic area presents a different challenge, since most methods of authenticating location today utilize easily faked methods for geolocation like GPS or require the use of a central authority like a cellular carrier.

So creating a fraud-proof, location-based authentication capability — or a “proof of location” — will be of significant importance to smart contracts that include location-based terms.

**Why This Matters Now**

Blockchains are driving the migration of internet applications from the confines of centralized “cloud-based” architectures: payments, supply chain, insurance, social media, gaming, and more to a decentralized, “permissionless” one. A common blockchain-based application implementation relies on [Ethereum](http://bit.ly/2Gblvad) and implements an autonomous, decentralized (i.e. no cloud server required) network architecture that uses tokens as a means of facilitating transactions.

But with this liberation from the cloud come new challenges, like verifying the physical location of one or more parties to an autonomous smart contract. While “trusted” centralized authorities like cellular carriers can authenticate someone’s location via cell tower trilateration, a decentralized, “trustless”smart contract has no such infrastructure available today to reliably authenticate location.

To illustrate — and my bias here is to look at how PoL will impact IoT applications — let’s use supply chain. How does a smart contract between the manufacturer and buyer of pharmaceutical inventory guarantee that the manufacturer’s inventory was in fact routed via agreed-upon shipping carriers, distribution centers, warehouses, etc. and not diverted for purposes of counterfeiting or gray market sales? How does a company’s autonomous delivery drone prove, in fact, that it landed by your front door to leave a package (that was later stolen) on your porch? These are examples of real-world, location-based risks whose externalities (a la [Coase’s theorem](http://bit.ly/2wkGzv7)) in cases of fraud or abuse are potentially large (e.g. dumping radioactive medical waste in a residential area instead of a pre-agreed location).

Mitigating location-based risk is therefore essential to the future of location-based smart contracts. As a result, we are in the initial phase of the development of a decentralized, terrestrial, global PoL network.

**Why Conventional Forms of PoL Won’t Fly With Smart Contracts**

While familiar means of determining location may have some role to play with smart contracts, they are ultimately insufficient to the task. And even though we at Haystack work extensively on integrating GNSS and LPWAN’s, for purposes of smart contracts the simple fact is that [GPS/GNSS can be faked](http://bit.ly/2ro7KAA). All GNSS systems are vulnerable to [spoofing](http://bit.ly/2HZShAP), jamming, or even [anti-satellite](http://bit.ly/2I1L0wx)weapons, yet the world depends on GNSS systems not just for conventional navigation applications, but for even more fundamental tasks like timestamping [financial transactions](http://bit.ly/2I03VYo). Most of us are oblivious to the pervasiveness of GNSS!

Additionally, GNSS isn’t always available. And getting a reliable GNSS signal amid inner city high rise buildings can be a challenge, not to mention indoors. And if satellites are jammed or made unreliable, then what? Drones need to fly, [autonomous vehicles](https://cnb.cx/2wnYTno) need to drive, you need to find your way home when there are no cellular signals available, etc.

Lastly, and perhaps most importantly for purposes of smart contracts, wireless signals from GNSS satellites are one-way transmissions that are unencrypted. There is no mechanism for implementing, say, public key cryptography using today’s civil GNSS systems. So if you want to authenticate location for a single, mobile endpoint in a decentralized network, public key crypto is going to be important. And one-way location beacons like GNSS won’t solve for this.

*NB: a sometimes-alternative to GNSS —* [*Loran*](http://bit.ly/2rAXYen) *— has been touted as a GNSS backup and an upgrade for Loran — “eLoRan” — has been denied government funding for years. Regardless, similar to GNSS, Loran signals are one-way, unencrypted, and like GNSS could be faked, so while Loran would seem to be a good navigation backup to GNSS, it’s utility for proof of location will, like GNSS, be of limited value.*

**Thinking About PoL From the Bottom-Up**

An alternative means of “**Proof of Location**” (“PoL”) that does not rely on GNSS or centralized location methods is therefore important to the future of location-based smart contracts. This alternative means of PoL will, for the foreseeable future, be a terrestrial-based network rather than space-based.

While implementing PoL requires plenty of thinking at the application layer — the team at [FOAM](http://bit.ly/2KYQF8c) is doing a nice job here — getting to successful PoL for most IoT use cases like supply chain or really requires thinking about PoL from the bottom-up. In other words, start with the physical (radio) layer and then work up the [OSI stack](http://bit.ly/2IzifuH) from there. Because if your underlying radio and networking layers are a poor fit for PoL, all the application layer tricks in your quiver won’t deliver reliable PoL. Thus for starters, PoL will require:

- **Non-reliance on centralized wireless communications technologies like those offered by cellular carriers.** A decentralized app would not rely on a centralized (and [easily compromised](http://bit.ly/2rLJckr)) actor like a cellular carrier. PoL will ultimately rely on wireless networking technologies that are being deployed (by default) primarily in unlicensed spectrum.
- **Support for public-key cryptography.** In order to implement PoL in a public network where devices are “strangers” to one another, the use of public keys to authenticate is important. For example, a carton of flu vaccine passing through an airport terminal is detected and authenticated via the endpoint’s public key. Note that the availability of public key cryptography for this next-gen PoL is a significant differentiator from GNSS and opens a number of interesting application venues that were previously closed to developers. More on this in a future post.
- **Fully bi-directional, low latency communications.** Implementing public key crypto, at a minimum, requires bi-directional communications. But implementing even more basic networking functions like queries, ad hoc networking, firmware updates cannot be accomplished with a uni-directional protocol like Bluetooth Low Energy or [Lorawan](http://bit.ly/lorawan).
- **Peer-to-peer, ad hoc, and multi-hop networking.** In a truly decentralized world, conventional “gateways” or “access points” with direct access to the internet may be unavailable, thus a networking protocol is required that is sufficiently flexible to respond to changing network participants but also allow for the kind of innovation that is inevitable with blockchain technologies. For example, a group of endpoints that are out of range of an internet gateway may nonetheless be able to authenticate the location of another mobile endpoint passing nearby.
- **Fast, efficient clock synchronization.** Clocks move out of sync and any time-based approach to PoL will require reliable, fast clock synchronization for large fleets of devices, including for low power devices. [More on this here](http://bit.ly/2uRSqfA).
- **Broadcast and multicast messaging.** This is related not only to the task of synchronizing endpoints and gateways in a wireless network, but also in deriving location, whether using time-based (e.g. TDoA, TOF) or signal-strength based (RSSI) techniques. A gateway, for example, may want the authenticated location (PoL) for a large fleet of endpoints simultaneously.
- **Support for time-based and signal-strength based location methodologies.** Ultimately, proving location requires getting your device and/or message stamped with irrevocable location coordinates. GNSS is a time-based methodology and time-based methodologies can be deployed in terrestrial networks as well. But signal-strength based methodologies (like the cellular trilateration your iPhone uses, among other things, to show your location in Google Maps) will be important as well. Note that legacy support for GNSS is likely to be important as GNSS is likely to provide an additional layer of authentication that some applications may require or at least prefer. However, not all wireless technologies can support GNSS, as I’ve written [here](http://bit.ly/2pBcYqp).
- **Support for low power devices.** Since PoL implies proving location for what is, logically speaking, a mobile device, it is short-sighted to assume all mobile devices will be high powered. In fact, the vast majority will be low power devices. Thus, the architecture for a global PoL network will require support for low power devices — i.e. multi-year battery life — from the outset.
- **Open network.** This should go without saying but to be clear, since anyone can build autonomous, permissionless, location-based blockchain apps, anyone should be able to leverage this global PoL network, a la civil GNSS today.

Wireless networking protocols are only one part of what will ultimately constitute a viable PoL solution, but there’s little doubt that without the right wireless protocol, PoL will be of limited value.

# Cryptocurrencies

**How To Make Better Cryptocurrencies with PoL and DASH7**

*Note: this is the second in a series on implementing Proof of Location using DASH7. You can find the first one* [*here*](http://bit.ly/2wJDLrJ)*.*

We are doing exciting work at Haystack around low power IoT [geolocation](http://bit.ly/2xuqQWv)and more recently have begun work on a project to develop [Proof of Location](http://bit.ly/2wJDLrJ)(PoL) using DASH7 running over LPWAN’s.

One use case for PoL cuts to the heart of a weakness in many cryptocurrency architectures: concentration of mining power. (If you’re unfamiliar with what this means or how this works, click [here](https://www.buybitcoinworldwide.com/mining/).) I’ll use Bitcoin in this post for the sake of simplicity but the arguments can be made for other proof of work- or proof of stake-based cryptocurrency systems. Basically, organizing 51% of the mining power for Bitcoin (and other cryptocurrencies) creates serious [challenges](https://medium.com/@cloudycalvin/potential-threats-to-bitcoin-1-mining-centralization-1fc1090694e5):

> When a single party controls more than half of the mining power, the bitcoin network is subject to **51% attack** because that single party can create the blocks for most of the time. This single miner can reject a valid transaction to be put into the block which creates the **censorship** in transaction processing. The miner can even **alter the record** of the previous block by recalculating the difficult mathematical equation which can make someone lose their bitcoin.

First, mining concentration by number of companies already puts Bitcoin at risk of a 51% attack:



![img](https://cdn-images-1.medium.com/max/800/1*EQdST1_FMjKImP-q6zLtKg.png)

Bitcoin mining concentration May 2018 (Source: <https://blockchain.info/pools>)

Interestingly, BTC.com and AntPool are both controlled by [BitMain](https://www.bitmain.com/), who happens also to be the dominant provider of Bitcoin mining hardware in the world. So yes, a single company controls 41% of the Bitcoin mining pool power in the world. And of course this assumes the mining rigs they sell are free of backdoors or other vulnerabilities that might add to this concentration.

And geographically, the news about concentration is actually worse: China controls over 80% of the bitcoin mining pools out there:



![img](https://cdn-images-1.medium.com/max/800/1*dgEekihxihNSvyn65AXuNg.png)

Top Bitcoin mining pools by location, April 2018 Estimate (Source: <https://www.buybitcoinworldwide.com/mining/pools/>)

Nothing against China or its success in blockchain, but a 51% attack is only a phone call to a mining competitor away. And as cryptocurrency architects attempt to engineer solutions like “[ASIC-resistant](http://bit.ly/2J53aOj)” protocols, hardware and firmware-savvy engineers outwit them and … the concentration continues apace.

Thus, concerns about mining centralization undermining the future of cryptocurrencies are more than valid. I will leave it to others to weigh in about the probabilities of a 51% attack/cooperation, but an entry level game theorist could hypothesize.

**Proof of Location As A Solution To Mining Centralization**

While PoL is not intended to solve directly for mining concentration by a single company, it can authenticate the geographic location of a given miner to allow future forks of Bitcoin or other cryptocurrencies to mandate geographic diversity when rewarding miners. For example, a future fork of the Bitcoin code could limit the number of block rewards allowed from a given geographic area (country, city, lat/long, etc.) in order to limit the risk of a 51% attack from that same geographic area.

GPS-based PoL is surprisingly common in the [financial world](http://bit.ly/2I03VYo) today, but is easily faked. LORAN, a much-discussed terrestrial backup to GPS, is interesting but like GPS (or GNSS) is a uni-directional signal that is incapable of supporting public key encryption and is therefore spoofable, among other drawbacks. So as we search for alternative means of PoL, basic requirements include a bi-directional wireless protocol, decentralized network topography (i.e., not carrier-based), very low latency, as well as support for public key cryptography.

**Importance of Low Power in PoL**

While Bitcoin mining rigs are (obviously) mains-powered, a good many other IoT devices that require PoL are not or will not be: e.g. unmanned aerial drones, Pokemon Go wristbands, access control badges, temperature sensors in a shipment of vaccines, etc. Thus implementing PoL over a low power wireless network is essential to arriving at a standard for PoL. Additionally, LPWAN-based mobile endpoints will serve as important actors in a winning PoL network.

Ultimately, I expect to see a global PoL network — perhaps led at the application layer by the team at [FOAM](https://www.foam.space/) — that solves for mining centralization and many other use cases. But the devil in creating this global, decentralized PoL network is really in the physical and networking layers. We believe Low Power Wide Area Network radios like LoRa (and others) are well suited to this job and a radio-agnostic networking stack like [this](http://bit.ly/2haytech) to be the foundation for the future of PoL.

# Junk

One exciting aspect of the iPhone 6 that has gone unnoticed is its potential to radically accelerate the growth in the Internet of Things or “IoT”. Here are five ways the iPhone 6 matters — profoundly— for this next wave of computing.

It’s been more than two weeks since Apple launched the iPhone 6 and so far, no big headlines about the IoT. Bigger screen size, better camera, increased storage, and mobile payments via [Apple Pay](https://www.apple.com/iphone-6/apple-pay/)—something many of us wish Apple had launched years ago — but the proverbial lump of coal for the IoT.

# References

[https://medium.com/@patburns/5-reasons-the-iphone-6-will-save-the-internet-of-things-7ac8b96fbd5](https://medium.com/@patburns/5-reasons-the-iphone-6-will-save-the-internet-of-things-7ac8b96fbd5)

https://medium.com/iotforall/why-you-can-t-google-the-internet-of-things-1f1207212a75

https://medium.com/the-startup-magazine-collection/a-simple-proposal-to-improve-security-for-the-internet-of-things-4fcc0663f70e

[https://medium.com/@patburns/how-to-solve-for-geofencing-in-the-low-power-iot-94567de29eaf](https://medium.com/@patburns/how-to-solve-for-geofencing-in-the-low-power-iot-94567de29eaf)

