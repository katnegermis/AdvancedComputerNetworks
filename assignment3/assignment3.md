% Advanced Computer Networks
% Assignment 3: Wireless Networks: Part 2
% Michael Bang, March 20th 2014

Question 1
============

Question 2
============

a)
----

b)
----

Question 3
============
If the computer, C, has two masters, it can send with twice the data rate to two different piconets. If the receiver, R only has one bluetooth receiver (one slave) this doesn't increase the throughput from C to R, as R can only participate in one piconet. If, on the other hand, R has two bluetooth receivers (two slaves) it can participate in two networks at once, allowing for the data rate to be doubled.


Question 4
============
In the bluetooth stack itself, there is no way to allow devices in different piconets to communicate with each other, even if one device is part of both piconets, creating a scatternet. This layer has to be built on top of the bluetooth stack.

Assuming that the layer described above is implemented, one way to arrange such a network would be to create a 'scatternet-circle', letting the master of each piconet be the slave of the neighboring piconet to the left (or right, as long as it's the same for all masters). On Figure \ref{fig:scatternet} below this is shown for $N=16$, where the numbered nodes are masters of the piconet with the same number, and, at the same time, they are slaves in piconet to their left, i.e. the master (M) of piconet P1 is the slave of piconet P2, M of P2 is a slave of P3, and M of P3 is a slave of P1.

![Scatternet with 16 Bluetooth devices.\label{fig:scatternet}](img/scatternet.jpg)


Question 5
============
Bluetooth devices connect to each other by going from the standby state to the connected state, through inquiry and page state. During the inquiry state, the devices discover each other. During the paging state they decide on a master whose clock and hardware address they will use to decide a common hopping sequence unique to the created piconet.

Standby
---------
The Bluetooth device is idle and can only move on to inquiry state, in order to try to connect to another device.

Inquiry
---------
Allows a Bluetooth device to discover or be discovered by other Bluetooth devices.

A device in inquiry state can move back to standby or forward to paging state, in order to initiate a connection with another device.

Paging
--------
Allows a pair of Bluetooth devices to form (or expand) a piconet by deciding on a common hopping sequence, determined by the master's hardware address and clock.

A device in paging state can move back to inquiry state or forward connected state once a connection has been established.


Connected
-----------
A device in connected state is an active part of a piconet (it listens for all messages), but does not reply to the master.

A device in connected state can move forward to transmit state in order to xx, or to any of the low power states (park, hold, and sniff) in order to save power.

Transmit
----------
A device in transmit state is actively communicating with its master.

A device in transmit state can move to connected or standby state.


Low power states
------------------
A device in a low power mode does not actively take part in the network. It still listens for messages from the master, but much less frequently than in the active states (connected and transmitting). A Bluetooth device in parked state even gives up its address in the piconet, allowing for more than 7 slaves to be in the piconet (even though they are not all actively part of it).

A master can tell slaves to go to a low power state, and slaves can themselves request to go to a low power state.

A device in a low power state can move to the connected state.


Question 6
============

a)
----
Quality of Service can provided by two different means, on the two different types of channels: synchronous and asynchronous.

On a synchronous channel the master and slave initially agree on an interval at which they will communicate, effectively agreeing on a minimum bandwidth for their connection.

On an asynchronous channel slaves are allowed only to "speak when spoken to"; the master of a piconet is responsible for polling the slaves, at which point the slaves may respond in the following slot, perhaps requesting more slots to transmit daa in. This means that, theoretically (I have not been able to find anything that says that this is actually an official part of Bluetooth), the master can set up agreements with its slaves, giving them some minimum amount of times per time interval they are asked to speak. This is very similar to the synchronous channel, but differs in the way that no specific interval for the communication is agreed upon.


b)
----
This has been answered in the section "Low power states" of Question 5.

Question 7
============
It is not practical for small sensors to use GPS because it uses a lot of power, which is often very limited in such sensors. A practical approach to learn of a sensor's location would be to have a more powerful device with a GPS near the sensor, to which the sensor could send an ID (perhaps even along with some of the information that the sensor has collected.) The powerful device doesn't have to be stationary, but could be moved near the sensor as often as the location of the sensor is required to be reestablished, perhaps requesting all nearby sensors to broadcast send their ID.


Question 8
============

a)
----
That one device A knows which packets ($p \in P$) other devices (to which A is sending) have received, so that these devices can use their p's to decode the packets that A is sending them, which are encoded with p.

This also implicitly assumes that A will receive some packets meant for some other device B, which B can't receive itself.


b)
----
