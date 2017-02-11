import time
import requests
import numpy as np
import httplib, urllib, base64
import pdb, sys, os
import youtube_dl
import cv2

def emot2search(emotion):
    headers = {
        # Request headers
        'Ocp-Apim-Subscription-Key': '9ea52833d51a43bebfd9fec0739b56cd',
    }

    params = urllib.urlencode({
        # Request parameters
        'q': emotion,
        'count': '10',
        'offset': '0',
        'mkt': 'en-us',
        'safesearch': 'Moderate',
    })

    if not os.path.exists('video'):
        os.makedirs('video')

    url = 'https://api.cognitive.microsoft.com/bing/v5.0/search?'
    try:
        response = requests.get(url, headers = headers, params = params)
        outputs = response.json()
        # print(outputs)
        # ydl_opts = {'outtmpl': 'video/%(title)s.%(ext)s'}
        # with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            # ydl.download([outputs['videos']['value'][0]['contentUrl']])
    except Exception as e:
        print("[Errno {0}] {1}".format(e.errno, e.strerror))
    return outputs
    # cap = cv2.VideoCapture('video/'+os.listdir('video')[0])
    # while(cap.isOpened()):
        # ret, frame = cap.read()
        # frame = cv2.resize(frame, (320, 240))
        # cv2.imshow('frame',frame)
        # if cv2.waitKey(1) & 0xFF == ord('q'):
            # break
    # cap.release()
    # cv2.destroyAllWindows()

_url = 'https://westus.api.cognitive.microsoft.com/emotion/v1.0/recognize'
_key = 'eb0df8e19abd48a19fccd361acd7205c'
_maxNumRetries = 10

def processRequest( json, data, headers, params ):

    """
    Helper function to process the request to Project Oxford

    Parameters:
    json: Used when processing images from its URL. See API Documentation
    data: Used when processing image read from disk. See API Documentation
    headers: Used to pass the key information and the data type request
    """

    retries = 0
    result = None
    
    while True:
        
        response = requests.request('post',_url, json = json, data=data, headers=headers, params=params)
    
        if response.status_code == 429: 
            print( "Message: %s" % ( response.json()['error']['message'] ) )
            if retries <= _maxNumRetries: 
                time.sleep(1) 
                retries += 1
                continue
            else: 
                print( 'Error: failed after retrying!' )
                break
        elif response.status_code == 200 or response.status_code == 201:
            
            if 'content-length' in response.headers and int(response.headers['content-length']) == 0: 
                result = None 
            elif 'content-type' in response.headers and isinstance(response.headers['content-type'], str): 
                if 'application/json' in response.headers['content-type'].lower(): 
                    result = response.json() if response.content else None 
                elif 'image' in response.headers['content-type'].lower(): 
                    result = response.content
        else:
            print( "Error code: %d" % ( response.status_code ) )
            print( "Message: %s" % ( response.json()['error']['message'] ) )

        break
        
    return result


path = 'A23cScT.jpg'
with open(path, 'rb') as f:
    data = f.read()

headers=dict()
headers['Ocp-Apim-Subscription-Key'] = _key
headers['Content-Type'] = 'application/octet-stream'
json = None
params = None
result = processRequest(json, data, headers, params)

emotion=''
for i in xrange(len(result)):
    print (result[i]['scores'])
    scores = result[i]['scores']
    flag = True
    max_score = 0

    for key in scores:
        if flag:
            max_score = scores[key]
            emotion = key
            flag = False
        else:
            if max_score<scores[key]:
                max_score = scores[key]
                emotion = key

print (emotion)
outputs = emot2search('videos with mood '+emotion)
pdb.set_trace()
