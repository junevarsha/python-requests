import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()
import requests
certificate = '/Users/varsha/Desktop/conf/new/server-cert.pem'
url = "https://localhost:4000/sensors/Sindhu/"
r = requests.get(url, verify=certificate)
print(r.text)

print('********************************************')

url_post = "https://localhost:4000/sensors/"
data = {
	'name':'Simply',
	'_id':'Sim'
}

p = requests.post(url_post, json=data, verify=certificate)
print(p.text)

print('********************************************')


