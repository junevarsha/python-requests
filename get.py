import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()
import requests
certificate = '/Users/varsha/Desktop/conf/new/server-cert.pem'
url = "https://localhost:4000/sensors/Josh/"
get_response = requests.get(url, verify=certificate)
print(get_response.text)