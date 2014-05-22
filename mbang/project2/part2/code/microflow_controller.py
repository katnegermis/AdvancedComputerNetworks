from pox.core import core

from utils import ControllerMixin, launch, Global

log = core.getLogger()


class LearningControllerReactive(ControllerMixin):
    def __init__(self, *args, **kwargs):
        super(LearningControllerReactive, self).__init__(*args, **kwargs)
        self.handle_packet = self.act_like_switch_reactive

    def act_like_switch_reactive(self, packet, packet_in):
        # Learn the port for the source MAC
        src_mac = packet.src
        src_port = packet_in.in_port

        # Send microflow rule to switch whenever it sends us a packet;
        # the switch will only send us packets when there are no matching
        # flow rules. Flow rules can timeout, so we actually need to do this
        # for every received packet, and not just for macs we don't know.
        # We could, of course, set unbounded timeouts on our rules.
        log.debug("Microflow rule: {} is on port {}".format(src_mac, src_port))
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


Global.controller = LearningControllerReactive
