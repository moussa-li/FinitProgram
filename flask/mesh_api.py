import requests
import json

url = 'https://nscc-xa.hpccube.com/ac/openapi/v2/tokens'
url2 = 'https://nscc-xa.hpccube.com/ac/openapi/v2/tokens/next'
test_url = 'http://192.168.1.7:5000/test'
data = {'user':'moussa','password':'lcn99325','orgId':'d4956deaada66db3c03738316a143aff'}
headers = {'Content-Type':'application/json','user':'moussa','password':'lcn99325','orgId':'d4956deaada66db3c03738316a143aff'}
# headers = {'Content-Type':'application/json'}
data_json = json.dumps(data)
print(data)
# headers= {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36'}
result = requests.post(url,headers = headers)
print(result.url)
result = json.loads(result.content)
print(result['data'][0]['token'])