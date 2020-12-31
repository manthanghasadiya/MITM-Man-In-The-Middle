# MITM-Man-In-The-Middle

Basic tools for a simple MITM attack.

The most common tools which are used in MITM are Arp Spoofer and Packet Sniffer. I provided both tools in this repository. BUt it will only work if both devices are connected on same network. You will get all URLs which target is searching on his/her device and if target try to login on http pages then you will also get the username and password of that target.

How to Use?

First you will have to run ArpSpoofer.py on your terminal.
  
  Open terminal where you downloaded this tool and type:
  
    >_*python3 ArpSpoofer.py -t x.x.x.x -g y.y.y.y*_
  
  Check **_python3 ArpSpoofer.py --help_** for more details.
  
Now open a new terminal and don't close the previous terminal where your Arp Spoofer is running,

  Open new terminal where you downloaded PacketSniffer.py and type:
  
    >_*python3 PacketSniffer.py*_
 
