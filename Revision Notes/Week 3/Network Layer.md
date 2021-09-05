# Network Layer (Layer 3)

A router is a networking device that forwards (routes) the traffic between computer networks. When routing data to a host on another network using a router, a device will also need to use a default gateway. A default gateway is the IP address of the NIC inside a network's router. A directly connected network is two or more networks that share a router with different NIC interfaces. A host will utilize a default gateway when it needs to send data to another device that does not share the same network. This is achieved through the usage of a subnet mask to identify the network ID.

A router will create a 'Routing table' filled with listings of IP addresses for different devices and networks it has interacted with as well as the associated subnet mask and router port interface. The routing table can be filled with both manual static routes and dynamic routes. Dynamic routing can be used for optimal routing, unlike static, dynamic allows for the routing paths to be changed in real-time according to logical network layout changes. This is achieved using multiple algoritmhs and protocols, such as Routing Information Protocol (RIP) and Open Shortest Path First (OSPF). When using dynamic routing, routers will communicate with each other in order to discover the shortest paths.


| Switch                                                                                                 | Router                                                                                                |
|--------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------|
| Forwards traffic based on destination MAC address                                                      | Forwards traffic based on destination IP address                                                      |
| Passes broadcast frames to all ports (except the port the frame was received on)                       | Doesn't forward any broadcast frames                                                                  |
| One broadcast domain                                                                                   | Broadcast domain split into multiple broadcast domains                                                |
| Connects devices that share the same network ID                                                        | Connects networks that have differing network ID                                                      |
| Forwards traffic between networks that are connected using the same data-link standard (e.g. Ethernet) | Can connect networks that are connected using different technologies (e.g. Ethernet, ADSL, Broadband) |
