from kandinsky import *
from random import *

def initmap():
    w=""
    for i in range(7):
        w=w+str(randint(0, 1))+str(",")
    w+=str(randint(0, 1))
    return w

class Perso:
  def __init__(self,x,y):
    self.x=x
    self.y=y
  def bomb(self,x,y):
    pass
def fond():
  c=(0,150,100)
  fill_rect(0,0,320,222,c)
def gros():
  carte1=[["0","0","0","1","1","1","0","1","1","1","0","0","0"],["0","0","0","1","1","1","1","1","1","1","0","0","0"] for i in range(8): ,[initmap()]]
  for c in range(len(carte1)):
    for l in range(len(carte1[c])):
      ll=carte1[c][l]
      if ll==1:
        fill_rect(22*l+5,22*c+5,20,20,(20,)*3)
      else:
        fill_rect(22*l+5,22*c+5,20,20,(0,100,50))

def loop():
  pass
gros()
