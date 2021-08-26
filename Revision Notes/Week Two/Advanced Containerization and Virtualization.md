# Advanced Containerization and Virtualization

## Vagrant

A tool for building and managing virtual machine environment in a single work flow. This helps to lower the environment development setup time by mirroring an installation. Vagrant depends on an external Hypervisor (such as, VirtualBox, Hyper-V and VMWare) in order to function.

Vagrant allows the user to create separate project environments utilizing different software / software versions on the same machine. This is achieved by mirroring directories from the physical machine and replicating them in a virtual machine.

### Usage

Go to desired directory or create a new one. Run 'vagrant init' followed by the desired operating system. For Ubuntu 18.04, the command 'vagrant init hashicorp/bionic64' will be utilized. You can find an online catalog of available Vagrant 'boxes' [here.](https://app.vagrantup.com/boxes/search)

After intializing Vagrant, a 'Vagrantfile' will be added to your directory. From here the Vagrant box can be configured in numerous different ways prior to finalizaiton, including network configurations and disabling auto-update ways. The configuration file can also be used in order to execute scripts. As an example this could be utilized to batch install packages to a virtual machine after intial installation. After completing configuration type 'vagrant up'. This will commence the download of the vagrant box OS after which it will be imported. After 'vagrant up' has finished, the virtual machine should now be visible to your hypervisor as well as listening for SSH connections. 'vagrant ssh' can be used to connect to the virtual machine via SSH.

The previously selected or created directory should be visible on the virtual machine under 'vagrant.' Files placed here will be visible on both host and guest machines. This project folder can also be connected to GitHub via GIT in order to simplify management as well as ensuring data redundancy.

Removing a snapshot (if available) can often help with issues when booting. If there's no snapshot available 'rm -rf .vagrant' can always be used from the project directory in order to remove the box software, after this running 'vagrant up' once again will give the user a fresh install on the virtual machine, whilst still maintaining the configuration file.

## Containers

A container is a piece of lightweight software that still bundles code, dependencies and configuration into a single image without the need for an OS. Containerization creates abstraction at an OS level that allows individal, modular, and distinct functionality of the app to run independently. Several isolated workloads (containers) can co-exist on a machine.

Where can containers be ran?
- Bare metal servers
- On top of Hypervisor
- In a cloud infrastructure

### Container vs Virtualization

A container will share the hardware and kernel from the host machine unlike viritualization, due to it's lack of operating system, however this allows the container image to be optimized down to be as lightweight as possible. When a container is set up on a host machine it does not isolate the harware that is shared, due to this it means that the entire host pc and containers will share the same vulnerabilities.

Containers are especially useful in the development, deployment and testing of modern distributed applications and microservices that can operate in isolated execution environments on the same host machine. The containers on the same host can be running different software and software whilst avoiding any conflicts.

### Docker

Docker is an open platform used for developing, shipping and running applications. An image will be used as a template when creating containers. Docker images are acquired from dockers library automatically, if missing locally when the user attempts to create a container.
