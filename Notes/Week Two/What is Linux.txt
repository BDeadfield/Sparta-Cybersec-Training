# What is Linux? And, How Is It Used?

## Architecture

![Architecture](images/linuxArchitecture.png)

The kernel consists of drivers and libraries that interact with the hardware. Linux flavours will often share kernels. The shell works as an interface between the user and the kernel. Applications will consist of software such as a browser, emails, file explorer and games.

## Distribution

Distributions are different forms of the Linux OS that come with different configurations and software installed. These distributions are built with the aim of focusing on different purposes and user requirements. Certain distributions have been built using other distributions as a foundation. Different distributions will utilize different command syntax. Main distributions include:
- **Debian**
  - Ubuntu
  - Kali

- **Fedora**

  - Red Hat
  - CentOS

- **Arch Linux**

## Filesystem

Linux utilizes EXT4, EXT3, BTRFS, XFS. Mainly EXT4 and EXT3. Linux works on the concept that everything starts at the **root** and "Everything is a file". When a device, such as a camera is plugged into a Linux machine, it will be treated as a file allowing for a simple read / write dynamic.

![Root Folders](images/rootFolders.png)

Linux utilizes a different naming scheme than windows machine opting to utilize '/' (also known as root) rather than a lettering partitions. All files will originate from root. Administrative privileges in Linux are known as root privileges. This privilege can be temporarily obtained through the usage of the command 'sudo'.

Commands and names of files and directories are case sensitive.

'~$' is used to represent the user's home directory.

Hidden files start with "."

## Shell
The Linux shell is a text interface to your computer (kernel.) Often referred to as command line, terminal, console or prompt.

**Common console commands:**
- 'pwd' = print the current directory
- 'mkdir' = makes a new folder
- 'ls' = list folders in current directory
- 'type' = displays origin of command [1^]
- 'man' = displays a manual for a command
- 'cd' example/directory/here = change directory
- 'touch' = create a new blank file
- 'cat' = check contents of a file
- 'echo' = print output to screen [2^]
- '.' - points to current directory
- '..' - points to previous directory

[1^] whether the command is originating from shell or third-party

[2^] '>' can be used to send the output to a file.

## Editing

Editors are used in order to alter files. Linux comes with numerous editors, but the default will vary depending on distribution, however additional editors can be installed post-installation of Linux. Some popular editors include: 'nano', 'vi', and 'gedit'. Certain editors will require a graphical user interface in order to be utilized.

When listing files in a directory, the 'r','w','x' represents the permissions of the current user, group and other, also known as read, write and execute. A 'd' prior to listed permissions indicates that the file is a directory. Directly after displayed permissions there is a number used to represent how hard links point to the file. After this, the owner's name will be displayed and that owner's group. Followed by file size and date of last modification.

The 'chmod' command can be utilized in order to edit a files RWX permissions. The 'chown' command can be utilized in order to change the ownership of a file.

- R = 4
- W = 2
- X = 1

You are able to set the permissions for a group by totalling each number relative to whether the permission is allowed, and concatenating the results.

| User | Group | Other |
| ---- | ----- | ----- |
| 421  | 421   | 421   |
| rwx  | rwx   | rwx   |
| 7    | 7     | 7     |

In this scenario permissions are enabled for read, write and execute on the user, therefore this will be represented by "7" (4 + 2 + 1). The same goes for group and other, therefore they will also be represented by '7'. This means that 'chmod 777' will enable all permissions across each of the three groups.


| User | Group | Other |
| ---- | ----- | ----- |
| 421  | 421   | 421   |
| r-x  | r-x   | r-x   |
| 5    | 5     | 5     |

Whilst 'chmod 555' would alter a file to give the user, group and other read and execute permissions, but not write.

| User | Group | Other |
| ---- | ----- | ----- |
| 421  | 421   | 421   |
| rwx  | ---   | ---   |
| 7    | 0     | 0     |

'chmod 700' would edit a file, so that a user would have full permissions, whilst the group and other would have zero permissions.
