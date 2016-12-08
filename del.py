import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()
import requests
certificate = '/Users/varsha/Desktop/conf/new/server-cert.pem'


url_del = "https://localhost:4000/sensors/Sim/"
data = {
	'token':'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJfaWQiOiJTaW0ifQ.kRUfXKouCaoQE2kKFucs7YKsYQjP2relHiL5XmRLwos'
}

p = requests.delete(url_del, json=data, verify=certificate)
print(p.text)

print('********************************************')