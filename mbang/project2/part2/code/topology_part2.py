from mininet.topo import Topo


class Part2Topology(Topo):

    def __init__(self):
        # Initialize topology
        Topo.__init__(self)

        # Add hosts and switches
        h1 = self.addHost('h1')
        h2 = self.addHost('h2')
        h3 = self.addHost('h3')
        h4 = self.addHost('h4')
        h5 = self.addHost('h5')
        s1 = self.addSwitch('s1')
        s2 = self.addSwitch('s2')
        s3 = self.addSwitch('s3')

        # Add links
        # Hosts to switches
        self.addLink(h1, s1)
        self.addLink(h2, s1)
        self.addLink(h3, s3)
        self.addLink(h4, s3)
        self.addLink(h5, s3)

        # Switches to switches
        self.addLink(s1, s2)
        self.addLink(s2, s3)


topos = {'part2': (lambda: Part2Topology())}
