4.2.3 MAC Learning Switch via MicroFlow Rules
===============================================

a)
----
- 'h1 ping h2 -c100':
~~~~~
rtt min   /   avg   /   max   /   mdev
  0.055  /  0.224  /  0.476  /  0.078 ms
~~~~~
- This is around two orders of magnitude faster.

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

~~~~~
mininet@mininet-vm:~$ dpctl dump-flows tcp:127.0.0.1:6634
stats_reply (xid=0x5f0f9d08): flags=none type=1(flow)
  cookie=0, duration_sec=2221s, duration_nsec=510000000s, table_id=0, priority=32768, n_packets=0, n_bytes=0, idle_timeout=0,hard_timeout=0,dl_dst=c2:c9:9d:a0:2d:97,actions=output:3
  cookie=0, duration_sec=2221s, duration_nsec=986000000s, table_id=0, priority=32768, n_packets=4, n_bytes=392, idle_timeout=0,hard_timeout=0,dl_dst=00:00:00:00:00:05,actions=output:3
  cookie=0, duration_sec=2221s, duration_nsec=727000000s, table_id=0, priority=32768, n_packets=4, n_bytes=392, idle_timeout=0,hard_timeout=0,dl_dst=00:00:00:00:00:03,actions=output:3
  cookie=0, duration_sec=2221s, duration_nsec=192000000s, table_id=0, priority=32768, n_packets=4, n_bytes=392, idle_timeout=0,hard_timeout=0,dl_dst=00:00:00:00:00:04,actions=output:3
  cookie=0, duration_sec=2221s, duration_nsec=442000000s, table_id=0, priority=32768, n_packets=29, n_bytes=2618, idle_timeout=0,hard_timeout=0,dl_dst=00:00:00:00:00:02,actions=output:2
  cookie=0, duration_sec=2221s, duration_nsec=814000000s, table_id=0, priority=32768, n_packets=0, n_bytes=0, idle_timeout=0,hard_timeout=0,dl_dst=e6:6f:ee:6f:c9:84,actions=output:3
  cookie=0, duration_sec=2221s, duration_nsec=909000000s, table_id=0, priority=32768, n_packets=31, n_bytes=2702, idle_timeout=0,hard_timeout=0,dl_dst=00:00:00:00:00:01,actions=output:1

mininet@mininet-vm:~$ dpctl dump-flows tcp:127.0.0.1:6635
stats_reply (xid=0xab57662f): flags=none type=1(flow)
  cookie=0, duration_sec=2223s, duration_nsec=309000000s, table_id=0, priority=32768, n_packets=0, n_bytes=0, idle_timeout=0,hard_timeout=0,dl_dst=c2:c9:9d:a0:2d:97,actions=output:2
  cookie=0, duration_sec=2223s, duration_nsec=909000000s, table_id=0, priority=32768, n_packets=0, n_bytes=0, idle_timeout=0,hard_timeout=0,dl_dst=f2:e0:29:88:c7:5f,actions=output:1
  cookie=0, duration_sec=2223s, duration_nsec=790000000s, table_id=0, priority=32768, n_packets=4, n_bytes=392, idle_timeout=0,hard_timeout=0,dl_dst=00:00:00:00:00:05,actions=output:2
  cookie=0, duration_sec=2223s, duration_nsec=527000000s, table_id=0, priority=32768, n_packets=4, n_bytes=392, idle_timeout=0,hard_timeout=0,dl_dst=00:00:00:00:00:03,actions=output:2
  cookie=0, duration_sec=2222s, duration_nsec=994000000s, table_id=0, priority=32768, n_packets=4, n_bytes=392, idle_timeout=0,hard_timeout=0,dl_dst=00:00:00:00:00:04,actions=output:2
  cookie=0, duration_sec=2223s, duration_nsec=237000000s, table_id=0, priority=32768, n_packets=9, n_bytes=714, idle_timeout=0,hard_timeout=0,dl_dst=00:00:00:00:00:02,actions=output:1
  cookie=0, duration_sec=2223s, duration_nsec=635000000s, table_id=0, priority=32768, n_packets=9, n_bytes=714, idle_timeout=0,hard_timeout=0,dl_dst=00:00:00:00:00:01,actions=output:1

mininet@mininet-vm:~$ dpctl dump-flows tcp:127.0.0.1:6636
stats_reply (xid=0x2e548289): flags=none type=1(flow)
  cookie=0, duration_sec=2225s, duration_nsec=138000000s, table_id=0, priority=32768, n_packets=12, n_bytes=952, idle_timeout=0,hard_timeout=0,dl_dst=00:00:00:00:00:05,actions=output:3
  cookie=0, duration_sec=2225s, duration_nsec=180000000s, table_id=0, priority=32768, n_packets=0, n_bytes=0, idle_timeout=0,hard_timeout=0,dl_dst=f2:e0:29:88:c7:5f,actions=output:4
  cookie=0, duration_sec=2224s, duration_nsec=870000000s, table_id=0, priority=32768, n_packets=14, n_bytes=1036, idle_timeout=0,hard_timeout=0,dl_dst=00:00:00:00:00:03,actions=output:1
  cookie=0, duration_sec=2224s, duration_nsec=337000000s, table_id=0, priority=32768, n_packets=13, n_bytes=994, idle_timeout=0,hard_timeout=0,dl_dst=00:00:00:00:00:04,actions=output:2
  cookie=0, duration_sec=2224s, duration_nsec=573000000s, table_id=0, priority=32768, n_packets=12, n_bytes=840, idle_timeout=0,hard_timeout=0,dl_dst=00:00:00:00:00:02,actions=output:4
  cookie=0, duration_sec=2224s, duration_nsec=973000000s, table_id=0, priority=32768, n_packets=12, n_bytes=840, idle_timeout=0,hard_timeout=0,dl_dst=00:00:00:00:00:01,actions=output:4
  cookie=0, duration_sec=2225s, duration_nsec=247000000s, table_id=0, priority=32768, n_packets=0, n_bytes=0, idle_timeout=0,hard_timeout=0,dl_dst=3a:91:9c:b7:f0:00,actions=output:4$
~~~~~

c)
----
~~~~~
mininet> iperf h1 h5
*** Iperf: testing TCP bandwidth between h1 and h5
*** Results: ['267 Mbits/sec', '267 Mbits/sec']
~~~~~

~~~~~
mininet> iperf h1 h2
*** Iperf: testing TCP bandwidth between h1 and h2
*** Results: ['344 Mbits/sec', '344 Mbits/sec']
~~~~~

- The results show that it is around two orders of magnitude faster not to send every single packet to the controller.