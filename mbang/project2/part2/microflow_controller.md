4.2.3 MAC Learning Switch via MicroFlow Rules
===============================================

The python file which implements the topology used, can be found in `code/topology_part2.py`.
The python file which implements the learning controller can be found in `code/microflow_controller.py`. This file uses functionality from `code/utils.py`.

a)
----
- 'h1 ping h2 -c100':
~~~~~
--- 10.0.0.2 ping statistics ---
100 packets transmitted, 100 received, 0% packet loss, time 99021ms
rtt min/avg/max/mdev = 0.027/0.322/26.336/2.614 ms
~~~~~
- A wireshark dump from this test can be found in `data/microflow_controller_h1_ping_h2`.
- The result shows that it is around two orders of magnitude faster to install microflow rules on the switches, compared to sending all packets through the controller.

b)
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
- A wireshark dump from this test can be found in `data/microflow_controller_pingall`.

- The microflow rules can be found in the file `data/microflow_controller_flow_rules.txt`. This dump was taken after a pingall command. In the flow rules we see that each switch has an entry all 5 hosts, meaning that the switches have enough rules to route between all of the hosts without communicating with the controller.


c)
----
~~~~~
mininet> iperf h1 h5
*** Iperf: testing TCP bandwidth between h1 and h5
*** Results: ['660 Mbits/sec', '661 Mbits/sec']
~~~~~

~~~~~
mininet> iperf h1 h2
*** Iperf: testing TCP bandwidth between h1 and h2
*** Results: ['1.04 Gbits/sec', '1.04 Gbits/sec']
~~~~~

- The results show that it is more than two orders of magnitude faster to install microflow rules on the switches, compared to sending all packets through the controller.