"""
if there are not a folder about sounds, Run this Script.
It help you to make sound files.
"""

from gtts import gTTS

f = open("document.txt", 'r', encoding='UTF-8')
data = f.read()
f.close()

text2 = data.split("\n\n ")
text3 = []
keyword = []
explain = []

for i in range(len(text2)):
    text3.append(text2[i].split(" : "))

for j in text3:
    keyword.append(j[0])
    explain.append(j[1])

print("keyword : " + str(len(keyword)) + "\nexplain : " + str(len(explain)))

for i in range(218):
    tts = gTTS(text=keyword[i], lang='ko')
    tts.save('sounds/keyword' + str(i) + ".mp3")
    tts = gTTS(text=explain[i], lang='ko')
    tts.save('sounds/explain' + str(i) + ".mp3")

print("음성 생성 완료!")
