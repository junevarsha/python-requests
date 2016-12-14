import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()
import requests
certificate = '/Users/varsha/Desktop/conf/new/server-cert.pem'
url_post = "https://localhost:4000/sensors/"
data = {
	'name':'Ashwin Krish',
	'_id':'Ashwin'
}
post_response = requests.post(url_post, json=data, verify=certificate)
print(post_response.text)


