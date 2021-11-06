import requests 
import sys
import os

phrase = sys.argv[1]
name = sys.argv[2]

home = os.environ['HOME']
sounds_path = home + '/catkin_ws/src/action_handler/scripts/interactive/speaking/sounds/'
alphabet = ",-:?abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
# https://texttospeech.responsivevoice.org/v1/text:synthesize?text=Salut.%0AVous%20%C3%AAtes%20les%20bienvenus%20%C3%A0%20Strim.&lang=fr&engine=g3&name=&pitch=0.5&rate=0.5&volume=1&key=0POmS5Y2&gender=male
js_encoded = ""
for ch in phrase:
    if ch == '\n':
        js_encoded+='%0A'
    if ch == ' ':
        js_encoded+='%20'
    elif ch not in alphabet:
        ch_encoded=ch.encode('utf-8').hex().upper()
        for (e,i) in zip(ch_encoded,range(len(ch_encoded))):
            if i%2 == 0:
                js_encoded+="%"
            js_encoded+=e
    else:
        js_encoded+=ch

print(js_encoded)
data = requests.get("https://texttospeech.responsivevoice.org/v1/text:synthesize?text="+js_encoded+"&lang=fr&engine=g3&name=&pitch=0.5&rate=0.43&volume=1&key=0POmS5Y2&gender=male")

file = open(sounds_path+name+'.mp3', 'wb+')
file.write(data.content)
file.close()