# AWS

## Best Practice

- Naming Convention: groupID_projectName_username_resourceName
  - cyber94_calculator_oabu_server
  - cyber94_calculator_oabu_security_group
- Always stop the instances (servers) when not in use
- Delete resources when they are no longer needed

## AWS: Elastic Compute Cloud (EC2)

EC2 provides scalable computing capacity and works functionally like a virtual server. EC2 allows for flexible scalability as and when needed as well as allowing for the configuration of security, networking and storage.

**Amazon Machine Images (AMIs)** are used as templates containing software. These are utilized for creating servers.

**Key Pairs** consist of a private and a public key, which are used as a set of security credentials for the user to authenticate when connecting to an instance. When instances are created the public key is added to the instance, once the user wants to access the instance, the private key will be utilized.
