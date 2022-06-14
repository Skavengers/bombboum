from kandinsky import *
from random import *


def initmap(li):
    w = []
    for i in range(14):
        w.append(randint(0,1))
    li.append(w)
    return li

class Perso:
  def __init__(self,x=1,y=1):
    self.x=x
    self.y=y
  def bomb(self,x,y):
    pass

  def skin(self):
    b=(0,)*3
    w=(155,)*3
    c1=(105,30,50)
    c2=(255,255,0)
    fill_rect(self.x+4,self.y+1,20,20,c2)
    fill_rect(self.x+6,self.y+3,4,8,b)
    fill_rect(self.x+18,self.y+3,4,8,b)
    fill_rect(self.x+10,self.y+15,10,4,b)

def fond():
  c=(0,150,100)
  fill_rect(0,0,320,222,c)

def gros():
  carte1=[[0,0,0,1,1,1,0,1,1,1,1,0,0,0],[0,0,0,1,1,1,1,1,1,1,1,0,0,0]]
  for i in range(8):
    carte=initmap(carte1)
  for c in range(len(carte)):
    for l in range(len(carte[c])):
      ll=carte1[c][l]
      if ll==1:
        fill_rect(22*l+5,22*c+2,20,20,(20,)*3)
      else:
        fill_rect(22*l+5,22*c+2,20,20,(0,100,50))

p1=Perso(1,1)

def loop():
  pass
gros()
p1.skin()
