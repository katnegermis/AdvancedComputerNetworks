from pox.core import core

from utils import ControllerMixin, launch, Global

log = core.getLogger()


class LearningController(ControllerMixin):
    def __init__(self, *args, **kwargs):
        super(LearningController, self).__init__(*args, **kwargs)
        self.handle_packet = self.act_like_switch

    def act_like_switch(self, packet, packet_in):
        # Learn the port for the source MAC
        src_mac = packet.src
        src_port = packet_in.in_port
        self.mac_to_port[src_mac] = src_port

        # If packet is multicast, flood it.
        if packet.dst.isMulticast():
            self.flood(packet, packet_in)
            return

        # Packet has only a single recipient.
        dst_mac = packet.dst
        dst_port = self.mac_to_port.get(dst_mac, None)
        # If we don't yet know the dst port, we flood the packet.
        if not dst_port:
            self.flood(packet, packet_in)
            return

        # Controller knows which port dst is on. Unicast packet.
        self.send_packet(packet_in.buffer_id, packet_in.data,
                         dst_port, packet_in.in_port)


Global.controller = LearningController
