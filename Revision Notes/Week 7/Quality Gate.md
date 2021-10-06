# Quality Gate

## Personal

**T.M.A.Y**

- I would describe myself as ambitious, as I always enjoy learning new things both in theory and pratical.

- I've always had a passion and curiosity for technology from an early age stemming from video games.

- Prior to formally studying IT, I had already begun to develop my skills around OS and Web Development.

- It was around this time that I had decided I would like to build a better understanding of both security and computer language.

- I am a recent graduate of Sheffield Hallam University in Computer and Information Security.

- During my time spent at university I was able to develop and strengthen new skills in areas such as networking, penetration testing and OOP programming.

- In my last year I worked on general cybersecurity frameworks such as ISO-270001 and NIST. (used for managing and minimizing security risks)

- On top of this, I was able to work on my goal of becoming more socially confident, as well as self-improvement in general.

**Why Cyber Security?**

- I’ve always found enjoyment out of discovering how things work and resolving technical issues

- Naturally I found myself intrigued by the security sector of IT as I believe it makes for a great foundation to expand from.

- As well as it's ever-growing size and presence in day to day life.

- Which is why I decided to study Computer Security and intend to continue to branch out my knowledge and skills

**Tell me about your time at Sparta**

- Since joining Sparta, we have studied a wide variety of topics, working from the foundation upwards and branching them together.

- Essentially starting with operating system architecutre and interacting with the system.

- Moving onwards to communication including the hardware, methodology and topologies

- In addition to this we have worked on software development using OOP and how we could implement them in diffent environments, such as containers.

- And, we've recently gone on to cover different methods of securing communications as well as software.

## Technical

### Security Basics

![Security Cube](https://upload.wikimedia.org/wikipedia/en/0/0a/McCumber_cube.jpg)

**Data:**

- Storage – Or, Data at Rest (DAR) is data in an information system, such as that stored on memory, a magnetic tape or disk.
- Transmission – Transferring data between two systems, also known as Data in Transit (DAT)
- Processing – Performing operation on data in order to achieve a desired objective

**Safeguards:**
- Policies & practices – administrative controls, also referred to as operations
- Human factors – Considering how users will behave around a system or any potential human errors that could occur, also referred to as personnel
- Technology – Software and hardware-based solutions

**Kill Chain:**

1. Reconnaissance
2. Weaponization
3. Delivery
4. Exploitation
5. Installation
6. Command and controls
7. Action on Objectives

### Architecture

Read = 4 | Write = 2 | Execute = 1

**Vagrant** can be used to replicate virtual environemnts by mirroring a folder, which could be created on the host OS and shared to a virtual machine.

### Networking

**Internet** is a large network utilized to connect devices across the world, including both public and private networks.

**Intranet** is a connection between several LANs that allow devices to connect to machines / services on a large private network.

**Extranet** similar to Intranet, is a private network, however partial resources are available to specific authorized users.

**Ephemeral Ports** are dynamic ports that servers use to reply back to clients. These ports are after the reserved ports (1023).

**HTTP:** 80 | **HTTPS:** 443 | **FTP:** 21 & 20 | **SSH:** 22 | **Telnet:** 23 | **RDP:** 3389 | **DNS:** 53

In a **Legacy Classful Addressing** system there are five different classes (A - E) used to represent different groups of IP addresses. For each class, there is a different requirement of how many bits need to be identified in order to identify the network portion from the host portion.

- Class A = 0.0.0.0 to 127.255.255.255 (0) - The first octet is used to identify the network portion of the address.
- Class B = 128.0.0.0 to 191.255.255.255 (10) - The first two octets are used to identify the network portion of the address.
- Class C = 192.0.0.0 to 223.255.255.255 (110) - The first three octets are used to identify the network portion of the address.
- Class D = 224.0.0.0 to 239.255.255.255 (1110) - The class D addresses can be assigned in order to use multicast.
- Class E = 240.0.0.0 to 255.255.255.255 (1111) - The class E addresses are experimental addresses and are not intended to be used.

![TCP/IP](https://i.imgur.com/p8BMbjQ.png)

Data will add transport header, add network header, add frame header. The process will be reversed by reciever.

### OOP

**Python** is a general purose OOP language that has a focus on code readability

- **Encapsulation:** is when an object remains private within a class, however it's public functions, known as methods, can stil be called.

- **Inheritance:** is the ability for one or more objects to acquire properties from a parent object

- **Polymorphism:** is where a function can be utilized differently based on a class it's in.

- **Abstraction:** is similar to encapsulation, but allows the user to
define the methods when calling inheritors (i.e class is move | function is bird = fly | function is dog = walk)

### Misc.

**Cookie** uses small amount of data, expires on logout
**Token** uses large amount of data, has a set expiry date

**Agile** is a framework used to help teams manage projects, roles and communication. Used in order to modernize software development. Using Agile allows software developers to deliver quicker results with more room for adaptation along the way

**SCRUM** is an iteration on Agile that is focused on communication and coordination between team members.

**Scrum Pillars:**
- Transparency
- Inspection
- Adaptation
