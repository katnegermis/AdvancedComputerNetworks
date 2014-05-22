4.2.2 Learning Controller
===========================

The python file which implements the topology used, can be found in `code/topology_part2.py`.
The python file which implements the learning controller can be found in `code/learning_controller.py`. This file uses functionality from `code/utils.py`.

a)
----
- 'h1 ping h2 -c100':
~~~~~
--- 10.0.0.2 ping statistics ---
100 packets transmitted, 100 received, 0% packet loss, time 99287ms
rtt min/avg/max/mdev = 2.247/31.663/71.968/15.567 ms
~~~~~

- The first ping took 32.0 ms in this specific test, but that fluctuates a lot between tests.
- There is no difference between the first ping in this test and in the hub tests; the first packet will be flooded to all switches and hosts in both cases.
- The wireshark dump from this test can be found in `data/learning_controller_h1_ping_h2`.

b)
----
- The wireshark dump from this test can be found in `data/learning_controller_h1_ping_h5`.
- 'h1 ping h5 -c100':
~~~~~
--- 10.0.0.5 ping statistics ---
100 packets transmitted, 100 received, 0% packet loss, time 99187ms
rtt min/avg/max/mdev = 15.320/43.396/101.097/17.474 ms
~~~~~


- The wireshark dump from this test can be found in `data/learning_controller_h1_ping_h4`.
- 'h1 ping h4 -c100':
~~~~~
--- 10.0.0.4 ping statistics ---
100 packets transmitted, 100 received, 0% packet loss, time 99228ms
rtt min/avg/max/mdev = 9.943/40.257/85.561/16.079 ms
~~~~~

- From the numbers above we see that there is no significant different between pinging H5 and H4. We didn't expect there to be a difference since the same number of switches are traversed.

c)
----

~~~~~
mininet> iperf h1 h5
*** Iperf: testing TCP bandwidth between h1 and h5
*** Results: ['2.25 Mbits/sec', '2.26 Mbits/sec']
~~~~~

~~~~~
mininet> iperf h1 h2
*** Iperf: testing TCP bandwidth between h1 and h2
*** Results: ['5.26 Mbits/sec', '5.30 Mbits/sec']
~~~~~
