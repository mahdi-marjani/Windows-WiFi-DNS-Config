import subprocess
import pyuac

dns = {
    0 : ['', ''],
    1 : ['178.22.122.100', '185.51.200.2'],
    2 : ['10.202.10.202', '10.202.10.102'],
}

dns_info = '''
0 -> No DNS
1 -> shecan
2 -> 403
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
