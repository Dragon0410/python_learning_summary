#!/usr/bin/python3
# -*- coding:utf-8 -*-
# author: 93207
# description: 
# datetime: 2022/3/25 20:51
# name: ip_check

import socket


def check_hostname_by_ip(host: dict):
    name, ip = host.get('hostname'), host.get('ip')

    hostname, alias, ips = socket.gethostbyaddr(ip)
    if hostname != name:
        return False
    return True


def check_ip_by_hostname(host: dict):
    name, ip = host.get('hostname'), host.get('ip')
    hostname, alias, ips = socket.gethostbyname_ex(name)
    if ips[0] != ip:
        print(f"根据 hostname({host.get('name')}) 查询到的 IP 与{host.get('ip')}不一致，更改 IP 为{ips[0]}")
        host[ip] = ips[0]
        return host
    return host


def available_host(host: dict):
    if check_hostname_by_ip(host) or not check_hostname_by_ip(host):
        return check_ip_by_hostname(host)


def main():
    # name 是需要添加域名的 hostname -A 查看
    host = {
        "ip": "192.168.38.132",
        "port": 22,
        "hostname": "192.168.38.132",
        "username": "king",
        "password": "wang3180",
    }
    new_host = available_host(host)
    print(new_host)

if __name__ == "__main__":
    main()
