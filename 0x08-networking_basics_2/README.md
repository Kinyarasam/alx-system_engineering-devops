# 0x08. Networking basics #1

`DevOps`  `Network`  `SysAdmin`

## Resources
#### Read or watch:

- [What is localhost](https://en.wikipedia.org/wiki/Localhost)
- [What is 0.0.0.0](https://en.wikipedia.org/wiki/0.0.0.0)
- [What is the hosts file](https://www.makeuseof.com/tag/modify-manage-hosts-file-linux/)
- [Netcat examples](https://www.thegeekstuff.com/2012/04/nc-command-examples/)

#### man or help:
- `ifconfig`
- `telnet`
- `nc`
- `cut`


## Learning Objectives
At the end of this project, you are expected to be able to [explain to anyone](https://fs.blog/feynman-learning-technique/), __without the help of Google__:

### General
* What is the localhost/127.0.0.1
* What is 0.0.0.0
* What is /etc/hosts
* How to display your machine's active network interfaces

## Requirements
### General
- Allowed editors: `vi`, `vim`, `emacs`
- All your files will be interpreted on Ubuntu 20.04 LTS
- All your files should end with a new line
- A `README.md` file, at the root of the folder of the project, is mandatory
- All your Bash script files must be executable
- The first line of all your Bash scripts should be exactly `#!/usr/bin/env bash`
- The second line of all your Bash scripts should be a comment explaining what is the script doing

## Files and Folders
The files in this folder are scripts written in Bash and executed on Ubuntu 20.04 LTS

| Files | Description |
|-------|-------------|
|[0. Change your home IP](./0-change_your_home_IP)|Configures an Ubuntu server with given specifications|
|[1. Show attached IPs](./1-show_attached_IPs)|Displays all active IPv4 IPs on the machine it’s executed on.|
