class Cat:
  def __init__(self, name=None, sex=None, age=None):
    self.name = name
    self.sex = sex
    self.age = age

  def show_cat(self):
    print(f'Cat "{self.name}",\n Sex: {self.sex},\n Age: {self.age}')

  def get_name(self):
    return self.name

  def get_sex(self):
    return self.sex

  def get_age(self):
    return self.age

  def set_name(self, name):
    if isinstance(name, str):
      self.name = name

  def set_sex(self, sex):
    if isinstance(sex, str):
      self.sex = sex

  def set_age(self, age):
    if age > 0 and isinstance(age, int):
      self.age = age

class Client:
  def __init__(self, name=None, money=0):
    self.name = name
    self.money = money

  def get_name(self):
    return self.name

  def get_money(self):
    return self.money

  def set_name(self, name):
    if isinstance(name, str):
      self.name = name

  def set_money(self, money):
    if isinstance(money, int):
      self.money += money

  def __str__(self):
    return f"Client «{self.name}». Money: ₽{self.money}"

class Volunteer(Client):
  def __init__(self, city=None, status=None):
    self.city = city
    self.status = status

  def get_city(self):
    return self.city

  def get_status(self):
    return self.status

  def set_city(self, city):
    if isinstance(city, str):
      self.city = city

  def set_status(self, status):
    if isinstance(status, str):
      self.status = status

  def __str__(self):
    return f"{self.name}, city: {self.city}, status: «{self.status}»"
