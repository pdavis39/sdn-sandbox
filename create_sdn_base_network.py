#!/usr/bin/python#
# author: Paul Davis
# email: pdavis39@gmail.com
# created: 9/15/2019
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# the purpose of this program is to establish the base SDN for experiments

from __future__ import print_function
from time import sleep
from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import CPULimitedHost
from mininet.link import TCLink
from mininet.util import dumpNodeConnections
from mininet.log import setLogLevel, info
from mininet.cli import CLI
import io

CONTROLLER_IP = '127.0.0.1'
CONTROLLER_PORT = 6653
IP_BASE = '10.0.5.0/24'

#topos = { 'sdntopo': ( lambda: SDNTopo() ) }

class SDNTopo(Topo):
#	Single switch connected to 2 hosts per switch.

    def __init__(self, lossy=True, **opts):
        # initialize topology
        Topo.__init__(self, **opts)
        # add topology of hosts and switches
     #   c0 = net.addController(name='c0', controller=RemoteController, ip=CONTROLLER_IP, port=CONTROLLER_PORT)
        edgeServer = self.addHost('h1', ip='10.0.5.1')
        internet = self.addHost('h2', ip='10.0.5.2')
        Host1 = self.addHost('h3', ip='10.0.5.3')
        Host2 = self.addHost('h4', ip='10.0.5.4')
        Host3 = self.addHost('h5', ip='10.0.5.5')
        Host4 = self.addHost('h6', ip='10.0.5.6')
        Host5 = self.addHost('h7', ip='10.0.5.7')
        Host6 = self.addHost('h8', ip='10.0.5.8')
        Host7 = self.addHost('h9', ip='10.0.5.9')
        Host8 = self.addHost('h10', ip='10.0.5.10')
        Host9 = self.addHost('h11', ip='10.0.5.11')
        Host10 = self.addHost('h12', ip='10.0.5.12')
        Host11 = self.addHost('h13', ip='10.0.5.13')
        Host12 = self.addHost('h14', ip='10.0.5.14')
        coreSwitch = self.addSwitch('s1')
        disSwitch1 = self.addSwitch('s2')
        disSwitch2 = self.addSwitch('s3')
        accSwitch1 = self.addSwitch('s4')
        accSwitch2 = self.addSwitch('s5')
        accSwitch3 = self.addSwitch('s6')
        accSwitch4 = self.addSwitch('s7')

        # link parameters
        linkopts = dict(bw=10, delay='5ms', loss=10, max_queue_size=1000, use_htb=True)
        # add links
        self.addLink(edgeServer, coreSwitch, **linkopts)
        self.addLink(internet, coreSwitch, **linkopts)
        self.addLink(coreSwitch, disSwitch1, **linkopts)
        self.addLink(coreSwitch, disSwitch2, **linkopts)
        self.addLink(disSwitch1, disSwitch2, **linkopts)
        self.addLink(disSwitch1, accSwitch1, **linkopts)
        self.addLink(disSwitch1, accSwitch2, **linkopts)
        self.addLink(disSwitch2, accSwitch3, **linkopts)
        self.addLink(disSwitch2, accSwitch4, **linkopts)
        self.addLink(accSwitch1, Host1, **linkopts)
        self.addLink(accSwitch1, Host2, **linkopts)
        self.addLink(accSwitch1, Host3, **linkopts)
        self.addLink(accSwitch2, Host4, **linkopts)
        self.addLink(accSwitch2, Host5, **linkopts)
        self.addLink(accSwitch2, Host6, **linkopts)
        self.addLink(accSwitch3, Host7, **linkopts)
        self.addLink(accSwitch3, Host8, **linkopts)
        self.addLink(accSwitch3, Host9, **linkopts)
        self.addLink(accSwitch4, Host10, **linkopts)
        self.addLink(accSwitch4, Host11, **linkopts)
        self.addLink(accSwitch4, Host12, **linkopts)

topos = { 'SDNTopo': ( lambda: SDNTopo() ) }

def CreateNetwork(lossy=True):
  #  "Create network and run simple performance test"
    topo = SDNTopo(lossy=lossy)
    net = Mininet(topo=topo, host=CPULimitedHost, link=TCLink, autoStaticArp=True, ipBase=IP_BASE, autoSetMacs=True)
    # build network
    log.info("building network")


    c0 = net.addController(name='c0', controller=RemoteController, ip=CONTROLLER_IP, port=CONTROLLER_PORT)
    net.build()
    # start controller
    net.start()
    log.info("starting controllers")

    for controller in net.controllers:
        controller.start()
    print("about to create network")
    print("Dumping host connections")
    dumpNodeConnections(net.hosts)
    print("Testing network connectivity")
    net.pingAll()

    # Example of running a command on a host
    h1 = net.get('h1')
    result = h1.cmd('ifconfig')
    print("result")
    print(result)
    # open cli
    CLI(net)
    # After the user exits the CLI, shutdown the network.
    log.info('Stopping network')
    net.stop()


if __name__ == '__main__':
    setLogLevel('info')
    # run create network
    CreateNetwork()
