### **General Linux Commands**

| **Command** | **Description** |
|-------------|-----------------|
| `ls`                     | List files and directories. |
| `cd <directory>`          | Change directory. |
| `pwd`                    | Print the current working directory. |
| `cp <source> <destination>` | Copy files or directories. |
| `mv <source> <destination>` | Move or rename files or directories. |
| `rm <file>`              | Remove files. |
| `rm -r <directory>`      | Remove directories recursively. |
| `mkdir <directory>`      | Create a new directory. |
| `rmdir <directory>`      | Remove an empty directory. |
| `touch <file>`           | Create a new file or update its timestamp. |
| `cat <file>`             | Display the contents of a file. |
| `more <file>`            | View file content page by page. |
| `less <file>`            | View file content page by page (allows backward navigation). |
| `head <file>`            | View the first 10 lines of a file. |
| `tail <file>`            | View the last 10 lines of a file. |
| `tail -f <file>`         | View live updates of a file (like log files). |
| `chmod <permissions> <file>` | Change file permissions. |
| `chown <owner>:<group> <file>` | Change file owner and group. |
| `find <path> -name <pattern>` | Search for files by name. |
| `grep <pattern> <file>`  | Search for a pattern within a file. |
| `df -h`                  | Display disk space usage in human-readable format. |
| `du -sh <directory>`     | Display the size of a directory in human-readable format. |
| `top`                    | Display running processes and system usage. |
| `ps`                     | Display running processes. |
| `kill <PID>`             | Terminate a process by process ID. |
| `history`                | Show command history. |
| `clear`                  | Clear the terminal screen. |
| `alias <shortcut>=<command>` | Create an alias for a command. |
| `uname -a`               | Show system information. |
| `man <command>`          | Display the manual page for a command. |
| `which <command>`        | Show the path to a command. |
| `echo <text>`            | Display text. |
| `export <variable>=<value>` | Set environment variables. |
| `scp <source> <user@host>:<destination>` | Securely copy files to a remote system. |
| `rsync -av <source> <destination>` | Sync files between directories. |
| `ssh <user@host>`        | Securely connect to a remote system. |
| `sudo <command>`         | Execute a command as superuser. |
| `apt-get update`         | Update the package list (Debian-based). |
| `apt-get upgrade`        | Upgrade installed packages. |
| `yum install <package>`  | Install packages (RedHat-based). |
| `tar -cvf <archive.tar> <directory>` | Archive a directory. |
| `tar -xvf <archive.tar>` | Extract a tar archive. |
| `zip <archive.zip> <file>` | Compress files into a zip archive. |
| `unzip <archive.zip>`    | Extract files from a zip archive. |
| `curl <URL>`             | Transfer data from or to a server. |
| `wget <URL>`             | Download files from the web. |
| `ping <host>`            | Check the network connection to a host. |
| `traceroute <host>`      | Trace the network path to a host. |
| `ifconfig`               | Display network interfaces. |
| `netstat -tuln`          | Show active network connections. |
| `iptables`               | Configure network packet filtering. |

---

### **Vim/Vi Commands**
| **Command** | **Description** |
|-------------|-----------------|
| `vi <file>` / `vim <file>` | Open a file in Vi/Vim. |
| `i`                         | Enter **insert mode** to edit text. |
| `Esc`                       | Exit insert mode and return to command mode. |
| `:w`                        | Save the file. |
| `:q`                        | Quit the editor. |
| `:wq`                       | Save and quit. |
| `:q!`                       | Quit without saving changes. |
| `u`                         | Undo the last change. |
| `Ctrl + r`                  | Redo the last undone change. |
| `dd`                        | Delete the current line. |
| `yy`                        | Yank (copy) the current line. |
| `p`                         | Paste below the current line. |
| `:%s/old/new/g`             | Search and replace all instances of 'old' with 'new'. |
| `:set number`               | Show line numbers. |

---

### **Neovim Commands**
| **Command** | **Description** |
|-------------|-----------------|
| `nvim <file>`              | Open a file in Neovim. |
| `:PlugInstall`             | Install plugins (requires **vim-plug**). |
| `:checkhealth`             | Check the health of the Neovim environment. |
| `:Telescope find_files`    | Use **Telescope** to find files. |
| `:LspInstall`              | Install LSP (Language Server Protocol). |

---

### **Nano Commands**
| **Command** | **Description** |
|-------------|-----------------|
| `nano <file>`           | Open a file in Nano. |
| `Ctrl + O`              | Save the file. |
| `Ctrl + X`              | Exit Nano. |
| `Ctrl + W`              | Search for text. |
| `Ctrl + K`              | Cut the current line. |
| `Ctrl + U`              | Paste (uncut) the last cut line. |
| `Ctrl + J`              | Justify (reformat) text. |
| `Ctrl + C`              | Show cursor position. |
| `Ctrl + \`              | Search and replace text. |
| `Alt + U`               | Undo the last action. |
| `Alt + E`               | Redo the last undone action. |

---

### **AWS CLI Commands**
| **Command** | **Description** |
|-------------|-----------------|
| `aws configure`            | Configure AWS credentials (access key, secret key, region). |
| `aws s3 ls`                | List S3 buckets and files. |
| `aws s3 cp <source> <destination>` | Copy files to/from S3. |
| `aws ec2 describe-instances` | List EC2 instances. |
| `aws ec2 start-instances --instance-ids <ID>` | Start an EC2 instance. |
| `aws ec2 stop-instances --instance-ids <ID>` | Stop an EC2 instance. |
| `aws ec2 reboot-instances --instance-ids <ID>` | Reboot an EC2 instance. |
| `aws ec2 terminate-instances --instance-ids <ID>` | Terminate an EC2 instance. |
| `aws ec2 create-key-pair --key-name <key_name>` | Create an EC2 key pair. |
| `aws s3 sync <source> s3://<bucket-name>` | Sync local files to S3 bucket. |
| `aws lambda list-functions` | List all AWS Lambda functions. |
| `aws cloudwatch get-metric-data` | Get CloudWatch metric data. |

---

### **Azure CLI Commands**
| **Command** | **Description** |
|-------------|-----------------|
| `az login`                | Login to Azure account. |
| `az group create --name <group> --location <location>` | Create a resource group. |
| `az vm create --resource-group <group> --name <vm-name> --image <image>` | Create a virtual machine. |
| `az vm list`              | List all virtual machines. |
| `az vm start --name <vm-name> --resource-group <group>` | Start a virtual machine. |
| `az vm stop --name <vm-name> --resource-group <group>` | Stop a virtual machine. |
| `az vm delete --name <vm-name> --resource-group <group>` | Delete a virtual machine. |
| `az storage account create --name <account> --resource-group <group> --location <location>` | Create a storage account. |
| `az storage blob upload --account-name <account> --container-name <container> --name <blob-name> --file <file>` | Upload a blob to Azure Storage. |
| `az group delete --name <group>` | Delete a resource group. |
| `az aks create --resource-group <group> --name <cluster-name> --node-count <count>` | Create a Kubernetes cluster on Azure. |
| `az aks get-credentials --resource-group <group> --name <cluster-name>` | Get Kubernetes credentials for AKS cluster. |

---

### **GCP gcloud Commands**
| **Command** | **Description** |
|-------------|-----------------|
| `gcloud init`            

 | Initialize GCP and authenticate the account. |
| `gcloud compute instances list` | List all compute instances. |
| `gcloud compute instances start <instance-name>` | Start a Compute Engine instance. |
| `gcloud compute instances stop <instance-name>` | Stop a Compute Engine instance. |
| `gcloud compute ssh <instance-name>` | SSH into a Compute Engine instance. |
| `gcloud compute instances create <name> --zone <zone> --machine-type <type> --image <image>` | Create a new Compute Engine instance. |
| `gcloud projects list`    | List all projects. |
| `gcloud config set project <project-id>` | Set the active project. |
| `gcloud iam service-accounts create <name>` | Create a new service account. |
| `gcloud app deploy`       | Deploy an application to Google App Engine. |
| `gcloud functions deploy <function-name>` | Deploy a Cloud Function. |
| `gcloud functions list`   | List all Cloud Functions. |

---

### **File Permissions and Ownership**
| **Command** | **Description** |
|-------------|-----------------|
| `chmod`     | Change file permissions. |
| `chown`     | Change file owner and group. |
| `ls -l`     | View file permissions in detail. |
| `umask`     | Set default file permissions for newly created files. |

---

### **Disk Usage and Management**
| **Command** | **Description** |
|-------------|-----------------|
| `df`        | Report file system disk space usage. |
| `du`        | Show disk usage of files and directories. |
| `mount`     | Mount a file system. |
| `umount`    | Unmount a file system. |
| `fdisk`     | Partition a disk. |

---

### **System Monitoring**
| **Command** | **Description** |
|-------------|-----------------|
| `top`       | Display real-time system processes. |
| `htop`      | An improved version of top (needs to be installed). |
| `ps`        | Report current processes. |
| `uptime`    | Show how long the system has been running. |
| `free`      | Display memory usage. |
| `df -h`     | Show disk usage in human-readable format. |
| `kill`      | Terminate a process by its PID. |

---

### **Networking**
| **Command** | **Description** |
|-------------|-----------------|
| `ping`      | Check connectivity to a host. |
| `ifconfig`  | Configure network interfaces (deprecated, use `ip` command). |
| `ip a`      | Show IP addresses assigned to network interfaces. |
| `netstat`   | Display network connections, routing tables, etc. |
| `ss`        | More modern and detailed network statistics than `netstat`. |
| `scp`       | Securely copy files between hosts. |
| `curl`      | Transfer data from or to a server. |
| `wget`      | Download files from the web. |

---

### **Package Management (Ubuntu/Debian)**
| **Command** | **Description** |
|-------------|-----------------|
| `apt-get update` | Update package lists. |
| `apt-get upgrade` | Upgrade installed packages. |
| `apt-get install <package>` | Install a package. |
| `apt-get remove <package>` | Remove a package. |
| `apt-cache search <keyword>` | Search for a package. |

---

### **Compression and Archiving**
| **Command** | **Description** |
|-------------|-----------------|
| `tar -cvf`  | Create an archive (tarball). |
| `tar -xvf`  | Extract an archive. |
| `gzip`      | Compress a file using gzip. |
| `gunzip`    | Decompress a file using gzip. |
| `zip`       | Compress files into a zip archive. |
| `unzip`     | Extract a zip archive. |

---

### **User Management**
| **Command** | **Description** |
|-------------|-----------------|
| `adduser`   | Add a new user. |
| `deluser`   | Remove a user. |
| `passwd`    | Change a user password. |
| `whoami`    | Show the current user. |
| `sudo`      | Execute a command as another user, typically as root. |
| `su`        | Switch user accounts. |

---

### **System Information**
| **Command** | **Description** |
|-------------|-----------------|
| `uname -a`  | Show system information. |
| `hostname`  | Display or set the system’s hostname. |
| `dmesg`     | View kernel messages. |
| `lscpu`     | Display CPU architecture information. |
| `lsblk`     | Show information about block devices (disks). |
| `cat /etc/os-release` | Display operating system details. |

---

### **Text Manipulation**
| **Command** | **Description** |
|-------------|-----------------|
| `grep`      | Search for patterns in files. |
| `sed`       | Stream editor for modifying files. |
| `awk`       | Pattern scanning and processing language. |
| `sort`      | Sort lines of text files. |
| `wc`        | Count lines, words, and characters in a file. |
| `cut`       | Remove sections from each line of files. |

---

### **Process Management**
| **Command** | **Description** |
|-------------|-----------------|
| `ps aux`    | List all processes. |
| `kill <PID>`| Terminate a process by PID. |
| `killall <name>` | Kill processes by name. |
| `bg`        | Resume a suspended job in the background. |
| `fg`        | Bring a job to the foreground. |
| `jobs`      | List active jobs. |

---

### **Miscellaneous**
| **Command** | **Description** |
|-------------|-----------------|
| `history`   | Show command history. |
| `alias`     | Create a shortcut for a command. |
| `date`      | Display the current date and time. |
| `clear`     | Clear the terminal screen. |
| `echo`      | Print text or variables to the terminal. |
| `man <command>` | Display the manual page for a command. |

---

### **Redirection and Pipes**
| **Command** | **Description** |
|-------------|-----------------|
| `>`         | Redirect output to a file, overwriting it. |
| `>>`        | Append output to a file. |
| `2>`        | Redirect errors. |
| `|`         | Pipe output from one command to another. |

---

### **SSH and Remote Access**
| **Command** | **Description** |
|-------------|-----------------|
| `ssh user@host` | Connect to a remote server using SSH. |
| `ssh-keygen`    | Generate SSH keys. |
| `rsync`         | Sync files and directories between two locations over SSH. |

---

### **Advanced File Operations**
| **Command** | **Description** |
|-------------|-----------------|
| `ln -s <target> <link>` | Create a symbolic (soft) link to a file or directory. |
| `ln <target> <link>`     | Create a hard link to a file. |
| `stat <file>`            | Display detailed information about a file or directory. |
| `diff <file1> <file2>`   | Compare the contents of two files. |
| `sort <file>`            | Sort lines of text in a file. |
| `uniq <file>`            | Report or omit repeated lines. |
| `file <file>`            | Determine the file type. |
| `truncate -s <size> <file>` | Shrink or extend the size of a file. |
| `head -n <number> <file>` | Display the first n lines of a file. |
| `tail -n <number> <file>` | Display the last n lines of a file. |

---

### **Advanced Search**
| **Command** | **Description** |
|-------------|-----------------|
| `locate <file>`        | Quickly find files by name. |
| `grep -r <pattern> <dir>` | Recursively search for a pattern in a directory. |
| `find <path> -name <name>` | Find files by name in a directory. |
| `find <path> -type f -size +100M` | Find files larger than 100 MB. |
| `grep -i <pattern> <file>` | Search for a pattern in a file (case-insensitive). |
| `grep -v <pattern> <file>` | Exclude lines matching a pattern. |
| `grep -o <pattern> <file>` | Show only matched parts of lines. |

---

### **Disk Management**
| **Command** | **Description** |
|-------------|-----------------|
| `lsblk`        | List information about all available block devices. |
| `fdisk -l`     | List disk partitions. |
| `mkfs.ext4 <partition>` | Format a partition with the ext4 filesystem. |
| `e2fsck <partition>` | Check and repair ext4 filesystems. |
| `resize2fs <partition>` | Resize an ext4 filesystem. |
| `dd if=<source> of=<destination>` | Copy data from one file or device to another. |
| `parted`       | Partition a hard disk. |
| `fsck`         | Check the integrity of a filesystem. |
| `mount /dev/sdX /mnt` | Mount a partition. |
| `umount /mnt`  | Unmount a partition. |

---

### **System Performance Monitoring**
| **Command** | **Description** |
|-------------|-----------------|
| `vmstat`       | Display system memory, processes, and CPU usage. |
| `iostat`       | Report CPU and I/O statistics. |
| `sar`          | Collect, report, or save system activity information. |
| `dstat`        | Show system resource usage over time. |
| `iotop`        | Monitor disk I/O usage by processes. |
| `mpstat`       | Report per-processor or processor core statistics. |
| `uptime`       | Show system uptime and load average. |
| `nmon`         | A performance monitor for CPU, memory, disk, and network (needs installation). |
| `perf`         | Collect performance data from the Linux kernel. |

---

### **Log File Management**
| **Command** | **Description** |
|-------------|-----------------|
| `tail -f <file>` | Continuously view new log file entries. |
| `journalctl`     | Query systemd logs. |
| `dmesg | less`   | View kernel logs. |
| `logger "message"` | Write a message to the system log. |
| `logrotate`      | Rotate, compress, and manage log files. |
| `last`           | Show the last logins of users. |
| `who`            | Show who is currently logged in. |

---

### **Cron Jobs (Scheduled Tasks)**
| **Command** | **Description** |
|-------------|-----------------|
| `crontab -e`    | Edit the crontab file to create scheduled tasks. |
| `crontab -l`    | List the current user's crontab entries. |
| `crontab -r`    | Remove the current user's crontab. |
| `systemctl start cron` | Start the cron service. |
| `systemctl enable cron` | Enable cron to start at boot. |

---

### **Package Management (RedHat/CentOS)**
| **Command** | **Description** |
|-------------|-----------------|
| `yum update`        | Update all installed packages. |
| `yum install <package>` | Install a package. |
| `yum remove <package>`  | Remove a package. |
| `yum search <package>`  | Search for a package. |
| `rpm -ivh <package.rpm>` | Install an RPM package. |
| `rpm -qa`          | List all installed RPM packages. |

---

### **User and Group Management**
| **Command** | **Description** |
|-------------|-----------------|
| `useradd <username>` | Create a new user account. |
| `usermod -aG <group> <user>` | Add a user to a group. |
| `groupadd <groupname>` | Create a new group. |
| `groups <user>` | Show groups a user belongs to. |
| `passwd <user>` | Change a user’s password. |
| `deluser <username>` | Delete a user account. |
| `delgroup <groupname>` | Delete a group. |

---

### **Archive and Backup Tools**
| **Command** | **Description** |
|-------------|-----------------|
| `tar -czvf <file>.tar.gz <directory>` | Create a compressed tar archive. |
| `tar -xzvf <file>.tar.gz` | Extract a compressed tar archive. |
| `rsync -av <source> <destination>` | Synchronize files between directories or systems. |
| `dd if=<source> of=<destination>` | Create a byte-by-byte copy of a disk or partition. |
| `scp <file> user@host:<path>` | Securely copy files between hosts. |
| `rclone` | Sync files and directories to and from cloud storage. |

---

### **Shell Customization**
| **Command** | **Description** |
|-------------|-----------------|
| `alias ll='ls -la'` | Create an alias for commands. |
| `unalias ll`        | Remove an alias. |
| `export PATH=$PATH:/new/path` | Add a directory to your PATH. |
| `. ~/.bashrc`       | Reload the bash configuration file. |
| `history -c`        | Clear the terminal history. |
| `source <file>`     | Execute commands from a file in the current shell. |

---

### **Security and Permissions**
| **Command** | **Description** |
|-------------|-----------------|
| `ssh-keygen`        | Generate SSH keys. |
| `chmod 755 <file>`  | Set read, write, and execute permissions for owner, and read and execute for others. |
| `chown user:group <file>` | Change the owner and group of a file. |
| `ufw enable`        | Enable UFW (Uncomplicated Firewall). |
| `ufw allow <port>`  | Allow incoming traffic on a port. |
| `ufw status`        | Check UFW status and rules. |
| `iptables -L`       | List firewall rules. |
| `gpg --gen-key`     | Generate a GPG encryption key. |
| `gpg -c <file>`     | Encrypt a file. |
| `gpg -d <file>`     | Decrypt a file. |

---

### **System Recovery and Rescue**
| **Command** | **Description** |
|-------------|-----------------|
| `fsck /dev/sda1`    | Check and repair a file system. |
| `mount -o remount,rw /` | Remount the root filesystem as read-write in recovery mode. |
| `chroot /mnt`       | Change the root directory to recover a broken system. |
| `grub-install /dev/sda` | Reinstall GRUB bootloader. |
| `passwd`            | Reset the root password. |

--

### **Networking Advanced**
| **Command** | **Description** |
|-------------|-----------------|
| `ip link`          | Display or manipulate network interfaces. |
| `ip addr show`     | Show IP addresses assigned to interfaces. |
| `ip route`         | Display or manipulate the routing table. |
| `nmcli`            | Control NetworkManager from the command line. |
| `nmap`             | Network exploration tool and security/port scanner. |
| `traceroute <host>`| Trace the route packets take to a host. |
| `whois <domain>`   | Retrieve domain information. |
| `dig <domain>`     | Query DNS for information about a domain. |
| `tcpdump`          | Capture network traffic. |

---

### **Virtualization and Containers**
| **Command** | **Description** |
|-------------|-----------------|
| `docker run <image>` | Run a Docker container. |
| `docker ps`          | List running Docker containers. |
| `docker build -t <image> <directory>` | Build a Docker image from a Dockerfile. |
| `docker-compose up`  | Start services defined in a Docker Compose file. |
| `vagrant up`         | Start a Vagrant virtual machine. |
| `virt-manager`       | Manage virtual machines through a graphical interface. |
| `virsh list`         | List running virtual machines in libvirt. |
