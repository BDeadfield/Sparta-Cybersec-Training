# Data-Link Layer (Layer 2)

The data-link layer is responsible for preparing data to be sent across the physical network for NIC-to-NIC communications (this can include the router).

## Ethernet Family

Half-duplex mode allows data to be sent or received, but not at the same time, whereas full-duplex mode allows for simultaneously sending and receiving data.

| Standard            | Speed   | Mode                      |
|---------------------|---------|---------------------------|
| Ethernet            | 10Mbps  | Half-duplex               |
| FastEthernet        | 100Mbps | Half-duplex / Full-duplex |
| 1 Gigabit Ethernet  | 1Gbps   | Half-duplex / Full-duplex |
| 10 Gigabit Ethernet | 10Gbps  | Full-duplex               |

## Layer 2 (L2) Switch

A switch is composed of integrated circuits as well as software that controls the data paths through the switch. Switches feature several ports. Each port can be utilized in order to connect an end-device or an additional intermediary device. Data is forwarded through a switch via the received port to the destination port by using the MAC address. When first initializing, a switch will need to build a cache table of MAC addresses on the network in order to route data to the right destination. Prior to building a cache table, a switch will build it's knowledge by forwarding all data received to every end-device on the switch excluding the end-device sending the data (the switch will read the MAC address associated with the data in order to determine this).

## Protocols

'Ping' is a command that can be used in order to determine whether a device is able to communicate with another device, and the elapsed response time. Ping utilizes the Internet Control Message Protocol (ICMP). When 'ping' is used a echo request is sent to a designated device, if it receives the request it should send back an echo reply.

Address Resolution Protocol (ARP) is a layer-three (Network) protocol that is used in order to find the MAC address of a NIC (on the same network) that has a specific IP. If your device requires a MAC address for an IP address, ARP will be used to broadcast on your network to all devices, however only the desired device will reply. ARP will fill the destination MAC address with '1111 1111' to signify a broadcast.
