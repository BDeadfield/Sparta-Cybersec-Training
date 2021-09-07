# Linux Networking Cheat Sheet

## Configuring IP Addresses and Routes

**Display IP Address** - Displays IP addresses on available interfaces.

> ip a

**Add IP Address** - Used for adding an IP address to an interface.

> sudo ip address add {x.x.x.x}/24 dev eth{x}

**Add Default Gateway** - Used for adding a default gateway to an end-device.

> sudo ip route add default via {x.x.x.x}

**Display Routes** - Used for showing traffic routes on an end-point or router.

> ip route

**Add Static Route** - Used for adding a static route to another network to a router.

> sudo ip route add {x.x.x.x/24} via {x.x.x.x}

## Configuring Firewall

**Delete Rules** - Removes existing firewall rules.

> sudo iptables -F

> sudo iptables -t nat -F

> sudo iptables -X

**Drop Packets by Default** - Sets the firewall to drop packets if another rule isn't determined

> sudo iptables -P FORWARD DROP

> sudo iptables -P INPUT DROP

> sudo iptables -P OUTPUT DROP

**Accept Traffic Rule** - Sets a new rule to allow traffic on the firewall

> sudo iptables -A FORWARD -p {protocol} --dport {port number} -s {x.x.x.x} -d {x.x.x.x} -j ACCEPT

*Allow associated traffic:* - Sets a rule to allow traffic associated with an allowed rule

> sudo iptables -A FORWARD -m conntrack  --ctstate ESTABLISHED,RELATED -j ACCEPT

## Configuring NAT

**Perfom NAT** - Sets the gateway to perform NAT on packets heading out on an inteface to an ISP router

> sudo iptables -t nat -A POSTROUTING -o eth{x} -j MASQUERADE

**Performing NAT on Destintation** - Sets the gateway on the destination router to route traffic

> sudo iptables -t nat -A PREROUTING -p {protocol} --dport {port number} -j DNAT --to-destination {x.x.x.x: port number}

> sudo iptables -t nat -A POSTROUTING -o eth{x} -j MASQUERADE

## Configuring VPN

**Establish VPN Connection** - Starts VPN service

> sudo openvpn --config {client / server}.conf -daemon

## Misc.

**Retrieve Web Page**

> wget http://x.x.x.x/

**Login to SSH** - Used for logging into an SSH server ('quit' to exit)

> ssh {accountname}@{x.x.x.x}

**Monitor Traffic** - Captures TCP / IP and other packets being received / transmitted

> sudo tcpdump -n -XX -i eth{x}
