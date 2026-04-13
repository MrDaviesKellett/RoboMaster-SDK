# -*-coding:utf-8-*-
# Copyright (c) 2020 DJI.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License in the file LICENSE.txt or at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


import ipaddress
import socket

import psutil


def get_local_ipv4_subnets(local_ip=None, prefixlen=24):
    """Return local IPv4 subnets limited to the requested prefix length."""
    subnets = []
    addr_list = []
    seen = set()
    target_broadcast = None
    if local_ip:
        target_broadcast = "{0}.255".format(local_ip.rsplit(".", 1)[0])

    for nic_addrs in psutil.net_if_addrs().values():
        for nic_addr in nic_addrs:
            if nic_addr.family != socket.AF_INET:
                continue
            if not nic_addr.address or not nic_addr.netmask:
                continue
            if target_broadcast and nic_addr.broadcast != target_broadcast:
                continue

            try:
                network = ipaddress.IPv4Network((nic_addr.address, nic_addr.netmask), strict=False)
            except ValueError:
                continue

            if network.prefixlen != prefixlen:
                continue

            subnet = (str(network.network_address), nic_addr.netmask)
            if subnet in seen:
                continue

            seen.add(subnet)
            subnets.append(subnet)
            addr_list.append(nic_addr.address)

    return subnets, addr_list


def get_ipv4_hosts(subnet, netmask):
    """Return all usable IPv4 host addresses for the given subnet."""
    network = ipaddress.IPv4Network((subnet, netmask), strict=False)
    return [str(host) for host in network.hosts()]
