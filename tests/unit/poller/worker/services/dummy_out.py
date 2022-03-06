import numpy as np

interface_out = [
    {
        "sqvers": 3.0,
        "ifindex": 1,
        "reason": "",
        "routeDistinguisher": "",
        "macaddr": "00:00:00:00:00:00",
        "interfaceMac": "",
        "type": "loopback",
        "description": "",
        "numChanges": 0,
        "speed": 0,
        "vlan": 0,
        "innerVlan": 0,
        "vlanName": "",
        "ipAddressList": np.array(["127.0.0.1/8"]),
        "srcVtepIp": "",
        "state": "up",
        "adminState": "up",
        "master": "",
        "ifname": "lo",
        "statusChangeTimestamp": 0.0,
        "vni": 0,
        "ip6AddressList": np.array(["::1/128"]),
        "lacpBypass": False,
        "mtu": 65536,
        "hostname": "leaf01",
        "namespace": "vagrant",
        "timestamp": 1644778941900,
        "active": True,
    },
    {
        "sqvers": 3.0,
        "ifindex": 3,
        "reason": "",
        "routeDistinguisher": "",
        "macaddr": "52:54:00:36:2a:a8",
        "interfaceMac": "",
        "type": "ethernet",
        "description": "",
        "numChanges": 0,
        "speed": 4294967295,
        "vlan": 0,
        "innerVlan": 0,
        "vlanName": "",
        "ipAddressList": np.array(['10.0.0.1/24', '192.168.16.1/24']),
        "srcVtepIp": "",
        "state": "down",
        "adminState": "down",
        "master": "",
        "ifname": "swp1",
        "statusChangeTimestamp": 0.0,
        "vni": 0,
        "ip6AddressList": np.array([]),
        "lacpBypass": False,
        "mtu": 1500,
        "hostname": "leaf01",
        "namespace": "vagrant",
        "timestamp": 1644778941900,
        "active": True,
    },
    {
        "sqvers": 3.0,
        "ifindex": 4,
        "reason": "",
        "routeDistinguisher": "",
        "macaddr": "52:54:00:ef:4c:1f",
        "interfaceMac": "",
        "type": "ethernet",
        "description": "",
        "numChanges": 0,
        "speed": 4294967295,
        "vlan": 0,
        "innerVlan": 0,
        "vlanName": "",
        "ipAddressList": np.array(['10.0.0.2/24', '192.168.16.2/24']),
        "srcVtepIp": "",
        "state": "down",
        "adminState": "down",
        "master": "",
        "ifname": "swp2",
        "statusChangeTimestamp": 0.0,
        "vni": 0,
        "ip6AddressList": np.array([]),
        "lacpBypass": False,
        "mtu": 1500,
        "hostname": "leaf01",
        "namespace": "vagrant",
        "timestamp": 1644778941900,
        "active": True,
    },
    {
        "sqvers": 3.0,
        "ifindex": 5,
        "reason": "",
        "routeDistinguisher": "",
        "macaddr": "52:54:00:e8:65:29",
        "interfaceMac": "",
        "type": "ethernet",
        "description": "",
        "numChanges": 0,
        "speed": 4294967295,
        "vlan": 0,
        "innerVlan": 0,
        "vlanName": "",
        "ipAddressList": np.array(['10.0.0.3/24', '192.168.16.3/24']),
        "srcVtepIp": "",
        "state": "down",
        "adminState": "down",
        "master": "",
        "ifname": "swp3",
        "statusChangeTimestamp": 0.0,
        "vni": 0,
        "ip6AddressList": np.array([]),
        "lacpBypass": False,
        "mtu": 1500,
        "hostname": "leaf01",
        "namespace": "vagrant",
        "timestamp": 1644778941900,
        "active": True,
    },
    {
        "sqvers": 3.0,
        "ifindex": 6,
        "reason": "",
        "routeDistinguisher": "",
        "macaddr": "52:54:00:1b:7b:95",
        "interfaceMac": "",
        "type": "ethernet",
        "description": "",
        "numChanges": 0,
        "speed": 4294967295,
        "vlan": 0,
        "innerVlan": 0,
        "vlanName": "",
        "ipAddressList": np.array(['10.0.0.4/24', '192.168.16.4/24']),
        "srcVtepIp": "",
        "state": "down",
        "adminState": "down",
        "master": "",
        "ifname": "swp4",
        "statusChangeTimestamp": 0.0,
        "vni": 0,
        "ip6AddressList": np.array([]),
        "lacpBypass": False,
        "mtu": 1500,
        "hostname": "leaf01",
        "namespace": "vagrant",
        "timestamp": 1644778941900,
        "active": True,
    },
    {
        "sqvers": 3.0,
        "ifindex": 7,
        "reason": "",
        "routeDistinguisher": "",
        "macaddr": "48:47:00:70:c9:db",
        "interfaceMac": "",
        "type": "ethernet",
        "description": "",
        "numChanges": 0,
        "speed": 4294967295,
        "vlan": 0,
        "innerVlan": 0,
        "vlanName": "",
        "ipAddressList": np.array([]),
        "srcVtepIp": "",
        "state": "down",
        "adminState": "down",
        "master": "",
        "ifname": "swp5",
        "statusChangeTimestamp": 0.0,
        "vni": 0,
        "ip6AddressList": np.array(['fe80::5/24']),
        "lacpBypass": False,
        "mtu": 1500,
        "hostname": "leaf01",
        "namespace": "vagrant",
        "timestamp": 1644778941900,
        "active": True,
    },
    {
        "sqvers": 3.0,
        "ifindex": 8,
        "reason": "",
        "routeDistinguisher": "",
        "macaddr": "48:47:00:95:95:a3",
        "interfaceMac": "",
        "type": "ethernet",
        "description": "",
        "numChanges": 0,
        "speed": 4294967295,
        "vlan": 0,
        "innerVlan": 0,
        "vlanName": "",
        "ipAddressList": np.array([]),
        "srcVtepIp": "",
        "state": "down",
        "adminState": "down",
        "master": "",
        "ifname": "swp6",
        "statusChangeTimestamp": 0.0,
        "vni": 0,
        "ip6AddressList": np.array(['fe80::6/24']),
        "lacpBypass": False,
        "mtu": 1500,
        "hostname": "leaf01",
        "namespace": "vagrant",
        "timestamp": 1644778941900,
        "active": True,
    },
    {
        "sqvers": 3.0,
        "ifindex": 2,
        "reason": "",
        "routeDistinguisher": "",
        "macaddr": "44:38:39:01:02:01",
        "interfaceMac": "",
        "type": "ethernet",
        "description": "",
        "numChanges": 0,
        "speed": 1000,
        "vlan": 0,
        "innerVlan": 0,
        "vlanName": "",
        "ipAddressList": np.array(["10.255.2.184/24"]),
        "srcVtepIp": "",
        "state": "up",
        "adminState": "up",
        "master": "mgmt",
        "ifname": "eth0",
        "statusChangeTimestamp": 0.0,
        "vni": 0,
        "ip6AddressList": np.array(["fe80::4638:39ff:fe01:201/64"]),
        "lacpBypass": False,
        "mtu": 1500,
        "hostname": "leaf01",
        "namespace": "vagrant",
        "timestamp": 1644778941900,
        "active": True,
    },
    {
        "sqvers": 3.0,
        "ifindex": 9,
        "reason": "",
        "routeDistinguisher": "",
        "macaddr": "72:ef:fd:a1:76:71",
        "interfaceMac": "",
        "type": "vrf",
        "description": "",
        "numChanges": 0,
        "speed": 0,
        "vlan": 0,
        "innerVlan": 0,
        "vlanName": "",
        "ipAddressList": np.array(["127.0.0.1/8"]),
        "srcVtepIp": "",
        "state": "up",
        "adminState": "up",
        "master": "",
        "ifname": "mgmt",
        "statusChangeTimestamp": 0.0,
        "vni": 0,
        "ip6AddressList": np.array(["::1/128"]),
        "lacpBypass": False,
        "mtu": 65536,
        "hostname": "leaf01",
        "namespace": "vagrant",
        "timestamp": 1644778941900,
        "active": True,
    },
]