# Network Address Translation (NAT)

Due to a lack of public IPv4 addresses to assign unique addresses to each device connected to the internet private IPv4 addresses are used within organizations or sites in order to allow devices to communicate locally. Private IPv4 addresses are not available to be used on the Internet (these include: 10.0.0.0/8, 172.16.0.0/12, and 192.168.0.0/16).

In order to allow a device with a private IPv4 address to access devices / resources outside of the local network, the private address must first be translated to a public address. NAT is used in order to provide this translation. This allows for a single public IPv4 can be shared by multiple devices using private IPv4 addresses. The NAT process will be handled by the router before connecting outside the local network, however certain ISPs will also handle NAT at their gateway before the Internet.

## Types of NAT

**Static** uses one-to-one mapping of local and global addresses. This can be beneficial in attempting to hide a network's design structure from the public.

**Dynamic** uses a pool of public address and assigns them on a first-come, first-served basis.

**Port Address Translation (PAT)** also known as NAT overload, maps multiple private IPv4 addresses to a single public IPv4 address or a few addresses. PAT utilizes a table of stored outgoing connections and their ports then utilizes these listings to organize incoming connections back to the destination point. A router utilizing PAT will assign a new port when forwarding a request from a client.
