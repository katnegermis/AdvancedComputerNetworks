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

from utils import ControllerMixin, launch, Global

log = core.getLogger()


class LearningController(ControllerMixin):
    def __init__(self, *args, **kwargs):
        super(LearningController, self).__init__(*args, **kwargs)
        self.handle_packet = self.act_like_switch

    def act_like_switch(self, packet, packet_in):
        # packet (ethernet)
        # packet_in (ofp_packet_in)

        # Learn the port for the source MAC
        src_mac = packet.src
        src_port = packet_in.in_port
        self.mac_to_port[src_mac] = src_port

        # If packet is multicast, flood it.
        if packet.dst.isMulticast():
            log.debug("Broadcast from {src}".format(src=src_mac))
            self.flood(packet, packet_in)
            return

        # Packet has only a single recipient.
        dst_mac = packet.dst
        dst_port = self.mac_to_port.get(dst_mac, None)
        # If we don't yet know the dst port, we flood the packet.
        if not dst_port:
            log.debug("Flooding unicast from {src} to {dst}".format(src=src_mac,
                                                                    dst=dst_mac))
            self.flood(packet, packet_in)
            return

        # We know dst port. U
        log.debug("Unicast from {src} to {dst}".format(src=src_mac,
                                                       dst=dst_mac))
        self.send_packet(packet_in.buffer_id, packet_in.data,
                         dst_port, packet_in.in_port)


Global.controller = LearningController
