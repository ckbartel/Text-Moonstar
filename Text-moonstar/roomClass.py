#this class works: to set a new item use room1['name'] = value
#to access it use room1['name']
#room1.add(dict) works like update() did before

class Room:
  def __init__(self):
    self.main = {
      'ID':'1',
      'permHasEntered':False,
      'hasEntered':False,
      'permDoorBlocked':'none',
      'hasPermMagicMonster':False,
      'hasPermMonster':False,
      'hasPermObjects':False,
      'hasMagicMonster':False,
      'hasMonster':False,
      'hasObjects':False,
      'floor':1,
      'hasUpStairs':False,
      'hasDownStairs':False,
      'canA':False,
      'canD':False,
      'doorBlocked':'none',
      'isWinRoom':False,
      'hasPermNPC':False,
      'hasNPC':False,
      'hasBed':False,
      'hasTrap':False,
      'hasPermTrap':False,
      'permObjects':[]
    }
  #  self.permDoorBlocked = 'none'
  #  self.hasPermMagicMonster = False
  #  self.hasPermMonster = False
  #  self.hasPermObjects = False
  #  self.hasMagicMonster = False
  #  self.hasMonster = False
  #  self.hasObjects = False
  #  self.objects = []
  #  self.floor = 1
  #  self.hasUpStairs = False
  #  self.hasDownStairs = False
  #  self.canA = False
  #  self.canD = False
  #  self.doorBlocked = 'none'
  #  self.isWinRoom = False
  #  self.roomToRight = 'none'
  #  self.roomToLeft = 'none'

  def __getitem__(self, key):
    return self.main[key]

  def __setitem__(self, key, newvalue):
    self.main[key] = newvalue
  
  def add(room, dict):
    for thing in dict:
      key = thing
      value = dict[thing]
      room[key] = value