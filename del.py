import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()
import requests
certificate = '/Users/varsha/Desktop/conf/new/server-cert.pem'
url_del = "https://localhost:4000/sensors/Ashwin/"
data = {
	'token':'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJfaWQiOiJBc2h3aW4ifQ.EEAd5-CCojwnh7Ex3-WyCjJaQBCuYyS3Td3fKSivlgk'
}
del_response = requests.delete(url_del, json=data, verify=certificate)
print(del_response.text)
