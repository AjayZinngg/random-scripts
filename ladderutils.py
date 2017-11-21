class Animal(object):
  features= {}

  def __init__(self,eyes,legs,hands,wings,fly):
    self.features = {
        'eyes': eyes,
        'legs': legs,
        'hands': hands,
        'wings': wings,
        'fly': fly
        }

 
  def __repr__(self):
    temp = ", ".join(
    "{}: {}".format(k, v) 
    for k, v in self.features.items() if v)
    return "{} <{}>".format(self.name, temp)
  def fly(self):
  	return self.features['fly']

class Monkey(Animal):

  def __init__(self,eyes,legs,hands):
    self.name = 'Monkey'
    Animal.__init__(self,eyes,legs,hands,0,False)
    Animal.__repr__(self)

 
class Squirrel(Animal):

  def __init__(self,eyes,legs):
    self.name = 'Squirrel'
    Animal.__init__(self,eyes,legs,0,0,False)   
    Animal.__repr__(self)
     
class Pigeon(Animal):

  def __init__(self,eyes,legs,wings):
    self.name = 'Pigeon'
    Animal.__init__(self,eyes,legs,0,wings,True)
    Animal.__repr__(self)  

class Eagle(Animal):

  def __init__(self,eyes,legs,wings):
    self.name = 'Eagle'
    Animal.__init__(self,eyes,legs,0,wings,True)
    Animal.__repr__(self)
  
class ladder:
  ladder_pos = {}
  #monkey_instance1 =Monkey(2,2,2) 

  def __init__(self):
    self.ladder_pos['3'] = Monkey(2,2,2)
    self.ladder_pos['5'] = Squirrel(2,4)
    self.ladder_pos['8'] = Pigeon(2,2,2)
    self.ladder_pos['15'] = Eagle(2,2,2)
    self.ladder_pos['17'] = Monkey(2,2,2)

  def animal_at_rung(self,pos):
    if(str(pos) in self.ladder_pos):
      return self.ladder_pos[str(pos)]
    else:
      return ('None')
 
  def get_animals_count(self):
    return len(self.ladder_pos)
 
  def hop(self,pos):
    if(str(pos+1) in self.ladder_pos):
      return ("Not Empty")
    else:
      self.ladder_pos[str(pos+1)] = self.ladder_pos[str(pos)]
      del self.ladder_pos[str(pos)]
      return ('None')
