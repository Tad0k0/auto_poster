"""
#read a file with token
print("Input a path to token file")
tokenPath = "/home/vitaliy/work/telegram_poster_bot/token"
#tokenPath = input()
with open(tokenPath, 'r') as f:
  token = f.read()
  f.close()
"""
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



