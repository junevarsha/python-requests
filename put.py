import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()
import requests
certificate = '/Users/varsha/Desktop/conf/new/server-cert.pem'


url_put = "https://localhost:4000/sensors/Sim/"
data = {
	'sensor_name':'Simply',
	'token':'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJfaWQiOiJTaW0ifQ.kRUfXKouCaoQE2kKFucs7YKsYQjP2relHiL5XmRLwos'
}

p = requests.put(url_put, json=data, verify=certificate)
print(p.text)

print('********************************************')