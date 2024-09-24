#987
from roomClass import Room

#XX5
#123
#46X
#template:
#template={
#  'permDoorBlocked':'none',
#  'hasPermMagicMonster':False,
#  'hasPermMonster':False,
#  'hasPermObjects':False,
#  'hasMagicMonster':False,
#  'hasMonster':False,
#  'hasObjects':False,
#  'floor':1,
#  'hasUpStairs':False,
#  'hasDownStairs':False,
#  'canA':False,
#  'canD':False,
#  'doorBlocked':'none',
#  'isWinRoom':False
#}
#required properties
  #permDoorBlocked
  #hasPermMagicMonster
  #hasPermMonster
  #hasPermObjects
  #hasMagicMonster
  #hasMonster
  #hasObjects
  #floor
  #hasUpStairs
  #hasDownStairs
  #canA
  #canD
  #doorBlocked
  #isWinRoom
#addition properties
  #objects
#added properties in nav
  #roomToRight
  #roomToLeft
  #roomAbove
  #roomBelow
#necessary objects
  #rooms
    #lists the rooms in an array


#room1, room2, room3, room4, room5, room6, room7, room8, room9 = Room(), Room(), Room(), Room(), Room(), Room(), Room(), Room(), Room()
#room1.canD=True

#room1.add({
#  'canD':True,
#  'roomToRight':room2,
#  'roomBelow':room4
#})

#room2.add({
#  'hasPermObjects':True,
#  'hasObjects':True,
#  'objects':['sword'],
#  'canA':True,
#  'canD':True,
#  'roomToRight':room3,
#  'roomToLeft':room1
#})

#room3.add({
#  'permDoorBlocked':'upstairs',
#  'hasPermMonster':True,
#  'hasMonster':True,
#  'hasUpStairs':True,
#  'canA':True,
#  'doorBlocked':'upstairs',
#  'roomToLeft':room2,
#  'roomAbove':room5
#})

#room4.add({
#  'permDoorBlocked':'right',
#  'hasPermMagicMonster':True,
#  'hasPermMonster':True,
#  'hasMagicMonster':True,
#  'hasMonster':True,
#  'floor':'Dungeon',
#  'hasUpStairs':True,
#  'canD':True,
#  'doorBlocked':'right',
#  'roomToRight':room6,
#  'roomAbove':room1
#})

#room5.add({
#  'floor':2,
#  'hasUpStairs':True,
#  'hasDownStairs':True,
#  'roomBelow':room3,
#  'roomAbove':room7
#})

#room6.add({
#  'floor':'Dungeon',
#  'canA':True,
#  'isWinRoom':True
#})

#room7.add({
#  'hasPermObjects':True,
#  'hasObjects':True,
#  'objects':['sword'],
#  'floor':3,
#  'hasDownStairs':True,
#  'canA':True,
#  'canD':False,
#  'roomBelow':room5,
#  'roomToLeft':room8
#})

#room8.add({
#  'permDoorBlocked':'left',
#  'hasPermMonster':True,
#  'hasMonster':True,
#  'floor':3,
#  'canA':True,
#  'canD':True,
#  'doorBlocked':'left',
#  'roomToRight':room7,
#  'roomToLeft':room9
#})

#room9.add({
#  'hasPermObjects':True,
#  'hasObjects':True,
#  'objects':['sword','magic stones'],
#  'floor':3,
#  'canD':True,
#  'roomToRight':room8
#})

#nav system

#room1.add({
#  'canD':True,
#  'hasDownStairs':True
#})
#room1.canD = True
#room1.hasDownStairs = True

#room1.add({
#  'roomToRight':room2,
#  'roomBelow':room4
#})
#room2.add({
#  'roomToRight':room3,
#  'roomToLeft':room1
#})
#room3.add({
#  'roomToLeft':room2,
#  'roomAbove':room5
#})
#room4.add({
#  'roomToRight':room6,
#  'roomAbove':room1
#})
#room5.add({
#  'roomBelow':room3,
#  'roomAbove':room7
#})
#room7.add({
#  'roomBelow':room5,
#  'roomToLeft':room8
#})
#room8.add({
#  'roomToRight':room7,
#  'roomToLeft':room9
#})
#room9.add({
#  'roomToRight':room8
#})

#rooms array for respawn regeneration
#rooms=[room1,room2,room3,room4,room5,room6,room7,room8,room9]

#tells inventory and location
#player={
#  'objects':['','',''],
#  'location':room1,
#  'hasWon':False
#}
#grab function
#def grab(roomObjects):
#  for i in roomObjects:
#    if(i!=''):
#      player['objects'].insert(0,i)
#      player['objects'].pop(3)
#    print('\n\ncheck inventory to see rewards!\n\n')
#  player['location']['hasObjects']=False
#  q=str(input('make your next move \n-------------------------------- '))
#  takeAction(q)
#if u press a
#def a():
#  if(player['location']['canA'] and player['location']['doorBlocked']!='left'):
#    player['location']=player['location']['roomToLeft']
#    if(player['location']['isWinRoom']):
#      player['hasWon']=True
#    if(player['location']['hasObjects']):
#      print('\n\nthis room contains treasures\n\n')
#    if(player['location']['hasUpStairs']):
#      print('\n\nthis room contains stairs leading up\n\n')
#    if(player['location']['hasDownStairs']):
#      print('\n\nthis room contains stairs leading down\n\n')
#    if(player['location']['hasMagicMonster']):
#      print('\n\nthis room contains a magic monster... blocking the '+player['location']['doorBlocked']+' door!\n\n')
#    elif(player['location']['hasMonster']):
#      print('\n\nthis room contains a monster... blocking the '+player['location']['doorBlocked']+' door!\n\n')
#    q=str(input('make your next move \n-------------------------------- '))
#    takeAction(q)
#  else:
#    print('\n\nyou hysterically ran into a wall!\n\n')
#    q=str(input('make your next move \n-------------------------------- '))
#    takeAction(q)
#if u press d
#def d():
#  if(player['location']['canD'] and player['location']['doorBlocked']!='right'):
#    player['location']=player['location']['roomToRight']
#    if(player['location']['isWinRoom']):
#      player['hasWon']=True
#      takeAction('')
#    if(player['location']['hasObjects']):
#      print('\n\nthis room contains treasures\n\n')
#    if(player['location']['hasUpStairs']):
#      print('\n\nthis room contains stairs leading up\n\n')
#    if(player['location']['hasDownStairs']):
#      print('\n\nthis room contains stairs leading down\n\n')
#    if(player['location']['hasMagicMonster']):
#      print('\n\nthis room contains a magic monster... blocking the '+player['location']['doorBlocked']+' door!\n\n')
#    elif(player['location']['hasMonster']):
#      print('\n\nthis room contains a monster... blocking the '+player['location']['doorBlocked']+' door!\n\n')
#    q=str(input('make your next move \n-------------------------------- '))
#    takeAction(q)
#  else:
#    print('\n\nyou hysterically ran into a wall!\n\n')
#    q=str(input('make your next move \n-------------------------------- '))
#    takeAction(q)
#if u press s
#def s():
#  if(player['location']['hasDownStairs'] and player['location']['doorBlocked']!='downstairs'):
#    player['location']=player['location']['roomBelow']
#    if(player['location']['isWinRoom']):
#      player['hasWon']=True
#    if(player['location']['hasObjects']):
#      print('\n\nthis room contains treasures\n\n')
#    if(player['location']['hasUpStairs']):
#      print('\n\nthis room contains stairs leading up\n\n')
#    if(player['location']['hasDownStairs']):
#      print('\n\nthis room contains stairs leading down\n\n')
#    if(player['location']['hasMagicMonster']):
#      print('\n\nthis room contains a magic monster... blocking the '+player['location']['doorBlocked']+' door!\n\n')
#    elif(player['location']['hasMonster']):
#      print('\n\nthis room contains a monster... blocking the '+player['location']['doorBlocked']+' door!\n\n')
#    q=str(input('make your next move \n-------------------------------- '))
#    takeAction(q)
#  else:
#    print('\n\nyou tried to ground pound like Mario... Only prevailing with a sore bum!\n\n')
#    q=str(input('make your next move \n-------------------------------- '))
#    takeAction(q)
#if u press w
#def w():
#  if(player['location']['hasUpStairs'] and player['location']['doorBlocked']!='upstairs'):
#    player['location']=player['location']['roomAbove']
#    if(player['location']['isWinRoom']):
#      player['hasWon']=True
#    if(player['location']['hasObjects']):
#      print('\n\nthis room contains treasures\n\n')
#    if(player['location']['hasUpStairs']):
#      print('\n\nthis room contains stairs leading up\n\n')
#    if(player['location']['hasDownStairs']):
#      print('\n\nthis room contains stairs leading down\n\n')
#    if(player['location']['hasMagicMonster']):
#      print('\n\nthis room contains a magic monster... blocking the '+player['location']['doorBlocked']+' door!\n\n')
#    elif(player['location']['hasMonster']):
#      print('\n\nthis room contains a monster... blocking the '+player['location']['doorBlocked']+' door!\n\n')
#    q=str(input('make your next move \n-------------------------------- '))
#    takeAction(q)
#  else:
#    print('\n\nyou leaped up through the roof and swiftly won \nthe game!!! then you woke up to realize your \nstill on floor '+str(player['location']['floor'])+'\n\n')
#    q=str(input('make your next move \n-------------------------------- '))
#    takeAction(q)
#if u press i
#def inventory():
#  print('\n\n')
#  print(player['objects'])
#  print('\n\n')
#  q=str(input('make your next move \n-------------------------------- '))
#  takeAction(q)
#takes action when new input is given
#def takeAction(inp):
#  isntInput=True
#  if(player['hasWon']):
#    isntInput=False
#    print('\n\nyou are winner, \nyou save Tarzan, \nhe make you his wife, \nyou have many TarTarBabies together, \nyou later get divorced... \nand lived happily ever after\nTHE END!!!\n\n')
#  else:
#    if(inp=='g'):
#      isntInput=False
#      if(player['location']['hasObjects']):
#        grab(player['location']['objects'])
#      else:
#        print('\n\nyou spent hours scrounging for anything...\nthen you grew tired and stopped\n\n')
#        q=str(input('make your next move \n-------------------------------- '))
#        takeAction(q)
#    if(inp=='i'):
#      isntInput=False
#      inventory()
#    if(inp=='a'):
#      isntInput=False
#      a()
#    if(inp=='d'):
#      isntInput=False
#      d()
#    if(inp=='w'):
#      isntInput=False
#      w()
#    if(inp=='s'):
#      isntInput=False
#      s()
#    if(inp=='f'):
#      isntInput=False
#      if(player['location']['hasMonster']):
#        if('sword' in player['objects'] and player['location']['hasMagicMonster']==False):
          #if you have sword
#          player['objects'].remove('sword')
#          player['objects'].insert(2,'')
#          player['location']['hasMonster']=False
#          player['location']['doorBlocked']='none'
#          print('\n\nyou won but -- at a cost... your sword remains lodged deeply in the great basin the monster\'s belly :(\n\n')
#          q=str(input('make your next move \n-------------------------------- '))
#          takeAction(q)
#        else:
          #respawn
#          player['location']=room1
#          print('\n\nthe monster got tired of your futile attacks and sat on you... you-- ya didn\'t make it...\n\nyou respawned in the first room\n\n')
#          for i in rooms:
#            if(i['hasPermObjects']):
#              i['hasObjects']=True
#            if(i['hasPermMonster']):
#              i['hasMonster']=True
#              i['doorBlocked']=i['permDoorBlocked']
#            if(i['hasPermMagicMonster']):
#              i['hasMagicMonster']=True
#          for i in player['objects']:
#            player['objects'].pop(2)
#            player['objects'].insert(0,'')
#          q=str(input('make your next move \n-------------------------------- '))
#          takeAction(q)
#      else:
        #if no monster
#        print('\n\nyou K.O.\'ed the air. Great Job!!!\n\n')
#        q=str(input('make your next move \n-------------------------------- '))
#        takeAction(q)
#    if(inp=='m'):
#      isntInput=False
#      if(player['location']['hasMagicMonster']):
#        if('magic stones'in player['objects']):
          #turns magic monster into normal monster
#          player['location']['hasMagicMonster']=False
#          player['objects'].remove('magic stones')
#          player['objects'].insert(2,'')
#          print('\n\nyour magic stones have weakened the monster\n\n')
#        else:
          #no magic stones
#          print('\n\nyou do not have magic stones... only kidney stones\n\n')
#      elif('magic stones'in player['objects']):
        #no monster
#        print('\n\nstop sniffing the magic stones!!!\n\n')
#      else:
        #no magic stones
#        print('\n\nyou do not have magic stones... only kidney stones\n\n')
#      q=str(input('make your next move \n-------------------------------- '))
#      takeAction(q)
#    if(inp=='h'):
      #help
#      isntInput=False
#      print('controls:\n\nd-move right\na-move left\nw-move up stairs\ns-move down stairs\ng-grab treasure\ni-check inventory\nf-attack with sword\nm-use magic stones\nh-help and controls')
#      q=str(input('make your next move \n-------------------------------- '))
#      takeAction(q)
#    if(isntInput):
      #not valid input
#      q=str(input('no no no!!! '))
#      takeAction(q)
#start the game
#q=str(input('welcome to hell!!!\npress h for help and controls \n-------------------------------- '))
#takeAction(q)