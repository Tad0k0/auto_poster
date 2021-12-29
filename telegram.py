from telethon import TelegramClient, events, sync


appIdPath = "/home/vitaliy/work/telegram_poster_bot/app_id"

# Get id and hash from file
with open(appIdPath) as f:
  for pos, l_num in enumerate(f):
      if pos == 1:
        idApp = l_num.strip()
      if pos ==3:
        hashApp = l_num.strip()
f.close()



interface = {
  "help": print("help: output info")
}

print("input help for get info about interface")
userAction = input()



client = TelegramClient('session_name', idApp, hashApp)
client.start()

while True:
  userActionTelegram=input()
  if userActionTelegram == "info":
    print(client.get_me().stringify())
  elif userActionTelegram == "exit":
    break 
  else:
    print("invalid action")
#client.send_message('Lyra1Heartstrings', 'Hello! Talking to you from Telethon')
#client.send_file('username', '/home/myself/Pictures/holidays.jpg')

#client.download_profile_photo('me')
#messages = client.get_messages('Lyra1Heartstrings')
#messages[0].download_media()

#@client.on(events.NewMessage(pattern='(?i)hi|hello'))
#async def handler(event):
#    await event.respond('Hey!')
