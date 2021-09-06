# Network Security

## Access Control List (ACL)

An Access Control List contains a set of rules that grant or deny access to a resource (e.g. file, computer, network or system). In networking, ACLs are generally applied on a specific interface in a certain direction and tell networking devices which type of traffic is allowed.

A networking device would apply an ACL on each packet as follows:

1. Get the destination and source addresses from the packet
2. Find a rule in the ACL that matches the source and/or destination addresses/ports.
3. If match found, check the action in the rule:
    - Allow the packet to pass
    - Deny and drop the packet
4. If a match isn't found, drop the packet.

### Wild card

ACLs will use the wildcard rule to check if the source / destination IP address matches a specific rule. This works in the opposite to a subnet mask (replace 1 with 0, 0 with 1). In this scenario, a '1' will represent a bit of an IP that should be compared against any existing ACL rules, whereas a '0' will represent a bit that should be ignored.

## Firewalls

A firewall is a system, or group of systems, that enforces an access control policy between networks. Firewalls prevent the exposure of sensitive hosts, resources and applications to untrusted users by sanitizing protocol flow, preventing the exploitation of protocol flaws. An IP table on hardware utilizing the Linux OS can be utilized as a firewall.

Firewalls will often be ran on both the host and the network, with the network acting as the front-line protection and the host firewall acting as a secondary back-up. Misconfiguring a firewall can lead to serious consequences, which is why it is beneficial to be certain about the security used.

### Firewall Zones

**Inside zone** is the most important part of the network, where devices are considered to consist of the most trusted and secured devices.

**Outside zone** consists of devices out of your immediate control (i.e. the internet), and due to this they are considered less secure and trusted.

Retrieving data from an outside zone to an inside zone is rarely prohibited, however vice versa (retrieving inside zone data from an outside zone) is usually much more heavily moderated in order to assist in minimalizing the threat of exploitation or attack.

A **Demilitarized Zone** is an additional network coming from the firewall that can work as an intermediary between your inside zone and outside zone adding an additional layer of security. By segregating the network using a DMZ, the DMZ will be facing the risk by interacting with the outside zone, whilst your trusted zone devices will only interact one way (outgoing) with the DMZ and outside zone. When considering network design using zones, the most secure devices should be able to access the less secure, but never vice versa.

![DMZ](images/DMZ.png)

### Policies

- **Allow List** (previously known as White-List): The firewall drops all packets except those specifically listed as acceptable.

- **Deny List** (previously known as Black-List): The firewall allows all packets except those specifically listed as unacceptable.

### Types

- **Packet Filtering** will filter both incoming and outgoing packets (packets from the same source will be treated differently incoming / outgoing) at the network and transport layer by comparing them against a set of rules.
- **Stateful Firewall** will inspect the packet header and state in order to determine which traffic to allow or disallow. Stateful firewalls are among the more common firewalls.
- **Proxy Firewall** operate on the Application layer and can be deployed between a remote user and a dedicated server on the internet. This is effective for shielding and filtering between public and private internal or protected networks. Proxy firewalls generally keep very detailed log, however they will also cause a performance hit on the speed.
- **Web Application Firewall (WAF)** are built to provide web applications security by applying a set of rules to a HTTP conversation. WAFs can be used to detected distributed denial of service attacks and protect against XSS.

### Delivery Methods

| Parameter                 | Network-based Firewall                                                           | Host-based Firewall                                                   |
|---------------------------|----------------------------------------------------------------------------------|-----------------------------------------------------------------------|
| Terminology               | Firewall filters traffic going from the Internet to secured LANs and vice versa. | A software or suite of applications installed on a singular computer. |
| Placement                 | At the perimeter or border of the network                                        | Placed at end host systems                                            |
| Hardware / Software-based | Hardware-based                                                                   | Software-based                                                        |
| Functions                 | At a network level                                                               | At a host level                                                       |
| Mobility                  | Cannot be moved until all the assets are move                                    | Mobility friendly                                                     |
| Network Protection        | Strong defence barrier                                                           | Limited defence barrier                                               |
| Scalability               | Easy to scale                                                                    | More effort required to scale                                         |
| Maintenance               | Manpower may be shared and limited                                               | Dedicated IT team required                                            |
| Skillset                  | Setup requires highly skilled resources                                          | Skillset of basic hardware / software                                 |
| Cost                      | Lower when it comes to large enterprises                                         | Higher when it comes to large enterprises                             |

## IDS and IPS

**Intrusion Detection System** is a tool utilized for monitoring the network and flagging unusual activity to an administrator. The key difference between a Firewall and IDS is the adaptability that IDS offers in it's monitoring. As opposed to strictly following rules like a Firewall, an IDS can flag events dynamically, such as a large number of pings on a port, whereas a Firewall will consider this standard activity if the port is enabled in the rules. IDS can be ran at both a network and host level.

**Intrusion Prevention System** is a control system that can not only detect intrusions, but can also accept or reject packets based on a configured ruleset. IPS is a continuation along the line of innovation in network security considered to be somewhat of a hybrid between an IDS and a Firewall, due to this IPS are generally favoured over IDS.

## Virtual Private Network (VPN)

A Virtual Privaite Network is a virtual connection between two networks that allows for tramsmittted data to be encrypted for security. This allows for a client to 'tunnel' into a private network by creating a virtual network in between the two exisinting networks (i.e. an office) allowing for enhanced security.

| Benefit        | Description                                                                                                                                                                                                                      |
|----------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Cost Savings   | With the advent of cost-effective, high-bandwidth technologies, organizations can use VPNs to reduce their connectivity costs while simultaneously increasing remote connection bandwidth.                                       |
| Security       | VPNs provide the highest level of security available, by usinng advanced encryption and authentication protocols that protect data from unaauthorized access.                                                                    |
| Scalability    | VPNs allow organizations to use the Internet, making it easy to add new users with adding significant infrastructure                                                                                                             |
| Compatability  | VPNs can be implemented across a wide variety of WAN link options including all the popular broadband technologies. Remote workers can take advantage of thee high-speed connections to gain secure access to corporate networks |

**VPN Protocols:**
- Point-to-Point Tunneling
- Generic Route Encapsulation
- Layer 2 Tunneling
- IP Security
- Secure Socket Layer

**Host-to-Host VPNs** allow for a client to virtually connect to another client privately across public networks.

**Host-To-Site VPNs** allow the client to virtually connect to a network's router gateway rather than a single mahcine. Allowing access to multiple devices / resources.

**Site-to-Site VPNs** allow for one network to form a virtual connection to another network privately across public networks. Allowing for multiple end-points to be able to tunnel into another network.
