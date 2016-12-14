import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()
import requests
certificate = '/Users/varsha/Desktop/conf/new/server-cert.pem'


url_put = "https://localhost:4000/sensors/Ashwin/Humidity Sensor/"
data = {
	'value':70,
	'token':"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJfaWQiOiJBc2h3aW4ifQ.EEAd5-CCojwnh7Ex3-WyCjJaQBCuYyS3Td3fKSivlgk"
}

put_response = requests.put(url_put, json=data, verify=certificate)
print(put_response.text)