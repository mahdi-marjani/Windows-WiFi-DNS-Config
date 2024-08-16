import subprocess
import pyuac

dns = {
    0 : ['', ''],
    1 : ['178.22.122.100', '185.51.200.2'],
    2 : ['10.202.10.202', '10.202.10.102'],
    3 : ['185.55.226.26', '185.55.225.25'],
    4 : ['78.157.42.101', '78.157.42.100'],
    5 : ['109.122.208.156', '109.122.208.158'],
    6 : ['8.8.8.8', '8.8.4.4'],
    7 : ['208.67.222.222', '208.67.220.220'],
    8 : ['1.1.1.1', '1.1.0.0'],
    9 : ['9.9.9.9', '149.112.112.112'],
    10 : ['103.86.96.100', '103.86.99.100'],
    11 : ['172.29.0.100', '172.29.2.100'],
    12 : ['91.92.255.160', '91.92.255.242'],
    13 : ['45.66.231.67', '0.0.0.0'],
    14 : ['10.202.10.10', '10.202.10.11'],
}

dns_info = '''
0 -> No DNS
1 -> shecan
2 -> 403
3 -> begzar
4 -> electro
5 -> server.ir
6 -> google
7 -> OpenDNS
8 -> Cloudflare
9 -> Quad9
10 -> NordVPN Private DNS Servers
11 -> hostiran
12 -> shelter1
13 -> shelter2
14 -> radargame
'''

def set_wifi_dns(dns_servers):
    wifi_interface_name = "Wi-Fi"
    if dns_servers[0] == '' and dns_servers[1] == '':
        command = f"Set-DnsClientServerAddress -InterfaceAlias {wifi_interface_name} -ResetServerAddresses"
    else:
        dns_string = ",".join(dns_servers)
        command = f"Set-DnsClientServerAddress -InterfaceAlias {wifi_interface_name} -ServerAddresses {dns_string}"
    subprocess.run(["powershell", "-Command", command], check=True)

def main():
    print(dns_info)
    dns_choice = input('choose dns server: ')
    set_wifi_dns(dns[int(dns_choice)])

if __name__ == "__main__":
    if not pyuac.isUserAdmin():
        print("Re-launching as admin!")
        pyuac.runAsAdmin()
    else:        
        main()
