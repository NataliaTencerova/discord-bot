from email.contentmanager import raw_data_manager
import os, sys, json, time

messageData = []
startTime = time.time()

while True:

    cmdGet = 'curl -s -H "Authorization: Bot OTg2NTg3NDkyNDY5ODUwMTcy.GbPs8p.OJiou_Jo0o1_WuqVt8-bIDg_qwemSpoJTJ-GMM" -H "User-Agent: discordBot (https://discord.com/api/webhooks/986616508182560798/hYkOCfWeybUkr7ryT5uZXn2r3NlEg8AWzEqO6za0-dmE84IaBWGPTThSJ4cpD9mS1BJh, v0.4)" -H "Content-Type: application/json" -X GET https://discord.com/api/channels/986631988859510865/messages?after=988358852531597352'
    result = os.popen(cmdGet).read()
    jsonData = json.loads(result)

    for i in range(len(jsonData)):
        ts = jsonData[i]['timestamp'].split('+')[0]
        messageData.append({'name': jsonData[i]['author']['username'], 'content': jsonData[i]['content'], 'time': ts})

    sortedMessageData = sorted(messageData, key=lambda x:x['time'], reverse=True)
    
    lastMessage = sortedMessageData[0]
    print(lastMessage)

    if 'ahoj' in lastMessage['content'].lower() and lastMessage['name'] != 'Bot 297':
        cmdPost = 'curl -H "Authorization: Bot OTg2NTg3NDkyNDY5ODUwMTcy.GbPs8p.OJiou_Jo0o1_WuqVt8-bIDg_qwemSpoJTJ-GMM" -H "User-Agent: discordBot (https://discord.com/api/webhooks/986616508182560798/hYkOCfWeybUkr7ryT5uZXn2r3NlEg8AWzEqO6za0-dmE84IaBWGPTThSJ4cpD9mS1BJh, v0.4)" -H "Content-Type: application/json" -X POST -d \'{"content":"Ahoj"}\' https://discord.com/api/channels/986631988859510865/messages?after=988358852531597352'
        os.system(cmdPost)

    time.sleep(5.0 - ((time.time() - startTime) % 5.0))
