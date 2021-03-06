#import telegram
from account import *
#create accountDataStorage file if it doesn't exist
with open('accountDataStorage.csv', 'a+') as f:
  pass
class userAction(object):
  def __init__(self, nameAct, parameter):
    self.inp = (nameAct, parameter)
    self.nameAct = (nameAct)
    self.parameter = (parameter)

helpAction = userAction("help", "")
helpActionAccount = userAction("help", "account")
helpActionMessage = userAction("help", "message")

accountAction = userAction("account", "")
accountActionCreate = userAction("account", "create")
accountActionDelete = userAction("account", "delete")

exitAction = userAction("exit", "")

userInputAction = userAction("", "")

while True:
  print("input command, help to get info")
  userIn=input()
  userIn = userIn.split()
  userInputAction.nameAct = userIn[0]
  try:
    userInputAction.parameter = userIn[1]
  except  IndexError:
    userIn.pop(1)

  if userInputAction.nameAct == helpAction.nameAct and userInputAction.parameter == helpAction.parameter:
    print("help: list commands, fot more info input help <comandName>;\naccount: to manage accounts;\nmessage: to post message;\nexit: to exit")
  elif userInputAction.nameAct == helpActionAccount.nameAct and userInputAction.parameter == helpActionAccount.parameter:
    print("account: shows a list of accounts;\n account create: to create an account\n account delete: to delete an account")
  elif userInputAction.nameAct == accountActionCreate.nameAct and userInputAction.parameter == accountActionCreate.parameter:
    createAccount()
  elif userInputAction.nameAct == accountAction.nameAct and userInputAction.parameter == accountAction.parameter:
    listAccount()
  elif userInputAction.nameAct == exitAction.nameAct:
    break
  else:
    print("command is not found")

"""
if userAction == "help" :
  print("help to get info;\naccount to manage account;\nmessage to post message")
elif userAction == "account" :
  print(choose account telegram,)
"""
