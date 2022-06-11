from kandinsky import *

def initmap():
    fill_rect(0,0,320,222,(150,50,0))

class Perso:
    def __init__(self,x,y):
      self.x=x
      self.y=y
    def bomb(self,x,y):
      pass
def gros():
  carte1=[[0,1,0,1,0,0,0,0],[0,1,0,1],[0,1,1,1]]
  for c in range(len(carte1)):
    for l in range(len(carte1[c])):
      ll=carte1[c][l]
      if ll==0:
        fill_rect(40*l,40*c,30,30,(20,)*3)
def loop():
  pass
gros()
