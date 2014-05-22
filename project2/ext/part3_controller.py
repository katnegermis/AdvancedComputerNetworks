# Copyright 2012 James McCauley
#
# This file is part of POX.
#
# POX is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# POX is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.    See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with POX.    If not, see <http://www.gnu.org/licenses/>.


from pox.core import core
from pox.lib.addresses import EthAddr

from utils import ControllerMixin, launch, Global

log = core.getLogger()

S1_PORT_H1 = 1
S1_PORT_H2 = 2
S1_PORT_S2 = 3
S1_PORT_S3 = 4

S2_PORT_H3 = 1
S2_PORT_H4 = 2
S2_PORT_S1 = 3
S2_PORT_S3 = 4

S3_PORT_S1 = 1
S3_PORT_S2 = 2

H1_MAC = EthAddr(1)
H2_MAC = EthAddr(2)
H3_MAC = EthAddr(3)
H4_MAC = EthAddr(4)

BROADCAST_MAC = EthAddr((1 << 48) - 1)


class Part3Controller(ControllerMixin):
    def __init__(self, *args, **kwargs):
        super(Part3Controller, self).__init__(*args, **kwargs)
        self.handle_packet = self.act_like_switch_reactive

    def act_like_switch_reactive(self, packet, packet_in):
        # Learn the port for the source MAC
        src_mac = packet.src
        src_port = packet_in.in_port

        if self.switch == 3:
            return

        # Send microflow rule to switch whenever it sends us a packet;
        # the switch will only send us packets when there are no matching
        # flow rules. Flow rules can timeout, so we actually need to do this
        # for every received packet, and not just for macs we don't know.
        # We could, of course, set unbounded timeouts on our rules.
        self.microflow_mac_to_dst_port(src_mac, src_port)
        self.mac_to_port[src_mac] = src_port

        # If packet is multicast, flood it.
        if packet.dst.isMulticast():
            self.flood(packet, packet_in)
            return

        # Packet is unicast, and the switch doesn't know the dst.
        dst_mac = packet.dst
        dst_port = self.mac_to_port.get(dst_mac, None)
        # If controller doesn't know dst, we flood the packet.
        if dst_port is None:
            self.flood(packet, packet_in)
            return

        # The switch didn't know the dst, but the controller does.
        # This happens when a flowrule has timed out on a switch.
        # Let's send packet directly to dst.
        self.send_packet(packet_in.buffer_id, packet_in.data,
                         dst_port, packet_in.in_port)

    def _handle_ConnectionUp(self, event):
        self.switch = int(event.dpid)

        # Here, I'm installing static routes in the switches.

        # Forwarding rules for switch 1
        if self.switch == 1:
            self.microflow_mac_to_dst_port(H4_MAC, S1_PORT_S3)

        if self.switch == 3:
            self.microflow_mac_to_dst_port(H4_MAC, S3_PORT_S2)


Global.controller = Part3Controller
