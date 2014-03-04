-- Advanced Computer Networks
-- Assignment 1: Network Principles
-- March 6th 2014

Assumptions
=============
In all exercise where nothing else is mentioned I assume that TCP is used for transmission, that transmission happens without loss, and that there is no processing delay in any hubs. Further more, the overhead of packet headers is not included, i.e. in calculating the time it takes to transfer a 10MB file, I will assume that only 10 MB are transferred.

Question 1
============
The bandwidth-delay product (BDP) is defined to be $BDP = bandwidth \cdot latency$. The BDP is important because it tells us how much data can be 'in flight', or 'stored', in a link at any given time. In case we're using TCP, the BPD tells us the 'throughput' of a link, measured in bits per RTT.

A high BDP, in the case of TCP, means that the sender needs to have big buffers to store the data he is sending, because he should be ready to send it again in case the receiver doesn't acknowledge having received the data. On a link where the BDP 1GB, i.e. there can be 1GB of data 'in flight', the sender needs to have a buffer of 1GB, since any of this data might need to be retransmitted.

From the equation we see that high/medium bandwidth and/or latency can lead to a high BDP. Examples of such systems are: interdatacenter communication (high bandwidth, medium latency), communication with spacecrafts (low/medium bandwidth, high latency), and intercontinental communication (high bandwidth, medium/high latency).


Question 2
============

Speed of light: $3*10^8 m/s \Rightarrow 3*10^5 km/s$

a)
----
\begin{align*}
    \text{Minimum RTT is: } & 2\cdot latency \Rightarrow\\
                            &2\cdot \frac{\text{distance}}{\text{speed}} \Rightarrow \\
                            &2\cdot \frac{385000\ km}{300000\ km/s} = 2.567\ seconds
\end{align*}

b)
----

\begin{align*}
    BDP &= bandwidth \cdot latency \Rightarrow\\
    BDP &= 100\ Mb/s \cdot \frac{2.567}{2}\ s = 128.35\ Mb = 16.04\ MB
\end{align*}

c)
----
Assuming that TCP is used and that a connection is already established, we need to wait one latency for the first packet to arrive at the receiver and one latency for the last acknowledgment to arrive at the sender. I will also assume that the transfer rate is constant
\begin{align*}
    Transmission time &= RTT + Time to transfer file
    Transmission time &= 2.567 + \frac{25 \cdot 8\ Mb}{100\ Mb/s} = 4.567
\end{align*}

Had it been the case that a TCP connection had not been established, we would need to add another RTT to the result since we would have perform the initial three way handshake, sending our first packet of data with the senders `ACK`. If the sender further wanted to close the connection afterwards, he would also have to wait a latency in the end, waiting for the receivers `ACK-FIN` packet.

Question 3
============

a)
----

$BDP = \frac{1\ Gb/s \cdot 0.05\ s}{8} = 51.2\ MB$

A receive window of 1 MB implies that the sender can send no more than 1 MB per RTT. Since the BDP is greater than 1MB, we know that the receive window is the limiting factor of these two.

We also need to account for TCP's slow start algorithm. This means that slow start will be the limiting factor until $n \ge 10$.

So the total number of RTTs $n$ to send a 10 MB file can be calculated as follows:

\begin{align*}
    \{n\ |\ \sum_{i=1}^{n}{min(2^{i-1} \cdot 1\ KB, 1\ MB)} \ge 10 * 1024^2\ bytes\}
\end{align*}

We see that $n = 20$ satisfies this formula, giving us a total number of 20 RTTs in which we could transfer a maximum of 10.999 MB.

I want to note here that this is only correct given the assumption of no losses, since a loss would mean that the slow start algorithm would need to back off and start from 1KB again, up until the `ssthresh` where it would increase linearly instead of exponentially.

Also, this result assumes that a TCP connection has already been established.

b)
----

Transmission time: $20\ RTT \cdot 0.1\ s = 2\ s$

Throughput: $\frac{10\ MB}{2\ s} \cdot 8 = 40\ Mb/s$

c)
----
We can pretty easily figure out how much we need to increase the receive window by in order not to have it be the limiting factor. We know that TCP's slow start algorithm doubles the congestion window every RTT (given there are no losses) which means that in order to not have the receive window be the limiting factor, we just need to make it at least $\frac{10 MB}{2} = 5 MB$. This works because, if slow start $\le$ 5 MB then slow start will be the limiting factor, and if slow start $\ge 5 MB$ then the receive window will technically be the limiting factor, but since the file is only 10 MB big it will not matter.

Question 4
============

a)
----
$1920 \cdot 1080 = 2073600$ pixels per frame

$2073600 \cdot 24 = 49766400$ bits per frame

$49766400 \cdot 30 = 1492992000 b/s = 1.39\ Gb/s$

b)
----
$8\ b \cdot 8000\ Hz = 64000\ b/s = 62.5\ Kb/s$


c)
----
$260\ b \cdot 50\ Hz = 13000\ b/s = 12.7\ Kb/s$

d)
----
Assuming that we represent a black/white pixel with 1 bit:

$8$ inches $\cdot 10$ inches $= 80$ square inches

$80\ \cdot 72$ pixels/square inch $= 5760\ b = 5.625\ b$

Transmitting 5.625 Kb on 14.4 Kb/s takes: $\frac{5.625}{14.4} = 0.39$ seconds

Question 5
============

a)
----
Since there is no segmentation and we're using store and forward packet switching, the first switch can't forward the message before it has received the **full** message.

The message size is $\frac{7.5*10^6\ b}{1024^2} = 7.15\ Mb$

Which means that it will take $\frac{7.15\ Mb}{1.5\ Mb/s} = 4.77$ seconds to forward the message to the first switch.

Since there are three links between source and destination, on which no data will be sent in parallel because we have no segmentation and we're using a store and forward policy, the total time to send the message from source to destination is $3 * 4.77 = 14.31$ seconds.

b)
----
Assuming that segmentation of the packets adds a 5% overhead because of headers, (which means that we actually need to send 5249 packets instead of 5000), the time it takes for the full message to traverse one link increases slightly from question 5 a). The total amount of data to be transferred increases to $7.15 \cdot 1.05 = 7.5075\ Mb$. Using segmentation it therefore takes $\frac{7.5075\ Mb}{1.5\ Mb/s} = 5.005$ seconds to forward the full message to the first switch.

c)
----
In this case, unlike in question 5 a), data can be transmitted in parallel: as soon as the first packet has arrived at the first switch, the first switch can forward it to the second switch _while the source is sending the next packet_. Since we have three hops, most of the packets will be sent in parallel until the source has sent all of its' 5249 packets, at which point the source has to wait for the last packet to propagate to the destination. This makes the total transfer time:
\begin{align*}
    \text{transfer time} &= \text{time per packet} \cdot (\text{number of packets} + \text{number of links} - 1).\\
                         &= \frac{1500/1024^2\ Mb}{1.5\ Mb/s}\cdot (5249 + 3 - 1) = 5.008\ \text{seconds}.
\end{align*}

We see that the time it takes to send a message across many hops decreases drastically when using segmentation. It took almost three times as long to transfer 7.15 Mb data without segmentation, compared to transferring 7.5075 Mb data with segmentation. This is due to the fact that packets are transferred in parallel when we have more than one packet.

d)
----
From what we've just seen it is clear that segmentation adds some overhead in the form of headers, which means that we have more data to transfer. When we have just one link, i.e. a point-to-point connection, there is no benefit of using segmentation (assuming no loss on the link).

Disadvantages of using segmentation:
\begin{itemize}
    \item Packets have to be ordered at the destination
    \item Headers are added to all packets. In the case of small payload, the size of the headers might be bigger than the payload.
\end{itemize}

Advantages of using segmentation:
\begin{itemize}
    \item Parallel transfer of data between hops
    \item Packets can take different paths through the network
    \item Smaller messages to retransmit in case of loss
\end{itemize}


Question 6
============
Saltzer observes that there is a difference in the use and meaning of the word ''name''. He observes that it can be used both to describe the name of a service, mostly used by humans, and to describe the name of a network component (node, attachment point, path), mostly used by machines in order to route data. One component might even have multiple names; for instance, he writes, it might ''...have both a hierarchical character string name and a unique binary identifier.''

Furthermore, Saltzer observes that naming isn't inherently difficult or confusing. He notes that names ''... can simply and concisely be described in terms of bindings and changes of bindings ...'' What I understand from this statement is that naming of network objects is much less complicated and less ambiguous when you consider context to be a part of a component's name.

<!-- A service (human readable) is attached to a node (machine readable)
A node is attached to an attachment point. In the context of routing both should probably be machine readable. In the context of talking about the particular machine between humans, the name should probably be human readable.
 -->


Question 7
============
a)
----
This restriction is imposed because it makes routing much simpler; each node only has to care about only one level of indirection, and not about multiple (theoretically up to n-1) levels of indirection. This allows for a somewhat aggressive collection of information (through probing) about the links between nodes in the RON. Furthermore, the data in the RON paper shows that in 98% of the time where the RON is used, one level of indirection gives a faster latency than multiple levels.

One disadvantage is that, in some cases, routing along more than two hops could yield a better route (reachability, or even better latency).

b)
----
1) It would greatly improve the efficiency of RONs if the underlying network could inform a node about failed links. This way, each node wouldn't have to infer this from unexpectedly low bandwidth or high loss, which would make the decision to route differently much easier and quicker to make.

2) If the underlying network were to accept route preferences from nodes, e.g. go to S via T, the RON could be used solely to find such preferences instead of also doing routing, leaving routing as the responsibility of the network. This would also to a higher degree conform with the layering of the Internet, where routing is the responsibility of the network.