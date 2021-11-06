import requests 
import sys
import os

phrase = sys.argv[1]
name = sys.argv[2]

home = os.environ['HOME']
sounds_path = home + '/catkin_ws/src/action_handler/scripts/interactive/speaking/sounds/'
phrase = phrase.encode('utf-8').hex().upper()
js_encoded = ""
for i in range(len(phrase)):
    if i%2 == 0:
        js_encoded+="%"
    js_encoded+=phrase[i]
data = requests.get("https://texttospeech.responsivevoice.org/v1/text:synthesize?text="+js_encoded+"&lang=ar&engine=g3&name=&pitch=0.5&rate=0.5&volume=1&key=0POmS5Y2&gender=male",timeout=3)
file = open(sounds_path+name+'.mp3', 'wb+')
file.write(data.content)
file.close()