% Advanced Computer Networks
% Assignment 5: Mobility
% Michael Bang, April 3rd 2014

Question 1
============
The reason this doesn't work for ad-hoc networks is that there is no intermediary node (the master) to buffer packets; each node has to send packets directly to each other. What is done instead, is that the nodes themselves are responsible for synchronizing their timers (and do so in a 'greedy', distributed fashion), for buffering their packets and for announcing to other nodes that they have packets for them. This is done during the ATIM (ad-hoc traffic indication map) period, in what closely resembles the contention period of the (reservation-)ALOHA protocol. Nodes that weren't mentioned during the ATIM period can sleep until the next time they synchronize their time (send a beacon).


Question 2
============
Because there is a limit to the amount of users using the same frequency within one cell. By creating small cells, the network providers can reuse the same frequencies frequently (the cells that use the same frequencies just shouldn't be in too close proximity), allowing them to serve more customers. It also conserves the battery of the mobile stations, because it allows them to transmit with less power.


Question 3
============
a)
----
\begin{align*}
    S &= 960\\
    N &= 4\\
    M &= \frac{2000}{4\cdot 6} = 84\ \text{clusters}\\
    C &= M\cdot S = 84 \cdot 960 = 80640
\end{align*}


b)
----
We repeat the calculations from a), but for $N = 7$.
\begin{align*}
    N &= 7\\
    M &= \frac{2000}{7\cdot 6} = 47\ \text{clusters}\\
    C &= M\cdot S = 48 \cdot 960 = 46080
\end{align*}

c)
----
$\frac{2000}{4\cdot 6} = 84$ times.

d)
----
Assuming that we make sure that the channels don't overlap when we decrease $N$, then yes, decreasing $N$ does increase the system capacity. This is true because each channel can serve a fixed amount of users \textit{independent of how large an area it covers}. This means that the more we replicate the channel, the more users we can serve. This also has a downside, though; the closer cells operate on the same frequencies, the more co-channel interference there is going to be.

This is also obvious if we just look at the formula $C = M \cdot S$, where $M = \frac{\text{total coverage area}}{\text{cell size}\cdot N}$.


Question 4
============
We say that an MS is roaming when it enters a new LA and stays fully functional during the switch to a different VLR. Roaming can take place within the network of a single operator, or between networks of two different operators. The operators can even be based in different countries. A user who roams between operators of different countries is what we would refer to as international roaming (which often dramatically increases the price of using the services of GSM for the user).

When an MS enters a new LA, the responsible VLR informs the HLR that the MS is in the LA of that VLR. Furthermore, the VLR retrieves information about the MS from the HLR which the VLR stores locally, such that the VLR doesn't have to query the HLR later, should the information be needed (e.g. the MS receives/initiates a call). This means that location updating is done when an MS roams.

Localizing an MS is done by contacting its HLR (which is identified using the phone number of the subscriber), which, as described above, always holds the current LA of the MS. The VLR further has to query the MSC which in turn queries its BSS, to figure out which BSS the MS is currently communicating with.

Question 5
============
Since information about the location of an MS always has to be updated at the HLR, it seems that the HLR quite easily can become the bottleneck of the system. Especially information about the location of an MS is apt to change frequently, requiring an update at the HLR. In case many users from the same HLR move between VLRs a lot (e.g. traveling at high speed), the HLR could become overloaded.