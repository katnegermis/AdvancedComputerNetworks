from pox.core import core
from pox.lib.addresses import EthAddr
import pox.openflow.libopenflow_01 as of

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


class Part3StaticController(ControllerMixin):
    def __init__(self, *args, **kwargs):
        super(Part3StaticController, self).__init__(*args, **kwargs)
        self.handle_packet = self.drop_packets

    def drop_packets(self, packet, packet_in):
        pass

    def _handle_ConnectionUp(self, event):
        self.switch = int(event.dpid)

        # Here, I'm installing all routing rules statically in to the switches.

        # Forwarding rules for switch 1
        if self.switch == 1:
            self.microflow_mac_to_dst_port(H1_MAC, S1_PORT_H1)
            self.microflow_mac_to_dst_port(H2_MAC, S1_PORT_H2)
            self.microflow_mac_to_dst_port(H3_MAC, S1_PORT_S2)
            self.microflow_mac_to_dst_port(H4_MAC, S1_PORT_S3)
            self.microflow_mac_to_dst_port(BROADCAST_MAC, of.OFPP_FLOOD)

        # Forwarding rules for switch 2
        if self.switch == 2:
            self.microflow_mac_to_dst_port(H1_MAC, S2_PORT_S1)
            self.microflow_mac_to_dst_port(H2_MAC, S2_PORT_S1)
            self.microflow_mac_to_dst_port(H3_MAC, S2_PORT_H3)
            self.microflow_mac_to_dst_port(H4_MAC, S2_PORT_H4)
            self.microflow_mac_to_dst_port(BROADCAST_MAC, of.OFPP_FLOOD)

        # Forwarding rules for switch 3
        if self.switch == 3:
            self.microflow_mac_to_dst_port(H4_MAC, S3_PORT_S2)


Global.controller = Part3StaticController
