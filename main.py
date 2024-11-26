import requests
import json
from mccolors import mcreplace

def get_server_status(version, ip):
    base_url = "https://api.mcstatus.io/v2/status/"
    url = f"{base_url}{version}/{ip}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None

def format_motd(motd_raw):
    return mcreplace(motd_raw)

def display_status(data):
    if data:
        print(f"Server online: {data['online']}")
        print(f"Host: {data['host']}")
        print(f"Port: {data['port']}")
        print(f"IP Address: {data['ip_address']}")
        print(f"Players online: {data['players']['online']}/{data['players']['max']}")
        print(f"Version: {data['version']['name_clean']}")
        print(f"EULA Blocked: {data['eula_blocked']}")
        formatted_motd = format_motd(data['motd']['raw'])
        print("MOTD:\n", formatted_motd)

        # Check for proxy/waterfall
        if data['proxy']:
            download_json(data)
    else:
        print("Unable to retrieve server status.")

def download_json(data):
    # Save JSON data to a file
    with open("server_data.json", "w") as f:
        json.dump(data, f, indent=4)
    print("Server data saved to server_data.json")

def main():
    version = input("Select Version (bedrock/java): ")
    ip = input("Enter Server IP: ")
    if version and ip:
        data = get_server_status(version, ip)
        display_status(data)
    else:
        print("Please enter all details.")

if __name__ == "__main__":
    main()
