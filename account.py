#manage account]
from telegram import *
import csv
import re
class account(object):
  def __init__(self, index, typeAcc, login, password):
    self.info = (index, typeAcc, login, password)
    self.typeAcc = (typeAcc)
    self.login = (login)
    self.password = (password)
    self.index =(index)
    print("Account is created")
  def __del__ (self):
    print("Account is removed")

existTypeAcc = ["telegram", "vk"]



def createAccount():
  j = 1
  while j == 1:
    print("you can creat account, admited type account is " + " ".join(existTypeAcc) + "\ninput type:")
    inputType = input()
    # check an account type is admited
    for i in existTypeAcc:
      if i == inputType:
        j = 1
        break
      else:
        j = 0
    if j == 0:
      print("wrong type")
      break
    #create an account object
    inputLogin = input("login:")
    inputPassword = input("password:")
    #for each new account add index +1
    with open('accountDataStorage.csv') as f:
      currentIndex = 0
      f.seek(0) #ensure you're at the start of the file..
      first_char = f.read(1) #get the first character
      if not first_char:
        print("file is empty") #first character is the empty string..
      else:
        reader = first_char + f.read()
        print(reader)
        reader = reader.split("\n")
        print(*reader)
        print(type(reader))
        print(re.search(r'^\d+', reader[0]))
        currentIndex = re.search(r'^\d+', reader[0]).group()
    print("index: " + str(currentIndex))
    currentAccount = account(int(currentIndex)+1, inputType, inputLogin, inputPassword)
    #save account data into file
    with open('accountDataStorage.csv', 'a', encoding='UTF8', newline='') as f:
      csvwriter = csv.writer(f)
      dataForSave = currentAccount.info
      csvwriter.writerow(dataForSave)
    #choose a soc.media for account logging
#    if currentAccount.typeAcc == "telegram":
#      print("trying to log in")
#      loginTelegramAccount(currentAccount.login)
#    print("logging is successful")
    break

def listAccount():
  with open('accountDataStorage.csv') as f:
    print(f.read())


#TODO delete account
#def deleteAccount()
  
