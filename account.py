class account(object):
  def __init__(self, typeAcc, login, password):
    self.info = (typeAcc, login, password)
    self.type = (typeAcc)
    self.login = (login)
    self.password = (password)

telegramAccount = account("telegram", "+79528652628", "")

print(telegramAccount.info)