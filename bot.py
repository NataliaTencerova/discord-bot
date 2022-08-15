import os, sys, json, time

startTime = time.time()

def getLastMessage():
    cmdGetLastMessage = 'curl -s -H "Authorization: Bot OTg2NTg3NDkyNDY5ODUwMTcy.GbPs8p.OJiou_Jo0o1_WuqVt8-bIDg_qwemSpoJTJ-GMM" -H "User-Agent: discordBot (https://discord.com/api/webhooks/986616508182560798/hYkOCfWeybUkr7ryT5uZXn2r3NlEg8AWzEqO6za0-dmE84IaBWGPTThSJ4cpD9mS1BJh, v0.4)" -H "Content-Type: application/json" -X GET https://discord.com/api/channels/986631988859510865/messages?after=988358852531597352'
    result = os.popen(cmdGetLastMessage).read()
    jsonData = json.loads(result)
    messageData = []

    for i in range(len(jsonData)):
        ts = jsonData[i]['timestamp'].split('+')[0]
        messageData.append({'name': jsonData[i]['author']['username'], 'content': jsonData[i]['content'], 'time': ts})

    sortedMessageData = sorted(messageData, key=lambda x:x['time'], reverse=True)
    lastMessage = sortedMessageData[0]

    return lastMessage

def postMessage(messageContent):
        cmdPost = 'curl -H "Authorization: Bot OTg2NTg3NDkyNDY5ODUwMTcy.GbPs8p.OJiou_Jo0o1_WuqVt8-bIDg_qwemSpoJTJ-GMM" -H "User-Agent: discordBot (https://discord.com/api/webhooks/986616508182560798/hYkOCfWeybUkr7ryT5uZXn2r3NlEg8AWzEqO6za0-dmE84IaBWGPTThSJ4cpD9mS1BJh, v0.4)" -H "Content-Type: application/json" -X POST -d \'{"content":"' +messageContent+ '"}\' https://discord.com/api/channels/986631988859510865/messages'
        os.system(cmdPost)

def reply_hi():
    lastMessage = getLastMessage()
    messageContent = 'Ahoj'

    if 'ahoj' in lastMessage['content'].lower() and lastMessage['name'] != 'Bot 297':
        postMessage(messageContent)

def check_weather():
    lastMessage = getLastMessage()

    if '!Weather' in lastMessage['content']:
        cmdGetWeather = 'curl -s "https://api.openweathermap.org/data/2.5/weather?appid=9ba642bc8b1825cca70ff6bd1066bcf4&lat=49.1533&lon=16.8765&units=metric" -H "Accept: application/json"'
        result = os.popen(cmdGetWeather).read()
        jsonData = json.loads(result)

        location = jsonData['name']
        weather = jsonData['weather'][0]['main']
        temperature = jsonData['main']['temp']
        feelsLike = jsonData['main']['feels_like']

        strLocation = str(location)
        strWeather = str(weather)
        strTemperature = str(temperature)
        strFeelsLike = str(feelsLike)

        messageContent = 'The weather in ' +strLocation+ ' is ' +strWeather+ '. The temperature is ' +strTemperature+ ', but it feels like ' +strFeelsLike+ '.'
        postMessage(messageContent)


while True:
    reply_hi()

    check_weather()

    time.sleep(5.0 - ((time.time() - startTime) % 5.0))
