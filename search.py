########### Python 2.7 #############
import httplib, urllib, base64
import pdb, sys, os
import requests
import ast
import youtube_dl
import cv2

headers = {
    # Request headers
    'Ocp-Apim-Subscription-Key': '9ea52833d51a43bebfd9fec0739b56cd',
}

params = urllib.urlencode({
    # Request parameters
    'q': sys.argv[1],
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
    ydl_opts = {'outtmpl': 'video/%(title)s.%(ext)s'}
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([outputs['videos']['value'][0]['contentUrl']])
except Exception as e:
    print("[Errno {0}] {1}".format(e.errno, e.strerror))

cap = cv2.VideoCapture('video/'+os.listdir('video')[0])
while(cap.isOpened()):
    ret, frame = cap.read()
    frame = cv2.resize(frame, (320, 240))
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()

