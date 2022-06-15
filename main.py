from kandinsky import *
from random import *


def initmap(li):
    w = []
    for i in range(14):
        w.append(randint(0,1))
    li.append(w)
    return li

class Perso:
  def __init__(self,x=1,y=1,k=0):
    self.x=x
    self.y=y
  def mov(self):
    if p==0:
      if keydown(KEY_RIGHT):
        if self.x!=0 :
          self.x-=20
        skin()
      if keydown(KEY_RIGHT):
        if self.x!=260 :
          self.x+=20
        skin()
      if keydown(KEY_UP):
        if self.y<=0 :
          self.y+=20
        skin()
      if keydown(KEY_DOWN):
        if self.x!=0 :
          self.x-=20
        skin()
    
  def bomb(self,x,y):
    pass

  def skin(self,c=(200,200,0)):
    b=(0,)*3
    w=(155,)*3
    fill_rect(self.x+4,self.y+1,20,20,c)
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
gros()
p1.skin()
while True:
  draw_string("/bimboum\ ",100,10)
  draw_string("[1]:play alone",50,50)
  draw_string("[1]:play in duo",50,80)
  if keydown(KEY_TWO):
    p2=Perso(13,1)
    p2.skin((105,30,50))
