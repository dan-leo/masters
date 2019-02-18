# Pat burns

This is a summary of all that Pat Burns is saying on medium and about Haystack. Each heading is a different topic.

# Indoor-Outdoor

**The Indoor-Outdoor IoT**

*Thoughts on an IoT blindspot*

**Two IoT Arenas**

- Companies competing to sell you their wireless IoT connectivity technology can be thought of as competing in one of two separate “arenas”: an **indoor arena** or an **outdoor arena**.
- The **indoor arena** is typically dominated by low power, local area networking (LPLAN) technologies focusing on home automation. ZigBee, Z-Wave, and Control4 are well known examples. Use cases beyond home automation include enterprise/industrial automation, whose users reluctantly adopt the same tech (e.g. Zigbee smart meters) or proprietary alternatives (e.g. Honeywell alarm systems). Most operate in the tragically overcrowded 2.45GHz unlicensed band. Short range, high levels of interference (and returned merchandise), weak battery life. And 99% of their customers are using these technologies for indoor use cases.
- Some of these offer real-time indoor location capabilities to help find an object located in a building or warehouse to within a few feet of precision. Since GPS can’t work indoors, this is how it’s done. Some of these also offer mesh networking features, sometimes as a way to overcome the innate short range of the technology, but usually disguised under a marketing gimmick known as “self-healing.”
- WiFi is making a new push at joining the indoor IoT arena with a reasonable likelihood of success due to access point footprint, though not sufficiently low power to make a serious run at battery-powered endpoints.
- Omitted here: one-way passive RFID (great, niche technology) and one-way Bluetooth low energy (hyper-short range personal area networking, not even local area networking).
- The **outdoor arena** is where the most intense IoT connectivity battles are taking place today. Cellular and satcom have promised long range/wide area IoT for years resulting in steady but low volume success, and almost always tied to use cases where mains electric power is available at the endpoint. Battery-based versions of these have largely failed so far due to form factor, price point, and of course battery life weaknesses. Viable outdoor solutions using battery power (e.g. LPWAN’s) are relative newcomers disrupting the outdoor arena.
- New entrants to the outdoor arena are arriving via **long range, low power wide area networking** (LPWAN) technologies, which are challenging the need for mains power in long-range outdoor IoT use cases. LoRa and SigFox in unlicensed bands, and NB-IoT, LTE Cat-M, and other LTE-based efforts in licensed bands). All carry question marks regarding actual vs. promised performance (e.g. NB-IoT) or scalability claims (e.g. LoRa) pending broader adoption, but there is sufficient evidence now to argue we are really turning a corner in bridging low power with long, multi-kilometer range. But nearly all LPWAN use cases being talked about are outdoor-only.

**The Indoor-Outdoor Orphans **

- One challenge to the two-arena segmentation approach of the IoT is those **use cases that straddle both indoor and outdoor arenas**.
- Three immediate examples come to mind:

1. **Supply chain.** Precisely locating cartons of high-value pharmaceuticals during shipment or while stored in a warehouse or medical facility.
2. **Access control**. Precisely locating an outside contractor or hospital patient within a secure building as well as within a campus or metropolitan area.
3. **IT asset management.** Precisely locating a laptop with PCI or PHI data as it moves within your 10-story headquarters building as well as around a large campus.

- Today, use cases that by definition straddle both arenas must instead compromise and play in one arena. Example: tracking cattle on a ranch via short-range ZigBee chokepoints scattered around a ranch. Provides nominal and non-real-time visibility into the location/health of the cow, but well short of what ranchers really need (e.g. being able to find a lost cow somewhere on a 1,000 acre ranch or to know.)
- LPWAN solutions for outdoor location rely on GPS. Good for outdoor location, but no good for indoor location. While LPWAN’s can and will be used for indoor sensing applications (e.g. what is the temperature of the sensor in the walk-in freezer?), precise indoor *location* (e.g. where is Mike’s laptop) is unaddressed in any of the new or emerging LPWAN networking protocols. *NB: real-time* [*trilateration*](http://bit.ly/2aE0qWl) *via networking stacks like LoRaWAN is unavailable at this time thus GPS is the near-universal means to achieving real-time outdoor location precision among LPWAN’s.*
- Low power indoor LAN solutions usually rely on received signal strength or time-based location systems, relying on a series of reference points to assist in calibration. But low power LAN’s (short range, remember) cannot address outdoor use cases.
- **Thus, indoor-outdoor use cases are a “blind spot” for the IoT,** with few straightforward solutions for addressing both short of using multiple radios and **exposing a horizontal application opportunity.**
- Indoor-outdoor feature set requirements: long range-capable, fully bi-directional comms, low power, low price point, and **real-time indoor location capabilities**. *NB: Increasingly, and for multiple reasons, real-time comms will be required for both indoor and outdoor use cases, but this is subject of* [*another post*](http://bit.ly/1N3MSmv)*.*

**A Third IoT Arena**

- With LPWAN’s, it’s easy to redraw our landscape maps and create a de facto third, hybrid arena that bridges the first two, which I’ll just call “**indoor-outdoor IoT**.”
- Indoor-outdoor IoT use cases require a) long range, low power outdoor connectivity b) outdoor location precision, typically via GPS, c) low power indoor connectivity and d) indoor location precision to ~1 meter or less, typically via a real-time, reference point-based system.
- LPWAN’s are a huge step towards solving for the indoor-outdoor IoT. But as solutions today, they are incomplete.

**Potential Remedies **

1. Using multiple radios is the traditional solution to bridging use cases like these. To cite one obvious example: smartphones host both long range (LTE) and short range (WiFi, BT, NFC) connectivity options, albeit in a package priced at hundreds of dollars. Multiple radios add to an endpoint’s bill of materials, and in addition often require additional memory as well as antenna and other sacrifices. Hypothetically, an endpoint could contain both a Zigbee and a NB-IoT radio, but this means creating two parallel access point systems, among other drawbacks.
2. Reflashing existing silicon and re-using existing antenna in order to accommodate a software-defined radio is a slightly better solution. It might mean limiting your radio choices to those available using an existing antenna or might mean re-designing the antenna to accommodate both radios. It might also mean adding additional memory, which may or may not fit your budget. But it still requires parallel access point systems, etc.
3. Same as #2, but interleave an existing firmware stack (e.g. LoRaWAN, NB-IoT) with additional features to accommodate real-time indoor location. **In other words, the long-range, low power WAN capability operates in its “native” mode unless it’s asked to operate in enhanced mode in order to facilitate indoor location.** Or vice-versa. This is the [approach](http://bit.ly/haystackiot) we are taking at [my company](http://bit.ly/2aSPRzX) and has the added benefit of requiring only minimal incremental memory if any, since our stack already compiles into less than 20kb.

**Takeaways …**

- **A two-arena segmentation model giving way, in the short term, to a three arena model** as as a) there are use cases that straddle both the indoor and outdoor arenas and b) we now have technologies that can solve for both. **The three-arena model will morph into a single arena in the long run. Or sooner.**
- The market opportunity of the indoor-outdoor arena is significant even in the short term. The sheer number of measurable things and people that move between indoor to outdoor environments is very large.
- If you are reading this and daydreaming about use cases that fall within this third indoor-outdoor arena, “[things that move](http://bit.ly/1J3BlEf)” is a good attribute for helping to identify use cases. Things that are battery powered are a close second.
- Companies in the outdoor arena at a minimum should be examining opportunities in the indoor-outdoor IoT. More aggressive participants may realize that there is little preventing them — from a technology standpoint — from competing directly in the indoor arena.
- Companies competing in the indoor arena should therefore expect encroachment by LPWAN’s capable of competing indoors. Since most LPWAN’s — all things being equal — offer better indoor signal propagation and rough pricing parity, indoor arena participants will want to consider adding LPWAN capabilities to their product lines.
- **Bonus takeaway:** solving for the indoor-outdoor IoT helps to solve for some deeper business process/big data challenges that the first two arenas can’t really solve on their own: associating a mobile person or thing with a fixed person or thing.

# Augmented reality

**Why Pokemon Go Will Make You Rethink the Internet of Things**

Pokemon Go already looks like a pretty major technology shift. Commercially, it’s one of the most successful mobile games of all time, people are literally [crashing](http://bit.ly/2bVObZi) into each other while playing, and the controversial headlines practically [write](http://bit.ly/2bFjTet) themselves.

But the technology industry impact of Pokemon Go goes beyond just gameplay. At its core, Pokemon does a good job of integrating real-world paradigms like smartphone maps and cameras with virtual paradigms like animated cartoon characters — excuse me “[fictional creatures](https://en.wikipedia.org/wiki/List_of_Pok%C3%A9mon)” — and making it all work together in a brilliant way. The game’s goal: capture as many characters around your town/city/country as possible, do battle with others, earn points and status, and so forth. If technology is part of your livelihood or you have no hobbies, I recommend trying it.

Why? Because Pokemon Go showcases the **parallel challenges for both**[**augmented reality**](http://bit.ly/2c6tsjg) **(AR) as well as the Internet of Things.**

** Augmented Reality 1.0 **

Pokemon Go utilizes AR and while today it is uncommon to see AR in the IoT, it will play an important role the future as the simplicity of just pointing your smartphone at a “thing” and viewing its “information shadow” overlaid on your screen has many potential applications for the IoT. You know, like this:



![img](https://cdn-images-1.medium.com/max/800/1*8nUcbPXNsra7iWyNDZKLUg.jpeg)

Terminator vision, via Jim Cameron

Information shadows include text and “virtual object” images that are superimposed over real-world images displayed on your smartphone screen, smart glass lenses, or other visually-based user interfaces. Here’s another example:



![img](https://cdn-images-1.medium.com/max/800/1*NdfkzjUhXIcCiliVey_tWw.jpeg)

Information shadows in “Iron Man“

My experience with Pokemon Go suggests the game is a *so-so* example of augmented reality, *not a great example*.



![img](https://cdn-images-1.medium.com/max/800/1*iW0ln_6zBGA_KWysu46bcA.jpeg)

AR implemented in Pokemon Go. The bird’s name is Pidgey.

Throwing a ball at a Pokemon juxtaposed on the actual sidewalk in front of you is neat and adds to the fun, but to me there is no inherent need for AR in this game. Yet this will be the first AR experience for many and Pokemon Go also makes extensive use of maps and “virtual objects” that are placed at fixed geographic locations on a map. So this is all very IoT-ey.

AR matters for the IoT in particular because it provides a powerful paradigm for interacting with endpoints. Browser-based IoT interfaces are normal today, but the user experience for users that are close to the actual IoT endpoints can’t compare with a the intimacy and interaction opportunities for pointing a smartphone at a thing and being able to interact with its information shadow. This matters more and more as users “in the field” depend on the IoT: field service techs, truck drivers, nurses, soldiers, firefighters, oil rig workers, and many more. Putting aside their access to reliable and low-latency cloud services, the ability to point a phone and begin interacting with an endpoint via AR creates big opportunities for developers.

One more point about the coming collision of AR and the IoT: AR is about placing virtual objects and information shadows on top of real world objects, e.g. Pokemon Go. The IoT is focus today on adding non-AR digital information (e.g. sensor logs) to real-world objects. In both cases, the technologies seek to enhance our interaction with the real/physical world. AR provides a new interaction paradigm that gels nicely with the needs of IoT users, albeit with local/on-premises users in mind. **Similarly, IoT endpoints provide a new dimension of data that improves the performance of AR in many situations.**



![img](https://cdn-images-1.medium.com/max/800/1*D9mLk6HfVTSecpB_jMaGEQ.png)

You can sort of *tell* when people are playing Pokemon Go …

** AR for IoT Needs Fixing **

Obviously, AR is not right for all applications, but for many it will become an essential part of the IoT user experience. But before this happens for the IoT, the state of AR will have to overcome several hurdles:

** 1. Poor Location Precision **

If your smartphone thinks you are standing somewhere you are not, your smartphone (using its onboard compass) is probably also going to think you are pointing your phone at something you are not. This is a problem for many AR implementations today — which rely on your phone’s compass and geolocation capabilities, including GPS — seeking to serve accurate AR information shadows.

Unfortunately, location precision in smartphones remains surprisingly weak. Plus or minus an average of 30 meters, due to a [variety of factors](http://www.mobilemarketer.com/cms/news/research/22928.html). My own experience using the map feature in Yelp, for example, is that the location precision in my iPhone is usually “good enough”.



![img](https://cdn-images-1.medium.com/max/800/1*5dA6OdVsthLZblcI-SJgRw.jpeg)

Compass + GPS = Outdoor AR in Yelp

However for applications where hyper-accurate and precise location can be mission-critical — like mobile advertising or augmented reality IoT applications— even a few meters of variance can lead to errors and failure. With Pokemon Go, I found outdoor location precision to be erratic at times, but indoor location precision was always a disaster. GPS doesn’t work indoors, cellular trilateration is an unsatisfactory substitute, and WiFi location can actually result in even worse location precision. I fully expect the Bluetooth minions to be working to fix some of this, as everything looks like a nail when you think you have a hammer, but even this provides only a partial solution to both the location problem as well as broader AR bugs discussed below.

** 2. Reliance On The Cloud **

If you point your phone at a thing and it only serves up an information shadow when a cloud server in, say, Ashland, Oregon is available, your AR experience will correlate with your ability to connect with that server. For me, this was the most frustrating aspect of playing Pokemon Go and it wasn’t limited to the AR features. Maybe the lag is just an [overloaded data center](http://www.comscore.com/Insights/Blog/Pokemon-GO-Captures-55-Million-Mobile-Users-in-July-Ranking-13th-Among-All-Apps)phenomenon, but if the vision for AR is to rely on a cloud lookup every time we point our phones at something in order to view its “information shadow”, this AR business is going to [take a while](http://bit.ly/1knol10).

** 3. Poor Mobile Resolution **

If you point your phone at something while you are moving at 20 mph in an attempt to view its AR information shadow, just know that Apple Maps will think you are somewhere different from where you were three seconds ago and your AR experience will likely vary. Same thing if you are standing still and you are pointing your phone at a moving object like a Ferrari or a dog running down the street.



![img](https://cdn-images-1.medium.com/max/800/1*-R0vPtmOwkbBzj83bP3vyA.jpeg)

AR works great when this thing is parked, not so much when it is moving …

The weak mobile capabilities of AR today is a subset of point #1 above and may be a less urgent bug/feature in Pokemon Go but nonetheless, it is of increasing importance for the IoT when required to connect under low power with a moving object (e.g. a car, bike, drone) or to connect while moving with a stationary object (e.g. highway infrastructure). **Good augmented reality**on smartphones — not necessarily the AR-lite on Pokemon Go — depends on precise, accurate location to determine where you are and in turn, at what are you pointing your phone. Today, [this is hard](http://bit.ly/1J3BlEf) with current smartphone and most IoT technologies.

** The Ideal AR Experience **

I have not seen criteria for an “ideal” AR user experience vis-a-vis the IoT so here goes:

1. **Pointing my phone at a thing and receiving a real-time information shadow about it, not a different thing located four feet away, while**
2. **Querying or controlling the thing in real-time, and**
3. **Without relying on a cloud connection, and with**
4. **No regard to whether I am moving or standing still.**

The AR in Pokemon Go does not meet the “ideal” criteria, but the game does provide a reference for future AR applications as well as a simulation of a wide area, open loop, multi-user AR IoT application that requires users to locate an object and interact with it, similar to the way public IoT networks will operate.

** Simultaneously Improving AR and IoT Performance **

At least part of the answer for better AR lies in work already underway with low power sensors and wireless communications.

1. **RTLS.** Some IoT endpoints outfitted with real-time, P2P wireless connectivity offer a bonus feature called real-time location services, or RTLS. A group of things scattered throughout a building can communicate amongst themselves in real-time and, using the strength of their radio signals and basic geometry, can help determine the location of a smartphone or any mobile endpoint **to within one meter**. This is generally very useful given the state of location precision generally, but particularly useful indoors, where location remains largely unresolved despite the best efforts of the WiFi community and others. Specifically, consumer apps like mobile advertising and industrial apps like in-person measurements of environmental sensors on pieces of industrial equipment will benefit tremendously from this improvement.
2. **P2P.** Again, some types of low power IoT endpoints offer real-time, peer-to-peer networking. The ability to query a thing in real-time, **without the need for a cloud lookup**, brings obvious decreases in latency, but it also creates opportunities to directly query or control the thing being viewed. You can easily imagine AR-enabled IoT apps that are interactive and do more than just passively view endpoint data via a smartphone and provide entire user experiences, not dissimilar from the virtual experience of Pokemon Go, without the need for a [cloud](http://bit.ly/1knol10) connection.
3. **Instant-on Connections.** A satisfactory AR experience enabled by IoT endpoints should not require lengthy handshaking or setup times every time a user comes into contact with an endpoint. Connections should be more or less instant. This is similarly true for connecting with moving objects or connecting with stationary objects while you are [moving](http://bit.ly/1LX6oNp). Some low power IoT technologies offer such an instant-on feature.

** The Near-Term Steps to Better AR **

Why all wireless IoT protocols weren’t designed with RTLS, P2P, or instant-on is the subject of an [earlier post](http://bit.ly/1hExgtG). Unfortunately, most low power wireless IoT implementations are not real-time and two-way in any meaningful sense: some continually broadcast a one-way unique ID (Bluetooth) that requires a cloud lookup, and other two-way technologies like WiFi can take minutes just to get a two-way conversation going, forget about something as real-time and interactive as AR.

Getting to a real-time, P2P AR will require silicon support on the smartphone to support it. Today, getting new silicon onto a smartphone is like getting an expedition of 50 cats safely to the summit of Everest, therefore I see two paths to AR 2.0 while relying only existing silicon on a smartphone:

- **LTE.** The cellular industry is doing its utmost to convince us all that they will finally deliver a wireless IoT standard that allows endpoints to communicate over several miles while preserving battery life of 3–5 years. And all with a chip that costs one dollar. Alas, these chips are not available today — yes I am shocked, shocked — and it could be years before they are, but when the time comes for NB-IoT (the most interesting of the various LTE-based IoT standards now in the works), it is possible — [with help from a real-time networking stack](http://bit.ly/2aSPRzX), which NB-IoT lacks — to perform direct, P2P AR using your phone. LTE is everywhere on smartphones so this approach makes a lot of sense on the phone, but the idea of cellular carriers charging subscriptions for thousands of endpoints in an industrial plant, for example, is more fantasy than probability.
- **NFC.** I’ve written about this [before](http://bit.ly/1NifkBs), but the [NFC](http://bit.ly/2bTnxQE) chip in most smartphones now can be re-purposed to support other frequencies and protocols including sub-1GHz frequencies where LPWAN technologies like LoRa or SigFox deploy. Retrofitting NFC to support one or more of these would be an IoT game changer and would cost next to nothing.

** Some Final Thoughts on IoT Application Opportunities with Next-gen AR **

- I am convinced, based really on my own experience with “AR-lite” in Pokemon Go, that AR is coming in a big way for the IoT, technology limitations notwithstanding. The cloud will probably serve as AR’s IoT training wheels at least initially, but real-time P2P connections are where the most exciting applications will be built.
- Pokemon Go deals primarily with “virtual objects”, while the IoT deals with physical objects or things. Overlaying a virtual object on a physical IoT endpoint is something for developers to contemplate, **as well as overlaying a physical IoT endpoint on a virtual object**. Adding, for example, a low power wireless endpoint at the same location where a Pokestop is located presents interesting opportunities for game developers and IoT developers alike.
- “Gamification” of the IoT is also intriguing from the perspective of mobile endpoints. In the Pokemon paradigm, there is no reason your dog could not be a mobile Pokestop. Or your car. Or your drone. Or you.
- Final-final thought: for the first time, I am considering the possibility that the entertainment industry might have a role to play in the IoT. By driving innovations in AR and through the sheer force of millions of AR users, the gaming industry has enough heft to demand real-world connectivity to their AR games. Nintendo, for example, is about to release a [Pokemon Go Plus](http://bit.ly/2cb7D3a) wearable device to help you play the game without using your phone. Extending this concept beyond the wearable will spawn a new category of hybrid AR/IoT gaming.

# Unified networking

Bridging the gap between LPLAN and LPWAN.

**How To Disrupt The Internet of Things With Unified Networking**

# IoT backchannel

Good for security

# Kill switch

**How To Build an IoT Kill Switch**

The idea of a “kill switch” for machines that cannot otherwise be disabled via conventional means is not a new one, but it is a trendy topic today. Conversations about the [future](http://bit.ly/muskrobot) of AI commonly include the word “apocalypse” as machines both big and small are becoming massively more intelligent, autonomous, and in some cases, dangerous to human life.

If you agree with this, you might also agree that it’s worth getting in front of this before your government steps in to “help”. Multiple groups like [Google](https://www.weforum.org/agenda/2016/06/does-ai-need-a-kill-switch/)are exploring kill switches from what appears to be a software-centric or even cloud-centric perspective, which is important. However if the single radio (e.g. the wifi radio in your wifi camera) in your IoT device has been hijacked by something like a Mirai botnet, there may be no way to execute the kill switch.

Thanks to some innovations in low power wireless radios, better networking software, and more powerful ARM-based chips, an IoT kill switch is not only viable across a wide range of devices, but it is inexpensive and low hassle. It also need not impact form factor or usability in any meaningful way. Here is our view of the challenges and opportunities with IoT kill switches, which starts with better security capabilities for IoT devices more broadly:

*UPDATE: here is the* [*European Parliament*](http://bbc.in/2jEgEDE) *calling for kill switches on a certain category of IoT devices.*

*UPDATE II:* [*follow-up on why*](https://medium.com/@patburns/thesisthewaythegovernmentwillsaveiotsecurity-1b51969cd21d#.iuqfp2b2v) *kill switches are likely to be a central part of near-term regulatory framework for IoT security.*

# Synchronization

**5 Reasons You Should Care About Synchronizing the IoT**

*The clocks on your IoT devices are way more important than you think*



![img](https://cdn-images-1.medium.com/max/1000/1*ddiyJUPtU5aB1whGwddnAA.jpeg)

Unless you are a networking nerd, **synchronization** is probably more familiar as a term used with wristwatches or iTunes than as an IoT term, but the future of the IoT may actually depend on this topic.

Synchronization — the way an IoT device adjusts its internal clock in order to align with the clocks of other devices in a network — lies (surprisingly) at the center of many of today’s IoT challenges, particularly for low-power IoT. Clocks help devices pinpoint the moment when, for example, a sensor measurement is going to be shared with the network. If your device’s clock is out sync with those of other devices in the network, it will miss messages, collide with other messages being sent by other devices, or waste energy trying to get back in sync.

Clocks drift out of synchronization, especially those using low cost, commodity computing parts like we in the low power IoT like to do. So to keep networking running efficiently, clocks need to be synchronized in order to make the data flow in a reliable way.

More than a few inventors of wireless IoT technologies didn’t focus too intensely on synchronization, perhaps because they were using [TCP/IP](http://bit.ly/2TCPIPdef) as their networking model, which while I’m thinking about it reminds me — even if slightly off topic — of this:



![img](https://cdn-images-1.medium.com/max/800/1*C-8Uc8LMG1BQ0V30w9CesQ.png)

Most “low power” IoT protocols implemented something similarly byzantine when they designed their method for network sync. For example, here is a picture of [6lowPAN](http://bit.ly/1P6RrM4) — which famously claims to be a low power means of implementing IPv6 on a wireless network — initiating the sync process:



![img](https://cdn-images-1.medium.com/max/800/1*0l9NidoMUGqYCOzg3Zx3NQ.png)

For 6lowPAN, this process is repeated many times — let’s refer to it as “strobing” — until the endpoint has synchronized its listening cycle with the host. Unfortunately, with 6lowPAN all this “strobing” takes power, can only be done one endpoint at a time, and if the data rate is low the endpoint will burn up lots of battery life as it listens and strobes.

**For 6lowPAN and others in the IoT using “old school” network sync, the cost of not getting it right is high for at least five reasons:**

1. **Battery life.** Like politicians promising to change Washington, most low power IoT technologies don’t tell the truth about battery life. Cellular people you already know who you are. ZigBee, Thread and others are also guilty because **bad sync processes do to batteries what badly under-inflated tires do to your car’s gas mileage**. Multi-year battery life is what makes the low power IoT … low power. Bad sync = bad battery life.
2. **Connection time.** Some wireless technologies can take many seconds or even minutes to connect, due almost entirely to weak synchronization schemes. For an on-demand world where we expect immediate results when it comes to IoT, a bad sync method in a mission critical environment can render obsolete information created only seconds earlier. Smart city or public safety applications, for example, are poorly served with slow-sync technologies. Slow-sync protocols are also a no-go for IoT control apps like implementing a [kill switch](http://bit.ly/iotkillswitch) on a piece of industrial equipment.
3. **Dense-packed endpoint environments.** Environments with lots of endpoints are intimidating to IoT protocols with weak sync schemes. As in, they shouldn’t even get into the ring to pretend to compete. Imagine trying to run a query in a warehouse with 2,000 endpoints and establishing sync with each endpoint— one-by-one — in order to engage in a group broadcast or to query a group of endpoints or to send out a security patch. Industrial IoT environments are particularly sensitive to this issue.
4. **Indoor location.** A growing part of the battery-powered IoT has to do with locating things. Outdoors, we seem to be relying more and more on GPS, but indoors is another matter. Being able to locate something indoors in any kind of real-time way requires fast synchronization with a gateway/access point or, more importantly, with other endpoints on a peer-to-peer basis. Slow-sync protocols are a no-go for these applications.
5. **Security.** IoT technologies with weak sync schemes take longer to exchange keys and are more vulnerable to unwanted discovery and spoofing. Fast-sync protocols are also better able to support [two-factor authentication](http://bit.ly/2ivKCfM) and can remain in a quiet/listen-before-talk mode that protects privacy and inhibits unauthorized discovery.

** Solving For Fast Group Synchronization in a Low Power IoT Network**

Back in 2011 when we started [Haystack](http://www.haystacktechnologies.com/), the issue of synchronization was front-and-center as we gathered requirements for the technology we invented, DASH7. Unlike the slow, serial method used by 6lowPAN and others, we employ a different scheme using a flood of “background frames” and the picture looks like this:



![img](https://cdn-images-1.medium.com/max/800/1*FhTenEmeyy7MzXCujZmppw.png)

Unlike 6lowPAN (sorry to keep picking on them, but trying to keep this brief), any number of endpoints can listen simultaneously for background frames and advertising protocol data. All endpoints can receive the request, all can send responses, and all are then synchronized to each other. **This is the fastest, most efficient method of group synchronization available in the low power IoT today.**

We are not the first company to attempt fast group synchronization via low power advertising, but we’re the first to do it in a (patented) way that actually works. For more information on how Haystack’s group synchronization works [click here](http://bit.ly/2haytech).

# Cellular IoT challenges



**How To Save Cellular IoT From Itself**

Step 1: Remove the“wires” from wireless technology

Wireless carriers like to hype new data capabilities. If you know technologies like [WiMax](https://en.wikipedia.org/wiki/WiMAX) or [CDPD](https://en.wikipedia.org/wiki/Cellular_digital_packet_data), you know how the cellular industry can overpromise. And if you are working in the IoT, you are probably hearing industry propaganda about their upcoming “low power wide area networking” (LPWAN) IoT technologies. LTE Cat M1 (especially in the USA) and LTE NB-IoT (Europe and elsewhere) are their emerging radio standards. And to compound the FUD even further, these are soon to be upstaged by a 5G LTE, which you can pre-order today for delivery in Q2 in 2026.

Huge bets are being placed on the success of LTE in the IoT, and while LTE will have success in the LPWAN arena, many investors will be disappointed. Here are a few thoughts on why and one recommendation for shoring things up.

**Cellular IoT Will Target Consumer Markets**

The strengths that carriers bring to LPWAN’s — and this is just shorthand, you can read more [here](http://bit.ly/2hMx6BZ) and [here](http://haystacktechnologies.com/the-myth-of-nb-iot/) — is going to be in the simplicity of system setup and management, their massive customer installed bases, and the ability to bundle IoT solutions into a customer’s monthly bill with other offerings. Total cost of ownership will be high relative to non-cellular LPWAN substitutes and battery life will disappoint. This has one target segment written all over it: consumers.

Weak battery life and high TCO is something carrier marketing departmetns can finesse with consumers. That monthly bill is a marketer’s Disney World of possibilities. And if they are mad, they can always call customer service …

** Industrial + Enterprise Markets Are Challenging for Cellular IoT**

Enterprise and industrial customers (I’ll just say enterprise for the sake of brevity) in the overwhelming majority of cases require a different product and ultimately, different distribution channels. But this won’t stop the carrier sales and marketing departments because their new LTE IoT story is a hammer for which there are no nails that are impervious to their pounding.

Addressing enterprise markets with LTE-based LPWAN’s, as I’ve [noted](http://bit.ly/2gVYjjF)previously, is fraught with risks. I won’t say there is no enterprise opportunity, rather it’s just not going to be the sweet spot. And for investors in cellular IoT, this is a problem as the lion’s share of IoT revenues lies not in consumer, but in enterprise/industrial IoT markets.

** To Penetrate The Enterprise, Look At Your Stack**

So, for the hard-nosed cellular IoT strategists out there who both intend to invade the enterprise but who recognize the weaknesses of the current LTE products, focus first on your networking stack.

**TCP/IP was built for AC-powered networks with wires.** Like the internet. For streaming huge files via HTTP or FTP. **It was not designed for wireless networks** **and it was most definitely not designed for low power wireless sensor networks.** It is bandwidth intensive, power hungry, and by today’s standards, almost comical in the way it establishes a connection between two computers. But legions of developers know TCP/IP so … in their eyes many IoT problems are just nails waiting for the TCP/IP hammer.

Since the LTE community has for years had the luxury of working with large amounts of wireless bandwidth for carrying voice calls or streaming video, we should not be too shocked that they want to try TCP/IP for the IoT.

For AC-powered IoT conections with lots of available wireless bandwidth, this might be fine. In fact, cellular carriers for years have touted their “M2M” capabilities that do just this.

**But there’s nothing “low power” about cellular’s M2M past** and nothing low power about TCP/IP. But this is not another low power rant — we will all just have to see for ourselves just how many “years” of battery life we see from our forthcoming LTE-based IoT devices, but I tend to think they are talking in dog years while we are talking about human years.

**No the real issue with TCP/IP is how it won’t (really) support LTE’s inevitable foray into the enterprise.**

> *Bonus Thought: anyone who uses the term “TCP/IP” in conjunction with “low power wireless networking” is most likely exaggerating battery life and likely in a big way.*

**Augmenting or Replacing TCP/IP for LPWAN’s**

To provide the enterprise with the type of application functionality they need for their LPWAN deployments, the cellular industry must look beyond TCP/IP.

For example, a real-world IoT pain point we at Haystack see every day is how to solve for indoor location using a LPWAN technology. Lately, we’ve seen lots of interest in Semtech’s LoRa product but also other sub-1GHz technologies. **Now, we’re being asked to solve for this for LTE**. So here are a few slides that describe our approach:

**Basically, we advocate the bolt-on of a companion (< 30 KB) real-time low power networking stack to LTE** in order to enable real-time indoor location for applications like supply chain, IT asset tracking, healthcare, and much more. In addition, this solves for the problem of the [“indoor-outdoor”](http://bit.ly/2b65gRQ)IoT, where assets, people, and things may move from wide area (WAN) environments and into local area (LAN) environments and still require connectivity and location in both cases. More on this [here](http://bit.ly/2b65gRQ).

A related problem with using TCP/IP in these cellular devices is peer-to-peer networking. If you are like me and think the cloud [is way overhyped](http://bit.ly/1knol10) as an IoT tool, the ability to interrogate a LTE-based IoT endpoint on a P2P basis and in real-time will be a significant part of your solution. A weakness for the LTE IoT is its inherent “cloud”-centric nature when the rest of the world is moving to “fog” computing. (Or, if you work with [Haystack](http://bit.ly/2haytech), we take computing all the way to the endpoint, but this is another topic altogether …) The move towards the fog is especially acute in enterprise markets which turns the cloud into a sort of millstone hanging around the neck of an LTE IoT industry that can’t, almost by definition, de-cloud itself.

Final note: telco’s parting ways with the networking stack that got them to the dance will be hard, but with the IoT it’s clearly time to reassess.

# IoT cost

**Is The IoT Just Too Expensive?**

In a [study](http://www.huffingtonpost.co.uk/simon-segars/the-economist-intelligenc_b_15108766.html) sponsored by ARM and IBM that should come as a frigid splash of arctic seawater on the IoT hype curve, the price of IoT infrastructure, more than security concerns, is slowing IoT rollouts across the industry.



![img](https://cdn-images-1.medium.com/max/800/1*oxFszCxxKPQJAOdeIbzqdw.png)

Three takeaways:

1. The report doesn’t divulge details on the definition of “IoT infrastructure”, but this won’t come as good news to advocates of bringing [high cost](http://bit.ly/2LTEDASH7)connectivity into the enterprise. If you are analyst looking for data to help you scrutinize cellular’s [IoT forecasts](http://bit.ly/2mTXw7j) for the enterprise, I’d call the EIU and ask if you can buy their crosstabs.
2. Security amazingly does not get the priority it deserves, indicating the majority of the respondents think they have not been hacked yet or their future IoT system won’t be hacked.
3. The lack of standards in what we are now calling the IoT (I exclude traditional IoT technologies like passive RFID from this mix) seems to be bothering surprisingly few people. The reality is that the IoT is in a state of standards anarchy right now apart from some application layer interoperability happening in cases like Alljoyn. Below the application layer, there is no consensus or de facto standard in the low power wireless WAN sector and it could be years — many years, in fact — away. The low power PAN sector is dominated by Bluetooth low energy but that’s only “IoT” in the most limited sense given its tiny range. The low power LAN space remains a home automation mosh pit. In other words, any vision of ubiquitous LAN- or WAN-based IoT interoperability is years and likely more than a decade away.

# MQTT

ALP / NDEF

CBOR



# IoT broadcasting

TCP/IP handles large data, but only between two devices

Sending a wireless message simultaneously from a gateway to lots of low power IoT devices should be a no-brainer, but for many networking technologies, it is brutally difficult or just impossible.

Some networking stacks can’t even try: battery powered LoRaWAN and Sigfox endpoints the easiest examples. Other protocols do it one endpoint at a time — 6lowPAN is one example — but that really isn’t broadcast, is it?

When do low power IoT networks need broadcast (messaging simultaneously to all devices in range) or multicast (messaging to multiple devices, but perhaps not all, devices in range) capability? Here are three quick examples:

1. **Location Queries**. Asking for the locations of a each cow in a herd of 500 cows. Or each shipping container in a yard. If you want real-time results, you’ll want a way to broadcast your query to everyone in real time.
2. **Implementing GPS.** [We recommend](https://hackernoon.com/now-this-is-the-way-to-make-gps-way-better-for-lpwans-ddad647784cd) the use of assisted GPS (A-GPS) when deploying GPS over a LPWAN endpoint. It’s definitely possible to do it without A-GPS, but the battery savings and performance boost using A-GPS is material.
3. **Firmware Updates.** The soft, white underbelly of today’s IoT is over-the-air (OTA) firmware updates, where so many devices are difficult to patch wirelessly or just don’t support OTA updates at all. (Shoulder shrugging is not a solution …) And no one wants to update endpoint firmware with a USB cable.

There are more use cases for broadcast, but these are good for starters.

We are implementing queries to some battery-powered LoRa devices running Haystack + DASH7 using the popular [MQTT](https://en.wikipedia.org/wiki/MQTT)publish-subscribe application. MQTT is not typically used for queries, but with the compression capabilities of Common Business Object Representation (CBOR), it is possible to do it with [Haystack](http://bit.ly/2haytech) + DASH7 with good results.

# LPWAN vs short range

**Is This The End Of The “Old” IoT?**

The analyst firm ABI sees [LPWAN’s encroaching on short range wireless](http://prn.to/2qWOuvr)technologies — which you may know is [not exactly a new idea](http://bit.ly/2cHRXFH). The easy question is: why would you pick short range technologies like Thread or ZigBee if you could get better range/signal propagation more or less for free using an LPWAN technology?

Bluetooth has a great chokehold on Personal Area Networks and while I have never seen WiFi as a viable solution for low power devices it dominates in mains-powered LAN connectivity. The remaining collage of short range wireless technologies, many operating at 2.4 GHz, remain ripe for disruption.

With luck, we may be approaching a more “[unified](http://bit.ly/2cHRXFH)” networking vision for the IoT that allows us to deploy a more limited number (not just one!) of wireless radio technologies in order to address both long range (WAN) and shorter range (LAN) use cases. Not only does this make IoT LAN’s better, it addresses use cases that straddle the LAN/WAN “dividing” line or that may [transition between indoor (e.g. warehouse) and outdoor](http://bit.ly/2b65gRQ) (wide area asset tracking) use cases.

This encroachment by LPWAN’s to me is inevitable and will happen more suddenly than most of us expect. You could say it’s a “new IoT” that is replacing years-old IoT technologies that were designed in a different era.

# LPWANs

**Free Advice: Pick A LPWAN That Will Survive**

Here’s a new analyst firm with an [intriguing report](http://www.prnewswire.com/news-releases/survival-of-the-timeliestcan-unlicensed-lpwa-beat-nb-iot-300484340.html) on LPWAN’s. I scanned the abstract but three things caught my eye:

1. **There can be only one LPWAN winner in the unlicensed spectrum.** If wireless history is a guide, there will most likely be a single “big” winner for low power, wide area narrowband connectivity. Same as it was for local area wireless broadband (WiFi) or personal area broadband (Bluetooth). The licensed vs. unlicensed distinction, for me, is driven by today’s wireless carriers who present themselves as a serious potential distribution channel for *low power* IoT connectivity, which is very much [TBD](http://bit.ly/2t4kIGw). Moreover, [some](http://bit.ly/2sBfHBv) of the larger carriers are skipping an LTE-based LPWAN option and embracing non-LTE LPWAN’s instead. Which frequency band(s) the LPWAN operates within — licensed or unlicensed — is immaterial to whether it is the big winner.
2. **There’s a shakeout/consolidation coming in low power wireless protocols.** I won’t list them but there are plenty. This report calls out the technology Haystack invented and patented, [DASH7](http://bit.ly/2haytech), as one that will survive. There are good reasons for this [here](http://bit.ly/lorawan) and [here](http://bit.ly/2pBcYqp) and [here](http://bit.ly/2uRSqfA).
3. **Bigger-than-exepcted opportunity for module vendors.** Here’s the quote:

> “According to Mobile Experts, connectivity module revenue will grow from about $1B in 2016 to about $33B in 2021, with volume growth in multiple markets clearly overcoming the drop in device pricing. At a semiconductor level, the revenue for MCUs and RF solutions will grow to more than $1B by 2021.”

33x better performance by module vendors vs. semiconductor vendors means … module vendors have more upside than I thought. FWIW the modules we work with don’t have a 33x price delta (in 2017) over the sum of individual components, etc. but the 33x could be driven by a) inflated cellular module pricing or b) expected cost reductions in components vs. module retail pricing, or c) higher than expected heterogeneity of use cases and customer volumes that drive thousands of small deployments where (overpriced) modules are the preferred go-to-market route vs. individual components. I’d go with c) if I had to pick …

A side note: this report claims to use a bottoms-up forecasting methodology for the LPWAN market based, it appears, on face-to-face interviews and other exploratory methods. After the cascade of IoT forecasts showing billions or trillions of devices by next year — or maybe it was 2020— it is refreshing to this approach.

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

# Here Are My Quick Reactions To The Verizon IoT Announcement

# LTE-M criticism

1. [**Here**](http://vz.to/2nTO6LD) **is the announcement**
2. **No multi-year battery life.** Usually when an LPWAN technology launches or tries to make waves, it emphasizes the “LP” (low power) part of the acronym. Verizon wisely and tellingly characterizes CAT M1’s battery store like this:

> “Verizon maintains a strong leadership position in IoT technology and solutions with a history of firsts, including the first deployment of 4G LTE, LTE Cat 1 and now LTE Cat M1. A game-changer for the industry, Cat M1 is a new class of LTE chipset that is designed for sensors. **They require less power, offer extended battery life** and support an array of use cases ranging from water meters to asset trackers to consumer electronics.”

If you’ve been in the low power IoT industry for a while, the industry vernacular for talking about “low power” is in terms of **years** of battery life. So absence of that term “years” confirms what many of us working ([and blogging](http://bit.ly/2LTEDASH7)) in this area have known for some time: LTE CAT M1 battery life is at best measured in months and is really more appropriate for fixed use cases where devices have access to mains/AC power. For you folks hoping to use LTE Cat M1 for battery powered use cases, it may be time to look elsewhere. Or **if you want to go ahead with a battery powered use case, your customers should be A-OK with frequent battery recharges/replacements.**

But I think this is the point where we can stop calling LTE Cat M1 “LPWAN”. Maybe Medium Power WAN? Anyone?

**3. Verizon smartly publishes its “best case” pricing per endpoint:**

> “The” low bandwidth use cases for Cat M1 chipsets demand new types of data plans, including **low rate, multi-year plans** to match the longer useful life of devices. Cat M1 devices can economically scale on Verizon’s wireless network on [data plans ](https://www.verizonwireless.com/biz/plans/m2m-business-plans/)that are **as low as $2 per month per device**, with customized options available for bulk activations and volume purchases.”

No use hiding your pricing — we were all [expecting the wors](http://bit.ly/2mXVVPy)t! — and probably good for Verizon to at least test at this level. $2.00 per month gets you 200KB of data — presumably this is going both from the endpoint to gateway as well as vice-versa.

Since LTE Cat M1 is using TCP/IP, which is like the [C-3PO](https://en.wikipedia.org/wiki/C-3PO) of networking protocols —unnecessarily verbose, using 10x the words necessary to communicate a point — it is conceivable that your 200KB could be flushed in seconds over HTTP, or perhaps in just a message or two per day using something like MQTT or UDP.

Just a hunch, but the $2.00 per month plan might be a “teaser” and they really want to “upsell” you on a richer plan with “more data”:



![img](https://cdn-images-1.medium.com/max/800/1*KnwOTy0KMOCA9dYve4pxow.png)

According to the text quoted above, the low rate is for a multi-year plan — “to match the longer useful life of devices” — so if multiple years is a minimum of two, your minimum subscription investment would appear to be $48, but more likely $72 or even $120.

Then this bit of text caught my eye:



![img](https://cdn-images-1.medium.com/max/800/1*KF1-I06dYScdE9KmbSQIjA.png)

I didn’t call my Verizon rep to talk about the details, but seems like a safe bet that your minimum service commitment per endpoint will be north of $48.00, perhaps much higher.

And we haven’t even seen hardware device pricing yet.

I’ve worked for years in and with telco’s and the byzantine pricing part of their business drives me crazy. I see the fingerprints of Verizon finance all over this, but this is not a pricing plan designed to get lots of developers in the door.

One bit of speculation: there’s an automotive market opportunity being targeted here.

**4. Lots of partners**

If you read the announcement, you will see a bevy of recognition from brand name silicon and module makers. As you’d expect from Verizon and also a reminder never to underestimate the power carriers have not only as distribution channels but also over their suppliers. All things being equal, carriers should be able to move IoT markets given their place in the ecosystem.

**5. Friday announcement**

If I were announcing a dramatic entry into the IoT, I would not announce on a Friday. Unless I was lacking confidence (or internal consensus) in what I was launching …

**Closing thought:**

I’ll try to dive in further to this in a subsequent post. But for now, **I think this is a significant announcement for the IoT**, but probably not for the reasons the cellular community expects. If you were/are a developer advocating LTE Cat M1 as a LPWAN solution, it might be time to expand your portfolio. If you are on the customer side and looking for a battery powered answer to your IoT problem, this is probably not your answer.

If you are interested in LPWAN’s you may want to read what we have to say [here](http://bit.ly/2nNFOFP) and [here](http://bit.ly/2lbtWLF) or at our [website](http://bit.ly/2haytech). Haystack offers a lightweight, low power, low latency firmware stack that works across LPWAN’s (and LTE Cat M1) in ways TCP/IP or LoRaWAN cannot. So email me if you are in a jam …pat at haystacktechnologies dot com or @patdash7

# NB-IoT positivity

**Does China Have an Unfair Competitive Advantage in IoT?**

Here are the folks at research firm Rethink Research discussing [Huawei’s warning](http://bit.ly/2oOqU2f) that this LTE NB-IoT hype is just a little overdone and that the technology for now is mainly for smart meters.

The warning about NB-IoT use case limitations is something [I’ve mentioned](http://bit.ly/2LTEDASH7)previously, but what caught my eye was some stark differences on pricing.

As I mentioned last week, Verizon announced plans to charge **$2 per month**for its entry level (i.e. smart meter/once per day message) per LTE CAT M1 endpoint in the USA, but this is positively affordable compared to Deutsche Telekom’s NB-IoT pricing of [EUR 9.95 per month for each connected machine](http://bit.ly/2nyTCV8). (!)

I wonder what Verizon and DT customers will think when they learn that China Telecom will charge **$0.15 per month per smart meter for its NB-IoT endpoint?**

> Smart meters will only be transmitting incredibly small amounts of data on an operator’s network. Xujianmin suggested that China Telecom will be charging $0.15 per month per smart meter device connection.

Now, applying pricing in China to pricing in the U.S. and Germany is not necessarily apples-to-apples, and China may simply be selling NB-IoT services below cost in order to grab market share, stimulate a nascent industry, etc. But global cellular LPWAN markets are all launching at around the same time, have common infrastructure and silicon providers, and … a 1,333% difference between Verizon in the USA and China Mobile in China is kind of shocking, no? A 7,026% difference between Deutsche Telekom and China Mobile is … beyond shocking.

So either a) China Mobile is radically selling below cost, b) China Mobile has an amazing unfair cost structure advantage vis-a-vis the rest of the world’s carriers, or c) Verizon and DT finance departments don’t do marketing. Whatever the case, I think cellular IoT pricing is one of its biggest challenges, especially in commercial/industrial markets and China Mobile just highlighted this for the world to see.

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

**Looks Like More Forking Going On In The IoT**

If you follow the hype on NB-IoT, you may have heard of the [dispute between Ericsson and Huawei](http://www.lightreading.com/iot/nb-iot/ericsson-huawei-incompatibility-threatens-nb-iot---sources/d/d-id/732345), which is throwing wrenches in lots of frothy cellular IoT forecasts.

This kind of dispute is not uncommon in standards bodies, and it’s not uncommon for vendors to start selling equipment using non-final draft specifications of a standard with the intention of making the equipment standards compliant — maybe via a firmware upgarde — once the standard is baked, ratified, and adopted.

It’s different, though, when two vendors don’t see eye-to-eye and just start selling incompatible hardware that no firmware upgrade will resolve down the road. Which is what appears to be happening here. So in addition to high silicon costs and questions about battery life, plus [TBD competitiveness around monthly subscription costs](http://bit.ly/2LTEDASH7), there is the basic question of “How would you like to be locked into Huawei/Ericsson’s proprietary flavor of NB-IoT?”

If you are a carrier that has participated in the NB-IoT hype-a-pallooza, this might make for a fun topic at a board of directors meeting. Or some really interesting sales calls with customers.

I would never recommend counting the carriers out of the IoT — many are too big and too threatened by the IoT to stand idle. But the challenges of a) a CAT M1 standard that is. not. low. power, and b) [technical](http://bit.ly/2mTXw7j) and standardization questions about NB-IoT, puts carriers in a quandary. Stick to your LTE guns or diversify and embrace another LPWAN technology?

Oh and for direct competitors to cellular carriers who like to charge monthly subscriptions, your competitors’ unbending loyalty to LTE looks like an opportunity to be exploited.

**How To Solve The Cellular IoT Prisoner’s Dilemma**


![img](https://cdn-images-1.medium.com/max/1000/1*bOwamb03P4-c8HdYB5lilw.jpeg)

It seems like we are finally getting clarity on features and pricing not just for high powered cellular IoT like LTE CAT M1, but also the long-awaited NB-IoT as well. NB-IoT famously claims to be a low power, wide area networking (LPWAN) technology.

[This piece](http://www.lightreading.com/iot/nb-iot/nb-iot-gets-insecurity-complex/a/d-id/733454?page_number=1) in Lightreading: “NB-IoT Gets Insecurity Complex” builds on other research we have seen that basically confirms that not only are NB-IoT modules not going to price at $1 each (what we were told just [six](http://www.nickhunn.com/nb-iot-is-dead-long-live-nb-iot/comment-page-1/#comment-118098) months ago) or even $5 each, but much, much more:

> “A likelier explanation is that customers are not ready for NB-IoT prices. Modules still cost somewhere between €10 ($11.25) and €15 ($16.87), according to Deutsche Telekom, against an industry target of just $5.”

It is worth noting that the article quotes pricing for NB-IoT “modules” — not completed devices. And NB-IoT *modules* are arriving at price points that are 2–3x or more over what was promised. Assuming the *lower end* of Deutsche Telekom’s per-module cost of $11.25 and adding additional bill of materials, packaging, shipping, taxes and other costs required to ship a completed device, and you likely end up with per endpoint costs of $20, probably more. And that’s before the concept of profit even kicks in. The commercial/industrial appetite at these levels, even amortized via a monthly subscription, is quite limited.

As I’ve mentioned [before](https://medium.com/@patburns/here-are-my-quick-reactions-to-the-verizon-iot-announcement-808da1692f8c), my experience with IoT products that come with this kind of premium pricing is that they self-segment into corners of the market where ease of use/ease of implementation cancels out the sins of high device or monthly subscription costs. Certain small business and consumer segments are the most likely targets for a premium product like this, while commercial and industrial customers with rudimentary systems integration capabilities and who don’t necessarily trust their carrier with their data will be slow to adopt. Obviously, the “[forking](https://hackernoon.com/looks-like-more-forking-going-on-in-the-iot-946a7220e967)” going on in the NB-IoT standardization community does little to assuage the worries of enterprise customers:

> The industry’s reactions to those reports are what betray the insecurity. Talk of interoperability problems between equipment vendors [Ericsson AB](http://www.lightreading.com/complink_redirect.asp?vl_id=1879) (Nasdaq: ERIC) and [Huawei Technologies Co. Ltd.](http://www.lightreading.com/complink_redirect.asp?vl_id=2430) is now rife at industry events. Numerous industry experts have also flagged the issue in discussions with Light Reading. Yet Ericsson and Huawei have pleaded ignorance, while operators have either denied there are problems or declined to comment.

> The timing of one recent statement on interoperability also looks odd. Vodafone this week said it was carrying out NB-IoT interoperability tests more than two months after it was supposed to have launched commercial services in some European markets, and having never previously acknowledged that interoperability is a concern. Those tests have shown that all is tickety-boo, it insists.

But assume that the standards folks get their work done sooner or later. Ease of use or ease of implementation still assumes, in the LPWAN space, that the customers can “plug and play” an IoT device (or thereabouts) and not need to worry about maintenance, etc. **Which brings us to the money question: battery life performance.** Dead batteries are the maintenance bane of IoT network operators everywhere. For now, NB-IoT is deploying TCP/IP as its networking stack, and TCP/IP is no friend to battery life. A real risk, therefore, for NB-IoT is that it ends up as a high powered backhaul or mains-only solution similar to its LTE Cat M1 cousin which is also showing its true colors as a high priced/high power solution. Or NB-IoT ends up as a repeat of previous high powered, high priced [consumer GPRS misfires](http://www.sandiegouniontribune.com/business/technology/sdut-Qualcomm-Tagg-Pet-Tracker-Private-Equity-2013jul10-story.html).

**If NB-IoT does not deliver multi-year battery life as promised — and I do not believe it will — the cellular industry has a bit of a situation on its hands.**

NB-IoT is really a “we-can-just-do-a-simple-base-station-firmware-upgrade-and-deliver-low-power-wide-area-IoT” pitch to analysts who track LTE. Free money! But without a technology to actually, you know, deliver the broader LPWAN market opportunity, the pitch is moot. So analysts might rethink their cellular LPWAN forecasts absent one or more of the following moves:

1. **Embrace an additional, non-LTE radio option like LoRa or Sigfox.** Or another emerging LPWAN PHY layer technology. Even if only as an “interim” solution until the LTE-based LPWAN woes can be resolved, assuming they can. If there’s a market worth going after — and there is — it’s probably not worth sacrificing early market share to wait years for your preferred radio technology to be ready for prime time.
2. **Align per-month endpoint pricing** to provide something closer (on a present value basis) to parity for a comparable, easy-to-use technology from an unlicensed band, e.g. LoRa. While this could help preserve earlier unit forecasts, it may be get howls from cellular finance departments. But if you can’t compete on battery life, at least soften the price blow if you are serious about competing for customers.
3. **Re-orient internal mindsets** from steadfast allegiance to LTE and instead embrace a more open-ish model, perhaps along the lines of [Made for iPhone](https://developer.apple.com/programs/mfi/), where carriers embrace multiple radio technologies and devices and provide a common networking layer to minimize maintenance and support. Like [this](https://www.slideshare.net/haystacktech/bringing-better-networking-to-lte-iot) one.

Others have offered [suggestions](https://iotbusinessnews.com/2017/04/26/37988-iot-will-little-impact-revenue-mobile-operators/) to help carriers out of this dilemma, and the answers don’t appear simple. And while I shouldn’t be surprised, I am nonetheless astonished that the LTE community has even come to this point given its massive resources and market power. What happened? Here’s an excerpt from the same piece:

> What seems undeniable is that NB-IoT was a rushed job following an abrupt rethink by the cellular industry on the need for a so-called low-power, wide-area (or LPWA) technology. Two and a half years ago, cellular industry folk at the [GSM Association (GSMA)](http://www.lightreading.com/complink_redirect.asp?vl_id=7572) were “dismissive” of LPWA, according to Tom Rebbeck, a director at the [Analysys Mason](http://www.lightreading.com/complink_redirect.asp?vl_id=11510) market research business. “Then within a year they had turned around because they saw the momentum behind Sigfox and LoRa,” he says.

I won’t underestimate their ability to turn the ship around, but based on what I hear from colleagues working on 5G (coming to your town in how many years? Five? Ten?), the cellular industry mindset appears to be one of doubling down on the current roadmap, which will be no friend to low power endpoints.

So maybe low power IoT was not so important to the cellular community after all and all the hype was … just that. Regardless, this represents a great opportunity for non-LTE LPWAN radios, LPWAN networking technologies, and network operators not saddled with LTE-or-die obligations. And it’s still early enough for carriers to re-think their plan.



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

# Localization battery life

**One More Thing …**

AA batteries are too large for some use cases and here at Haystack we do work with coin cell batteries at the endpoint. A couple of things I wanted to at least hint at here:

- Coin cell batteries are generally not designed for long discharges. I haven’t seen any LoRaWAN + GPS devices with coin cell batteries and I doubt that I ever will.
- Deploying on-demand A-GPS on a coin cell-based LPWAN device — which has only 620 milliamp hours using a CR 2450 coin cell — still delivers remarkable battery life using Haystack/DASH7:



![img](https://cdn-images-1.medium.com/max/800/1*OND3fzjbUfn33QQpbLZx1A.png)

Maybe we’ll do another post on coin cell form factors …

# Trilateration

**For Outdoor LPWAN Location Start With RSSI**

I’ll explain how to overcome GPS hell on a LPWAN device below, but the first step in getting around the seemingly massive obstacles starts by not using GPS at all. Instead, we recommend allowing a gateway to take received signal strength indicator (RSSI) measurements from a mobile device and in some cases [trilaterating](http://bit.ly/2aE0qWl) (similar to triangulation) their measurements using multiple gateways.



![img](https://cdn-images-1.medium.com/max/600/1*zH17V2lqvN4oaD5Lh-XWsg.png)

Example of Non-GPS trilateration over cellular

Theoretically, even some of the notoriously bad networking stacks like LoRaWAN or Sigfox can do something like this (LoRaWAN [tries to market](https://hackernoon.com/this-iot-technology-pretends-to-be-something-its-not-b09319efb320)trilateration using a time-based method called Time Difference of Arrival, since the protocol can’t support RSSI, which is a superior approach for reasons I don’t have room for here.) With LoRaWAN your mobile device a) will need plenty of LoRaWAN gateways in range, b) better stand still for 30 minutes, and c) will not know if your location beacon was received by the gateway. (LoRaWAN packet loss is legendary.)

Our experience with trilateration is that the accuracy of the estimated location can vary from surprisingly accurate — say, within 25 meters — or wildly off — by a mile or more— depending on the number of available gateways, terrain, RF environment, movement of the mobile device or the gateway, and more.

There’s nothing wrong with RSSI-based trilateration, in fact we recommend it as part of your outdoor (and indoor) location technology portfolio, but implemented with one-way LPWAN protocols won’t work for most of us. Haystack does this with DASH7 in a far more efficient and relevant way, as you’ll see below.

**The Importance of Real-Time Location**

We hear about asset tracking every day at Haystack but ultimately it’s about asset tracking in **real-time**. That is, answering the everyday question “Where is it?” As in, “Where is my power drill?” or “Where is my bag of electronic equipment?” or “Where is my husband?”



![img](https://cdn-images-1.medium.com/max/600/1*ioJHoLBQAGvf68AwqZaxbA.jpeg)

Some customers want to know the location of things and don’t like being told to wait

Rarely or never is the question: “I am looking for my champion Poodle, but hey no rush! Just get back to me with an approximate location sometime in the next 30 minutes or the next day and that will be just fine …” No, the question is almost invariably “I need to find my Poodle … RIGHT NOW.” And for most use cases, the end user wants to repeat the question again two minutes later. And again. And again. When you think about it, anything that is mobile that is worth enabling with a LPWAN tracking device is usually valuable enough to require asking this question and receiving an answer in real-time. Unless you don’t really love your Poodle.

So at Haystack we’ve invented a [portfolio](http://bit.ly/2haytech) of solutions to help the LPWAN + GPS community that are uniquely achievable via the networking firmware stack Haystack invented and patented, DASH7.

**The Importance of On-Demand in the IoT**

I’ve written before about the importance of allowing endpoints to remain in a “[listen-before-talk](https://medium.com/@patburns/why-the-internet-of-things-is-going-nowhere-112540e79ae)” mode rather than engaging in constant chattering and needless handshaking. Benefits include power savings, real-time queries, [real-time location](https://medium.com/@patburns/the-indoor-outdoor-iot-2544d1026cae), better privacy and [security](https://medium.com/the-startup-magazine-collection/a-simple-proposal-to-improve-security-for-the-internet-of-things-4fcc0663f70e) options, and more. But when dealing with a feature as power-intensive as GPS, on-demand capabilities become paramount.

**On-Demand RSSI Queries**

As a first step in answering the “where is it right now?” question, we recommend starting with an on-demand RSSI query. Rather than invoking GPS on a mobile device, it may just be more practical to “probe” for a device’s location using a simple test of signal strength from a gateway that serves as a proxy for whether the mobile object (in the above use case, a chainsaw) is within an acceptable distance from the gateway/access point. A strong signal whose value is ≥x may give an owner peace of mind that the chainsaw is nearby.



![img](https://cdn-images-1.medium.com/max/600/1*5OyIdzEBDP6MI29CHaesUw.png)

A weaker signal whose value is ≤x might trigger either a trilateration sequence, e.g. for a device that is moving use repeated queries to the mobile device to measure changes in signal strength and for a fixed device use either a mobile gateway or multiple gateways. For those of you familiar with geofences, it’s possible to construct one using RSSI values.

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

# Assisted-GPS

**On-Demand Assisted GPS**

But let’s say you are modeling GPS usage for an upcoming LPWAN project but you are concerned that the end users you have in mind might not read your documentation that says to use GPS sparingly and instead might pummel the battery with nonstop queries. Think lost dementia patients, lost family dogs, a lost vintage Fender Stratocaster pre-performance at Lollapalooza, etc. Or that obstructions might be more common than normal and acquisition times might be longer. Even on-demand GPS (along with on-demand RSSI probing or geofencing) with Haystack might not be enough to prevent a fast dead battery.

One of the more exciting things we are implementing at Haystack is Assisted GPS or “A-GPS”. If you are interested in learning more about A-GPS go [here](http://bit.ly/2p1E6hh), or if you prefer pictures, here is one:



![img](https://cdn-images-1.medium.com/max/600/1*HaxwIymUtQzPzVoGvN4eeA.png)

Basically A-GPS is a way of providing information to a LPWAN device, via a gateway, to help it acquire GPS satellite coordinates much more quickly than without A-GPS. As in, **shrinking acquisition and processing time from 2 minutes to 20 seconds.**

A-GPS information includes information about the location of all 32 satellites orbiting the earth for a given time of day and location, time, satellite health information, etc. The total data payload is typically around 1KB. A-GPS is used extensively in cellular telephony and is one of the reasons it doesn’t take your iPhone two minutes to acquire GPS coordinates when you use Apple Maps.

**But to send A-GPS information to mobile LPWAN devices requires a fully two-way networking communications protocol, preferably with robust multicast and broadcast capabilities, like the kind you get with Haystack.**For example, rather than have a group of LPWAN cow tracking devices attempting unassisted GPS location acquisition, a DASH7 gateway can simply multicast A-GPS information as it becomes available. Endpoints could request A-GPS information individually but multicast is faster and more efficient.

As is probably obvious by now, A-GPS is a no-go with LoRaWAN, Sigfox, and other one-way or similar protocols. But using the same lost chainsaw example from above shows how impressive the battery life extension with A-GPS can be using Haystack:



![img](https://cdn-images-1.medium.com/max/800/1*HLjmg2t8SUTHnYWVWDfI-w.png)

There are multiple providers of A-GPS information that your LPWAN gateway can access. Here’s [one from u-Blox](http://bit.ly/2pPSUDJ) who offer their A-GPS location services free to their OEM customers.

Needless to say, we are big advocates of A-GPS for LPWAN’s for those customers looking for high precision outdoor location.

# Geolocation



**Now THIS is the Way to Make GPS Way Better for the IoT**


![img](https://cdn-images-1.medium.com/max/800/1*MmUzJp2NFUK1tmwn2Urx1Q.png)

The IoT doesn’t appear on award-winning TV that often, but if you liked the TV series “Breaking Bad”, you might also be watching its [prequel](http://www.amc.com/shows/better-call-saul), “Better Call Saul”. Without giving away the plot, this season a small, long-range GPS tracking device is prominently featured in multiple episodes and, well, **the battery doesn’t last very long**.

You can watch for yourself — I highly recommend it for both the screenwriting and the acting — but I’m glad to see the issue getting popular visibility because in the LPWAN (Low Power Wide Area Network) corner of the IoT where some of us live, we have yet to have “the talk” about a huge challenge: **GPS melts LPWAN battery life**.

So this piece is about implementing GPS in the low power IoT. As you probably know, LPWAN’s are supposed to be low power devices which implies … no AC power connection. If you are thinking about fixed or non-mobile LPWAN endpoints, then you have no need for GPS and reading this article is probably a distraction from being productive. **But if you are deploying mobile LPWAN endpoints, read on**.

**Asset Tracking**

A major use case for LPWAN’s is what analysts boringly refer to as “asset tracking”. In my native pleb-speak this translates to “where is my stuff?” Tools, dogs, cows, bicycles, weapons, shipping containers, Alzheimer’s patients … the list of asset tracking use cases is extremely long.

I’ve touched on locating things in the IoT [here](https://medium.com/@patburns/the-indoor-outdoor-iot-2544d1026cae) and here and I’ve noticed how some LPWAN technologies make [ridiculous claims](http://bit.ly/2nNFOFP) about their ability to locate things outdoors. But here’s a fact: **deploying GPS on a LPWAN device is hard.**

**GPS — LPWAN Facts**

Many developers *think* they know how GPS works but if you have doubts and think you could use a refresher, try [this](http://bit.ly/2p1nvfY). To compute its location, **an IoT device needs to acquire GPS signals from at least three but ideally four out of 32 GPS satellites** orbiting the earth.



![img](https://cdn-images-1.medium.com/max/600/1*RPFWYsReSn3OgR0D7qDCsg.gif)

32 birds, orbiting on six separate planes

But what most also don’t know is that GPS is a **very slow communication channel** — just 50 bps! — which means the amount of time your little mobile LPWAN device must be “on” in order to receive GPS messages (technically 37,500 bits per message, per satellite) can be multiple *minutes* in order to acquire the GPS coordinates being sought.

**Battery-consuming factors:**

1. **Flutter.** If your LPWAN device has an obstructed view of a satellite (chainsaws may be locked in a shed or the passenger seat of a pickup truck) or the device is moving (highway overpasses, tall buildings, etc.) a GPS receiver can experience “flutter”, causing the receiver to work overtime to search for error-free GPS packets. If the flutter is bad enough, this can take a LONG TIME and further deplete your battery in the process.
2. **GPS “idling”.** GPS receivers don’t do a good job of retaining satellite location information while in a low power state. If you want to keep satellite location data fresh in your mobile device’s memory so that the next time your device tries to acquire GPS info it can do it faster, you’ll need to budget a continual flow of power — approximately 0.44 milliamps on average — or risk needing to acquire GPS from a “cold start”. GPS satellite info has a shelf-life of four hours so at a minimum you will need “fresh” satellite info at that interval. The 0.44 milliamp average is a weighted average of idle power and GPS on time for a system sampling GPS every 30 minutes.
3. **The radio.** Acquiring GPS coordinates is not enough as you’ll have to transmit them to a gateway. This is in addition to any other messaging your device might do.
4. **The MCU and the rest.** Your mobile device needs to do everyday computing tasks managing whatever onboard sensors, radios, memory, etc. it is carrying. This burns battery life.

So it’s no wonder we haven’t seen more action with GPS and LPWAN’s. Practically speaking, for most LPWAN protocols (but not all!), GPS is like going swimming with a 35-pound kettlebell tied to your ankle.

**On-Demand GPS**

If your on-demand RSSI query shows a signal that is ≤x (i.e. meaning it is located somewhere outside your geofence) and you want more precise location coordinates, you can invoke a GPS receiver on a LPWAN device.

Assuming a 16 milliamp GPS receiver and an AA battery, **invoking standard GPS on a LPWAN device is something most developers will want to do only sparingly** or, if you plan to execute repeated queries, ideally when an item occasionally goes missing and not daily or even weekly. So for example, let’s say the chainsaw on a construction job site goes missing on average once every two weeks and the end user — frantic at the thought of having to tell the boss that he spent an hour looking unsuccessfully for the chainsaw again and couldn’t find it — invoked GPS five different times before recovering the chainsaw. **Using** [**DASH7 technology from Haystack**](http://bit.ly/2haytech)**, using an on-demand GPS approach is much better than the beacon approach:**



![img](https://cdn-images-1.medium.com/max/800/1*aBPz08hz7k30rdJXAiatYA.png)

It’s important to repeat that 750 days battery life modeled here is theoretical and doesn’t take into account flutter, other device duties, etc. but **using an on-demand (real-time query) approach to invoking GPS is vastly better than the concept of the same device acquiring and beaconing GPS coordinates at preset intervals.**

- If you plan to deploy location-based services with your LPWAN, your choice of networking protocol has major consequences in terms of basic feature set, performance, and the breadth of use cases you can support.
- If you plan to deploy GPS over an LPWAN, there are few downsides to deploying A-GPS and plenty of upsides.
- Obviously there is more than location to consider in an LPWAN product. For example, being able to send a command in real-time or the ability to ship over-the-air security patches or firmware upgrades is important, too. But if your LPWAN solution calls for high-reliability/high-precision outdoor ([or indoor](https://medium.com/@patburns/the-indoor-outdoor-iot-2544d1026cae)!) location, the right option is pretty obvious:



![img](https://cdn-images-1.medium.com/max/800/1*v4FfuGDCHCs2nxm9SUR3tA.png)

- If you are in an outdoor or indoor location jam and need someone to talk to, email me at pat at haystacktechnologies dot com or visit our [website](http://www.haystacktechnologies.com/).

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

**Cellular-based Geofencing**

**Conclusion**

Geofencing is an exciting opportunity for mobile asset tracking over LPWAN systems, but the importance of the [right](http://bit.ly/2haytech) networking stack cannot be overstated. A unidirectional protocol is a poor choice for most LPWAN implementations but in particular those seeking to implement geofencing. A bi-directional protocol that supports multicasting/broadcasting as well as low power wakeup is, for the LPWAN world, essential.

# LoRaWAN geolocation / tracking

**This IoT Technology Pretends To Be Something It’s Not**

I’ve written before about Low Power Wide Area Networks (LPWAN’s) and the pros and cons of [cellular](http://bit.ly/2mTXw7j)-based LPWAN’s as well as the same for those non-cellular technologies operating in unlicensed radio spectrum.

One technology we at [Haystack](http://bit.ly/2aSPRzX) like is Semtech’s [LoRa](http://bit.ly/2oal5bq) LPWAN radio. Long range, low power, and reasonable-ish pricing. Some freeware they helped create called LoRaWAN, however, is [not good](http://bit.ly/lorawan). We get a steady stream of LoRaWAN refugees who, eager to build a long-range device with multi-year battery life, believed the various misleading statements about its two-way communications capabilities (sorry, not happening), security (really bad), ability to update firmware (you can’t, practically speaking), and a few others. As I’ve said before, serious developers don’t use LoRaWAN and sooner or later, the good ones figure out the truth of LoRaWAN and bail.

But it gets worse.

Recently at least one prominent company announced [plans](http://bit.ly/2o6LGWX) to work on geolocation with this same team, something Semtech announced [last summer](http://bit.ly/2o6LGWX):

> “LoRa technology has a GPS-free geolocation functionality (LoRa geolocation) that enables a wide range of applications required to determine location as part of the platform.”

Literally speaking, there’s nothing incorrect in the above statement: a LoRa radio can indeed support GPS-free location. In their announcement, they recommend using a time-based approach called Time Difference of Arrival in order to determine the location of a mobile device relative to two or more base stations. Is this the best approach among non-GPS location methodologies? No. But it’s true you don’t need a GPS receiver to acquire location coordinates … you just use the [synchronized clocks](http://bit.ly/2lbtWLF) on the devices in your LoRa network to make (hopefully) a pretty good guess. (Simply put, if Gateway A is located one mile from an endpoint and Gateway B is located two miles from the same endpoint, it will take longer for the message from the endpoint to reach Gateway B. Then use geometry.)

But where this is all misleading is not in the claims about the Semtech radio itself — which we like and work with every day — but in the networking software stack that sits above the radio. Unwitting LoRa developers find themselves led to use the LoRaWAN freeware that is often marketed alongside LoRa, which is the geolocation equivalent of recommending solitaire as the killer app for a supercomputer.

I’ve written on the [pitfalls of LoRaWAN](http://bit.ly/2hjJE5T) before, but to summarize, here are the basics you need to know before trying LoRaWAN for geolocation on battery powered LoRa IoT devices:

1. **One-way only.** LoRaWAN only communicates in one direction: from the endpoint to the gateway, and not vice-versa. This means there’s no practical way to ask the device a question like “where are you?” and get an answer. There’s also no way to know if the message sent by a endpoint was received by the access point or gateway.
2. **Not real-time.** You can program a LoRaWAN device to “beacon” every 30 minutes or so, but similar to #1 above, you can’t do a real-time query like “where is my lost dog?” Combine this with the high failure rate of messages sent via LoRaWAN, and you could wait hours to locate a mobile device.
3. **No real-time indoor location, either.** Because LoRaWAN has no peer-to-peer capability and is not real-time, you can forget about locating a mobile endpoint indoors in real-time. So if that laptop with sensitive customer data goes missing in your building, good luck finding it via LoRaWAN. (More on this [here](http://bit.ly/2b65gRQ).)
4. **Limited location support.** LoRaWAN precludes the use of a Received Signal Strength Indicator (RSSI) which on radios like LoRa is a far more accurate approach to determining location via trilateration/triangulation. In addition, the accuracy of time-based location approaches (like TDOA) correlate positively with available bandwidth and signal-to-noise ratio (SNR) — both of which are quite low on LoRa. In other words, their default GPS-less approach is not very accurate.
5. **Huge latency**. Even if you program your LoRaWAN endpoint to create an alert based on some event (e.g. temperature deviation), the minimum latency between initiating the alert and sending the alert is more than **two minutes**. If you are attempting to locate something important — like an Alzheimer’s patient or the family dog — that two minute lag might just be less than acceptable.

So just to illustrate how absurd the LoRaWAN “geolocation” approach is, a LoRaWAN-based solution might hypothetically work where: a) your mobile endpoint is standing still, ideally for a few hours, b) you don’t need to know its location coordinates in real-time, c) you are OK waiting until the next beacon 30 minutes from now, d) you don’t need very accurate location coordinates, and e) you don’t want to locate anything indoors.

Other than that, it’s great for geolocation.

But this gets to the heart of the issue of developing for the mobile IoT, which I’ve written about [here](http://bit.ly/1J3BlEf) and [here](http://bit.ly/2b65gRQ): solving for the battery powered LPWAN (e.g. combining long range and multi-year battery life) is not enough when the LPWAN is being deployed on a mobile device. The case of geolocation via LoRaWAN is a perfect example of a LPWAN networking stack that was (expediently) developed without — among a long list of oversights — contemplating the “killer” app for LPWAN’s: **mobile, battery-powered devices**. I’m convinced LoRaWAN was a demo built over a weekend over beer, bad Chinese takeout, and too much Toblerone that some product manager decided to commercialize without informing engineering.

LoRa is a good radio technology. But if you want to do location — indoors or outdoors — over LoRa, don’t use LoRaWAN. [Here’s a much better way](http://bit.ly/2haytech).

Update: [more thoughts here](http://bit.ly/2pBcYqp) on implementing GPS over LPWAN’s.

**Let’s Try This With LoRaWAN**

We could pick on Sigfox here, but that would be too easy so let’s further illustrate the battery impact of GPS on a LPWAN device by assuming you are using a one-way LPWAN networking stack for Semtech LoRa devices called [LoRaWAN](https://medium.com/@patburns/announcing-haystacks-lorawan-replacement-program-1a72cb4cf201). Since it’s a one-way device, assume it emits a periodic one-way beacon with GPS coordinates every 30 minutes to track a valuable piece of construction equipment at a job site. Why use a beacon? Because with a one-way protocol like LoRaWAN there is no way to query “Where is my chainsaw?” if the chainsaw goes missing.

So assuming an acquisition time of 2 minutes for all four satellites multiplied by 48 times per day, your GPS module is already working a total of more than 1.5 hours a day. Divide the 1,000 hours of your AA battery by 1.5 hours of GPS duty per day and **you might get just over one month of battery life.**



![img](https://cdn-images-1.medium.com/max/800/1*3RoC_WDTcBtoJXqqHWvR6g.png)

But, alas, even those 42 days are only theoretical since this calculation doesn’t include a number of other battery-consuming factors.

**I Found It: a GPS-Enabled LoRaWAN Device …**

It advertises **10 hours** (yes, hours, not years) of battery life:



![img](https://cdn-images-1.medium.com/max/800/1*K9TmCtG2dIDN2C-qvJdVPA.png)

[**FIELD_TEST_DEVICE_LoRaWAN_868 - Adeunis RF**
*Field Test Device - Network validation, prior to your solution deployment The LoRaWAN Field Test Device by ADEUNIS RF…*www.adeunis-rf.com](http://www.adeunis-rf.com/en/products/lorawan-products/field_test_device_lorawan_868)

Yes, it’s a field testing device and not a “true” mobile endpoint. But … this is the only LoRaWAN GPS out there that I see.

Update: Found [another](http://www.globalsat.com.tw/s/2/product-199335/LoRaWAN%E2%84%A2-Compliant-GPS-Tracker-LT-100H-LT-100E.html) device with a 820 mAh battery which might last three weeks.



![img](https://cdn-images-1.medium.com/max/800/1*tYy6lFfy-WRyX3ytN_BTJg.png)

Note: GPS devices whose batteries survive three weeks have been tried before in the cellular community with [well-known](http://www.sandiegouniontribune.com/business/technology/sdut-Qualcomm-Tagg-Pet-Tracker-Private-Equity-2013jul10-story.html) results.

If I learn about more of these I will post them here. But now, come on people, LoRaWAN [wasn’t made for GPS](https://hackernoon.com/now-this-is-the-way-to-make-gps-way-better-for-lpwans-ddad647784cd) and it isn’t a networking stack for [people building serious IoT products](https://medium.com/@patburns/announcing-haystacks-lorawan-replacement-program-1a72cb4cf201).

**One IoT Technology Responds To A Geolocation Dilemma**

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

**A Bluetooth Tracker Pretends To Do LPWAN Geolocation And … Tragedy**

There’s [one LPWAN technology, LoRaWAN,](http://bit.ly/2sWkq0w) that pretends to offer real-time geolocation when for all practical purposes it does not. Still, a few of its backers promote this capability — which is at best characterized as a hack — and hope customers don’t get wise until after the implementation. [Other bloggers](https://www.linkedin.com/pulse/calling-iot-connectivity-bluff-while-crossing-chasm-james-newton) are catching on as well:



![img](https://cdn-images-1.medium.com/max/800/1*ehCow1vxduq5bB2wEzh-5w.png)

But even worse is a *short range* technology that pretends to be a wide area geolocation technology as well. [Here is a tragic case](http://www.news-journalonline.com/news/20170713/public-invited-to-help-search-for-missing-vet-harold-cantrell) of a Bluetooth tracker, advertised as having a wide area geolocation capability, failing to locate a lost Alzheimer’s patient after **17 days**. 17 days and counting. And they still can’t find him.

Lost car keys are one thing and Bluetooth is not bad for finding low value items wedged beneath your living room seat cushions. And if you want to *pretend* that you really do love your mother-in-law’s spoiled dog, give her a bluetooth tracker as a gift and then feign shock when she can’t find him when he goes missing. (OK — that wasn’t nice.) Bluetooth has its uses in the IoT.

**But marketing a short range technology like this as a wide area tracking device and allowing (or at a minimum, not warning against) its use on human beings crosses a bright line.** I don’t know the fate of this Alzheimer’s patient and hope and pray he will be found safe and sound, but folks in the Bluetooth tracking business should be paying attention.

With an average range of about 30 feet, using Bluetooth to track something — especially something very valuable — over wide areas is just usually not done. Bluetooth is a Personal Area Networking technology — as in, a FitBit or a Sonos speaker — and certainly not a Wide Area Networking technology. In my experience, the handful of people I have seen putting Bluetooth trackers on dogs or bikes do so based on utter technical naiveté, bad marketing hype, or hearsay from other uninformed users. Like “My brother-in-law told me I could use it on my dog and if she went missing the Bluetooth tracker would find her via satellite. Or via the cell phone network.”

The community finding feature that this article references what provides the makers of this Bluetooth tracker with the weak “cover” for the wide area networking claims. (There are other Bluetooth folks out there doing the same thing, last time I checked.) Unfortunately, without massive numbers of concurrent users actively invoking their tracking app, the probability of a detection is — as the 12 day delay in locating the missing patient demonstrates — very, very small.

How small?

Covering the city of Daytona Beach (where the Alzheimer’s patient went missing) requires enough active users — each with ~2,800 square feet (that’s 30 feet² x π) of Bluetooth “coverage” — to cover 65 square miles of city (1.8 billion square feet). Or **about 647,000 concurrent users just in Daytona**Beach. All distributed evenly throughout the city, all with ~30 feet of Bluetooth coverage, all with their phones turned on and the tracking app enabled. And all of this assumes the patient didn’t run off to another town nearby.

And this is made somewhat more problematic by the U.S. Census Bureau, which says **the total population of Daytona Beach is 63,000 people**.

End user confusion about how wireless technologies work is pretty rampant. High powered cellular technology is the paradigm that I have observed makes some of this possible. Misconceptions about how GPS works are even more abundant. Bluetooth radio spec sheets claim certain capabilities, often based on “best case” conditions that don’t reflect a real world environment. And in a rush to turn Bluetooth into a relevant Internet of Things technology, hacks were invented to make it sound more compelling as a tracking technology than it really is.

It is possible the Bluetooth tracking company here warned their customers against tracking humans with their product (I didn’t see it on their website …), but when you market a community finding feature replete with “success stories” of objects like lost bicycles, and then claim that the range is potentially “limitless”, people are going to take your word for it and get creative.

If you want real-time tracking over wide areas using a device that provides multi-year battery life and GPS-based location, there are more [serious technologies](http://bit.ly/2pBcYqp) out there than Bluetooth.

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

# Cloud criticism

Anchor gateways.

**Why The Internet of Things and the Cloud Should Break Up**

Some innovations are so good they make it *too* easy. Parabolic [skis](http://nyti.ms/1MhrXZ7) and [AutoTune](http://www.theverge.com/2014/7/9/5884649/untouched-britney-spears-vocal-track-no-autotune), to name just two. For the Internet of Things, it’s the cloud that is making things way too easy.

For IoT developers, the cloud is like beer in a college dorm: a cold one is around every corner you turn and … beer just becomes a constant of academic life. At least this is the way it works in America. So when an IoT developer is offered free cloud-based frameworks, databases, analytics, etc., reactions like “Hey look at all this cool cloud stuff! I think I’ll use it to build an IoT product!” is more norm than exception.

But like that one guy in your dorm who had a hard time saying no and then quietly dropped out before the end of his freshman year, IoT developers risk a similar fate if they become too dependent upon the cloud.



![img](https://cdn-images-1.medium.com/max/600/1*hbQ-aoidyiGlx8uWk2bpEw.gif)

**Admit It: The IoT Has A Problem**

In case you weren’t paying attention, the IoT and the cloud have advanced to what can only be described as a very intimate relationship. Consider:

- A Nest thermostat has a WiFi radio and is accessed via your smartphone, which also has WiFi. Yet for your smartphone to access your Nest thermostat, it does so via a long-distance internet session with a Nest [cloud](http://www.groovypost.com/howto/fix-annoying-nest-thermostat-issues-that-google-wont/) server, even though it would be faster and more reliable to connect your thermostat and smartphone on a peer-to-peer basis.
- Cloud-based IoT “developer platforms” [pop up](http://www.forbes.com/sites/janakirammsv/2015/04/13/6-iot-startups-that-make-connecting-things-to-the-cloud-a-breeze/) weekly, no doubt due to low entry barriers provided by the cloud, the extreme example being the shark-jumping [salesforce-for-iot](http://www.govtech.com/products/Salesforce-Launches-Internet-of-Things-City-Cloud.html) platform. According to one [survey](http://www.businesscloudnews.com/files/2015/07/IoT_Outlook_2015_Survey_Report_Hi_res_IBM.pdf) of 651 developers and IT professionals by IBM (not an unbiased source, but directionally consistent with my own experience), 75% were using some form of cloud-based development platform for an IoT project.
- Microsoft, [GE](http://www.informationweek.com/cloud/ge-charges-into-iot-cloud-analytics-space-/d/d-id/1322548), and others each sell “industrial cloud” platforms with the aim of enabling legions of manufacturing companies to bring the IoT to their factories and products via the cloud. Features run the full gamut from controlling and configuring endpoints to analytics.
- A FitBit wristband connects via Bluetooth with your smartphone but sends your activity data to a FitBit cloud app. Does your personal health data *really* need to sit in the cloud or can you extract sufficient value from it by simply keeping the data stored locally on your smartphone?
- Next-gen IoT computing platforms that include augmented reality already use a round trip to the cloud in order to resolve some objects discovered in an AR headset. For mobile devices engaged in real-time cognitive assistance that rely on IoT devices to help do their jobs, the cloud doesn’t exactly speed things up. You can learn more [here](http://fortune.com/2015/10/12/ptc-buys-vuforia-from-qualcomm/).

> “I really worry about everything going to the cloud. I think it’s going to be horrendous. I think there are going to be a lot of horrible problems in the next five years.”— Steve Wozniak, 2012

For most of the IT industry — let’s just get this on the table — the cloud today is the hammer and there’s almost nothing that isn’t a nail. And the cloud is an easy place to build an IoT application and operates without the messy hassles of embedded software, endpoint security, FCC regulations, or [fertility](http://www.ncbi.nlm.nih.gov/pmc/articles/PMC3778601/) risks, to name a few. And more and more, the cloud is a norm that pervades the IoT with increasing risk.



![img](https://cdn-images-1.medium.com/max/600/1*-8r2nQP9JS-_ZO_YDLGXtA.gif)

** How The Cloud Is Infecting the IoT**

The popularity of the cloud in the IoT is the result of several colliding realities:

1. **It’s cheap and everywhere.**Like beer in your dorm, the cloud today is so popular and so well-capitalized that infecting the IoT was only a matter of when, not if. Spin-offs like cloud analytics or cloud perimeter security (no laughing!) are simply too affordable and too visible to pass up. Traditional enterprise IoT pilots that used to cost $250,000 in enterprise software and systems integration services can be executed at a fraction of this price now due to the cloud.
2. **Tools.** Compared to older desktop-based tools, cloud-based environments and API’s are vastly simpler to use and integrate while offering robust functionality. [Heroku](https://www.heroku.com/), to cite just one example, is a complete but inexpensive cloud-based environment used by a number of IoT companies for deploying Ruby- or Python-based applications in the cloud and it is popular with novice and elite users alike.
3. **Weak endpoints and edges.** Endpoints that don’t do analytics, support real-time queries, or even support full two-way messaging tend to spew data remorselessly to an edge router and/or the cloud. Bluetooth, ZigBee, 6lowPAN, and others are all guilty as charged and as a result, they end up driving their users to the cloud.
4. **Cupertino.** It is hard to recall another company’s passivity stunting an industry’s growth the way Apple has for the IoT. First, Apple takes pride in a “slow follower” wireless strategy, unwittingly resulting in an IoT industry where 90% of new hardware devices rely on 1990's-era Bluetooth or WiFi just to ensure iPhone connectivity. Second, When it embraces a new wireless technology, the pace is plodding: the API for NFC remains closed, for example, preventing non-payment IoT use cases for NFC from seeing the light of day with the iPhone. Third, Apple just redefines what it means to be a great hardware company by layering cloud-based services on top of its [dominant](http://techcrunch.com/2015/02/26/apple-eating-all-the-profits/) hardware platforms, a lesson that is lost on few IoT hardware entrepreneurs.
5. **Mountain View.** This may come as a shock, but there are those who would drive your data to the cloud for purposes of finding new ways to sell you stuff. Yes, I know I am sticking my neck out here, but some companies are pushing your data to the cloud not because they have to, but because it’s profitable to do so or represents future revenue streams. It probably has the ancillary result of making some IoT products less expensive today, though, so we’ve got that going for us.



![img](https://cdn-images-1.medium.com/max/600/1*Sz337SDthl7_A4ziUO-SRw.gif)

** Why Your IoT-Cloud Relationship (Probably) Isn’t Healthy**

A few years ago, a rock-climbing buddy of mine who was in what some might call a tragically unhealthy relationship ignored warnings from me and others and got married on a whim. Well, the wedding reception was epic, and two months later (that’s 2 months) the whole thing came crashing down and he was back on the street — single again. With the IoT and the cloud, it is IT departments, not fellow rock climbers, waving red flags:

1. **It’s not secure.** This one is hard to overstate as crummy IoT security is the sordid “yeah, but” in so many discussions about the IoT. IDC [predicts](https://www.idc.com/getdoc.jsp?containerId=prUS25291514) that nearly every IT network will have an IoT security breach by the end of 2016 and IT departments are in full [freakout](http://h20195.www2.hp.com/V2/GetDocument.aspx?docname=4AA5-4759ENW&cc=us&lc=en) mode [now](http://thehill.com/blogs/congress-blog/technology/257814-internet-of-things-use-it-with-extreme-care). Endpoint security is [comically](http://bit.ly/1WQYcXC) bad and compounded with a [hacker-friendly](https://www.symantec.com/content/en/us/enterprise/media/security_response/whitepapers/insecurity-in-the-internet-of-things.pdf) cloud, what could go wrong? Maybe your company can get some free PR on [60 Minutes](http://www.cbsnews.com/news/car-hacked-on-60-minutes/).
2. **It may not be reliable.** If your IoT system relies on a cloud that you don’t own or control and the cloud fails, then what? Tracking a sales pipeline via the [cloud](http://techcrunch.com/2015/10/09/the-dog-ate-our-homework-google-drive-is-down/?ncid=tcdaily#.elat5p:I4ob) is one thing, managing [a fleet of vehicles](http://highscalability.com/blog/2015/9/21/uber-goes-unconventional-using-driver-phones-as-a-backup-dat.html), a mission-critical city power grid, or perishable flu vaccines in the cloud, that’s different.
3. **It’s not real-time.** IoT apps that require real-time responses can’t tolerate the extra seconds or minutes required for a cloud lookup. Ditto real-time analytics. The cloud = increased latency.
4. **It may not be faithful.** The integrity of your data in the cloud is only as good as the people and systems hosting it. Sensors in your manufacturing facility in Taipei showing you running at 50% below your normal run rate or showing a supply chain hiccup? Hedge funds and competitors enjoy learning about this kind thing! The cloud is the jackpot of data repositories and it’s where hackers focus.
5. **Getting out may be easier than getting in.** Once you’ve married a cloud service, how easy will it be to disengage/migrate to another solution at some future date? Is standardization and interoperability in a state that will increase the risk of vendor lock-in? What if the cloud vendor is bought by your competitor and changes policies?

> “Vendor [lock-in](http://fortune.com/2015/09/21/cio-challenge-priorities/) is a concern, it always is. Today’s leading-edge cloud companies are tomorrow’s dinosaurs.” — AstraZenica CIO David Smoley





**How To Unbundle The Cloud and the IoT**

De-clouding your IoT roadmap means substituting some or all of the cloud with … something else. So let’s start with:

**A new golden rule of IoT network design** is to store sensor data as close as possible to its point of origin and limit its sharing across the network unless absolutely necessary. This was previously not really practical with 1990’s-era endpoint technologies, but today if an endpoint can run its own analytics and other applications autonomously, what is the point of sending the data upstream at all, much less all the way to the cloud? If for no other reason, the IoT golden rule should be applied for the sake of IoT security and privacy.



![img](https://cdn-images-1.medium.com/max/1000/1*0NsEcd0YBrP-6F5tZKLmOA.png)

**The endpoint is key to the golden rule.** Better processors, cheaper memory, and better networking stacks from companies like [Haystack](http://www.haystacktechnologies.com/) are evolving endpoints from dumb terminals to independent, distributed computing devices with real-time query (think [Google](http://bit.ly/1N3MSmv) for the IoT) and NoSQL-like filesystem support. Endpoint-centric designs also have the bonus of being [more stealthy and secure](http://bit.ly/1WQYcXC), faster, cheaper, and better stewards of battery life and wireless [bandwidth](http://bit.ly/haystackiot). In short, good IoT network design should begin with the endpoint in mind and “dumb” endpoint technologies that beacon or create unnecessary [security](http://wrd.cm/1ik7UB4) risks should be phased out.

**Endpoint-centric design brings us closer to a P2P IoT.** If you envision a future with IoT devices that can operate more or less autonomously using artificial intelligence, intelligent agents, or [blockchain](http://blogs.wsj.com/cio/2015/07/27/blockchain-in-the-corporate-environment-has-big-potential-but-faces-implementation-challenges/)-based contracts, it means reducing (or eliminating) our dependence on clouds and edge gateways and allowing devices to communicate on a peer-to-peer basis to do their jobs. This could be a separate post unto itself, but here are just a few examples of P2P IoT application opportunities:

- Driverless cars and drones communicating with smart city infrastructure. You need immediate, [low latency](http://bit.ly/1LX6oNp) info about the icy bridge or railroad track you are about to cross. Waiting 2–3minutes for a cloud app to make time for you is a non-starter. Actually, any [moving thing](http://bit.ly/1LX6oNp) that communicates with a fixed thing using low power wireless needs P2P.
- Moisture sensors coordinating in a cornfield to better manage irrigation. Where water is scarce, programs residing on endpoints bid and arbitrate in order to optimize for food production.
- Access control. Second-factor authentication. The P2P IoT as an additional security layer for data centers and other computing devices.
- Supply chain networks. Chain-of-custody tracking. A nurse querying the temperature history of a carton of flu vaccine can do so without the cloud.
- [Bitcoin](https://news.bitcoin.com/programmable-economy-internet-things-bitcoin-transforming-future/). P2P payments. Autonomous, battery-powered, wireless things will bid, negotiate, and execute financial transactions based on the condition of what or who they are sensing.
- Augmented reality [wearables](http://recode.net/2015/07/30/google-glass-isnt-dead-but-its-all-about-the-enterprise-for-now/).

**Most of today’s wireless IoT technologies were not designed for P2P:**

- Bluetooth low energy is basically a one-way beaconing technology so is not P2P. It’s sister standard, Bluetooth 4.0, can “pair” with another Bluetooth 4.0 device but it’s a long, laborious process that is neither real-time nor low power and is full of security [vulnerabilities](https://blog.kaspersky.com/bluetooth-security/1637/). Bluetooth’s short range and poor signal propagation make it a poor choice for anything but the shortest range IoT projects.
- ZigBee and 6lowPAN tout “meshing” as a way for their short range technologies to daisy-chain messages to an edge gateway. This might qualify as “P2P-lite” but for private networks only since the feature is useless in public network scenarios like driverless cars or AR wearables where true P2P discovery and authentication must occur almost instantly. These technologies are also good if you are OK with hackers being able to [easily find and exploit](http://www.networkworld.com/article/2969402/microsoft-subnet/researchers-exploit-zigbee-security-flaws-that-compromise-security-of-smart-homes.html) their endpoints.
- WiFi supports mesh networking as well and [recently](http://siliconangle.com/blog/2015/07/14/wi-fi-alliance-rolls-out-p2p-standard-for-the-internet-of-things/) announced plans for better P2P support, though its [woeful security](http://bit.ly/1WQYcXC) and high power consumption make it rarer and rarer in IoT deployments. WiFi, too, suffers from molasses-like discovery and authentication which is a non-starter for most IoT networks, especially public ones. I do not expect WiFi to find its way into serious P2P IoT discussions despite its ubiquity on smartphones.
- Newer wireless IoT technologies like [DASH7](http://haystacktechnologies.com/products-and-services/what-is-dash7/) were built directly for P2P and provide “instant-on” connections in public and private IoT networks. The technology is still young, but it gets P2P more right than any other low power wireless IoT technology. DASH7 does not currently support meshing (it supports 2-hop, which is typically more than sufficient) but since it uses [longer range](http://bit.ly/haystackiot) physical layer technologies, meshing is almost always unnecessary.

> “Quite a lot of this content won’t be sent over the network to be processed by the ‘enterprise-based’ cloud infrastructure. Rather, you will need cloud computing-like processing at the edge … Quite simply, this is a big deal.” — Vernon Turner, SVP @ [IDC](http://www.eweek.com/networking/fog-computing-aims-to-reduce-processing-burden-of-cloud-systems.html).



![img](https://cdn-images-1.medium.com/max/800/1*LE5-XCulhpSham923XeEMQ.png)

**When endpoints are not enough, then add the edge.** For processes that can’t logically reside entirely at the endpoint, the edge gateway (or edge router or server) is their next logical home in the network. An edge gateway can interact with endpoints, host applications like [analytics](http://www.networkworld.com/article/2996086/internet-of-things/cisco-acquires-iot-analytics-company.html), store data, manage security, and more. There are no rules about the size or capabilities of edge gateways — they can be very simple or very large computing devices or may be a component of a much larger computing device. But the essential point in all of this is that the edge gateway is controlled and maintained locally and not in the cloud and not by a third party.

**Think of the edge as a “**[**cloudlet**](https://en.wikipedia.org/wiki/Cloudlet)**”.** Smart cloud vendors will help customers bring cloud functionality to their edge devices as functionality that is usually delegated to the cloud can often be executed at the edge gateway. Gateway hardware is cheap and powerful, and much of what resides in the cloud can be placed at the edge for an increasingly ridiculous low price. Cisco, IBM, and a few others are trying to make “[fog computing](http://www.wsj.com/articles/SB10001424052702304908304579566662320279406)” a trendy term and … this is all for the better. And for those legacy firms doing yoga moves to transition into this cloud thing, it’s possible that your product lines can more easily make a more successful and shorter leap to the edge/fog.

**The “Intranet of Things” is already here.** Remember that the IoT is not new. Barcode and RFID networks have used fog computing for decades and hundreds of building automation, defense, manufacturing, and other types of local IoT networks existed before the cloud became a trend.

**Special reminder to** [**cloud people**](http://sv6.imageupload.be/wp-content/uploads/2012/07/Partly-Cloudy.jpg) **reading this with clenched teeth:**helping your customers to keep more of their data at the edge of their network is a *good* thing for you. If you keep what belongs in the cloud in the cloud (e.g. global network analytics) and what belongs at the edge at the edge, your customers (and their CSO’s and PR people) will thank you for it. Some of you already market “private clouds” or “hybrid clouds”, so marketing “local clouds” may be easier than you think. And keep in mind that [40%](https://www.idc.com/getdoc.jsp?containerId=prUS25291514) of all IoT data is predicted to be “stored, processed, analyzed, and acted upon close to, or at the edge, of the network,” by 2018 according to IDC.



![img](https://cdn-images-1.medium.com/max/800/1*P8AzYL3vE05AVXgtrAQnrA.png)

**When the edge is still not enough, it’s OK to look to the cloud.** The cloud has a role to play in the IoT, and where processes cannot be practically executed at the endpoint or the edge, the cloud may be the only reasonable choice. Batching data from gateways around the world for non-real time, non-mission critical analysis is one example of a “smart” cloud+IoT process. Controlling, configuring, and querying endpoints via a cloud-based application is not, however.

**Pilot in the cloud, deploy in the fog.** The cloud is a fast and affordable way to prototype, demonstrate, and pilot, but it is the IoT’s [Faustian bargain](https://en.wikipedia.org/wiki/Deal_with_the_Devil). For projects requiring scale, it’s a good idea, again, to default to the endpoint and/or the edge gateway and then ask how the cloud can complement them, not vice-versa.

**If you deploy in the cloud, have a Plan B.** If the temptation to deploy in the cloud is too great, at least be able to articulate how the system will function in the case of a cloud outage, hack, or other “unforeseen” event. At a minimum, a Plan B lays the groundwork for a future phase you may need in order to reduce your IoT system’s exposure to the cloud. You know, the phase that happens after your cloud IoT system is hacked and your board of directors asks “so now what?”.

** So Now What?**

The cloud is a useful tool for jump-starting IoT initiatives and has an important role to play in non-real time analytics. But it is inevitable — if only for the sake of security — that the IoT as an industry will go through a kind of cloud “detox” that results in a healthier and more resilient IoT where the cloud is deployed with eyes wide open to the accompanying risks. If your organization is talking about designing an IoT network and you are hearing or seeing the word “cloud”, it’s worth raising your hand and asking questions like “Is there a good reason not to execute this (insert process/feature) at the edge, rather that in the cloud?” or “Are we able to deploy stealthy endpoints that don’t over-share data?”

The momentum behind the cloud is strong and some of you may encounter resistance to arguments for pushing IoT functionality to the edge. If so, you can always take comfort in the fact that endpoints are only increasing in functionality, security “accidents” in the cloud will only become more numerous and more lethal, and that in the history of computing, the arc of history [clearly](http://www.techspot.com/article/874-history-of-the-personal-computer/) supports the inevitability of more autonomous IoT endpoints.

# IoMT

**Why Movement is Important to the IoT**

An Internet of Moving Things is at its core a network of physical objects that are mobile or moveable and can be wirelessly measured or controlled. Amazingly, the designers of today’s IoT gave little or no thought to connecting things that move and today we are stuck with wireless IoT technologies that require a lengthy pairing ritual that renders them nearly useless for connecting with a moving thing. **Yet solving for moving things is of critical importance to the future of the IoT because:**

1. **Things move!** An IoT that cannot measure or control things that move or things that are moving is an IoT that … is an Internet of Only Some Of The Things. It’s like the internet without SMTP email.
2. **Movement = news.** When a thing moves, it is often an important or “newsworthy” event. For example, sensing movement on your parked bicycle might be an indication that it is being stolen.
3. **Location.** Moving things often change geographic location. The question “Where is it?” is asked every day by billions of people about everything from car keys to shovels to humvees. DoD spends millions of hours every year just [looking](https://www.washingtonpost.com/world/national-security/pentagon-loses-sight-of-500-million-in-counterterrorism-aid-given-to-yemen/2015/03/17/f4ca25ce-cbf9-11e4-8a46-b1dc9be5a8ff_story.html) for stuff like humvees, fyi.
4. **Cause and Effect.** When things move, it’s often caused by or associated with someone or something else. “Movers”, as Aristotle might say, are highly relevant to the big data questions being asked every day. “Who was the last guy to use this broken chainsaw?” or “Which truck carried these frozen vials of flu vaccine?”
5. **Absence.** Conversely, an absence of movement can itself be meaningful. A cow on a ranch or a stay-at-home senior that does not move for 24 hours might be injured or sick.
6. **Battery life.** Movement can be an important power saving tool for managing sleep/wake cycles battery-powered devices. A mobile device that doesn’t move might sleep more than one constantly on the move.
7. **Movement changes risk.** A moving thing may set in motion other events — or at least the potential for other events to occur. A moving car or bicycle or fighter jet is far more likely to crash or experience mechanical failure than one that is parked.

**Moving Things Are Already Making Today’s IoT Obsolete**

While the mobile internet is expected to be [10x the size](http://techcrunch.com/gallery/mary-meeker-internet-trends/slide/7/) of the desktop internet, the forecasts seem not to have affected most of the folks working on the IoT.



![img](https://cdn-images-1.medium.com/max/600/1*0U4B0cIC6AZeLcZ9rQxb2A.jpeg)

For example, drones are forecasted to be a [multi-billion dollar](http://for.tn/1FoMw8S) industry unto themselves and are already showing their potential as “IoT gateways in the sky” for everything from monitoring [oil pipelines](http://www.fastcompany.com/3031725/fast-feed/oil-giant-bp-is-first-company-approved-to-use-commercial-drones) to moisture content on [farmland](http://ww2.kqed.org/science/2014/04/21/drones-the-newest-water-saving-tool-for-parched-farms/). But the go-to wireless technologies for today’s drones are … wait for it … WiFi and Bluetooth, which can’t communicate with terrestrial-based sensors while moving because they were designed 20+ years ago when CompuServe was still hot.

Along with Bluetooth, ZigBee, Thread, and others, WiFi radios perform an elaborate mating ritual when they connect to a new endpoint. If you’ve ever logged onto a new WiFi access point and it took many seconds or even minutes, it’s because there’s an outdated and obsolete sequence of discovery, handshaking, authentication, payload delivery, and more. As a result, **to connect with any of these, you must remain still — completely still, usually — in order to establish a connection.**

For local area networks like your house where endpoints and access points are mostly fixed, this is probably not an issue. **But for things that move at speeds of 5 mph or more, requiring endpoints to stop whatever they are doing and remain still while a wireless technology “locks on” is simply a non-starter.**

*Note to cellular people reading this: you can drive a drone from afar using cellular, but expecting the rest of the IoT to deploy high-cost and high-powered cellular at the endpoint is fantasy apart from some niche use cases where cost and battery life are not important.*

**A Fast Moving World Needs an IoT That Can Keep Up**

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

**Four Killer Apps for the Internet Of Moving Things**

I meet many developers with cool IoT ideas and here are a few that I consider to be killer apps for an Internet of Moving Things:



![img](https://cdn-images-1.medium.com/max/600/1*JIxD50o4TJYsEuNqTJcUEw.jpeg)

**Driverless cars.** To be successful, driverless cars are going to need help from wireless IoT technologies to solve some [big, unsolved vehicle-to-infrastructure problems](http://www.technologyreview.com/news/530276/hidden-obstacles-for-googles-self-driving-cars/)including detecting icy bridges, pedestrians, potholes, uncovered manholes, operating in snow and rain, or maneuvering around construction road crews. Interfacing securely and in real-time with other moving or parked cars more than a few feet away is an unsolved problem as well as communicating with “smart city” and other battery-powered fixed infrastructure like smart street signs or bridge stress sensors. Solving for V2I (and vehicle-to-pedestrian, “V2P”) is fundamentally a low power IoT problem (most V2I situations will not include access to mains power sources) and while the auto industry’s current dalliance with WiFi may make for some nice demos, it won’t solve for V2I or V2P in any secure, private, safe, or scalable way.



![img](https://cdn-images-1.medium.com/max/600/1*yaGi1DD_bwFSAKMHJOkYNA.jpeg)

**Agriculture Drones.** Some of the most exciting drone apps focus on the agricultural sector where drones not only provide high-resolution imagery and infrared sensing, but also an “IoT gateway in the sky” capturing data from animals, water troughs, tools and equipment in the field, and more. The opportunity extends just as easily to other industries where drones are becoming popular like oil and gas, mining, construction, and defense.



![img](https://cdn-images-1.medium.com/max/600/1*E5g8qNqxH9ls7Yu6Y0O7Rg.jpeg)

**Search and Rescue.** Locating missing firefighters or hikers in a forest, shipwreck survivors, lost dogs, and more via moving vehicles like drones or cars. The “eyeball” method for these use cases is now officially obsolete and fast moving vehicles need a wireless technology that can locate things in hard to reach, hard to see places.



![img](https://cdn-images-1.medium.com/max/600/1*kZ50ELsU1KXsoqy1tuAtBA.jpeg)

**E-commerce.** A killer mobile IoT opportunity — perhaps with a longer time horizon? — is in the area of e-commerce, where everything from the handbag carried by a woman walking her dog to passing buses will effectively become a query-able, wireless IoT endpoint. Soon, we will be able to learn the make and model of a cool mountain bike as it passes by or capture a promo code as we pass a billboard on a highway.

**How To Get The IoT Moving**



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

**Preparing Your Company For The Internet of Moving Things**

If your company is throwing elbows and punches inside the mosh pit of home automation, perhaps the Internet of Moving Things is not your biggest priority. However if your company is investing in smart cities, driverless cars, drones, wearables, or any of the other industries mentioned above, you should be taking note of the shortcomings of the most common wireless IoT technologies in the marketplace as it relates to movement. In some cases it may be possible to demand incumbents update their technologies to better support movement, in other cases the right decision will be to start afresh. My company, [Haystack](http://www.haystacktechnologies.com/), is one of the few in the IoT marketplace that designed its IoT networking stack (based on [DASH7](http://haystacktechnologies.com/products-and-services/what-is-dash7-2/)) with the Internet of Moving Things in mind from the beginning.

But one thing is certain: a failure to address movement will bode poorly not ony for the IoT, but for many new innovations, including many we haven’t even imagined, that will depend on an IoT that can adequately communicate with things that move. The same way that “unforeseen” companies like Uber took advantage of foundational breakthroughs like smartphones, Google Maps, and low cost GPS chipsets, similar companies will be built around an IoT that properly addresses movement.


# Security

**How You Can Prevent An IoT Security Nightmare**

*Adding a “secret” connection to your IoT device will make a difference*

Today we published what is probably one of our most important presentations. The topic is IoT security and we break some important new ground while offering something that almost everyone in the IoT space should find useful.

Two-factor authentication is common in e-commerce today — if you try logging into your bank’s website from a new computer, you are usually asked to prove you are who you are via a userid and password, but also via a second authentication credential that is sent to me via SMS text or email.



![img](https://cdn-images-1.medium.com/max/800/1*3S47y45QtRa_RSWsNQtP2A.png)

The core thesis of our presentation is that there is an opportunity to outfit wireless IoT endpoints with a *second* wireless link whose primary job is to support two-factor authentication.



![img](https://cdn-images-1.medium.com/max/600/1*H9iFYCxCQQEac8arNUODzA.png)

I have written on IoT security [before](http://bit.ly/1WQYcXC), focusing on the benefits of listen-before-talk and the idea that endpoints shouldn’t talk more than necessary for a whole list of reasons. But combining this with a back channel for endpoints provides for unique opportunities to secure the endpoint and to make them more efficient. We think back channels are of immediate benefit to WiFi endpoints like IP cameras, but there is no practical limitation of where you can deploy a back channel given the range/signal propagation of LPWAN technologies.

If you design or sell endpoints that are likely to be vulnerable to hacking (this is basically everyone today), a back channel could make a huge difference in your security story but could make your IoT story vastly more compelling.

If you work in IoT or follow the news, IoT security is a huge challenge. Last fall, the Mirai botnet attack took down the internet in parts of the US and it only used ~100,000 hijacked cameras, DVR’s, and routers. It’s safe to say there are other botnet armies lying in wait out there, perhaps much larger than what we saw last fall, along with scads of other security and privacy problems that the IoT has not tackled. Some of this is due to crummy ways wireless IoT protocols (not Haystack’s) were engineered, and some is just plain human screw-ups. But scanning the news while building this presentation, to me it’s clear that adding two-factor authentication to the IoT is a big step towards responsibly addressing what is today an IoT security quagmire.




**A Simple Proposal To Improve Security for the Internet of Things.**

**A small change can help stop big hackers.**

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

**Why Stealthy IoT Endpoint Design Matters**

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

**Principles of Stealthy IoT Endpoint Design**

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

**How We Can Bring Stealth to the IoT … Now**

If security is such a big deal for the IoT — and there are [more than a few](http://www.networkworld.com/article/2921004/internet-of-things/beware-the-ticking-internet-of-things-security-time-bomb.html)[experts](http://www.zdnet.com/article/internet-of-things-you-have-even-worse-security-problems/) who think it is — then we should be taking steps now towards implementing stealthier endpoints.

- **Rethink roadmaps.** First, and most importantly, established vendors should re-think wireless protocol design roadmaps and incorporate full stack stealth at least as a matter of corporate responsibility, if not for revenue opportunities. The kind of shareholder and brand fallout experienced in recent [payment card](http://www.bloomberg.com/bw/articles/2014-03-13/target-missed-alarms-in-epic-hack-of-credit-card-data) and [email](http://www.thewrap.com/11-revelations-from-wikileaks-sony-hack-emails-amy-pascals-travel-expenses-david-fincher-complains-of-leak/) hacks is sure to reach the Internet of Things soon, so responsible CXO’s and boards are asking whether IoT roadmaps include full stack stealth. There is also little reason why standards bodies like the ZigBee Alliance, the [Thread](http://threadgroup.org/) Group, and others who profess to care about IoT security cannot add stealth as a requirement for their next iterations of their stacks.
- **New ventures may already have the answer.** The huge number of new IoT ventures being created every month reflects the scale and scope of the opportunity. Companies like the one I co-founded, [Haystack](http://www.haystacktechnologies.com/), are bringing new stealth-based IoT technologies like [DASH7](http://haystacktechnologies.com/products-and-services/what-is-dash7/) to the marketplace and others may follow, but LBT and event-driven messaging is at the core of what we designed at Haystack.
- **Borrow & Mix.** A combination of the first two may provide the industry with an interim solution. Melding new technologies and standards [on top of existing standards](https://medium.com/@patburns/5-reasons-the-iphone-6-will-save-the-internet-of-things-7ac8b96fbd5) may provide a way of staunching some of the bleeding.



![img](https://cdn-images-1.medium.com/max/600/1*haw2_8dv6Eszb2SXIEOVfA.jpeg)

“We believe that by adopting the best practices we’ve laid out, businesses will be better able to provide consumers the protections they want and allow the benefits of the Internet of Things to be fully realized.” — FTC’s Edith Ramirez

- **Regulatory pressure.** Short of industry moving to stealthier connectivity for business reasons, we will likely see external drivers of stealth, too. The prospect of [government regulation](http://www.usatoday.com/story/news/politics/2015/02/09/internet-of-things-house-caucus-senate-hearing/22927075/) of the IoT is a [growing threat](http://www.rt.com/usa/227111-ftc-internet-things-risks/) now in Washington as the IoT is seen as rife with risks to consumer privacy and [homeland security](http://www.nextgov.com/cybersecurity/2014/11/report-government-has-only-5-years-secure-internet-things/99446/).

# Real-time

**Real-Time Is A Must-Have for the IoT**

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

**Beyond Real-Time Networking**

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

**Today’s Wireless Is Killing the IoT**

To pinpoint the origins of the data tsunami, go to the source: the wireless IoT endpoint. Wireless endpoints are essentially a computer chip, a **radio**, an antenna, one or more sensors, some memory, and a power supply. Endpoints can be very tiny or quite large and can be standalone or integrated with other devices, but all share these basic attributes. **The purpose of an endpoint is simple: to sense its environment and report to the network as programmed.**

The radio in an endpoint can employ one of a number of low power wireless communications protocols yet most protocols were created to be a sort of WiFi-lite. As a result, nearly all are oriented around pushing data (remember [Pointcast](http://askville.amazon.com/happened-Pointcast-push-technology-general/AnswerViewer.do?requestId=7037556)?) — to the network rather than endpoints standing by for intelligent queries to pull data, a la Google Search.

> **“Not only has the demand for capacity on our wireless networks been accelerating significantly, but it’s been accelerating in a non-scalable way,” says Charles Golvin, analyst @** [**Forrester Research**](http://www.forrester.com/rb/research/)**.**

Unfortunately, as the data tsunami is upon us, technologies like [Bluetooth](https://en.wikipedia.org/wiki/Bluetooth), [6lowPAN](https://en.wikipedia.org/wiki/6LoWPAN), [ZigBee](https://en.wikipedia.org/wiki/ZigBee) and others are utterly unfit to the task of the next phase of the IoT.

**Where The Tsunami Is Happening**

![img](https://cdn-images-1.medium.com/max/800/1*xjB7g0GluWNb7i2tR8-71Q.jpeg)

**“IoT threatens to generate massive amounts of input data from sources that are globally distributed. Transferring the entirety of that data to a single location for processing will not be technically and economically viable.” — Joe Skorupa, VP Distinguished Analyst @ Gartner**

# Google-like IoT search

That none of today’s protocols seriously contemplated a Google-like future for the IoT is astonishing. Searching in real-time for objects in the Internet of Things using simple or complex queries — and thereby pushing the maximum amount of data cleansing and analysis to the edge of the network — didn’t make anyone’s priority list 10–20 years ago?

**The IoT Needs A Google**

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

**How To Add A Google To the IoT**

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

**How The IoT Was Blindsided**

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

**Today’s IoT Is Pretty Damn Noisy**

# Future

If we look ahead to the things smartphones will do for us in the future but can’t do today, the IoT figures prominently in the discussion.

**For IoT unit sales to even approach analyst** [**forecasts**](http://www.idc.com/getdoc.jsp?containerId=prUS24903114) **requires a next generation IoT connectivity option that resides in a smartphone, is not named Bluetooth nor WiFi, and can connect to IoT hardware nodes directly via a smartphone without a hub.**

What does this next generation option look like? For starters:

- It should be **effortless to set-up and use**
- It should consume **minuscule amounts of power**
- It offers much **longer communications range**
- It is **very low cost**

If you agree that to ship the next 10 billion IoT devices there has to be a better way to connect IoT hardware endpoints, then keep reading.

**Why The Internet of Things Is Going Nowhere**

The next phase of the IoT is stuck unless we replace crummy outdated technology

# LoRaWAN to Haystack

**Announcing Haystack’s LoRaWAN Replacement Program**

We are excited to announce the availability of the Haystack Software Developer Toolkit for Semtech’s [LoRa®](https://www.globenewswire.com/Tracker?data=udBXzEs0D_wRfZA_4U8t8qpgv3tg2yC3PkzMj3JXDDe1_6FXbNR4to8i4-UC5nD7kNav90ZJyDJbt0oMmJzKGSwUecxd3Z9aVdBd161dwnUvcEpgOA2QJqGBmjN3WBBZaw8LukpG34aFKBCNJNC2cg==) wireless IoT platform.

First, let me emphasize that *we like LoRa.* We believe LPWAN technologies operating in unlicensed radio spectrum will eventually dominate the enterprise and industrial IoT arena and for now, Semtech is running at the front of the pack with LoRa. *(Note to IoT analysts: enterprise and industrial are where those extra commas in your IoT forecasts come from.)*

Despite LoRa’s front-runner status, some LoRa networking freeware called LoRaWAN is still alive. LoRaWAN is basically a one-way, barebones networking stack that enables tags to upload small bits of data to the cloud. It’s not secure, it doesn’t work in real-time, it’s expensive to maintain, and you can’t really send commands to a LoRa endpoint with it. Still, a few companies you’ve heard of appear to be trying it despite the risks.

So we are here to help. Haystack’s SDK for LoRa solves for those risks while providing additional features that are unmatched by anyone in the industry. Including:

- **Total compatibility and co-existence with LoRaWAN**
- **Complete bi-directional communications vs. LoRaWAN one-way**
- **Real-time indoor location with up to one meter precision**
- **Over-the-air firmware updates for easier maintenance and better security**
- **Real-time endpoint queries and commands**
- **50% greater range vs. LoRaWAN**
- **200% greater system density vs. LoRaWAN**

So to sum things up, with Haystack your LoRa solution has much better range, costs less, is more secure, can do high-precision indoor location, and can still work with “legacy” LoRaWAN gateways.

**Security**

We believe Haystack’s security story is unmatched among low power IoT networking stacks. Haystack enables two-factor authentication, an encyrpted MAC address, listen-before-talk operations, AES/CCM 128-bit crypto, and methods for public key exchanges. We have not solved everything about IoT security, but we don’t think anyone has come this far.

Anyone contemplating a LoRaWAN implementation is exposed to serious security risks.

UPDATE: More LoRaWAN security risks <http://bit.ly/2Lorasec>

**The SDK**

The Haystack SDK for LoRa includes:

1. Haystack OpenTag firmware for LoRa
2. LoRaWAN integration (optional)
3. Haystack sample apps for LoRa, including:

- indoor location example, using node-to-node multilateration with seamless LoRaWAN integration
- ultra-low-power wireless TTY example
- ultra-low-power bulk data transfer

**Availability**

The Haystack SDK for LoRa is available today to Haystack subscribers. For all subscription details, [click here](http://haystacktechnologies.com/products-services/#products_TechnologyLicensing).

**Resources**

For more information on LoRa technology, visit [Semtech’s site](http://bit.ly/semtechlora).

For a comparison between Haystack and LoRaWAN:

For more on Haystack security capabilities, [click here](http://bit.ly/iotkillswitch).

*Our media contact is Jennifer Skorlich (650) 302–1716 or media@haystacktechnologies.com*

# NFC

**Hiding In Plain Sight: Game-Changing Plumbing for the IoT**

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

**DASH7 Advertising Protocol Basics**

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

[https://www.slideshare.net/haystacktech/how-to-disrupt-the-internet-of-things-with-unified-networking](https://www.slideshare.net/haystacktech/how-to-disrupt-the-internet-of-things-with-unified-networking)

[https://hackernoon.com/looks-like-more-forking-going-on-in-the-iot-946a7220e967](https://hackernoon.com/looks-like-more-forking-going-on-in-the-iot-946a7220e967)

[https://medium.com/@patburns/5-reasons-the-iphone-6-will-save-the-internet-of-things-7ac8b96fbd5](https://medium.com/@patburns/5-reasons-the-iphone-6-will-save-the-internet-of-things-7ac8b96fbd5)

https://medium.com/iotforall/why-you-can-t-google-the-internet-of-things-1f1207212a75

https://medium.com/the-startup-magazine-collection/a-simple-proposal-to-improve-security-for-the-internet-of-things-4fcc0663f70e

[https://medium.com/@patburns/how-to-solve-for-geofencing-in-the-low-power-iot-94567de29eaf](https://medium.com/@patburns/how-to-solve-for-geofencing-in-the-low-power-iot-94567de29eaf)

