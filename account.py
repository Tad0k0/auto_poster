#manage account
class account(object):
  def __init__(self, typeAcc, login, password):
    self.info = (typeAcc, login, password)
    self.typeAcc = (typeAcc)
    self.login = (login)
    self.password = (password)
    print("Account is created")
  def __del__ (self):
    print("Account is removed")

existTypeAcc = ["telegram", "vk"]



def createAccount():
  j = 1
  while j == 1:
    print("you can creat account, admited type account is " + " ".join(existTypeAcc) + "\ninput type:")
    inputType = input()
    # check the account type is admited
    for i in existTypeAcc:
      if i == inputType:
        j = 1
        break
      else:
        j = 0
    if j == 0:
      print("wrong type")
      break
    inputLogin = input("login:")
    inputPassword = input("password:")
    print("trying to log in")
    print("logging is successful")

createAccount()