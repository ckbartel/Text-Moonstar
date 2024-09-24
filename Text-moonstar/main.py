from roomClass import Room
from replit import clear
#XX678
#9543
#AB12
#each room is 5 characters or spaces, and it fills with the first index being the top floor
#A̲B̲C̲D̲E̲F̲G̲H̲I̲J̲K̲L̲M̲N̲O̲P̲
#map
room1, room2, room3, room4, room5, room6, room7, room8, room9, roomA, roomB, roomC, roomD, roomE, roomF=Room(),Room(),Room(),Room(),Room(),Room(),Room(),Room(),Room(),Room(),Room(),Room(),Room(),Room(),Room()
floor3='            [F]__[G̲]__[H̲]  '
floor2='  [I]__[E̲]__[D̲]__[C]  '
floor1='  [J̲]__[K]  [A̲]__[B̲]  '
floor0='       [L̲]__[M̲]__[N̲]__[O̲]  '
floors=[floor3,floor2,floor1,floor0]
#NPC's
NPC1={
  'name':'old man joe',
  'taskText':'\n\nI will not let you pass unless you find my lost coin...\nI know I left it around here somewhere\n\n',
  'rewardText':'\n\nYou found it!!! I mean thanks.\nI can get a little handsy sometimes,\nnow you may pass\n\n',
  'rewards':['magic sword'],
  'taskItems':['lost coin'],
  'hasMonsterToPlace':False,
  'hasItemsToPlace':False
}
NPC2={
  'name':'clue giver',
  'taskText':'\n\nMuhuhahaha!\nso you\'ve Made it this far.\nit\'s quite a shaMe, but now you\'ll be forced to create your own deMise.\n\nnow go on and fetch Me soMe spikes.\nit is where once it was.\n\n',
  'rewardText':'\n\nThanks, cya later\n\n',
  'rewards':['sword'],
  'taskItems':['spikes'],
  'hasMagicMonsterToPlace':True,
  'hasMonsterToPlace':True,
  'monsterLocation':room7,
  'monsterDoorBlocked':'right',
  'hasItemsToPlace':True,
  'itemsPlaced':['spikes'],
  'itemsLocation':room8
}
NPC3={
  'name':'clue giver',
  'taskText':'\n\n(panting...)\nAha!\ndid you think you could outrun me...\ni wAs A high school trAck stAr so don\'t try and get Any ideAs.\n\nnow you must Acquire A trAp config and bring it to me.\nit is found where you fought your first fight\n\n',
  'rewardText':'\n\nperfect! it\'s Almost complete\n\n',
  'rewards':['magic stones'],
  'taskItems':['trap config'],
  'hasMagicMonsterToPlace':False,
  'hasMonsterToPlace':True,
  'monsterLocation':room4,
  'monsterDoorBlocked':'right',
  'hasItemsToPlace':True,
  'itemsPlaced':['trap config'],
  'itemsLocation':room3
}
NPC4={
  'name':'clue giver',
  'taskText':'\n\n(panting...)\nThanks for being so cooperaTive.\nyou\'ve made This a loT easier.\ni beT your Tired of my presence, buT this is my lasT Task...\nif you have The sTamina for iT.\n\ngo To where you resT and Take The Treasures back To me.\n\n',
  'rewardText':'\n\nnow iT is compleTe... have fun in The nexT room.\ndon\'T even Try To disarm my Trap,\ni am a masTer of decepTion.\njusT in case, have some luck...\nyou\'ll need iT\n\n',
  'rewards':['luck'],
  'taskItems':['pressure plate'],
  'hasMagicMonsterToPlace':True,
  'hasMonsterToPlace':True,
  'monsterLocation':room2,
  'monsterDoorBlocked':'left',
  'hasItemsToPlace':True,
  'itemsPlaced':['pressure plate'],
  'itemsLocation':room1
}
#traps
trap1={
  'cipher':'01000110 01101001 01010011 01101000',
  'answer':'FiSh'
}
trap2={
  'cipher':'what is the clue giver\'s name(all caps)',
  'answer':'MAT'
}
room1.add({
  'ID':'A̲',
  'canD':True,
  'roomToRight':room2,
  'hasBed':True
})
room2.add({
  'ID':'B̲',
  'canA':True,
  'hasUpStairs':True,
  'hasPermObjects':True,
  'hasObjects':True,
  'objects':['sword','compactor','magic stones'],
  'permObjects':['sword','compactor','magic stones'],
  'roomAbove':room3,
  'roomToLeft':room1
})
room3.add({
  'ID':'C',
  'hasDownStairs':True,
  'canA':True,
  'permDoorBlocked':'left',
  'hasPermMagicMonster':True,
  'hasPermMonster':True,
  'hasMagicMonster':True,
  'hasMonster':True,
  'doorBlocked':'left',
  'roomToLeft':room4,
  'roomBelow':room2,
  'floor':2
})
room4.add({
  'ID':'D̲',
  'hasPermNPC':True,
  'hasNPC':True,
  'NPC':NPC1,
  'permDoorBlocked':'left',
  'doorBlocked':'left',
  'canA':True,
  'canD':True,
  'hasUpStairs':True,
  'roomToRight':room3,
  'roomToLeft':room5,
  'roomAbove':room6,
  'floor':2
})
room5.add({
  'ID':'E̲',
  'canD':True,
  'canA':True,
  'roomToRight':room4,
  'floor':2,
  'roomToLeft':room9
})
room6.add({
  'ID':'F',
  'hasDownStairs':True,
  'hasPermObjects':True,
  'hasObjects':True,
  'objects':['sword'],
  'permObjects':['sword'],
  'canD':True,
  'roomToRight':room7,
  'roomBelow':room4,
  'floor':3
})
room7.add({
  'ID':'G̲',
  'hasPermMonster':True,
  'hasMonster':True,
  'canD':True,
  'canA':True,
  'roomToRight':room8,
  'roomToLeft':room6,
  'permDoorBlocked':'right',
  'doorBlocked':'right',
  'floor':3
})
room8.add({
  'ID':'H̲',
  'hasPermObjects':True,
  'hasObjects':True,
  'objects':['lost coin','compactor','food'],
  'permObjects':['lost coin','compactor','food'],
  'canA':True,
  'roomToLeft':room7,
  'floor':3
})
room9.add({
  'ID':'I',
  'canD':True,
  'roomToRight':room5,
  'hasDownStairs':True,
  'roomBelow':roomA,
  'hasPermTrap':True,
  'hasTrap':True,
  'trap':trap1,
  'floor':2
})
roomA.add({
  'ID':'J̲',
  'hasPermObjects':True,
  'hasObjects':True,
  'objects':['sword'],
  'permObjects':['sword'],
  'hasUpStairs':True,
  'canD':True,
  'roomAbove':room9,
  'roomToRight':roomB
})
roomB.add({
  'ID':'K',
  'permDoorBlocked':'downstairs',
  'doorBlocked':'downstairs',
  'hasPermNPC':True,
  'hasNPC':True,
  'NPC':NPC2,
  'hasDownStairs':True,
  'canA':True,
  'roomToLeft':roomA,
  'roomBelow':roomC
})
roomC.add({
  'ID':'L̲',
  'permDoorBlocked':'right',
  'doorBlocked':'right',
  'hasPermNPC':True,
  'hasNPC':True,
  'NPC':NPC3,
  'canD':True,
  'roomToRight':roomD,
  'hasUpStairs':True,
  'roomAbove':roomB,
  'floor':'Dungeon'
})
roomD.add({
  'ID':'M̲',
  'permDoorBlocked':'right',
  'doorBlocked':'right',
  'hasPermNPC':True,
  'hasNPC':True,
  'NPC':NPC4,
  'canD':True,
  'roomToRight':roomE,
  'canA':True,
  'roomToLeft':roomC,
  'floor':'Dungeon'
})
roomE.add({
  'ID':'N̲',
  'canD':True,
  'roomToRight':roomF,
  'canA':True,
  'roomToLeft':roomD,
  'hasPermTrap':True,
  'hasTrap':True,
  'trap':trap2,
  'floor':'Dungeon'
})
roomF.add({
  'ID':'O̲',
  'canA':True,
  'roomToLeft':roomE,
  'floor':'Dungeon',
  'isWinRoom':True
})
#text displayed when entered winning room
winningText='clue giver:\n\nhow did you do ThAT...\nyou MusT\'ve died ATleAsT once coMe on...\nTry-hArd!\ngo ousTide And geT soMe sun wouldyA!!!\nwhy Are you sTill reAding This!\nyou won!\noh... you wAnnA know whAT you won,\nhow AbouT soMe TiMe spenT elsewhere noT wATching Me groAn in Agony AbouT My sorrows\nAnd AbouT The fAcT you\'ll jusT scuff AT My MAsTer plAn As Meh,\nAnd TAlk AbouT how you would\'ve done beTTer!\nhow dAre you jusT wipe your feeT on Me As if i\'M soMe sorT of A door MAT...\nMAt...\nMat...\nmat...\nma...\nm...\n...'
#rooms array for respawn regeneration
rooms = [room1, room2, room3, room4, room5, room6, room7, room8, room9, roomA, roomB, roomC, roomD, roomE, roomF]
#tells player inventory, location, and whether or not they've won
player={
  'objects':['','',''],
  'location':room1,
  'hasWon':False,
  'energy':3
}
#sets map up using apropriate floors
map=''
tmap=''
for i in floors:
  tmap=map+'\n'+i
  map=tmap
tmap=map
#draws map
def drawMap():
  global tmap
  global map
  #retrieves map backbone
  tmap=map
  for i in rooms:
    #set player location to X
    if(i['hasEntered']):
      if(player['location']==i):
        if(i['hasDownStairs']):
          tmap=tmap.replace(i['ID'],'X')
        else:
          tmap=tmap.replace(i['ID'],'X̲')
    #sets non-entered rooms to spaces
    else:
      if(i['canA']):
        left='_'
      else:
        left=' '
      if(i['canD']):
        right='_'
      else:
        right=' '
      tmap=tmap.replace(left+'['+i['ID']+']'+right,'     ')
    if(i['hasDownStairs']):
      tmap=tmap.replace(i['ID'],' ')
    else:
      tmap=tmap.replace(i['ID'],'_')
  print(tmap)
#gives player their movement info
def playerMoves():
  left=''
  right=''
  print('')
  if(player['location']['hasUpStairs'] and player['location']['doorBlocked']!='upstairs'):
    print(' ⬆️')
  if(player['location']['canA'] and player['location']['doorBlocked']!='left'):
    left = '⬅️'
  else:
    left = ' '
  if(player['location']['canD'] and player['location']['doorBlocked']!='right'):
    right = '➡️'
  else:
    right = ' '
  print(left,right)
  if(player['location']['hasDownStairs'] and player['location']['doorBlocked']!='downstairs'):
    print(' ⬇️')
  print('')
#respawn
def respawn():
  print('\n\nyou respawned in the first room\n\n')
  player['energy']=3
  player['location']=room1
  playerMoves()
  for i in rooms:
    #replinishes rooms with permanent attributes
    i['hasObjects']=i['hasPermObjects']
    i['hasMonster']=i['hasPermMonster']
    i['doorBlocked']=i['permDoorBlocked']
    i['hasMagicMonster']=i['hasPermMagicMonster']
    i['hasNPC']=i['hasPermNPC']
    i['hasTrap']=i['hasPermTrap']
    i['hasEntered']=i['permHasEntered']
    i['objects']=i['permObjects']
  player['location']['hasEntered']=True
  #removing items from player inventory
  for i in player['objects']:
    player['objects'].pop(2)
    player['objects'].insert(0,'')
#grab function
def grab(roomObjects):
  for i in roomObjects:
    if(i!=''):
      player['objects'].insert(0,i)
      player['objects'].pop(3)
  print('\n🎒\ncheck inventory to see rewards!\n\n')
  player['location']['hasObjects']=False
#gets info about room upon entering
def info():
  hasNoReaction=True
  #if room has trap
  if(player['location']['hasTrap']):
    if(hasNoReaction):
      playerMoves()
    hasNoReaction=False
    print('\n💣\nyou have fallen into a trap,\ndecifer the message to disengage the trap:\n\n')
    print('message:\n\n'+player['location']['trap']['cipher']+'\n\n')
    q=str(input('disengagement sequence: '))
    #if sequence is correct
    if(q==player['location']['trap']['answer']):
      print('\n\nyou successfully disarmed the trap,\nyou are free to pass!\n\n')
      player['location']['hasTrap']=False
      playerMoves()
    #if sequence is incorrect
    else:
      print('\n\nthe trap tortured you to your final breath\n\n')
      respawn()
  #if room has NPC
  if(player['location']['hasNPC']):
    hasNoReaction=False
    #If has NPC task items
    taskItemsObtained=0
    for i in player['location']['NPC']['taskItems']:
      if(i in player['objects']):
        taskItemsObtained+=1
    if(len(player['location']['NPC']['taskItems'])==taskItemsObtained):
      print('\n😃\nGreat job on helping the local prisoners!\n\n'+player['location']['NPC']['name']+':')
      print(player['location']['NPC']['rewardText'])
      #gives player their due rewards
      for i in player['location']['NPC']['taskItems']:
        player['objects'].remove(i)
        player['objects'].insert(2,'')
      grab(player['location']['NPC']['rewards'])
      player['location']['hasNPC']=False
      player['location']['doorBlocked']='none'
      playerMoves()
    #else receive task
    else:
      playerMoves()
      print('\n🤔\nyou have ran into a prisoner blocking the '+player['location']['doorBlocked']+' door\n\n'+player['location']['NPC']['name']+':')
      print(player['location']['NPC']['taskText'])
      #place itemsPlaced
      if(player['location']['hasEntered']==False):
        if(player['location']['NPC']['hasItemsToPlace']):
          player['location']['NPC']['itemsLocation'].add({
            'hasObjects':True,
            'objects':player['location']['NPC']['itemsPlaced']
          })
        #place the monsterToPlace
        if(player['location']['NPC']['hasMonsterToPlace']):
          player['location']['NPC']['monsterLocation']['doorBlocked']=player['location']['NPC']['monsterDoorBlocked']
          player['location']['NPC']['monsterLocation']['hasMonster']=player['location']['NPC']['hasMonsterToPlace']
          player['location']['NPC']['monsterLocation']['hasMagicMonster']=player['location']['NPC']['hasMagicMonsterToPlace']
  #if room is win room
  if(player['location']['isWinRoom']):
    player['hasWon']=True
    takeAction('')
  #if room has bed
  if(player['location']['hasBed']):
    if(hasNoReaction):
      playerMoves()
    hasNoReaction=False
    print('\n\n🛏️\n\n')
  #if room has treasure
  if(player['location']['hasObjects']):
    if(hasNoReaction):
      playerMoves()
    hasNoReaction=False
    print('\n\n💰\n\n')
  #if room has magic monster
  if(player['location']['hasMagicMonster']):
    if(hasNoReaction):
      playerMoves()
    hasNoReaction=False
    print('\n✨👿\nthis room contains a magic monster... blocking the '+player['location']['doorBlocked']+' door!\n\n')
  #if room has monster
  elif(player['location']['hasMonster']):
    if(hasNoReaction):
      playerMoves()
    hasNoReaction=False
    print('\n👿\nthis room contains a monster... blocking the '+player['location']['doorBlocked']+' door!\n\n')
  player['location']['hasEntered']=True
  #if no info is found about room, still display player movement info
  if(hasNoReaction):
    playerMoves()
#if u press a
def a():
  if(player['location']['canA'] and player['location']['doorBlocked']!='left'):
    player['location']=player['location']['roomToLeft']
    info()
  else:
    info()
    print('\n\nyou hysterically ran into a wall!\n\n')
#if u press d
def d():
  if(player['location']['canD'] and player['location']['doorBlocked']!='right'):
    player['location']=player['location']['roomToRight']
    info()
  else:
    info()
    print('\n\nyou hysterically ran into a wall!\n\n')
#if u press s
def s():
  if(player['location']['hasDownStairs'] and player['location']['doorBlocked']!='downstairs'):
    player['location']=player['location']['roomBelow']
    info()
  else:
    info()
    print('\n\nyou tried to ground pound like Mario... Only prevailing with a sore bum!\n\n')
#if u press w
def w():
  if(player['location']['hasUpStairs'] and player['location']['doorBlocked']!='upstairs'):
    player['location']=player['location']['roomAbove']
    info()
  else:
    info()
    print('\n\nyou leaped up through the roof and swiftly won \nthe game!!! then you woke up to realize your \nstill on floor '+str(player['location']['floor'])+'\n\n')
#if u press i
def inventory():
  print('\n🎒\n')
  print(player['objects'])
  print('\n\n')
#takes action when new input is given
def takeAction(inp):
  clear()
  isntInput=True
  #player won
  if(player['hasWon']):
    isntInput=False
    print(winningText)
  else:
    if(inp=='a'):
      isntInput=False
      a()
    if(inp=='d'):
      isntInput=False
      d()
    if(inp=='w'):
      isntInput=False
      w()
    if(inp=='s'):
      isntInput=False
      s()
    if(inp=='g'):
      playerMoves()
      isntInput=False
      if(player['location']['hasObjects']):
        grab(player['location']['objects'])
      else:
        print('\n\nyou spent hours scrounging for anything...\nthen you grew tired and stopped\n\n')
    if(inp=='i'):
      playerMoves()
      isntInput=False
      inventory()
    if(inp=='e'):
      playerMoves()
      isntInput=False
      #eating
      if('food'in player['objects']):
        print('\n\nyou savagely consumed your food\n\n')
        player['objects'].remove('food')
        player['objects'].insert(2,'')
        player['energy']+=1
        print('stamina left: '+str(player['energy'])+'\n\n')
      else:
        print('\n\nyou nibbled on your finger tips a bit\n\n')
    #resting
    if(inp=='r'):
      playerMoves()
      isntInput=False
      if(player['location']['hasBed']):
        player['energy']=3
        print('\n\nyou have fully rested and have replinished your stamana back to 3\n\n')
      elif('sleeping bag'in player['objects']):
        player['energy']=3
        player['objects'].remove('sleeping bag')
        player['objects'].insert(2,'')
        print('\n\nyou have fully rested and have replinished your stamana back to 3\n\n')
      else:
        print('\n\nyou could not sleep on the hard stone floor.\nnext time try sleeping on a bed or in a sleeping bag\n\n')
    if(inp=='c'):
      playerMoves()
      isntInput=False
      #if player has compactor
      if('compactor' in player['objects']):
        #and has sword and magic stones
        if('sword'in player['objects'] and 'magic stones' in player['objects']):
          player['objects'].remove('compactor')
          player['objects'].remove('sword')
          player['objects'].remove('magic stones')
          player['objects'].insert(0,'magic sword')
          player['objects'].insert(1,'')
          player['objects'].insert(1,'')
          print('\n\nyou have successfully compacted\nyour sword and magic stones to make a magic sword\nunfortunately, the compactor seems to have compacted itself\n\n')
        #no magic stones and sword
        else:
          playerMoves()
          print('you have compacted the air, decreasing your life expectancy... next time try to compact a sword and magic stones')
      #no compactor
      else:
        playerMoves()
        print('\n\ndon\'t try pushing on those objects too hard... you may want a compactor to do that\n\n')
    if(inp=='f'):
      isntInput=False
      if(player['location']['hasMonster']):
        if('sword' in player['objects'] and player['location']['hasMagicMonster']==False and player['energy']>0):
          #if you have sword
          player['objects'].remove('sword')
          player['objects'].insert(2,'')
          player['location']['hasMonster']=False
          player['location']['doorBlocked']='none'
          playerMoves()
          print('\n\nyou won but -- at a cost... your sword remains lodged deeply in the great basin the monster\'s belly :(\n\n')
          player['energy']-=1
          print('stamina left: '+str(player['energy'])+'\n\n')
          #if you have magic sword
        elif('magic sword' in player['objects'] and player['energy']>0):
          player['objects'].remove('magic sword')
          player['objects'].insert(2,'')
          player['location']['hasMonster']=False
          player['location']['hasMagicMonster']=False
          player['location']['doorBlocked']='none'
          playerMoves()
          print('\n\nyou won but -- at a cost... your sword remains lodged deeply in the great basin the monster\'s belly :(\n\n')
          player['energy']-=1
          print('stamina left: '+str(player['energy'])+'\n\n')
        else:
          #if you died
          print('\n\nthe monster got tired of your futile attacks and sat on you... you-- ya didn\'t make it...\n\n')
          respawn()
      else:
        playerMoves()
        #if no monster
        print('\n\nyou K.O.\'ed the air. Great Job!!!\n\n')
    if(inp=='m'):
      playerMoves()
      isntInput=False
      if(player['location']['hasMagicMonster']):
        if('magic stones'in player['objects']):
          #turns magic monster into normal monster
          player['location']['hasMagicMonster']=False
          player['objects'].remove('magic stones')
          player['objects'].insert(2,'')
          print('\n\nyour magic stones have weakened the monster\n\n')
        else:
          #no magic stones
          print('\n\nyou do not have magic stones... only kidney stones\n\n')
      elif('magic stones'in player['objects']):
        #no monster
        print('\n\nstop sniffing the magic stones!!!\n\n')
      else:
        #no magic stones
        print('\n\nyou do not have magic stones... only kidney stones\n\n')
    if(inp=='h'):
      #help
      isntInput=False
      print('\n\nstamina left: '+str(player['energy']))
      print('\n\ncontrols:\n\nd-move right\na-move left\nw-move up stairs\ns-move down stairs\ng-grab treasure\ni-check inventory\nf-attack with sword\nm-use magic stones\nc-compact sword and magic stones to make magic sword\nr-to rest in a room containing a bed (the spawn room) or in a sleeping bag\ne-eat food\nh-help and controls\n\n')
    if(isntInput):
      #not valid input
      q=str(input('no no no!!! '))
      takeAction(q)
    print('\n\nMAP:')
    drawMap()
    print('\n\n')

    q=str(input('make your next move \n-------------------------------- '))
    takeAction(q)
#start the game
player['location']['hasEntered']=True
playerMoves()
q=str(input('welcome to hell!!!\npress h for help and controls \n-------------------------------- '))
takeAction(q)