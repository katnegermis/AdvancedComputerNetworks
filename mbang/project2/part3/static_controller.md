4.3 Custom Network Topology - II: Controller with policies
============================================================

The python file which implements the topology used, can be found in `code/topology_part3.py`.
The python file which implements the learning controller can be found in `code/part3_static_controller.py`. This file uses functionality from `code/utils.py`.

Using the custom topology and the static controller as described above, I ran a ping from h1 to h4. During this ping I dumped all traffic going on at all links. These dumps can be found in `data/` and are named static_[one end of link]_[other end of link].
Especially the two files `static_s3_s2` and `static_s2_s1` are interesting. These show that the ICMP request packet passed through the link s3->s2, and that the ICMP reply packet passed through s2->s1.