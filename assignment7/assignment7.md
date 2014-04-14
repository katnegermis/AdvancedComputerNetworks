% Advanced Computer Networks
% Assignment 7: Layer7 Switching and High Performance Networking
% Michael Bang (mbang), April 17th 2014

Question 1
============
- IPv6 has enough addresses such that all mobile stations (MS) can have multiple unique addresses without exhausting the address space.
- "Transparent" routing to the care-of address _built in_ to the protocol.
- No special support required by router on foreign network (i.e. foreign agent in IPv4). It should be noted that a home agent is still required.
- If the correspondent node supports Mobile IP, the mobile node may register itself with its care-of address at the correspondent node. The correspondent node will then route packets directly to the mobile node, avoiding the triangular routing problem. This will (most likely) decrease latency and avoid that crahes/errors at the home router affects the mobile node. This means that IP-in-IP can be avoided.

Question 2
============
Mobile IP provides only addressing of nodes, and therefore is only concerned with nodes and subnets. Since Mobile IP only has notions of nodes and subnets, it 'only' supports nodes moving between subnets.

SIP provides addressing of nodes, users (indirectly addressing of nodes), moving sessions between nodes, and service mobility. This means that, in addition to nodes moving between subnets, SIP supports users and sessions moving between nodes.


Question 3
============
a)
----
The end-to-end semantics no longer hold when the end host crashes. In this case there is no way for the sender to implicitly determine that the end host has crashed, since there is no direct connection to the end host.
Assuming that the router buffers all messages for the end host while it is unavailable, as a way to 'help the connection', this might not even help if the router since the messages might depend on state that no longer exists in the end host, when it becomes available again. This would mean a lot of unnecessary work has been done by the router.

b)
----
In the case of indirect TCP, all state (both TCP connections) has to be transferred to the other router during handover. This is not necessary in snooping TCP, where the state that is kept can be safely thrown away. I would say that indirect TCP has the highest delay.

c)
----
Assuming that TCP Reno was used (which seems to be the case because of the way the first segment loss is handled), the second segment loss is detected due to a timeout. This is the case since the congestion window is lowered to 1; had the segment loss been due to three duplite ACKs, the congestion window would've been halved (as in the first segment loss on the figure).

d)
----
With indirect TCP, the access point acts as a middle man. In this case, if the middle man is compromised, the encryption will not help the end host. It also may be the case that the access point doesn't encrypt the connection between itself and the end host, in which case others may listen in on the the traffic. Unless the access point is _known_ to be non-compromised and non-hostile, the connection can not be considered safe.

Snooping TCP is simply not possible with an encrypted TCP payload; there is no way for the access point to know whether a packet has been lost or not since it doesn't have access to port- and sequence numbers of the TCP packet.

Selective retransmission and fast retransmit will work well with encrypted packets since the access point is not involved.


Question 4
============
a)
----
They note in the paper that they found that ''Energy consumption grows almost linearly with RTT''. This makes sense because the longer the RTT is, the longer the radio has to be active.

Using PSM when the RTT is low potentially has the effect that the power consumption goes up. This happens, in part, due to the fact that TCP slow start and PSM don't play along nicely; for RTTs <= 100 ms, the RTT is ''unnecessarily'' increased to ~100 ms, which means that TCPs slow start takes longer than it would without PSM. This causes the radio to be active for longer time, which in turn uses more power.

b)
----
This happens because the amount of power required to transmit the required to state to and from the MAUI server is higher than performing the calculations locally. The high RTT of 3G plays a role in this.