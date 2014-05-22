4.2.1 Hub Controller
======================

The python file which implements the topology used, can be found in `code/topology_part2.py`.
The python file which implements the hub controller can be found in `code/hub_controller.py`. This file uses functionality from `code/utils.py`.

a)
----
- 'h1 ping h2 -c100':
~~~~~
--- 10.0.0.2 ping statistics ---
100 packets transmitted, 100 received, 0% packet loss, time 99253ms
rtt min/avg/max/mdev = 2.241/31.443/61.825/15.617 ms
~~~~~

- Since all of the switches acted as hubs, all switches and all hosts received all packets. This is evident from the wireshark dump in `data/hub_controller_h1_ping_h2`.

b)
----
- 'h1 ping h5 -c100':
~~~~~
--- 10.0.0.5 ping statistics ---
100 packets transmitted, 100 received, 0% packet loss, time 99213ms
rtt min/avg/max/mdev = 10.305/41.672/79.983/15.747 ms
~~~~~

- Yes, on average there was 10ms difference. This seems reasonable since the packets have to traverse an additional two switches. The wireshark dump can be found in `data/hub_controller_h1_ping_h5`.

c)
----

~~~~~
mininet> pingall
*** Ping: testing ping reachability
h1 -> h2 h3 h4 h5
h2 -> h1 h3 h4 h5
h3 -> h1 h2 h4 h5
h4 -> h1 h2 h3 h5
h5 -> h1 h2 h3 h4
*** Results: 0% dropped (0/20 lost)
~~~~~

- The wireshark dump can be found in `data/hub_controller_pingall`.