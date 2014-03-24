% Advanced Computer Networks
% Assignment 4: Wireless Networks: Part 3
% Michael Bang, March 27th 2014

Question 1
============

a)
----
The figure couldn't be an ACL transmission since the receiver wouldn't know to send a NAK for a packet it didn't receive, since it couldn't know that it was supposed to have received a packet. This is unlike SCO where a receiver knows a rate at which it's supposed to receive packets, and therefore knows to send a NAK if it doesn't receive packets at this rate.

b)
----
In this case the figure would be correct since the recipient knows that he was supposed to receive a packet (but couldn't decode the contents) and should request a retransmission by sending a NAK.

Question 2
============
If a node wants to send a message that takes longer to send than an awake-time, he would have to wait a sleep-time to send the rest of the packet.

If a node $x$ on schedule $A$ wants to send something to node $y$ on schedule $C$, in this example using node $z$, which is synchronized to both schedules, as a relay node. It could be the case that schedules $A$ and $C$ are scheduled such that $y$ is awake in a short period in the beginning of $x$'s transmission, but goes to sleep before the message is relayed from $z$ to $y$. This means that the message will have to wait at $z$ until $y$ wakes up again.

Question 3
============
If you are a node and want to send a message to another node, you will have to send a preamble for at least $sleep time + \epsilon$, in order to make sure that the other node is awake and listening for your message. This means that if you want to send a small packet, the time spent sending your data will be a small fraction of the total time spent transmitting. This means that a lot of battery will be "wasted" on sending the preamble.

Question 4
============
% Use slide 12-14 from lecture 5
\begin{align*}
    \text{Symbol duration} = \frac{1}{500000} = 0.0000002 s = 2 \my s\\
    \text{Time between rays} = 1 \my s\\
    \text{Inter-symbol interference} = 1 / 2 = 50\%
\end{align*}

We see that the inter-symbol rate is very high, meaning that it will be difficult to correctly decode the signal correctly at the receiver.

In the following I do not account for guard-space needed between sub-channels.

If we spread the symbols over 10 sub-channels, it will take 10 times longer to send each symbol, but 10 symbols will be sent simultaneously. This gives us less inter-symbol interference:

\begin{align*}
    \text{Symbol duration} = \frac{10}{500000} = 0.000002 s = 20 \my s\\
    \text{Time between rays} = 1 \my s\\
    \text{Inter-symbol interference} = 1 / 20 = 5\%
\end{align*}

This decreases the inter-symbol interference greatly, meaning that it will be easier to decode the signal correctly at the receiver.

Question 5
============

% Read paper

a)
----

b)
----


Question 6
============
It is possible that no acknowledgements would be received since data packets would have higher priority than acknowledgements.

Question 7
============
As can be seen on slide 22 from lecture 5, instead of each station choosing a new random backoff time each time the channel has been busy, the stations use the residual backoff time, meaning that a station that has waited for a longer time is more likely to get the channel in the future. This technique avoids the problem that a station might continuously choose a random backoff time that is greater than some other station's backoff time, such that that the first station never gets to use the shared medium.