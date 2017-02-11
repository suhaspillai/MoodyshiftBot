########### Python 2.7 #############
import httplib, urllib, base64
import ipdb
import requests

headers = {
    # Request headers
    'Ocp-Apim-Subscription-Key': 'e61708c939d0426ba3627329ccbba99e',
}

params = urllib.urlencode({
    # Request parameters
    'q': 'top songs for happy',
    'count': '10',
    'offset': '0',
    'mkt': 'en-us',
    'safesearch': 'Moderate',
})


url = 'https://api.cognitive.microsoft.com/bing/v5.0/search?'
# try:
    # conn = httplib.HTTPSConnection('api.cognitive.microsoft.com')
    # conn.request("GET", "/bing/v5.0/search?%s" % params, "{body}", headers)
    # response = conn.getresponse()
    # data = response.read()
response = requests.get(url, params = params, headers = headers)	
ipdb.set_trace()
print(data)
conn.close()
# except Exception as e:
    # print("[Errno {0}] {1}".format(e.errno, e.strerror))