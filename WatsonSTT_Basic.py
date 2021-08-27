import time

start_time = time.time()
from ibm_watson import SpeechToTextV1
from ibm_watson.websocket import RecognizeCallback, AudioSource
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import json


# ## 1. Setup STT Service

apikey = ''
url = ''

authenticator = IAMAuthenticator(apikey)
stt = SpeechToTextV1(authenticator = authenticator)
stt.set_service_url(url)

with open('record.wav', 'rb') as f:
    res = stt.recognize(audio=f, content_type='audio/wav', model='en-US_NarrowbandModel', continuous=True).get_result()

text= []
for elements in res['results']:
    #print(elements)
    text.append(elements['alternatives'][0]['transcript'].rstrip() + '.\n')
print(text)

with open('output.txt', 'w') as out:
    out.writelines(text)
print(time.time()-start_time)
