import requests
import json
import os
from datetime import datetime

def get_current_ip():
    try:
        response = requests.get('https://api.ipify.org?format=json')
        data = response.json()
        return data['ip']
    except Exception as e:
        print("Error fetching IP:", e)
        return None

def read_json_file(file_name):
    if os.path.exists(file_name):
        with open(file_name, 'r') as file:
            return json.load(file)
    else:
        return {'OldIP': '', 'NewIP': '', 'IPChangeTime': ''}

def write_to_json_file(file_name, data):
    with open(file_name, 'w') as file:
        json.dump(data, file, indent=4)

def check_ip_change():
    file_name = 'ip_data.json'
    ip_data = read_json_file(file_name)
    current_ip = get_current_ip()

    if current_ip:
        if ip_data['OldIP'] != current_ip:
            ip_data['IPChangeTime'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

            print(f"IP changed at: {ip_data['IPChangeTime']} from {ip_data['OldIP']} to {current_ip}"  )
            
            ip_data['OldIP'] = ip_data['NewIP']
            ip_data['NewIP'] = current_ip
            
            write_to_json_file(file_name, ip_data)
    else:
        print("Could not retrieve the current IP.")

if __name__ == "__main__":
    check_ip_change()
