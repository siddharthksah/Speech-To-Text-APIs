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

with open('audio.wav', 'rb') as f:
    res = stt.recognize(audio=f, content_type='audio/wav', model='en-US_NarrowbandModel', speaker_labels=True).get_result()

def listToString(s):
    # initialize an empty string
    str1 = " "

    # return string
    return (str1.join(s))


transcription = res

text= []
transcribe = []
for elements in transcription['results']:
    for keys in elements['alternatives'][0]['timestamps']:
        # print(keys[0])
        transcribe.append(keys[0])

    # text.append(elements['alternatives'][0]['transcript'].rstrip() + '.\n')

speaker_label = []
numberofelements = 0
for elements in transcription['speaker_labels']:
    # print(elements['speaker'])
    speaker_label.append(elements['speaker'])
    numberofelements = numberofelements + 1


from itertools import groupby

grouped_L = [(k, sum(1 for i in g)) for k,g in groupby(speaker_label)]

count = 0
for elements in grouped_L:
    # print(elements)
    print("Speaker", elements[0], ":", listToString(transcribe[count:count + elements[1]]))
    count = count + elements[1]
