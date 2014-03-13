% Advanced Computer Networks
% Assignment 2: Wireless Networks: Fundamentals
% March 13th 2014

Question 1
============
a)
----
The path loss (path attenuation) model is a mathematical model for predicting electro magnetic wave propagation.
The formula is as follows:
\begin{align*}
        loss = \frac{P_t}{P_r} = (\frac{4\cdot \pi d}{\lambda})^a
\end{align*}
where $P_t$ is transmitted power, $P_r$ is received power, $d$ is distance, $\lambda$ is wavelength, and $a$ is the path loss exponent. The path loss exponent has been emperically measured for different environments, and, for instance, is 2 in a vacuum[^1].

The path loss is often given in dB, which has the formula:
\begin{align*}
    loss (dB) = 10log(\frac{P_t}{P_r}) = 10a\cdot log(\frac{4\cdot \pi d}{\lambda})
\end{align*}

b)
----
The log-normal shadowing model takes, by very simple means, account for ''random'' effects such as shadowing, refraction, reflection, scattering, and diffraction. The model takes these effects in to account by adding a gaussian random variable with zero mean and standard deviation $\sigma$ typically in the range $[2; 8]$. The formula then becomes:

\begin{align*}
    loss (dB) = 10log(\frac{P_t}{P_r}) = 10a\cdot log(\frac{4\cdot \pi d}{\lambda}) + X[dB]
\end{align*}

c)
----
Theoretically, the Signal to Interference + Noise Ratio (SINR) should be a good estimator for whether a signal can be decoded or not, but empirical data (such as from the MIT roofnet) shows that this is in fact not the case.

d)
----
The log-normal shadowing model does not very accurately predict what we will measure in real life because it is just a random variable and therefore doesn't take the actual environment in to account.

Question 2
============
The spread spectrum technique is a way to deliberately spread signals with a particular bandwidth over a wider band, resulting in a signal with a wider bandwidth[^2]. This allows the receiver to despread the signal and recover the original signal while removing both broad- and narrowband interference.

One of the main benefits of using a spread spectrum system is that it is resistant to narrow band interference. DSSS is resistant to multiple-path propagation, and is somewhat more secure (if the chipping sequence is kept secret.)

Question 3
============
The spreading factor $s$ is given as the formula $s = \frac{t_b}{t_c}$, where $t_b$ is the duration of a 'user bit', and $t_c$ is the duration of a 'chipping bit', i.e. the user bit encoded with the chipping sequence. $s$, the spreading factor, then tells us how many chipping bits are sent in order to represent a user bit. Since we're representing a single user bit by sending $s$ chipping bits, the bandwidth required to send a user bit increases by the factor $s$.
\
\
The following shows how the user bits $0110$ are encoded and decoded with the chipping sequence $0110101$ before and after sending the user bits.

~~~
Chipping Sequence (CS)  0110101

User Bit (UB)           0       1       1       0
UB XOR CS               0110101 1001010 1001010 0110101

data sent/received      0110101 1001010 1001010 0110101
data received XOR CS    0000000 1111111 1111111 0000000

Interpreted UB          0       1       1       0
~~~

Question 4
============
a)
----
According to the paper, the top level goal was to ''develop an effective technique for multiplexed networks.'' Since there were already different kinds of networks, it was decided that the DARPA internet interconnect these, creating a network of networks. This gave the Internet natural borders for administration, i.e. allows each network to be administered by different entities.

b)
----
An alternative to the fate sharing principle could be that the network is made responsible for sending messages, which means that the network becomes stateful. This could, for instance, be implemented as a circuit switched network. This would push a lot of complexity in to the network, e.g. reliability.

Advantages of the fate-sharing approach include: less complex network nodes and easy/simple rerouting in case of node failures.
A disadvantage is that when an end-host crashes, it is possible that the messages that he sent will never reach the intended receiver.

c)
----
One of the main advantages of using datagrams is that the network doesn't need to save any state. This means that traffic can easily be rerouted in case of network node failures. Another advantage is that the datagram has proven to be a great lowest-denominator building block on which to build other protocols on top of; both connectionless (UDP) and connection oriented (TCP) protocols have been built on top of datagrams.

A disadvantage of using datagrams is that the network isn't reliable, but follows a best-effort approach. This means that packets can arrive out of order, and need to be reassembled at the receiving end-host. It also means that the same packet might be unnecesarily sent multiple times, and that retransmission is much more expensive since all retransmissions start at the sending end-host instead of a place closer to where the packet got dropped. Furthermore, there is an overhead in adding multiple headers to all packets, regardless of their size.

A different approach would be to create a circuit switched network.


Question 5
============
a)
----
The end-to-end argument says that everything that is not required to be implemented in the network (and can be implemented in the end-hosts) shouldn't be.

One reason is that some end-hosts might not need such an 'extra' service and, if the service has been implemented at a lower layer, cannot choose not to use such service, which might unnecessarily degrade the performance of these clients.

b)
----
- Implementing reliability of transmission of data in end-hosts.
- Implementing secure transmission of data between end-host applications in end-host applications.

c)
----
- Implementing reliability of data transmission in the network.
    - Retransmission can be much slower and uses more bandwidth.
    - Intended recipient might not receive messages that were successfully delivered to the network by the sending host, if the sending host crashes.
    - End-to-end checksums have to be implemented regardless of the reliability of the network.

- Implementing secure transmission of data in the network.
    - Transmission system has to be trusted with encryption keys.
    - Data not encrypted between transmission system and application.
    - Authenticity of application not established (though authenticity of transmission system is).

- Implementing delivery guarantees in the network
    - Application might not receive/react to message even though it has been received at transmission system.


[^1]: http://en.wikipedia.org/wiki/Log-distance_path_loss_model#Empirical_coefficient_values_for_indoor_propagation
[^2]: http://en.wikipedia.org/wiki/Spread_spectrum
